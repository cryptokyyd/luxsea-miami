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
  }
  burger.addEventListener('click', function () {
    var open = burger.getAttribute('aria-expanded') === 'true';
    panel.classList.toggle('is-open', !open);
    burger.setAttribute('aria-expanded', String(!open));
  });
  panel.addEventListener('click', function (e) { if (e.target.tagName === 'A') close(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
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
   6. Enquiry forms → a prefilled WhatsApp message.
   No backend, no dead endpoint. Validates before it sends.
   ------------------------------------------------------------------ */
(function enquiry() {
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
