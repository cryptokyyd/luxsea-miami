/* LUXSEA MIAMI — shared behaviour.
   No framework, no build step. Progressive: everything works with JS off
   except the language toggle and the WhatsApp message composer. */

/* ------------------------------------------------------------------
   1. CONTACT CONFIG  ← the only block the owner needs to edit.
   Put the real numbers in and every CTA on every page updates.
   ------------------------------------------------------------------ */
const LUXSEA = {
  // Taken from the captions on @luxseamiami. Two variants were posted —
  // 786 878 0701 and 786 878 0107. CONFIRM which one is live before launch.
  whatsapp: '17868780701',        // international format, digits only, for wa.me
  phone:    '(786) 878-0701',
  instagram: 'https://www.instagram.com/luxseamiami/'
};

document.documentElement.classList.add('js');

/* ------------------------------------------------------------------
   2. Wire contact config into the page
   ------------------------------------------------------------------ */
(function contact() {
  document.querySelectorAll('[data-tel]').forEach(function (el) {
    el.href = 'tel:' + LUXSEA.phone.replace(/[^\d+]/g, '');
    if (el.dataset.tel === 'text') el.textContent = LUXSEA.phone;
  });
  document.querySelectorAll('[data-wa]').forEach(function (el) {
    var msg = el.dataset.wa || '';
    el.href = 'https://wa.me/' + LUXSEA.whatsapp + (msg ? '?text=' + encodeURIComponent(msg) : '');
    el.target = '_blank';
    el.rel = 'noopener';
  });
})();

/* ------------------------------------------------------------------
   3. Language toggle (ES/EN)
   Any element carrying data-es swaps its text. Placeholders use data-es-ph.
   The English copy is the markup, so the page is correct with JS disabled.
   ------------------------------------------------------------------ */
(function language() {
  var btn = document.querySelector('[data-lang-toggle]');
  if (!btn) return;

  var nodes = document.querySelectorAll('[data-es]');
  var fields = document.querySelectorAll('[data-es-ph]');

  nodes.forEach(function (el) { el.dataset.en = el.innerHTML; });
  fields.forEach(function (el) { el.dataset.enPh = el.placeholder; });

  function apply(lang) {
    var es = lang === 'es';
    nodes.forEach(function (el) { el.innerHTML = es ? el.dataset.es : el.dataset.en; });
    fields.forEach(function (el) { el.placeholder = es ? el.dataset.esPh : el.dataset.enPh; });
    document.documentElement.lang = es ? 'es' : 'en';
    // Shows the language you'd switch TO. Two characters keeps the phone header
    // inside 375px, which the ES / EN form did not.
    btn.textContent = es ? 'EN' : 'ES';
    btn.setAttribute('aria-label', es ? 'Switch to English' : 'Cambiar a español');
    try { localStorage.setItem('luxsea-lang', lang); } catch (e) { /* private mode */ }
  }

  var saved;
  try { saved = localStorage.getItem('luxsea-lang'); } catch (e) { saved = null; }
  if (!saved && (navigator.language || '').toLowerCase().indexOf('es') === 0) saved = 'es';
  apply(saved === 'es' ? 'es' : 'en');

  btn.addEventListener('click', function () {
    apply(document.documentElement.lang === 'es' ? 'en' : 'es');
  });
})();

/* ------------------------------------------------------------------
   4. Mobile nav
   ------------------------------------------------------------------ */
(function nav() {
  var burger = document.querySelector('.burger');
  var panel = document.getElementById('mobile-nav');
  if (!burger || !panel) return;

  function close() {
    panel.classList.remove('is-open');
    burger.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('nav-open');
  }
  burger.addEventListener('click', function () {
    var open = burger.getAttribute('aria-expanded') === 'true';
    panel.classList.toggle('is-open', !open);
    burger.setAttribute('aria-expanded', String(!open));
    // The sticky CTA hides while the drawer is open; a tall drawer reaches the
    // bottom of the screen and would otherwise run underneath it.
    document.body.classList.toggle('nav-open', !open);
  });
  panel.addEventListener('click', function (e) { if (e.target.tagName === 'A') close(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
})();

/* ------------------------------------------------------------------
   4b. Nav dropdowns.
   CSS already opens them on hover and on focus-within, which covers mouse and
   keyboard. This adds the tap: a touch device fires no hover, so the chevron
   has to be a real button.
   ------------------------------------------------------------------ */
(function navMenus() {
  var items = document.querySelectorAll('.nav__item');
  if (!items.length) return;

  function closeAll(except) {
    items.forEach(function (item) {
      if (item === except) return;
      item.classList.remove('is-open');
      var b = item.querySelector('.nav__more');
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  }

  items.forEach(function (item) {
    var btn = item.querySelector('.nav__more');
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var open = item.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', String(open));
      closeAll(item);
    });
  });

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    var open = document.querySelector('.nav__item.is-open');
    closeAll(null);
    // Send focus back to the control that opened it, not to the top of the page.
    if (open) { var b = open.querySelector('.nav__more'); if (b) b.focus(); }
  });

  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav__item')) closeAll(null);
  });
})();

/* ------------------------------------------------------------------
   5. Reveal — enhances content that is already visible and already painted.
   Nothing is gated on this running.
   ------------------------------------------------------------------ */
(function reveal() {
  var items = document.querySelectorAll('.rise');
  if (!items.length) return;

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) {
    items.forEach(function (el) { el.classList.add('is-in'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry, i) {
      if (!entry.isIntersecting) return;
      var el = entry.target;
      var delay = parseInt(el.dataset.delay || (i * 70), 10);
      setTimeout(function () { el.classList.add('is-in'); }, delay);
      io.unobserve(el);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

  items.forEach(function (el) { io.observe(el); });

  // Safety net: if anything is still hidden after load, show it.
  window.addEventListener('load', function () {
    setTimeout(function () {
      document.querySelectorAll('.rise:not(.is-in)').forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight) el.classList.add('is-in');
      });
    }, 400);
  });
})();

/* ------------------------------------------------------------------
   5b. Hero video: still footage for anyone who asked for less motion.
   The poster frame stays, so the hero never goes blank.
   ------------------------------------------------------------------ */
(function heroVideo() {
  var v = document.querySelector('.hero__media video');
  if (!v) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    v.removeAttribute('autoplay');
    v.pause();
  }
})();

/* ------------------------------------------------------------------
   5c. Availability calendars.
   Reads /api/availability, which returns busy DATES only — no titles, no
   customer names. Renders two months per boat. If the feed is not configured
   (or we're on a static preview with no /api), it falls back to a plain
   "message us" line rather than implying every date is free.
   ------------------------------------------------------------------ */
(function availability() {
  var mounts = document.querySelectorAll('[data-availability]');
  if (!mounts.length) return;

  var ES = { mon: ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'],
             dow: ['L','M','X','J','V','S','D'], booked: 'Reservado', free: 'Libre',
             note: 'Se actualiza solo desde el calendario del capitán. Si tu día aparece libre, casi siempre lo está — confírmalo por WhatsApp.',
             off: 'Escríbenos por WhatsApp y te confirmamos la fecha al momento.' };
  var EN = { mon: ['January','February','March','April','May','June','July','August','September','October','November','December'],
             dow: ['M','T','W','T','F','S','S'], booked: 'Booked', free: 'Open',
             note: 'Updated straight from the captain’s calendar. If your day shows open it almost certainly is — confirm it on WhatsApp.',
             off: 'Message us on WhatsApp and we’ll confirm the date straight away.' };

  function iso(d) { return d.toISOString().slice(0, 10); }

  function month(base, offset, busy, L, todayIso) {
    var d = new Date(Date.UTC(base.getUTCFullYear(), base.getUTCMonth() + offset, 1));
    var y = d.getUTCFullYear(), m = d.getUTCMonth();
    var first = (new Date(Date.UTC(y, m, 1)).getUTCDay() + 6) % 7;   // Monday-first
    var len = new Date(Date.UTC(y, m + 1, 0)).getUTCDate();
    var cells = '';
    for (var i = 0; i < first; i++) cells += '<div class="avail__d avail__d--pad"></div>';
    for (var day = 1; day <= len; day++) {
      var key = iso(new Date(Date.UTC(y, m, day)));
      var cls = 'avail__d';
      if (busy.indexOf(key) !== -1) cls += ' avail__d--busy';
      if (key < todayIso) cls += ' avail__d--past';
      cells += '<div class="' + cls + '" title="' + key + (busy.indexOf(key) !== -1 ? ' · ' + L.booked : '') + '">' + day + '</div>';
    }
    return '<div class="avail__m"><div class="avail__mh">' + L.mon[m] + ' ' + y + '</div>' +
           '<div class="avail__grid" role="presentation">' +
           L.dow.map(function (x) { return '<div class="avail__dow">' + x + '</div>'; }).join('') +
           cells + '</div></div>';
  }

  mounts.forEach(function (el) {
    var boat = el.dataset.availability;
    var L = document.documentElement.lang === 'es' ? ES : EN;
    var today = new Date();
    var todayIso = iso(today);

    fetch('/api/availability?boat=' + encodeURIComponent(boat))
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (data) {
        if (!data.configured) throw new Error('not configured');
        var busy = data.busy || [];
        el.innerHTML =
          '<div class="avail__months">' + month(today, 0, busy, L, todayIso) + month(today, 1, busy, L, todayIso) + '</div>' +
          '<p class="avail__key"><span><i style="background:var(--ember)"></i>' + L.booked + '</span>' +
          '<span><i style="background:var(--surface);outline:1px solid var(--line)"></i>' + L.free + '</span></p>' +
          '<p class="avail__note">' + L.note + '</p>';
        var block = el.closest('[data-avail-block]');
        if (block) block.hidden = false;          // only now is there anything to show
      })
      .catch(function () {
        // No feed configured, or no /api at all. Say nothing rather than take
        // up a heading to tell people to do what the page already asks them to.
        var block = el.closest('[data-avail-block]');
        if (block) block.hidden = true; else el.innerHTML = '';
      });
  });
})();

/* ------------------------------------------------------------------
   6. Enquiry forms → a prefilled WhatsApp message.
   No backend, no dead endpoint. Validates before it sends.
   ------------------------------------------------------------------ */
(function enquiry() {
  // Nobody can charter a boat last Tuesday. Set the floor to today so the
  // picker cannot offer a date the captain would only have to reject.
  var today = new Date();
  var iso = new Date(today.getTime() - today.getTimezoneOffset() * 60000)
              .toISOString().slice(0, 10);
  document.querySelectorAll('form[data-enquiry] input[type="date"]')
    .forEach(function (input) { if (!input.min) input.min = iso; });

  document.querySelectorAll('form[data-enquiry]').forEach(function (form) {
    var status = form.querySelector('[data-status]');

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;

      var d = new FormData(form);
      var es = document.documentElement.lang === 'es';
      var lines = es
        ? ['¡Hola LuxSea! Quiero reservar un día en el agua.', '']
        : ['Hi LuxSea — I\'d like to book a day on the water.', ''];

      var labels = es
        ? { date: 'Fecha', hours: 'Horas', guests: 'Personas', boat: 'Barco', occasion: 'Ocasión', name: 'Nombre', notes: 'Notas' }
        : { date: 'Date', hours: 'Hours', guests: 'Guests', boat: 'Boat', occasion: 'Occasion', name: 'Name', notes: 'Notes' };

      Object.keys(labels).forEach(function (k) {
        var v = (d.get(k) || '').toString().trim();
        if (v) lines.push(labels[k] + ': ' + v);
      });

      window.open('https://wa.me/' + LUXSEA.whatsapp + '?text=' + encodeURIComponent(lines.join('\n')),
                  '_blank', 'noopener');

      if (status) {
        status.textContent = es
          ? 'Abrimos WhatsApp con tu mensaje listo. Si no se abrió, escríbenos directo.'
          : 'WhatsApp opened with your message ready. If it did not open, message us directly.';
      }
    });
  });
})();

/* ------------------------------------------------------------------
   6. Sticky WhatsApp bar.
   The hero buttons scroll away within a screen, and the sticky header only
   carries "Book a day", which opens the contact form rather than WhatsApp —
   his actual channel. On a phone that left the main action off-screen for the
   whole page. Injected here rather than in the markup so all 33 pages get it
   from one place; CSS decides where it shows.
   ------------------------------------------------------------------ */
(function stickyCta() {
  var source = document.querySelector('[data-wa]');
  if (!source) return;

  var es = document.documentElement.lang === 'es';
  var bar = document.createElement('div');
  bar.className = 'sticky-cta';
  bar.hidden = true;
  var a = document.createElement('a');
  a.className = 'btn btn--primary';
  // Reuse whatever message this page already puts on its first WhatsApp
  // button, so the sticky one never says something more generic than the page.
  a.href = 'https://wa.me/' + LUXSEA.whatsapp +
           (source.dataset.wa ? '?text=' + encodeURIComponent(source.dataset.wa) : '');
  a.target = '_blank';
  a.rel = 'noopener';
  a.innerHTML = document.querySelector('.btn__ico')
    ? document.querySelector('.btn__ico').outerHTML + (es ? 'Escribir por WhatsApp' : 'Message on WhatsApp')
    : (es ? 'Escribir por WhatsApp' : 'Message on WhatsApp');
  bar.appendChild(a);
  document.body.appendChild(bar);

  // Show once the opening buttons are gone; hide again over the closing CTA,
  // so the page never shows the same action twice at once.
  var opening = document.querySelector('.hero .btn-row') || document.querySelector('.strip');
  var closing = document.querySelector('.cta-final');
  var passedOpening = false, overClosing = false;

  function sync() {
    var show = passedOpening && !overClosing;
    bar.hidden = !show;
    document.body.classList.toggle('has-sticky-cta', show);
  }

  if (!('IntersectionObserver' in window)) return;   // bar simply stays hidden

  if (opening) {
    new IntersectionObserver(function (entries) {
      var e = entries[0];
      passedOpening = !e.isIntersecting && e.boundingClientRect.top < 0;
      sync();
    }, { threshold: 0 }).observe(opening);
  } else {
    // No opening buttons to scroll past — the contact page is the case. Wait for
    // a screenful rather than covering the booking form the moment it loads.
    window.addEventListener('scroll', function () {
      var passed = window.scrollY > window.innerHeight * 0.6;
      if (passed !== passedOpening) { passedOpening = passed; sync(); }
    }, { passive: true });
  }

  if (closing) {
    new IntersectionObserver(function (es_) {
      overClosing = es_[0].isIntersecting;
      sync();
    }, { threshold: 0 }).observe(closing);
  }
  sync();
})();
