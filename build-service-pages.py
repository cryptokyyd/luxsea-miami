#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generates the 12 service landing pages (6 English + 6 Spanish twins).

One template, twelve unique content blobs. Run it again after editing the
DATA block below and every page picks up the change:

    python build-service-pages.py

The Spanish pages are REAL URLs under /es/, not a JavaScript toggle, because
Google only indexes what is in the HTML. Each pair is joined with hreflang.
"""
import io, os, json, pathlib

BASE = "https://luxsea-miami.vercel.app"   # swap when the real domain is connected
OUT = pathlib.Path(__file__).parent

# ---------------------------------------------------------------- chrome ----
NAV_EN = [("index.html","Home"),("fleet.html","The three boats"),
          ("experiences.html","Occasions at Sea"),("about.html","About"),("contact.html","Book")]
NAV_ES = [("../index.html","Inicio"),("../fleet.html","Los tres botes"),
          ("../experiences.html","Ocasiones en el mar"),("../about.html","Nosotros"),("../contact.html","Reservar")]

MARK = '''<svg class="brand__mark" viewBox="0 0 64 64" aria-hidden="true" focusable="false">
        <clipPath id="hm"><rect x="0" y="0" width="64" height="37"/></clipPath>
        <circle cx="32" cy="27" r="16" fill="#c25a33" clip-path="url(#hm)"/>
        <rect x="4" y="39" width="56" height="4" rx="2" fill="#12333d"/>
        <rect x="13" y="48" width="38" height="4" rx="2" fill="#12333d" opacity=".62"/>
        <rect x="23" y="57" width="18" height="4" rx="2" fill="#12333d" opacity=".32"/>
      </svg>'''
MARK_FOOT = MARK.replace('id="hm"','id="hf"').replace('url(#hm)','url(#hf)') \
                .replace('#c25a33','#e08a5f').replace('#12333d','#dfe9ec')

def sibling(p, es):
    """Link between service pages. Spanish twins sit in /es/ together, so they
    reference each other by filename, never by the /es/-prefixed slug."""
    return p["slug_es"].split("/")[-1] if es else p["slug_en"]


CHEVRON = ('<svg viewBox="0 0 12 8" aria-hidden="true" focusable="false">'
           '<path d="M1 1.5 6 6.5 11 1.5" fill="none" stroke="currentColor" '
           'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')

BOATS = [("chris-craft-45-miami.html", "Chris Craft 45\u2032"),
         ("sea-ray-sundancer-40-miami.html", "Sea Ray Sundancer 40\u2032"),
         ("sea-ray-amberjack-32-miami.html", "Sea Ray Amberjack 32\u2032")]


def submenu(kind, es, root):
    """Hub children. Spanish pages sit inside /es/ together, so they link by
    bare filename; English pages prefix with root."""
    if kind == "boats":
        return [(f'{"" if es else root}{h}', l) for h, l in BOATS]
    return [(sibling(p, es), p["nav_es" if es else "nav_en"]) for p in DATA]


def nav_entry(href, label, es, root, mobile):
    """A plain link, unless it is one of the two hubs, which get a panel."""
    kind = ("boats" if href.endswith("fleet.html")
            else "occasions" if href.endswith("experiences.html") else None)
    if kind is None:
        return f'<a href="{href}">{label}</a>'

    pad = "      " if mobile else "          "
    kids = ("\n" + pad).join(f'<a href="{h}">{l}</a>' for h, l in submenu(kind, es, root))
    if mobile:
        return (f'<a href="{href}">{label}</a>\n    '
                f'<div class="mobile-nav__sub">\n      {kids}\n    </div>')
    mid = "m-boats" if kind == "boats" else "m-occasions"
    aria = {("boats", True): "Ver los botes", ("boats", False): "Show the boats",
            ("occasions", True): "Ver las ocasiones",
            ("occasions", False): "Show the occasions"}[(kind, es)]
    return (f'<div class="nav__item">\n'
            f'        <a href="{href}">{label}</a>\n'
            f'        <button class="nav__more" type="button" aria-expanded="false" '
            f'aria-controls="{mid}" aria-label="{aria}">{CHEVRON}</button>\n'
            f'        <div class="nav__menu" id="{mid}">\n'
            f'          {kids}\n'
            f'        </div>\n'
            f'      </div>')


def header(es, root, alt_href, alt_label):
    nav = NAV_ES if es else NAV_EN
    home = f"{root}index.html"
    book = f"{root}contact.html"
    call = "Llamar" if es else "Call"
    bookl = "Reservar" if es else "Book a day"
    menu = "Menú" if es else "Menu"
    items = "\n      ".join(nav_entry(h, l, es, root, False) for h, l in nav)
    mitems = "\n    ".join(nav_entry(h, l, es, root, True) for h, l in nav)
    return f'''<a class="skip" href="#main">{"Ir al contenido" if es else "Skip to content"}</a>

<header class="site-head">
  <div class="wrap site-head__in">
    <a class="brand" href="{home}" aria-label="LuxSea Miami">
      {MARK}
      <span class="brand__type">LUX<em>SEA</em></span>
    </a>
    <nav class="nav" aria-label="Main">
      {items}
    </nav>
    <div class="head-tools">
      <a class="lang" href="{alt_href}" hreflang="{'en' if es else 'es'}" aria-label="{alt_label}">{'EN' if es else 'ES'}</a>
      <a class="btn btn--ghost" href="tel:+17868780701">{call}</a>
      <a class="btn btn--primary" href="{book}">{bookl}</a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="{menu}"><span></span></button>
    </div>
  </div>
  <nav class="mobile-nav wrap" id="mobile-nav" aria-label="Mobile">
    {mitems}
  </nav>
</header>'''

def footer(es, root):
    t = {
      True: dict(blurb="Botes privados con capitán en Miami Beach y Key Biscayne. Tres botes, dos idiomas, un capitán.",
                 boats="Los botes", cel="Ocasiones en el mar", contact="Contacto", book="Reservar",
                 note="Todos los paseos van con capitán y chalecos salvavidas para cada persona a bordo."),
      False: dict(blurb="Captained private boat charters around Miami Beach and Key Biscayne. Three boats, two languages, one captain.",
                 boats="The boats", cel="Occasions at Sea", contact="Contact", book="Book a day",
                 note="Every charter is captained and carries a life jacket for every guest on board."),
    }[es]
    # Spanish pages already live inside /es/, so link to the bare filename —
    # using the full slug from in there produces /es/es/... .
    cel = "\n          ".join(
        f'<li><a href="{sibling(p, es)}">{p["nav_es" if es else "nav_en"]}</a></li>'
        for p in DATA)
    return f'''<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="{root}index.html" aria-label="LuxSea Miami">
          {MARK_FOOT}
          <span class="brand__type">LUX<em>SEA</em></span>
        </a>
        <p style="margin-top:1rem;max-width:32ch;font-size:var(--step--1)">{t["blurb"]}</p>
      </div>
      <div>
        <h4>{t["boats"]}</h4>
        <ul>
          <li><a href="{root}fleet.html#chriscraft">Chris Craft 45′</a></li>
          <li><a href="{root}fleet.html#sundancer">Sea Ray Sundancer 40′</a></li>
          <li><a href="{root}fleet.html#amberjack">Sea Ray Amberjack 32′</a></li>
        </ul>
      </div>
      <div class="foot-col--wide">
        <h4>{t["cel"]}</h4>
        <ul>
          {cel}
        </ul>
      </div>
      <div>
        <h4>{t["contact"]}</h4>
        <ul>
          <li><a href="tel:+17868780701">(786) 878-0701</a></li>
          <li><a data-wa="Hola LuxSea — quiero consultar una fecha." href="#">WhatsApp</a></li>
          <li><a href="https://www.instagram.com/luxseamiami/" target="_blank" rel="noopener">@luxseamiami</a></li>
          <li><a href="{root}contact.html">{t["book"]}</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-note">
      <span>© <span id="yr">2026</span> LuxSea Miami · Miami Beach &amp; Key Biscayne, Florida</span>
      <span>{t["note"]}</span>
    </div>
  </div>
</footer>

<script src="{root}main.js"></script>
<script>document.getElementById('yr').textContent = new Date().getFullYear();</script>'''

# ------------------------------------------------------------------ page ----
def build(p, es):
    root = "../" if es else ""
    k = (lambda n: p[n + ("_es" if es else "_en")])
    slug_self = p["slug_es"] if es else p["slug_en"]
    slug_alt  = p["slug_en"] if es else p["slug_es"]
    url_self  = f"{BASE}/{slug_self}".replace(".html","")
    url_en    = f"{BASE}/{p['slug_en']}".replace(".html","")
    url_es    = f"{BASE}/{p['slug_es']}".replace(".html","")
    alt_href  = (f"{root}{p['slug_en']}" if es else p["slug_es"])
    alt_label = "Read this page in English" if es else "Ver esta página en español"

    faqs = k("faqs")
    faq_ld = json.dumps({"@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]},
        ensure_ascii=False, indent=2)
    svc_ld = json.dumps({"@context":"https://schema.org","@type":"Service",
        "serviceType": k("service_type"),
        "name": k("h1"),
        "provider":{"@type":"LocalBusiness","name":"LuxSea Miami","telephone":"+1-786-878-0701",
                    "url":BASE,"areaServed":["Miami","Miami Beach","Key Biscayne","Biscayne Bay"]},
        "areaServed":["Miami, FL","Miami Beach, FL","Key Biscayne, FL"],
        "availableLanguage":["es","en"],
        "description": k("desc")}, ensure_ascii=False, indent=2)

    secs = []
    for h2, paras, img in k("sections"):
        media = ""
        if img:
            f, alt = img
            media = f'''
      <div class="split__media rise">
        <img src="{root}assets/media/{f}" alt="{alt}" loading="lazy">
      </div>'''
        body = "\n        ".join(f"<p>{x}</p>" for x in paras)
        cls = "split split--flip" if len(secs) % 2 else "split"
        if media:
            secs.append(f'''  <section class="band{' band--surface' if len(secs)%2 else ''}">
    <div class="wrap {cls}">{media}
      <div class="stack-4 rise prose">
        <h2>{h2}</h2>
        {body}
      </div>
    </div>
  </section>''')
        else:
            secs.append(f'''  <section class="band{' band--surface' if len(secs)%2 else ''}">
    <div class="wrap wrap--narrow stack-4 rise prose">
      <h2>{h2}</h2>
      {body}
    </div>
  </section>''')
    sections = "\n\n".join(secs)

    faq_html = "\n        ".join(
        f'<details{" open" if i==0 else ""}>\n          <summary>{q}</summary>\n          <div><p>{a}</p></div>\n        </details>'
        for i,(q,a) in enumerate(faqs))

    hero_img, hero_alt = k("hero")
    lock = '<script>try{localStorage.setItem("luxsea-lang","es")}catch(e){}</script>\n' if es else ""

    return f'''<html lang="{"es" if es else "en"}">
<meta charset="utf-8">
<title>{k("title")}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{k("desc")}">
<link rel="canonical" href="{url_self}">
<link rel="alternate" hreflang="en" href="{url_en}">
<link rel="alternate" hreflang="es" href="{url_es}">
<link rel="alternate" hreflang="x-default" href="{url_en}">
<link rel="icon" href="{root}assets/mark.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:title" content="{k("title")}">
<meta property="og:description" content="{k("desc")}">
<meta property="og:url" content="{url_self}">
<meta property="og:image" content="{BASE}/assets/media/{hero_img}">
<meta name="theme-color" content="#12333d">
<link rel="stylesheet" href="{root}styles.css">
{lock}
<script type="application/ld+json">
{svc_ld}
</script>
<script type="application/ld+json">
{faq_ld}
</script>

{header(es, root, alt_href, alt_label)}

<main id="main">

  <section class="hero">
    <div class="hero__media">
      <img src="{root}assets/media/{hero_img}" alt="{hero_alt}" fetchpriority="high">
    </div>
    <div class="hero__scrim" aria-hidden="true"></div>
    <div class="hero__glow" aria-hidden="true"></div>
    <div class="wrap hero__in">
      <span class="said" style="color:var(--sun-hi)">{k("said")}</span>
      <h1>{k("h1")}</h1>
      <p class="hero__sub">{k("lede")}</p>
      <div class="btn-row">
        <a class="btn btn--light" data-wa="{k("wa")}" href="#">{k("cta1")}</a>
        <a class="btn btn--outline-light" href="{root}contact.html">{k("cta2")}</a>
      </div>
    </div>
  </section>

{sections}

  <section class="band band--bay">
    <div class="wrap wrap--narrow">
      <div class="head rise">
        <span class="said">{"Lo que siempre preguntan" if es else "What everybody asks"}</span>
        <h2>{k("faq_h")}</h2>
      </div>
      <div class="faq rise">
        {faq_html}
      </div>
    </div>
  </section>

  <section class="band band--drench">
    <div class="wrap cta-final rise">
      <h2>{k("cta_h")}</h2>
      <p>{k("cta_p")}</p>
      <div class="btn-row" style="justify-content:center">
        <a class="btn btn--light" data-wa="{k("wa")}" href="#">{"Escribir por WhatsApp" if es else "Message on WhatsApp"}</a>
        <a class="btn btn--outline-light" href="{root}contact.html">{"Enviar los detalles" if es else "Send the details"}</a>
      </div>
    </div>
  </section>

  <section class="band band--tight">
    <div class="wrap">
      <div class="head rise"><h2 style="font-size:var(--step-2)">{"Otras celebraciones" if es else "Other celebrations"}</h2></div>
      <div class="rows rise">
        {"".join(f'<div class="row"><h3><a href="{sibling(o, es)}" style="text-decoration:none">{o["nav_es" if es else "nav_en"]}</a></h3><p>{o["blurb_es" if es else "blurb_en"]}</p></div>' for o in DATA if o is not p)}
      </div>
    </div>
  </section>

</main>

{footer(es, root)}
'''

# ------------------------------------------------------------------ data ----
DATA = json.loads(pathlib.Path(OUT / "service-pages.json").read_text(encoding="utf-8"))

if __name__ == "__main__":
    (OUT / "es").mkdir(exist_ok=True)
    written = []
    for p in DATA:
        for es in (False, True):
            slug = p["slug_es"] if es else p["slug_en"]
            path = OUT / slug
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(build(p, es), encoding="utf-8")
            written.append(slug)
    # sitemap with hreflang pairs
    urls = []
    for s in ["", "fleet.html", "experiences.html", "about.html", "contact.html"]:
        urls.append(f'  <url><loc>{BASE}/{s.replace(".html","")}</loc></url>')
    for p in DATA:
        en = f'{BASE}/{p["slug_en"]}'.replace(".html","")
        es = f'{BASE}/{p["slug_es"]}'.replace(".html","")
        for loc, other, lang in ((en, es, "es"), (es, en, "en")):
            urls.append(
                f'  <url><loc>{loc}</loc>\n'
                f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{other}"/>\n'
                f'    <xhtml:link rel="alternate" hreflang="{"en" if lang=="es" else "es"}" href="{loc}"/>\n'
                f'  </url>')
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n",
        encoding="utf-8")
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nDisallow: /brand.html\n\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
    print(f"wrote {len(written)} pages + sitemap.xml + robots.txt")
    for w in written: print("  ", w)
