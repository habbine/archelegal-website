/* Archè — small progressive enhancements. Site works without JS. */
(function () {
  "use strict";

  // Mobile nav
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Time bridge: Paris / Seoul / Hong Kong office hours
  var bridge = document.getElementById("bridge");
  if (bridge && window.Intl) {
    var OPEN = 9, CLOSE = 18;
    var rows = bridge.querySelectorAll("[data-tz]");
    var L = {
      open: bridge.getAttribute("data-open") || "Open now",
      closed: bridge.getAttribute("data-closed") || "Closed"
    };

    function offsetHours(tz, date) {
      var p = new Intl.DateTimeFormat("en-GB", {
        timeZone: tz, hourCycle: "h23",
        year: "numeric", month: "2-digit", day: "2-digit",
        hour: "2-digit", minute: "2-digit", second: "2-digit"
      }).formatToParts(date).reduce(function (a, x) { a[x.type] = x.value; return a; }, {});
      var asUTC = Date.UTC(+p.year, +p.month - 1, +p.day, +p.hour, +p.minute, +p.second);
      return (asUTC - Math.floor(date.getTime() / 1000) * 1000) / 3600000;
    }
    function parts(tz, date) {
      var f = new Intl.DateTimeFormat("en-GB", {
        timeZone: tz, hourCycle: "h23", hour: "2-digit", minute: "2-digit", weekday: "short"
      }).formatToParts(date).reduce(function (a, x) { a[x.type] = x.value; return a; }, {});
      return { h: +f.hour, m: +f.minute, wd: f.weekday, str: f.hour + ":" + f.minute };
    }

    function render() {
      var now = new Date();
      var parisOff = offsetHours("Europe/Paris", now);
      var pParis = parts("Europe/Paris", now);
      rows.forEach(function (row) {
        var tz = row.getAttribute("data-tz");
        var p = parts(tz, now);
        var weekend = (p.wd === "Sat" || p.wd === "Sun");
        var isOpen = !weekend && p.h >= OPEN && p.h < CLOSE;
        row.querySelector(".time").textContent = p.str;
        var dot = row.querySelector(".dot");
        dot.className = "dot" + (isOpen ? " open" : "");
        row.querySelector(".label").textContent = isOpen ? L.open : L.closed;

        // 24h strip, aligned on Paris time
        var diff = offsetHours(tz, now) - parisOff;
        var track = row.querySelector(".track");
        if (track && !track.dataset.built) {
          for (var i = 0; i < 24; i++) track.appendChild(document.createElement("i"));
          var mark = document.createElement("span");
          mark.className = "now";
          track.appendChild(mark);
          track.dataset.built = "1";
        }
        if (track) {
          var cells = track.querySelectorAll("i");
          for (var h = 0; h < 24; h++) {
            var local = ((h + diff) % 24 + 24) % 24;
            cells[h].className = (local >= OPEN && local < CLOSE) ? "on" : "";
          }
          var frac = (pParis.h + pParis.m / 60) / 24;
          track.querySelector(".now").style.left = "calc(" + (frac * 100) + "% - 1px)";
        }
      });
    }
    render();
    setInterval(render, 30000);
  }

  // Contact form: open the visitor's email app with every answer written into the message.
  // Labels and texts come from the page, so the email is in the page's language.
  document.querySelectorAll("form.contact").forEach(function (form) {
    function labelOf(name) {
      var field = form.querySelector('[name="' + name + '"]');
      var label = field && field.closest("label");
      if (!label) return name;
      var text = "";
      label.childNodes.forEach(function (n) { if (n.nodeType === 3) text += n.textContent; });
      return text.trim() || name;
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form-status");
      var to = form.getAttribute("data-to");
      var d = new FormData(form);
      function v(k) { return String(d.get(k) || "").trim(); }
      var topic = v("topic");
      var sep = form.getAttribute("data-sep") || ": ";

      var subject = (form.getAttribute("data-subject") || "Website enquiry") +
        sep + topic;
      // Name, position and company are left blank at the top for the sender to fill in.
      var intro = [];
      try { intro = JSON.parse(form.getAttribute("data-intro") || "[]"); } catch (err) {}
      var bare = sep.replace(/\s+$/, "");
      var body = intro.map(function (label) { return label + bare + " "; })
        .concat(["", labelOf("topic") + sep + topic, "", labelOf("object") + bare, v("object")])
        .join("\r\n");

      window.location.href = "mailto:" + to +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);

      if (!status) return;
      // For visitors without an email app on this device (webmail only).
      status.textContent = (form.getAttribute("data-mail") || "") + " " +
        (form.getAttribute("data-fallback") || "") + " ";
      var link = document.createElement("a");
      link.href = "mailto:" + to;
      link.textContent = to;
      status.appendChild(link);
      if (navigator.clipboard) {
        status.appendChild(document.createTextNode(" "));
        var copy = document.createElement("button");
        copy.type = "button";
        copy.className = "copy-message";
        copy.textContent = form.getAttribute("data-copy") || "Copy";
        copy.addEventListener("click", function () {
          navigator.clipboard.writeText(to + "\n" + subject + "\n\n" + body).then(function () {
            copy.textContent = form.getAttribute("data-copied") || "Copied";
          }, function () {});
        });
        status.appendChild(copy);
      }
    });
  });
})();

(function(){var d=document.querySelector('dialog.lightbox');if(!d)return;var im=d.querySelector('img'),cap=d.querySelector('p');
document.querySelectorAll('.gallery .g-open').forEach(function(b){b.addEventListener('click',function(){var f=b.closest('figure'),i=b.querySelector('img');im.src=i.currentSrc||i.src;im.alt=i.alt;cap.textContent=f.querySelector('figcaption').textContent;if(d.showModal)d.showModal();});});
d.addEventListener('click',function(e){if(e.target===d)d.close();});})();
