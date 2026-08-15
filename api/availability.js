/**
 * GET /api/availability?boat=chriscraft|sundancer|amberjack
 *
 * Reads each vessel's Google Calendar "Secret address in iCal format" from an
 * environment variable, server-side, and returns ONLY the busy date ranges.
 *
 * Two things this deliberately does not do:
 *   1. It never returns event titles, descriptions, locations or attendees.
 *      Customer names live in those fields and they are none of the internet's
 *      business.
 *   2. It never exposes the ICS URL to the browser. That URL is effectively a
 *      password for the whole calendar — anyone holding it can read every
 *      booking. It stays in the Vercel env var and nowhere else.
 *
 * Set these in Vercel → Settings → Environment Variables:
 *   ICS_CHRISCRAFT, ICS_SUNDANCER, ICS_AMBERJACK
 * Any that are unset simply report configured:false and the UI falls back to
 * "message us for availability".
 */

const FEEDS = {
  chriscraft: 'ICS_CHRISCRAFT',
  sundancer:  'ICS_SUNDANCER',
  amberjack:  'ICS_AMBERJACK',
};

const DAY = 86400000;
const HORIZON_DAYS = 120;

/** Unfold RFC 5545 continuation lines (a leading space continues the line). */
function unfold(text) {
  return text.replace(/\r\n[ \t]/g, '').replace(/\n[ \t]/g, '');
}

/** "20260912" | "20260912T140000Z" → epoch ms (UTC). */
function parseICSDate(raw) {
  const v = raw.trim();
  const m = v.match(/^(\d{4})(\d{2})(\d{2})(?:T(\d{2})(\d{2})(\d{2}))?/);
  if (!m) return null;
  const [, y, mo, d, hh, mm, ss] = m;
  return Date.UTC(+y, +mo - 1, +d, +(hh || 0), +(mm || 0), +(ss || 0));
}

/**
 * Pull busy ranges out of an ICS body. Returns [{start, end}] in epoch ms,
 * all-day events included, cancelled events skipped.
 */
export function parseBusy(ics) {
  const out = [];
  const blocks = unfold(ics).split(/BEGIN:VEVENT/).slice(1);
  for (const block of blocks) {
    const body = block.split('END:VEVENT')[0];
    if (/^STATUS:CANCELLED/m.test(body)) continue;
    if (/^TRANSP:TRANSPARENT/m.test(body)) continue;   // marked "free"

    const ds = body.match(/^DTSTART[^:]*:(.+)$/m);
    const de = body.match(/^DTEND[^:]*:(.+)$/m);
    if (!ds) continue;

    const start = parseICSDate(ds[1]);
    if (start == null) continue;

    let end = de ? parseICSDate(de[1]) : null;
    if (end == null || end <= start) end = start + DAY;   // treat as one day
    out.push({ start, end });
  }
  return out.sort((a, b) => a.start - b.start);
}

/** Collapse busy ranges into a flat list of YYYY-MM-DD strings. */
export function busyDays(ranges, from, to) {
  const days = new Set();
  for (const r of ranges) {
    for (let t = Math.max(r.start, from); t < Math.min(r.end, to); t += DAY) {
      days.add(new Date(t).toISOString().slice(0, 10));
    }
    // an event ending exactly at midnight still occupies its final day
    if (r.end > from && r.end <= to && (r.end - r.start) < DAY) {
      days.add(new Date(r.start).toISOString().slice(0, 10));
    }
  }
  return [...days].sort();
}

export default async function handler(req, res) {
  const boat = String((req.query && req.query.boat) || '').toLowerCase();
  const envName = FEEDS[boat];

  if (!envName) {
    res.status(400).json({ error: 'unknown boat', valid: Object.keys(FEEDS) });
    return;
  }

  const url = process.env[envName];
  if (!url) {
    // Not wired up yet — say so plainly instead of pretending everything is free.
    res.setHeader('Cache-Control', 'public, s-maxage=300');
    res.status(200).json({ boat, configured: false, busy: [] });
    return;
  }

  try {
    const r = await fetch(url, { headers: { 'User-Agent': 'luxsea-availability' } });
    if (!r.ok) throw new Error('feed responded ' + r.status);
    const ics = await r.text();

    const from = Date.UTC(new Date().getUTCFullYear(), new Date().getUTCMonth(), new Date().getUTCDate());
    const to = from + HORIZON_DAYS * DAY;
    const busy = busyDays(parseBusy(ics), from, to);

    // 15 min at the edge: fresh enough for a booking calendar, gentle on Google.
    res.setHeader('Cache-Control', 'public, s-maxage=900, stale-while-revalidate=3600');
    res.status(200).json({ boat, configured: true, days: HORIZON_DAYS, busy });
  } catch (err) {
    res.setHeader('Cache-Control', 'no-store');
    res.status(502).json({ boat, configured: true, error: 'could not read the calendar feed', busy: [] });
  }
}
