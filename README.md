# LuxSea Miami — brand identity + site

Static site. No build step, no dependencies. Open `index.html` or serve the folder.

```bash
python -m http.server 4321 --directory luxsea-miami
```

## What's here

| File | What it is |
|---|---|
| `index.html` | Home — hero video, the three boats, celebrations, FAQ |
| `fleet.html` | The three boats in detail + a "which one fits" guide |
| `experiences.html` | Birthdays, bachelorettes, family, sunset, sandbar, skyline |
| `about.html` | The owner-not-broker argument |
| `contact.html` | Booking form → prefilled WhatsApp message |
| `chris-craft-45-miami.html` | Boat page + 10-photo gallery (ES twin in `es/`) |
| `sea-ray-sundancer-40-miami.html` | Boat page + 8-photo gallery (ES twin in `es/`) |
| `sea-ray-amberjack-32-miami.html` | Boat page + gallery (ES twin in `es/`) |
| `es/index.html` | Spanish home — targets *renta de botes en miami* |
| `build-service-pages.py` | Generates the 12 celebration pages from `service-pages.json` |
| `build-boat-pages.py` | Generates the 6 boat pages, the Spanish home and `sitemap.xml` |
| `brand.html` | The brand guide (noindex — internal reference) |
| `styles.css` | The whole design system, OKLCH tokens at the top |
| `main.js` | Contact config, ES/EN toggle, nav, reveal, form |
| `assets/media/` | LuxSea's own photos and video, pulled from @luxseamiami |

## Before this goes live — things only the owner can confirm

1. **The phone number.** Two appear in the Instagram captions: `786-878-0701` and
   `786-878-0107`. The site uses **786-878-0701**. If that's wrong, change
   `LUXSEA.whatsapp` and `LUXSEA.phone` at the top of `main.js` — every button on
   every page reads from there — then search-replace `+17868780701` and
   `(786) 878-0701` in the HTML (they're there so the links work without JS).
2. ~~Which photo is which boat.~~ **Resolved.** All three are confirmed from
   his own labelled posts: the Chris Craft 45 (`#45ft #sportfish` carousel), the
   Sea Ray Sundancer 40 (`#40ft` carousel), and the Sea Ray Amberjack 32 (the
   reel captioned "Disponible / Sea ray Amberjack 32ft" — burned-in text cropped
   off for `assets/media/amberjack-32.jpg`).
3. **Prices.** Deliberately absent. The site's promise is "send the date, get the
   whole number back", which is also the strongest thing it has against the
   brokers. If fixed starting prices get published later, put them on the boat
   rows in `fleet.html` and in the first FAQ answer.
4. **The domain.** `<link rel="canonical">` tags and `sitemap.xml` were removed
   on purpose — pointing them at `luxseamiami.com` before that domain exists
   tells Google to index a page that 404s. Add both back once the real domain is
   connected in Vercel.
5. **Email.** There isn't one on the site — Instagram and WhatsApp are the real
   channels. Add one to the `.rail` in `contact.html` if that changes.

## Turning on the live availability calendars

The fleet page shows two months of real availability per boat, straight from
the captain's Google Calendars. Until the feeds are set it shows "message us on
WhatsApp" instead — it never implies a date is free when it doesn't know.

**Do not make the calendars public.** A public calendar publishes event titles,
and those titles hold customer names and phone numbers. Use the private feed:

1. Google Calendar → hover the vessel's calendar → **Settings and sharing**
2. Scroll to **Integrate calendar** → copy **Secret address in iCal format**
3. Repeat for all three boats
4. In Vercel → the project → Settings → Environment Variables, add:
   - `ICS_CHRISCRAFT`
   - `ICS_SUNDANCER`
   - `ICS_AMBERJACK`
5. Redeploy

That secret URL is effectively a password for the whole calendar, so it lives
only in Vercel. `api/availability.js` reads it server-side and returns nothing
but busy dates — no titles, no names, no numbers. `npm test` proves that.

If a booking should NOT block the boat, mark the event "Free" in Google
Calendar (or cancel it) and it disappears from the site.

## Biggest remaining growth item

A **Google Business Profile**. Every competitor ranks on one, and "boat rental
miami" traffic lands there before it lands on any website. Same name, same
photos, both languages. That is worth more than any further page here.

## Rebuilding the generated pages

Twenty of the 25 pages are generated. Edit the source, then:

```bash
python build-service-pages.py && python build-boat-pages.py
```

Run them in that order — the boat script imports the service script for the
shared header/footer and writes the sitemap covering everything.

## Notes for whoever edits this next

- **Colour is OKLCH only**, tokens at the top of `styles.css`. White text always
  goes on `--ember`, never on `--sun` (it's too light to hold text).
- **Fonts come from Fontshare.** Only request weights that exist — asking for a
  missing weight makes Fontshare silently drop every family after it in the URL.
  Gambetta stops at 700 and Switzer runs 100-900; ask for a weight
  outside those and every family *after* it in the query is dropped.
- **Spanish is not a translation layer.** Any new copy needs a `data-es`
  attribute or the toggle will leave it in English. Placeholders use `data-es-ph`.
- **The photos are the identity.** All 49 images in `assets/media/` came off
  @luxseamiami. Don't replace them with stock.
- **No photo is used on two different pages.** The boat galleries are exclusive
  to their boat, and each celebration page has its own four. If you add a page,
  add photos rather than reusing — a repeated image reads as a stock library.
