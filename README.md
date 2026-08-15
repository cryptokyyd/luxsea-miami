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
2. **The Amberjack photo.** The Chris Craft 45 and the Sea Ray Sundancer 40 are
   confirmed from captions that name them. The Amberjack image on `fleet.html`
   and `index.html` (`assets/media/bay.jpg`) is the best match found but is
   **not confirmed** — swap it if it's the wrong boat.
3. **Prices.** Deliberately absent. The site's promise is "send the date, get the
   whole number back", which is also the strongest thing it has against the
   brokers. If fixed starting prices get published later, put them on the boat
   rows in `fleet.html` and in the first FAQ answer.
4. **Email.** There isn't one on the site — Instagram and WhatsApp are the real
   channels. Add one to the `.rail` in `contact.html` if that changes.

## Biggest remaining growth item

A **Google Business Profile**. Every competitor ranks on one, and "boat rental
miami" traffic lands there before it lands on any website. Same name, same
photos, both languages. That is worth more than any further page here.

## Notes for whoever edits this next

- **Colour is OKLCH only**, tokens at the top of `styles.css`. White text always
  goes on `--ember`, never on `--sun` (it's too light to hold text).
- **Fonts come from Fontshare.** Only request weights that exist — asking for a
  missing weight makes Fontshare silently drop every family after it in the URL.
  Panchang stops at 700.
- **Spanish is not a translation layer.** Any new copy needs a `data-es`
  attribute or the toggle will leave it in English. Placeholders use `data-es-ph`.
- **The photos are the identity.** Everything in `assets/media/` came off
  @luxseamiami. Don't replace them with stock.
