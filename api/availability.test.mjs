/**
 * node api/availability.test.mjs
 * Smallest thing that fails if the ICS parsing breaks.
 */
import assert from 'node:assert/strict';
import { parseBusy, busyDays } from './availability.js';

const DAY = 86400000;

const ICS = `BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART;VALUE=DATE:20260912
DTEND;VALUE=DATE:20260913
SUMMARY:Chris Craft - Maria birthday 786-555-0000
END:VEVENT
BEGIN:VEVENT
DTSTART:20260915T140000Z
DTEND:20260915T200000Z
SUMMARY:Sundancer - despedida
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20260920
DTEND;VALUE=DATE:20260923
SUMMARY:Multi-day chart
 er spanning a folded line
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20260925
DTEND;VALUE=DATE:20260926
STATUS:CANCELLED
SUMMARY:Cancelled - should not appear
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20260927
DTEND;VALUE=DATE:20260928
TRANSP:TRANSPARENT
SUMMARY:Marked free - should not appear
END:VEVENT
END:VCALENDAR`;

const ranges = parseBusy(ICS);
assert.equal(ranges.length, 3, 'cancelled and transparent events must be dropped');

const from = Date.UTC(2026, 8, 1);
const days = busyDays(ranges, from, from + 60 * DAY);

assert.ok(days.includes('2026-09-12'), 'all-day event');
assert.ok(days.includes('2026-09-15'), 'timed event occupies its day');
assert.deepEqual(days.filter(d => d >= '2026-09-20' && d <= '2026-09-23'),
  ['2026-09-20', '2026-09-21', '2026-09-22'],
  'multi-day event is exclusive of its DTEND day');
assert.ok(!days.includes('2026-09-25'), 'cancelled must not leak');
assert.ok(!days.includes('2026-09-27'), 'free-marked must not leak');

// The whole point: nothing but dates ever comes back.
assert.ok(JSON.stringify(days).indexOf('Maria') === -1, 'no customer names in output');
assert.ok(JSON.stringify(days).indexOf('786') === -1, 'no phone numbers in output');

console.log('availability parser OK —', days.length, 'busy days,', ranges.length, 'ranges, no PII leaked');
