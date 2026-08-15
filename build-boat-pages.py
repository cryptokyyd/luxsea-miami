#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generates a page per vessel (English + Spanish) and the Spanish home page.

    python build-boat-pages.py

Galleries are the point of these pages: the photographs come from the posts
where the owner names the boat himself, so a boat page is substantial content
by construction rather than a keyword page with padding.
"""
import json, pathlib
from importlib.machinery import SourceFileLoader

OUT = pathlib.Path(__file__).parent
svc = SourceFileLoader("svc", str(OUT / "build-service-pages.py")).load_module()
BASE, header, footer = svc.BASE, svc.header, svc.footer

BOATS = [
{
 "id": "chriscraft", "slug_en": "chris-craft-45-miami.html", "slug_es": "es/chris-craft-45-miami.html",
 "name": "Chris Craft 45′", "nav_en": "Chris Craft 45′", "nav_es": "Chris Craft 45′",
 "title_en": "Chris Craft 45 Charter Miami | Up to 13 Guests | LuxSea Miami",
 "title_es": "Chris Craft 45 en Miami | Hasta 13 Personas | LuxSea Miami",
 "desc_en": "Charter the Chris Craft 45 in Miami — up to 13 guests, fitted cabin, bathroom with a shower, fridge, microwave and a floating pool. Captain and fuel included.",
 "desc_es": "Alquila el Chris Craft 45 en Miami — hasta 13 personas, camarote equipado, baño con ducha, nevera, microondas y piscina flotante. Capitán y gasolina incluidos.",
 "said_en": "The big one", "said_es": "El grande",
 "h1_en": "Thirteen people, a shower, and somewhere to put the cake",
 "h1_es": "Trece personas, una ducha, y dónde poner el bizcocho",
 "lede_en": "The boat that goes out when the group is big or the occasion carries weight. It is the only one of the three that can do a six-hour day without anyone wishing it were shorter.",
 "lede_es": "El bote que sale cuando el grupo es grande o la ocasión pesa. Es el único de los tres que aguanta un día de seis horas sin que nadie desee que fuera más corto.",
 "hero": "chriscraft-45.jpg",
 "hero_alt_en": "The Chris Craft 45 anchored side-on in green water off a mangrove island",
 "hero_alt_es": "El Chris Craft 45 anclado de lado en agua verde frente a una isla de manglares",
 "specs_en": [("Guests","up to 13"),("Length","45 ft"),("Hours","4 · 5 · 6"),("Head &amp; shower","Yes"),("Cabin","Fitted"),("Galley","Fridge + microwave")],
 "specs_es": [("Personas","hasta 13"),("Largo","45 pies"),("Horas","4 · 5 · 6"),("Baño y ducha","Sí"),("Camarote","Equipado"),("Cocina","Nevera + microondas")],
 "body_en": [
   ("Why this is the celebration boat",
    ["Thirteen guests is the number that rules out most of what is advertised in Miami, and it is why almost every bachelorette and every round-number birthday we run goes out on this hull.",
     "It has a fitted cabin to change in, a bathroom with a shower, a fridge and a microwave. On a July afternoon those stop being luxuries somewhere around hour four — which is exactly when a four-hour booking becomes a six-hour one."]),
   ("What comes with it",
    ["Captain and fuel. Cooler on ice and drinking water. Speaker. Floating pool mat. Fitted cabin, head and shower, fridge and microwave.",
     "You bring the food, the cake, the drinks, the decorations and the playlist. Tell us in advance and the boat is set up before you walk down the dock."]),
   ("The day it is best at",
    ["Four hours gets you the sandbar and the skyline. Six gets you the sandbar, lunch on board and the sunset on the way back, which is the version people book when it is somebody's thirtieth.",
     "If the group is larger than thirteen we can raft a second boat alongside at the sandbar so it stays one party. That has to be arranged when you book, not on the day."]),
 ],
 "body_es": [
   ("Por qué este es el bote de las celebraciones",
    ["Trece personas es el número que descarta a casi todo lo que se anuncia en Miami, y por eso casi todas las despedidas y todos los cumpleaños redondos que hacemos salen en este casco.",
     "Tiene camarote equipado para cambiarse, baño con ducha, nevera y microondas. En una tarde de julio eso deja de ser un lujo más o menos a la cuarta hora — que es justo cuando una reserva de cuatro horas se convierte en una de seis."]),
   ("Qué va incluido",
    ["Capitán y gasolina. Nevera con hielo y agua. Bocina. Piscina flotante. Camarote equipado, baño con ducha, nevera y microondas.",
     "Tú traes la comida, el bizcocho, las bebidas, la decoración y la playlist. Avísanos antes y el bote está montado cuando bajes por el muelle."]),
   ("El día que mejor hace",
    ["Con cuatro horas te da el banco de arena y la ciudad. Con seis te da el banco, almorzar a bordo y el atardecer de regreso, que es la versión que se reserva cuando alguien cumple treinta.",
     "Si el grupo pasa de trece podemos amarrar un segundo bote al lado en el banco de arena para que siga siendo una sola fiesta. Eso se arregla al reservar, no el mismo día."]),
 ],
 "gallery": [
   ("cc-01.jpg","The Chris Craft at anchor with the swim float streamed off the stern","El Chris Craft fondeado con el flotador por la popa"),
   ("cc-02.jpg","Looking aft across the cockpit from the flybridge ladder","Vista hacia popa desde la escalera del puente"),
   ("cc-03.jpg","The teak cockpit sole and mezzanine seating","La cubierta de teca y el asiento del mezzanine"),
   ("cc-04.jpg","The cockpit lit up alongside the dock at night","La bañera iluminada junto al muelle de noche"),
   ("cc-05.jpg","Bow cushions laid out forward of the helm","Los cojines de proa puestos delante del timón"),
   ("cc-06.jpg","The saloon interior looking forward","El interior del salón mirando a proa"),
   ("cc-07.jpg","The fitted cabin below deck","El camarote equipado bajo cubierta"),
   ("cc-08.jpg","The galley with fridge and microwave","La cocina con nevera y microondas"),
   ("cc-09.jpg","The head, with the shower and marlin plaque","El baño, con la ducha y la placa del marlín"),
   ("cc-10.jpg","The helm station and instruments","El puesto de mando y los instrumentos"),
   ("cc-11.jpg","The Chris Craft at anchor off the shoreline with the swim float streamed astern","El Chris Craft fondeado frente a la costa con el flotador por la popa"),
   ("cc-12.jpg","Straight down over the boat and the ring float at anchor","Vista cenital del bote y el flotador fondeados"),
   ("cc-13.jpg","At anchor close to the mangroves, guests out on the float","Fondeado junto a los manglares, con invitados en el flotador"),
   ("cc-14.jpg","The bow sunpads laid out, marina and towers behind","Los cojines de proa puestos, con la marina y las torres detrás"),
   ("cc-15.jpg","The saloon looking aft to the cockpit door","El salón mirando a popa hacia la puerta de la bañera"),
   ("cc-16.jpg","The saloon looking forward past the bar to the galley","El salón mirando a proa, pasando la barra hacia la cocina"),
   ("cc-17.jpg","The second cabin, with a single berth and reading light","El segundo camarote, con litera sencilla y luz de lectura"),
   ("cc-18.jpg","The forward cabin with its vanity and mirror","El camarote de proa con su tocador y espejo"),
 ],
 "faqs_en": [
   ("How many people fit on the Chris Craft 45?","Up to 13 guests, and that includes everyone stepping aboard. It is a Coast Guard limit rather than a preference."),
   ("Does it have a real bathroom?","Yes — a head with a shower and a fitted cabin to change in. The Sundancer 40 has both as well; the Amberjack 32 has a smaller head without the shower stall."),
   ("Can we cook or keep food cold on board?","There is a fridge and a microwave in the galley, and a cooler on ice in the cockpit. Cakes go straight into the fridge when you arrive."),
   ("Is it the right boat for four people?","Usually not — you would be paying for space you are not using. For a small group the Amberjack 32 does the same day for less."),
 ],
 "faqs_es": [
   ("¿Cuántas personas caben en el Chris Craft 45?","Hasta 13, y eso incluye a todos los que suben. Es un límite de la Guardia Costera, no una preferencia."),
   ("¿Tiene baño de verdad?","Sí — baño con ducha y camarote equipado para cambiarse. El Sundancer 40 también tiene los dos; el Amberjack 32 tiene un baño más chico, sin la ducha."),
   ("¿Se puede cocinar o mantener comida fría a bordo?","Hay nevera y microondas en la cocina, y una nevera con hielo en la bañera. Los bizcochos van directo a la nevera cuando llegas."),
   ("¿Es el bote correcto para cuatro personas?","Normalmente no — estarías pagando por espacio que no usas. Para un grupo chico el Amberjack 32 hace el mismo día por menos."),
 ],
},
{
 "id": "sundancer", "slug_en": "sea-ray-sundancer-40-miami.html", "slug_es": "es/sea-ray-sundancer-40-miami.html",
 "name": "Sea Ray Sundancer 40′", "nav_en": "Sea Ray Sundancer 40′", "nav_es": "Sea Ray Sundancer 40′",
 "title_en": "Sea Ray Sundancer 40 Rental Miami | Covered &amp; Shaded | LuxSea",
 "title_es": "Sea Ray Sundancer 40 en Miami | Cubierto y con Sombra | LuxSea",
 "desc_en": "Charter the Sea Ray Sundancer 40 in Miami — covered, shaded all afternoon and the easiest of the three to board. The right boat with grandparents or small kids.",
 "desc_es": "Alquila el Sea Ray Sundancer 40 en Miami — cubierto, con sombra toda la tarde y el más fácil de abordar de los tres. El bote correcto con abuelos o niños chiquitos.",
 "said_en": "The regular", "said_es": "El de siempre",
 "h1_en": "The one with shade, for the people who need it",
 "h1_es": "El que tiene sombra, para quien la necesita",
 "lede_en": "Comfortable, covered and uncomplicated. This is the Sunday-with-the-family boat, and the one we would pick for you if the youngest guest is four or the oldest is seventy.",
 "lede_es": "Cómodo, cubierto y sin complicaciones. Es el bote del domingo en familia, y el que elegiríamos por ti si el más chico tiene cuatro años o el mayor setenta.",
 "hero": "sundancer-40.jpg",
 "hero_alt_en": "The Sea Ray Sundancer anchored off a mangrove island with the Miami skyline behind",
 "hero_alt_es": "El Sea Ray Sundancer anclado frente a una isla de manglares con el skyline de Miami detrás",
 "specs_en": [("Length","40 ft"),("Hours","4 · 5 · 6"),("Shade","Covered"),("Best for","Families"),("Boarding","Easiest of the three"),("Swim platform","Ladder aft")],
 "specs_es": [("Largo","40 pies"),("Horas","4 · 5 · 6"),("Sombra","Cubierto"),("Mejor para","Familias"),("Abordaje","El más fácil"),("Plataforma","Escalera en popa")],
 "body_en": [
   ("Shade is the whole argument",
    ["Six hours of direct Florida sun is not a nice afternoon for a four-year-old or a seventy-year-old, and no amount of sunscreen fixes it. This boat is covered, which is why we do not simply put every family on the biggest hull we own.",
     "The 45 has more room. The 40 has more shade. On a family day shade wins, every time."]),
   ("Easy to get on and off",
    ["It has the lowest boarding of the three and a swim platform with a ladder at the stern. If someone in the group has trouble with steps, say so when you book and the captain brings the boat alongside instead of expecting anyone to drop down into it.",
     "Child-size life jackets are carried as standard. You do not have to ask for them and you do not need to bring your own."]),
   ("Where it goes",
    ["We anchor where the water comes up to about chest height on an adult, over firm sand, so people who are not strong swimmers can stand. The floating pool goes in as soon as we stop.",
     "Late in the day it is also the most comfortable boat to watch the city light up from, because everyone is already sitting down and out of the wind."]),
 ],
 "body_es": [
   ("La sombra es todo el argumento",
    ["Seis horas de sol directo de Florida no son una tarde agradable para un niño de cuatro años ni para alguien de setenta, y no hay bloqueador que lo arregle. Este bote es cubierto, y por eso no metemos a todas las familias en el casco más grande que tenemos.",
     "El 45 tiene más espacio. El 40 tiene más sombra. En un día en familia gana la sombra, siempre."]),
   ("Fácil de subir y bajar",
    ["Tiene el abordaje más bajo de los tres y plataforma de baño con escalera en la popa. Si a alguien del grupo le cuestan los escalones, dilo al reservar y el capitán acerca el bote en vez de esperar que alguien salte adentro.",
     "Los chalecos de talla infantil van de serie. No hay que pedirlos ni traerlos."]),
   ("A dónde va",
    ["Anclamos donde el agua llega más o menos al pecho de un adulto, sobre arena firme, para que quien no nada bien haga pie. La piscina flotante se tira apenas paramos.",
     "Al final del día también es el bote más cómodo para ver encenderse la ciudad, porque todos ya están sentados y fuera del viento."]),
 ],
 "gallery": [
   ("sd-01.jpg","The Sundancer at anchor with the bimini up","El Sundancer fondeado con el bimini puesto"),
   ("sd-02.jpg","The cockpit and wet bar under the canvas","La bañera y el mueble bar bajo la lona"),
   ("sd-03.jpg","Aft sunpad and swim platform","El solárium de popa y la plataforma de baño"),
   ("sd-04.jpg","The cockpit at night alongside the dock","La bañera de noche junto al muelle"),
   ("sd-05.jpg","Looking forward from the helm seat","Mirando a proa desde el asiento del timón"),
   ("sd-06.jpg","The cabin below, looking aft","El camarote de abajo, mirando a popa"),
   ("sd-07.jpg","The V-berth forward","La litera en V a proa"),
   ("sd-08.jpg","The head compartment, with its shower","El baño, con su ducha"),
   ("sd-09.jpg","Straight down over the teak cockpit with the floating pool astern","Vista cenital de la bañera de teca con la piscina flotante por la popa"),
   ("sd-10.jpg","At anchor in the bay with the downtown skyline behind","Fondeado en la bahía con el skyline del downtown detrás"),
   ("sd-11.jpg","The cockpit and wet bar alongside the dock after dark","La bañera y el mueble bar junto al muelle de noche"),
   ("sd-12.jpg","Anchored off the sand with guests swimming alongside","Anclado frente a la arena con invitados nadando al lado"),
   ("sd-13.jpg","The galley and dinette below deck","La cocina y el comedor bajo cubierta"),
   ("sd-14.jpg","Anchored off a mangrove island, floating pool out","Fondeado frente a una isla de manglares, con la piscina flotante afuera"),
   ("sd-15.jpg","Looking aft from the cabin to the steps up","Mirando a popa desde el camarote hacia los escalones"),
 ],
 "faqs_en": [
   ("Is the Sundancer 40 covered?","Yes — it is the shaded boat of the three, which is why we recommend it for families, grandparents and anyone spending a full afternoon out."),
   ("Do you carry life jackets for children?","Yes, child sizes as standard on this boat and on the other two. No need to request them in advance."),
   ("How many guests does it take?","Smaller groups than the Chris Craft 45. Tell us your headcount and we will confirm which boat fits before you book anything."),
   ("Is it easy for older guests to board?","It has the lowest boarding of the three and a stern ladder. Mention mobility when booking and the captain will bring it alongside."),
 ],
 "faqs_es": [
   ("¿El Sundancer 40 es cubierto?","Sí — es el bote con sombra de los tres, y por eso lo recomendamos para familias, abuelos y para cualquiera que pase la tarde completa afuera."),
   ("¿Llevan chalecos para niños?","Sí, tallas infantiles de serie en este bote y en los otros dos. No hace falta pedirlos con anticipación."),
   ("¿Cuántas personas lleva?","Grupos más chicos que el Chris Craft 45. Dinos cuántos son y te confirmamos qué bote sirve antes de que reserves nada."),
   ("¿Es fácil de abordar para gente mayor?","Tiene el abordaje más bajo de los tres y escalera en popa. Menciona la movilidad al reservar y el capitán lo acerca."),
 ],
},
{
 "id": "amberjack", "slug_en": "sea-ray-amberjack-32-miami.html", "slug_es": "es/sea-ray-amberjack-32-miami.html",
 "name": "Sea Ray Amberjack 32′", "nav_en": "Sea Ray Amberjack 32′", "nav_es": "Sea Ray Amberjack 32′",
 "title_en": "Sea Ray Amberjack 32 Miami | Small-Group Sandbar Boat | LuxSea",
 "title_es": "Sea Ray Amberjack 32 en Miami | Bote para Grupos Chicos | LuxSea",
 "desc_en": "The Sea Ray Amberjack 32 — open, quick and pointed at the sandbar. The right LuxSea boat for four or five people who want turquoise water and not much else.",
 "desc_es": "El Sea Ray Amberjack 32 — abierto, rápido y directo al banco de arena. El bote correcto para cuatro o cinco personas que quieren agua turquesa y poco más.",
 "said_en": "The open one", "said_es": "El abierto",
 "h1_en": "Four people, turquoise water, no ceremony",
 "h1_es": "Cuatro personas, agua turquesa, sin ceremonia",
 "lede_en": "The midweek boat — the one people book the same morning they decide to go. Open cockpit, bimini up, and the shortest run to the sandbar of anything we own.",
 "lede_es": "El bote de entre semana — el que se reserva la misma mañana en que se decide salir. Bañera abierta, bimini arriba, y el camino más corto al banco de arena de todo lo que tenemos.",
 "hero": "aj-06.jpg",
 "hero_alt_en": "The Sea Ray Amberjack 32 at anchor in clear turquoise water with the bimini up",
 "hero_alt_es": "El Sea Ray Amberjack 32 fondeado en agua turquesa clara con el bimini puesto",
 "specs_en": [("Length","32 ft"),("Hours","4 · 5 · 6"),("Best for","Small groups"),("Layout","Cockpit + cabin"),("Shade","Bimini"),("Speciality","The sandbar")],
 "specs_es": [("Largo","32 pies"),("Horas","4 · 5 · 6"),("Mejor para","Grupos chicos"),("Cubierta","Bañera + camarote"),("Sombra","Bimini"),("Especialidad","El banco de arena")],
 "body_en": [
   ("The cheapest way to have the same day",
    ["For four or five people the Amberjack does everything the big boat does — the sandbar, the swimming, the skyline on the way back — without charging you for thirteen seats you are not sitting in.",
     "It is open, it is quick, and it gets to turquoise water faster than anything else we run."]),
   ("What it is not",
    ["It is not the boat for a thirteen-person bachelorette, and we will tell you that rather than take the booking. There is a cabin below with an enclosed head and a small galley, but the head is a compact one — toilet and sink, not the shower compartment the other two have — and the shade on deck is a bimini rather than a hardtop.",
     "If the day is long, the group is big, or the occasion is the point, the Chris Craft 45 is the honest answer and we would rather say so up front."]),
   ("What it comes with",
    ["Captain and fuel, cooler on ice, drinking water, speaker, floating pool mat and life jackets in every size — the same standard kit as the other two boats.",
     "Below deck there is a cabin with a V-berth, a head and a galley — small, but real, and more than most open boats this size give you."]),
 ],
 "body_es": [
   ("La forma más barata de tener el mismo día",
    ["Para cuatro o cinco personas el Amberjack hace todo lo que hace el bote grande — el banco de arena, el baño, la ciudad de regreso — sin cobrarte trece asientos en los que no te vas a sentar.",
     "Es abierto, es rápido, y llega al agua turquesa antes que cualquier otra cosa que tengamos."]),
   ("Lo que no es",
    ["No es el bote para una despedida de trece personas, y te lo decimos en vez de tomar la reserva. Abajo hay camarote con baño cerrado y una cocina chica, pero el baño es chico — inodoro y lavamanos, no el compartimiento con ducha que tienen los otros dos — y la sombra en cubierta es un bimini y no un hardtop.",
     "Si el día es largo, el grupo es grande, o la ocasión es lo importante, el Chris Craft 45 es la respuesta honesta y preferimos decirlo de entrada."]),
   ("Qué trae",
    ["Capitán y gasolina, nevera con hielo, agua, bocina, piscina flotante y chalecos de todas las tallas — el mismo equipo de serie que los otros dos botes.",
     "Abajo hay camarote con litera en V, baño y cocina — chicos, pero de verdad, y más de lo que da la mayoría de los botes abiertos de este tamaño."]),
 ],
 "gallery": [
   ("aj-06.jpg","The Amberjack 32 at anchor in turquoise water, bimini up","El Amberjack 32 fondeado en agua turquesa, con el bimini puesto"),
   ("aj-02.jpg","Straight down over the coral bow sunpad and the open cockpit","Vista cenital del solárium coral de proa y la bañera abierta"),
   ("aj-01.jpg","Anchored off a sandbar beach with other boats along the shore","Anclado frente a la playa del banco de arena con otros botes en la orilla"),
   ("aj-03.jpg","The cockpit alongside the dock, coral upholstery and the arch above","La bañera junto al muelle, tapicería coral y el arco arriba"),
   ("aj-04.jpg","Bow on at the dock, the sunpad cover in place","De proa en el muelle, con la funda del solárium puesta"),
   ("aj-05.jpg","The cabin below, with the V-berth and dinette","El camarote de abajo, con la litera en V y el comedor"),
   ("aj-07.jpg","The head, with toilet and sink","El baño, con inodoro y lavamanos"),
   ("aj-08.jpg","The galley, with sink, cooktop, microwave and fridge","La cocina, con fregadero, hornilla, microondas y nevera"),
 ],
 "faqs_en": [
   ("How many people fit on the Amberjack 32?","It is our small-group boat — four or five is where it is happiest. Tell us your headcount and we will confirm before you book."),
   ("Does it have a bathroom?","Yes — an enclosed head with a toilet and sink in the cabin below, next to a small galley with a sink, cooktop, microwave and fridge. What it does not have is the separate shower compartment that the Chris Craft 45 and the Sundancer 40 both have."),
   ("Why is it cheaper?","It is a smaller boat that burns less fuel. For a small group it does the same day for less, which is the only reason it exists in the fleet."),
   ("Is it good for the sandbar?","It is the best of the three for it. Open cockpit, quick to get there, and the floating pool goes in the moment we anchor."),
 ],
 "faqs_es": [
   ("¿Cuántas personas caben en el Amberjack 32?","Es nuestro bote para grupos chicos — cuatro o cinco es donde mejor está. Dinos cuántos son y te confirmamos antes de reservar."),
   ("¿Tiene baño?","Sí — un baño cerrado con inodoro y lavamanos en el camarote de abajo, al lado de una cocina chica con fregadero, hornilla, microondas y nevera. Lo que no tiene es el compartimiento con ducha que sí tienen el Chris Craft 45 y el Sundancer 40."),
   ("¿Por qué es más barato?","Es un bote más chico y gasta menos combustible. Para un grupo pequeño hace el mismo día por menos, que es la única razón por la que está en la flota."),
   ("¿Sirve para el banco de arena?","Es el mejor de los tres para eso. Bañera abierta, llega rápido, y la piscina flotante se tira apenas anclamos."),
 ],
},
]


def boat_page(b, es):
    root = "../" if es else ""
    k = lambda n: b[n + ("_es" if es else "_en")]
    url_en = f"{BASE}/{b['slug_en']}".replace(".html", "")
    url_es = f"{BASE}/{b['slug_es']}".replace(".html", "")
    url_self = url_es if es else url_en
    alt_href = f"{root}{b['slug_en']}" if es else b["slug_es"].split("/")[-1]
    if not es:
        alt_href = "es/" + b["slug_es"].split("/")[-1]

    specs = "".join(
        f'<div><dt>{n}</dt><dd>{v}</dd></div>' for n, v in k("specs"))

    body = ""
    for i, (h2, paras) in enumerate(k("body")):
        ps = "\n        ".join(f"<p>{x}</p>" for x in paras)
        body += f'''  <section class="band{' band--surface' if i % 2 else ''}">
    <div class="wrap wrap--narrow stack-4 rise prose">
      <h2>{h2}</h2>
      {ps}
    </div>
  </section>

'''

    figs = "".join(
        f'<figure><img src="{root}assets/media/{f}" alt="{(ces if es else cen)}" loading="lazy">'
        f'<figcaption>{(ces if es else cen)}</figcaption></figure>'
        for f, cen, ces in b["gallery"])

    faqs = "\n        ".join(
        f'<details{" open" if i == 0 else ""}><summary>{q}</summary><div><p>{a}</p></div></details>'
        for i, (q, a) in enumerate(k("faqs")))

    others = "".join(
        f'<div class="row"><h3><a href="{(o["slug_es"].split("/")[-1] if es else o["slug_en"])}" style="text-decoration:none">{o["nav_es" if es else "nav_en"]}</a></h3>'
        f'<p>{o["lede_es" if es else "lede_en"][:118]}…</p></div>'
        for o in BOATS if o is not b)

    ld = json.dumps({
        "@context": "https://schema.org", "@type": "Product",
        "name": b["name"],
        "description": k("desc"),
        "image": [f"{BASE}/assets/media/{f}" for f, _, _ in b["gallery"]],
        "brand": {"@type": "Brand", "name": b["name"].split()[0]},
        "offers": {"@type": "Offer", "availability": "https://schema.org/InStock",
                   "priceCurrency": "USD", "url": url_self,
                   "seller": {"@type": "LocalBusiness", "name": "LuxSea Miami",
                              "telephone": "+1-786-878-0701"}},
    }, ensure_ascii=False, indent=2)
    faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in k("faqs")]},
        ensure_ascii=False, indent=2)

    lock = '<script>try{localStorage.setItem("luxsea-lang","es")}catch(e){}</script>\n' if es else ""
    avail_h = "Disponibilidad" if es else "Availability"
    gal_h = "Todas las fotos son de un paseo real" if es else "Every photo is from a real charter"
    gal_p = ("Ninguna es de catálogo. Salieron de las publicaciones donde el capitán nombra este bote."
             if es else
             "None of these are stock. They came off the posts where the captain names this boat himself.")

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
<meta property="og:image" content="{BASE}/assets/media/{b["hero"]}">
<meta name="theme-color" content="#12333d">
<link rel="stylesheet" href="{root}styles.css">
{lock}
<script type="application/ld+json">
{ld}
</script>
<script type="application/ld+json">
{faq_ld}
</script>

{header(es, root, alt_href, "Read this page in English" if es else "Ver esta página en español")}

<main id="main">

  <section class="hero">
    <div class="hero__media">
      <img src="{root}assets/media/{b["hero"]}" alt="{k("hero_alt")}" fetchpriority="high">
    </div>
    <div class="hero__scrim" aria-hidden="true"></div>
    <div class="hero__glow" aria-hidden="true"></div>
    <div class="wrap hero__in">
      <span class="said" style="color:var(--sun-hi)">{b["name"]} · {k("said")}</span>
      <h1>{k("h1")}</h1>
      <p class="hero__sub">{k("lede")}</p>
      <div class="btn-row">
        <a class="btn btn--light" data-wa="{"Hola LuxSea — quiero reservar el " + b["name"] if es else "Hi LuxSea — I'd like to book the " + b["name"]}." href="#">{"Consultar una fecha" if es else "Check a date"}</a>
        <a class="btn btn--outline-light" href="{root}contact.html">{"Enviar los detalles" if es else "Send the details"}</a>
      </div>
    </div>
  </section>

  <section class="band band--tight">
    <div class="wrap stack-4 rise">
      <dl class="spec">{specs}</dl>
      <div class="stack-3">
        <h2 style="font-size:var(--step-2)">{avail_h}</h2>
        <div class="avail" data-availability="{b["id"]}" aria-live="polite">
          <p class="avail__note">{"Cargando disponibilidad…" if es else "Loading availability…"}</p>
        </div>
      </div>
    </div>
  </section>

{body}  <section class="band band--surface">
    <div class="wrap stack-4">
      <div class="head rise">
        <span class="said">{"Las fotos" if es else "The gallery"}</span>
        <h2>{gal_h}</h2>
        <p class="lede">{gal_p}</p>
      </div>
      <div class="gallery rise">{figs}</div>
    </div>
  </section>

{svc.kit(es, "band")}

  <section class="band band--bay">
    <div class="wrap wrap--narrow">
      <div class="head rise">
        <span class="said">{"Lo que preguntan" if es else "What people ask"}</span>
        <h2>{b["name"]}</h2>
      </div>
      <div class="faq rise">
        {faqs}
      </div>
    </div>
  </section>

  <section class="band band--drench">
    <div class="wrap cta-final rise">
      <h2>{"Dinos la fecha y te decimos el precio" if es else "Tell us the date, we'll tell you the price"}</h2>
      <p>{"Bote, capitán y gasolina en un solo número." if es else "Boat, captain and fuel in one number."}</p>
      <div class="btn-row" style="justify-content:center">
        <a class="btn btn--light" data-wa="{"Hola LuxSea — quiero reservar el " + b["name"] if es else "Hi LuxSea — I'd like to book the " + b["name"]}." href="#">{"Escribir por WhatsApp" if es else "Message on WhatsApp"}</a>
        <a class="btn btn--outline-light" href="{root}contact.html">{"Enviar los detalles" if es else "Send the details"}</a>
      </div>
    </div>
  </section>

  <section class="band band--tight">
    <div class="wrap">
      <div class="head rise"><h2 style="font-size:var(--step-2)">{"Los otros dos botes" if es else "The other two boats"}</h2></div>
      <div class="rows rise">{others}</div>
    </div>
  </section>

</main>

{footer(es, root)}
'''


# ---------------------------------------------------------------- Spanish home
def spanish_home():
    tiles = "".join(
        f'''<a class="tile{' tile--wide' if i == 0 else ''}" href="{p["slug_es"].split("/")[-1]}">
          <img src="../assets/media/{p["hero_es"][0]}" alt="{p["hero_es"][1]}" loading="lazy">
          <span class="tile__es">{p["said_es"]}</span>
          <h3>{p["nav_es"]}</h3>
        </a>''' for i, p in enumerate(svc.DATA))

    boats = "".join(
        f'''<div class="boat rise{' boat--flip' if i == 1 else ''}">
        <div class="boat__media">
          <img src="../assets/media/{b["hero"]}" alt="{b["hero_alt_es"]}" loading="lazy">
          <span class="boat__tag">{b["said_es"]}</span>
        </div>
        <div class="boat__body">
          <h3 class="boat__name"><a href="{b["slug_es"].split("/")[-1]}" style="text-decoration:none">{b["name"]}</a></h3>
          <p>{b["lede_es"]}</p>
          <dl class="spec">{"".join(f"<div><dt>{n}</dt><dd>{v}</dd></div>" for n, v in b["specs_es"][:3])}</dl>
          <div class="btn-row"><a class="btn btn--primary" href="{b["slug_es"].split("/")[-1]}">Ver el {b["name"].split()[-1]}</a></div>
        </div>
      </div>''' for i, b in enumerate(BOATS))

    ld = json.dumps({
        "@context": "https://schema.org", "@type": "LocalBusiness",
        "name": "LuxSea Miami", "alternateName": "LuxSea - Boat Rental",
        "description": "Renta de botes privados con capitán en Miami. Tres botes propios para cumpleaños, despedidas de soltera, paseos en familia y atardeceres en la bahía.",
        "telephone": "+1-786-878-0701", "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": "Miami Beach",
                    "addressRegion": "FL", "addressCountry": "US"},
        "areaServed": ["Miami", "Miami Beach", "Key Biscayne", "Coconut Grove", "Biscayne Bay"],
        "availableLanguage": ["es", "en"],
        "sameAs": ["https://www.instagram.com/luxseamiami/"],
    }, ensure_ascii=False, indent=2)

    return f'''<html lang="es">
<meta charset="utf-8">
<title>Renta de Botes en Miami | Con Capitán, en Español | LuxSea Miami</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Renta de botes privados en Miami con capitán incluido. Tres botes propios para cumpleaños, despedidas de soltera, paseos en familia y atardeceres. Te atendemos en español.">
<link rel="canonical" href="{BASE}/es/">
<link rel="alternate" hreflang="es" href="{BASE}/es/">
<link rel="alternate" hreflang="en" href="{BASE}/">
<link rel="alternate" hreflang="x-default" href="{BASE}/">
<link rel="icon" href="../assets/mark.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:title" content="Renta de Botes en Miami | Con Capitán, en Español | LuxSea Miami">
<meta property="og:description" content="Tres botes propios, capitán incluido, y todo el día en español. Cumpleaños, despedidas y atardeceres en la bahía de Miami.">
<meta property="og:image" content="{BASE}/assets/media/hero-poster.jpg">
<meta name="theme-color" content="#12333d">
<link rel="stylesheet" href="../styles.css">
<script>try{{localStorage.setItem("luxsea-lang","es")}}catch(e){{}}</script>

<script type="application/ld+json">
{ld}
</script>

{header(True, "../", "../index.html", "Read this page in English")}

<main id="main">

  <section class="hero">
    <div class="hero__media">
      <video autoplay muted loop playsinline preload="metadata" poster="../assets/media/hero-poster.jpg"
             aria-label="Vista aérea de tres botes de LuxSea amarrados juntos en el banco de arena de Miami, con piscinas flotantes al lado en agua verde">
        <source src="../assets/media/hero.mp4" type="video/mp4">
        <img src="../assets/media/hero-poster.jpg" alt="Vista aérea de tres botes de LuxSea amarrados juntos en el banco de arena de Miami, con piscinas flotantes al lado en agua verde">
      </video>
    </div>
    <div class="hero__scrim" aria-hidden="true"></div>
    <div class="hero__glow" aria-hidden="true"></div>
    <div class="wrap hero__in">
      <h1>El mejor día de Miami empieza cuando <span class="sun">baja el sol</span>.</h1>
      <p class="hero__sub">Renta de botes privados con capitán en Miami. Tres botes propios para cumpleaños, despedidas de solteras, paseos en familia y atardeceres en la bahía — y todo el día en español.</p>
      <div class="btn-row">
        <a class="btn btn--light" href="../contact.html">Reservar tu día</a>
        <a class="btn btn--outline-light" href="#botes">Ver los tres botes</a>
      </div>
      <p class="hero__meta">
        <span><strong>3</strong> botes propios, no una flota alquilada</span>
        <span>Hasta <strong>13</strong> personas a bordo</span>
        <span>Hablas con el <strong>capitán</strong>, no con un bróker</span>
      </p>
    </div>
  </section>

  <section class="strip" aria-labelledby="q-h">
    <div class="wrap">
      <div class="strip__head">
        <h2 id="q-h">Mira una fecha antes de escribir</h2>
        <p>Dinos el día y te mandamos el total por WhatsApp: bote, capitán y gasolina en una sola cifra, en español o en inglés.</p>
      </div>
      <form data-enquiry>
        <div class="field"><label for="q-date">¿Qué día?</label><input type="date" id="q-date" name="date" required></div>
        <div class="field"><label for="q-hours">¿Cuántas horas?</label>
          <select id="q-hours" name="hours"><option selected>4 horas — lo más pedido</option><option>5 horas</option><option>6 horas</option><option>Todavía no sé</option></select>
        </div>
        <div class="field"><label for="q-guests">¿Cuántas personas?</label><input type="number" id="q-guests" name="guests" min="1" max="13" value="8" required></div>
        <button class="btn btn--primary" type="submit"><svg class="btn__ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.96L2 22l5.25-1.38a9.9 9.9 0 0 0 4.79 1.22c5.46 0 9.92-4.45 9.92-9.91C21.96 6.45 17.5 2 12.04 2Zm5.8 14.16c-.24.68-1.2 1.26-1.96 1.42-.52.11-1.2.2-3.49-.75-2.93-1.21-4.81-4.18-4.96-4.38-.14-.2-1.18-1.57-1.18-3s.75-2.13 1.02-2.42c.26-.29.58-.36.77-.36h.55c.18 0 .42-.03.65.5.24.57.82 1.99.89 2.14.7.14.12.31.02.51-.1.2-.14.32-.29.49-.14.17-.3.38-.43.51-.14.14-.29.3-.13.58.17.29.74 1.22 1.59 1.98 1.09.97 2.01 1.27 2.3 1.42.29.14.46.12.63-.7.17-.2.72-.85.92-1.14.19-.29.39-.24.65-.14.26.09 1.67.79 1.96.93.29.14.48.22.55.34.07.12.07.69-.17 1.36Z"/></svg><span>Pedir precio por WhatsApp</span></button>
        <p class="strip__fine">Sin cargo de reserva. Normalmente contestamos el mismo día.</p>
        <p class="vh" role="status" data-status></p>
      </form>
    </div>
  </section>

  <section class="band band--drench">
    <div class="wrap">
      <div class="head head--split rise">
        <h2>Tres botes. Un capitán. Ningún intermediario.</h2>
        <p class="lede">Casi todo lo que ves en Miami es un bróker alquilando el bote de otro. Estos tres son nuestros, y el que te contesta el mensaje es el que maneja.</p>
      </div>
      <div class="rows">
        <div class="row rise"><h3>Un solo número, antes de subir</h3>
          <p>Bote, capitán y gasolina en una sola cifra. Nada de cargos de reserva ni sorpresas en el muelle. Nos mandas la fecha y te llega el total.</p></div>
        <div class="row rise"><h3>Todo el día en español</h3>
          <p>La reserva, el paseo completo y las instrucciones de seguridad en español. Si una persona a bordo no entiende qué hacer, todos están menos seguros — por eso lo decimos aquí y no en letra chica.</p></div>
        <div class="row rise"><h3>Vienes a celebrar, no a posar</h3>
          <p>Trae el bizcocho, la comida, los globos y tu playlist. Llegamos temprano, montamos el bote y guardamos el bizcocho en frío hasta que lo pidas.</p></div>
      </div>
    </div>
  </section>

  <section class="band" id="botes" aria-labelledby="botes-h">
    <div class="wrap">
      <div class="head head--split rise">
        <div><span class="said">Los tres, y nada más</span><h2 id="botes-h">Una flota pequeña, a propósito</h2></div>
        <p class="lede">Tres botes que conocemos de memoria. Cada uno hace bien un día distinto.</p>
      </div>
      {boats}
    </div>
  </section>

  <section class="band band--surface" aria-labelledby="cel-h">
    <div class="wrap">
      <div class="head head--split rise">
        <div><span class="said">Para qué nos llaman</span><h2 id="cel-h">Casi nadie sale al mar sin una razón</h2></div>
        <p class="lede">Estas son las diez razones por las que suena el teléfono. Si la tuya no está aquí, igual la hacemos.</p>
      </div>
      <div class="tiles tiles--six rise">
        {tiles}
      </div>
    </div>
  </section>

{svc.kit(True, 'band')}

  <section class="band band--bay">
    <div class="wrap cta-final rise">
      <span class="said">Nos vemos en el muelle</span>
      <h2>Dinos la fecha y te decimos el precio</h2>
      <p>Contesta el capitán, normalmente en menos de una hora.</p>
      <div class="btn-row" style="justify-content:center">
        <a class="btn btn--primary" data-wa="Hola LuxSea — quiero consultar una fecha." href="#">Escribir por WhatsApp</a>
        <a class="btn btn--outline-light" href="../contact.html">Enviar los detalles</a>
      </div>
    </div>
  </section>

</main>

{footer(True, "../")}
'''


if __name__ == "__main__":
    (OUT / "es").mkdir(exist_ok=True)
    n = 0
    for b in BOATS:
        for es in (False, True):
            (OUT / (b["slug_es"] if es else b["slug_en"])).write_text(boat_page(b, es), encoding="utf-8")
            n += 1
    (OUT / "es" / "index.html").write_text(spanish_home(), encoding="utf-8")

    # Full sitemap, written here because this script runs last and sees everything.
    urls = [f'  <url><loc>{BASE}/</loc></url>', f'  <url><loc>{BASE}/es/</loc></url>']
    for s in ("fleet.html", "experiences.html", "about.html", "contact.html"):
        urls.append(f'  <url><loc>{BASE}/{s[:-5]}</loc></url>')
    pairs = [(p["slug_en"], p["slug_es"]) for p in svc.DATA] + [(b["slug_en"], b["slug_es"]) for b in BOATS]
    for en, es_ in pairs:
        a, z = f"{BASE}/{en[:-5]}", f"{BASE}/{es_[:-5]}"
        for loc, other, lang in ((a, z, "es"), (z, a, "en")):
            back = "en" if lang == "es" else "es"
            urls.append(
                f'  <url><loc>{loc}</loc>\n'
                f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{other}"/>\n'
                f'    <xhtml:link rel="alternate" hreflang="{back}" href="{loc}"/>\n'
                f'  </url>')
    head = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n')
    (OUT / "sitemap.xml").write_text(head + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    print(f"wrote {n} boat pages + es/index.html + sitemap.xml ({len(urls)} urls)")
