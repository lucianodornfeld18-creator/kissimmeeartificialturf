(function () {
  "use strict";
  var d = document;
  d.documentElement.classList.remove("nojs");
  function track(name, params) {
    try { (window.__katEvents = window.__katEvents || []).push([name, params || {}]); if (window.gtag) window.gtag("event", name, params || {}); } catch (e) {}
  }
  var b = d.getElementById("navb"), n = d.getElementById("nav");
  if (b && n) {
    b.addEventListener("click", function () {
      var open = n.classList.toggle("open");
      b.setAttribute("aria-expanded", open ? "true" : "false");
    });
    d.addEventListener("keydown", function (e) { if (e.key === "Escape" && n.classList.contains("open")) { n.classList.remove("open"); b.setAttribute("aria-expanded", "false"); b.focus(); } });
  }
  [].forEach.call(d.querySelectorAll('a[href^="tel:"]'), function (a) { a.addEventListener("click", function () { track("tel_click", { page: location.pathname }); }); });
  [].forEach.call(d.querySelectorAll('a[href^="sms:"]'), function (a) { a.addEventListener("click", function () { track("sms_click", { page: location.pathname }); }); });
  [].forEach.call(d.querySelectorAll("form.lead"), function (f) {
    if (f.getAttribute("data-opera") === "skip") return;
    var started = false;
    var pu = f.querySelector('[name="page_url"]'); if (pu) pu.value = location.href.split("#")[0].slice(0, 300);
    f.addEventListener("focusin", function () { if (!started) { started = true; track("form_start", { page: location.pathname }); } });
    f.addEventListener("invalid", function () { track("form_error", { page: location.pathname }); }, true);
    f.addEventListener("submit", function (ev) {
      try {
        var v = function (k) { var e = f.querySelector('[name="' + k + '"]'); return (e && e.value) || ""; };
        var s = f.querySelector('[name="subject"]');
        if (s) s.value = "[Kissimmee Artificial Turf] " + (v("service") || "Quote request") + " · " + (v("city") || "no city") + " · " + v("name");
      } catch (e) {}
      track("form_submit", { page: location.pathname });
      var btn = f.querySelector('button[type="submit"]'); if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
      /* Send in the background so the visitor lands on our own thank-you page. Without fetch, the normal POST still works. */
      if (!window.fetch || !window.FormData) return;
      ev.preventDefault();
      var data = {}; new FormData(f).forEach(function (val, key) { if (typeof val === "string") data[key] = val; });
      delete data.redirect;
      var fail = function () {
        track("form_error", { page: location.pathname, reason: "delivery" });
        if (btn) { btn.disabled = false; btn.textContent = "Request my quote"; }
        var m = f.querySelector(".ferr"); if (!m) { m = d.createElement("p"); m.className = "ferr full"; m.setAttribute("role", "alert"); f.appendChild(m); }
        m.textContent = "That didn't go through. Please call or text (689) 202-3710 and we'll take it from there.";
      };
      fetch(f.action, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().catch(function () { return { success: r.ok }; }); })
        .then(function (j) { if (j && j.success) { location.href = "/thank-you/"; } else { fail(); } })
        .catch(fail);
    });
  });

  /* cost calculator (/artificial-turf-cost/calculator/) */
  var calc = d.getElementById("calc");
  if (calc) {
    var R = JSON.parse(calc.getAttribute("data-rates"));
    var out = d.getElementById("calc-out");
    var run = function () {
      var L = parseFloat(calc.elements.len.value) || 0, W = parseFloat(calc.elements.wid.value) || 0, A = parseFloat(calc.elements.area.value) || L * W;
      var r = R[calc.elements.kind.value]; if (!A || !r) { out.textContent = "Enter a length and width, or an area."; return; }
      var rm = calc.elements.remove.checked ? [1, 2] : [0, 0];
      var lo = Math.round(A * (r[0] + rm[0]) / 50) * 50, hi = Math.round(A * (r[1] + rm[1]) / 50) * 50;
      var base = (A * (3 / 12) / 27 * 1.15), infill = A * 1.5;
      out.innerHTML = "<strong>" + Math.round(A).toLocaleString() + " sq ft:</strong> about $" + lo.toLocaleString() + " to $" + hi.toLocaleString() + " installed. Materials for planning: roughly " + base.toFixed(1) + " cubic yards of crushed base at 3 inches (15% compaction allowance) and about " + Math.round(infill).toLocaleString() + " lb of infill at 1.5 lb per sq ft. Market range, not a quote.";
    };
    calc.addEventListener("input", run); calc.addEventListener("submit", function (e) { e.preventDefault(); run(); });
  }
  /* turf vs sod 10-year (/tools/turf-vs-sod/) */
  var ts = d.getElementById("tvs");
  if (ts) {
    var o2 = d.getElementById("tvs-out");
    var go = function () {
      var A = parseFloat(ts.elements.area.value) || 0, tr = parseFloat(ts.elements.turf.value) || 12, mow = parseFloat(ts.elements.mow.value) || 0, water = parseFloat(ts.elements.water.value) || 0, other = parseFloat(ts.elements.other.value) || 0;
      if (!A) { o2.textContent = "Enter the lawn area."; return; }
      var turf = A * tr + 10 * Math.max(150, A * 0.3), sod = A * 1.5 + 10 * 12 * (mow + water) + 10 * other + A * 1.5;
      var yr = 0, tc = A * tr, sc = A * 1.5; while (yr < 30 && tc > sc) { yr++; tc += Math.max(150, A * 0.3); sc += 12 * (mow + water) + other + (yr === 6 ? A * 1.5 : 0); }
      o2.innerHTML = "<strong>Ten years, " + Math.round(A).toLocaleString() + " sq ft:</strong> turf about $" + Math.round(turf).toLocaleString() + ", natural grass about $" + Math.round(sod).toLocaleString() + " (includes one re-sod). " + (yr < 30 ? "Turf catches up in roughly year " + yr + "." : "With these numbers grass stays cheaper.") + " Your inputs, simple arithmetic, no inflation.";
    };
    ts.addEventListener("input", go); ts.addEventListener("submit", function (e) { e.preventDefault(); go(); });
  }
})();

/* Opera portal: mirrors each lead into the CRM without touching the form's own delivery.
   Fires on submit (capture), uses sendBeacon, never throws. */
(function () {
  var EP = "https://opera-portal.lucianodornfeld18.workers.dev/api/lead";
  var BRAND = "kissimmee-turf";
  var KEYS = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "fbclid"];
  try {
    var q = new URLSearchParams(location.search);
    KEYS.forEach(function (k) { var v = q.get(k); if (v) sessionStorage.setItem("op_" + k, v); });
    if (!sessionStorage.getItem("op_landing")) sessionStorage.setItem("op_landing", location.href);
  } catch (e) {}
  document.addEventListener("submit", function (ev) {
    try {
      var f = ev.target;
      if (!f || f.tagName !== "FORM" || !f.classList.contains("lead") || f.getAttribute("data-opera") === "skip") return;
      if (f.checkValidity && !f.checkValidity()) return;
      var fd = new FormData(f), g = function (k) { var v = fd.get(k); return (typeof v === "string" ? v : "").trim(); };
      var p = new URLSearchParams();
      p.set("brand", BRAND); p.set("name", g("name")); p.set("phone", g("phone")); p.set("email", g("email"));
      p.set("job_type", g("service")); p.set("address", g("city"));
      p.set("message", [g("message"), g("size") && "Area: " + g("size"), g("pets") && "Dogs: " + g("pets"), g("hoa") && "HOA: " + g("hoa")].filter(Boolean).join(" | "));
      p.set("company_website", fd.get("botcheck") ? "bot" : "");
      if (!p.get("name") && !p.get("phone") && !p.get("email")) return;
      var land = "";
      try { KEYS.forEach(function (k) { var v = sessionStorage.getItem("op_" + k); if (v) p.set(k, v); }); land = sessionStorage.getItem("op_landing") || ""; } catch (e) {}
      p.set("page", land || location.href); p.set("referrer", document.referrer || "");
      if (!(navigator.sendBeacon && navigator.sendBeacon(EP, p))) { fetch(EP, { method: "POST", body: p, keepalive: true, mode: "no-cors" }).catch(function () {}); }
    } catch (e) {}
  }, true);
})();
