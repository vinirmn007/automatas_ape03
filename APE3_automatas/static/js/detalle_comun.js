(function () {
  const AUTO_ID = window.AUTO_ID;
  const DEFINICION = window.DEFINICION;
  const config = window.AUTOMATA_CONFIG || {};

  if (!AUTO_ID || !DEFINICION) {
    return;
  }

  const DEFS = '<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 Z" fill="#5a6480"/></marker></defs>';

  function circle(cx, cy, r, id, isAccept, isTrap, isInicial, nombres) {
    const stroke = isAccept ? "#00d4aa" : isTrap ? "#ff4757" : "#3a4460";
    const fill = isAccept ? "rgba(0,212,170,0.1)" : isTrap ? "rgba(255,71,87,0.1)" : "#1c2130";
    let s = "";
    if (isInicial) {
      s += '<line x1="' + (cx - r - 25) + '" y1="' + cy + '" x2="' + (cx - r - 3) + '" y2="' + cy + '" stroke="#5a6480" stroke-width="1.5" marker-end="url(#arr)"/>';
    }
    s += '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="' + fill + '" stroke="' + stroke + '" stroke-width="' + (isAccept ? 2.5 : 1.5) + '"/>';
    if (isAccept) {
      s += '<circle cx="' + cx + '" cy="' + cy + '" r="' + (r - 5) + '" fill="none" stroke="' + stroke + '" stroke-width="1" opacity="0.5"/>';
    }
    s += '<text x="' + cx + '" y="' + (cy - 6) + '" text-anchor="middle" font-family="Space Mono" font-size="11" fill="#dde3f0" font-weight="700">' + id + "</text>";
    s += '<text x="' + cx + '" y="' + (cy + 9) + '" text-anchor="middle" font-family="Syne" font-size="8" fill="#5a6480">' + ((nombres[id] || "").split("/")[0]) + "</text>";
    return s;
  }

  function arrow(x1, y1, x2, y2, lbl, r, curve, side) {
    const dx = x2 - x1;
    const dy = y2 - y1;
    const len = Math.sqrt(dx * dx + dy * dy);
    const nx = dx / len;
    const ny = dy / len;
    const sx = x1 + nx * r;
    const sy = y1 + ny * r;
    const ex = x2 - nx * r;
    const ey = y2 - ny * r;

    let d;
    let lx;
    let ly;

    if (curve) {
      const mx = (sx + ex) / 2;
      const my = (sy + ey) / 2;
      const off = side * 35;
      const cx2 = mx - ny * off;
      const cy2 = my + nx * off;
      d = "M " + sx + " " + sy + " Q " + cx2 + " " + cy2 + " " + ex + " " + ey;
      lx = cx2 + (mx - cx2) * 0.3;
      ly = cy2 + (my - cy2) * 0.3;
    } else {
      d = "M " + sx + " " + sy + " L " + ex + " " + ey;
      lx = (sx + ex) / 2 - ny * 14;
      ly = (sy + ey) / 2 + nx * 14;
    }

    return '<path d="' + d + '" fill="none" stroke="#3a4460" stroke-width="1.5" marker-end="url(#arr)"/>' +
      '<text x="' + lx + '" y="' + ly + '" text-anchor="middle" font-family="Space Mono" font-size="10" fill="#a0aec0">' + lbl + "</text>";
  }

  function loop(cx, cy, r, lbl, side) {
    const a = side === "top" ? -Math.PI / 2 : 0;
    const lx = cx + Math.cos(a) * (r + 20);
    const ly = cy + Math.sin(a) * (r + 20);
    const x1 = cx + Math.cos(a - 0.5) * r;
    const y1 = cy + Math.sin(a - 0.5) * r;
    const x2 = cx + Math.cos(a + 0.5) * r;
    const y2 = cy + Math.sin(a + 0.5) * r;

    return '<path d="M ' + x1 + ' ' + y1 + ' Q ' + lx + ' ' + (ly - (side === "top" ? 20 : 0)) + ' ' + x2 + ' ' + y2 + '" fill="none" stroke="#3a4460" stroke-width="1.5" marker-end="url(#arr)"/>' +
      '<text x="' + lx + '" y="' + (ly - (side === "top" ? 26 : 0)) + '" text-anchor="middle" font-family="Space Mono" font-size="10" fill="#a0aec0">' + lbl + "</text>";
  }

  function initExamples() {
    const examples = config.ejemplos || [];
    const container = document.getElementById("examplesContainer");

    if (!container) {
      return;
    }

    examples.forEach(function (item) {
      const ej = item[0];
      const ok = item[1];
      const btn = document.createElement("button");
      btn.className = "quick-btn";
      btn.textContent = ej + (ok ? " OK" : " NO");
      btn.onclick = function () {
        document.getElementById("simInput").value = ej;
        window.runSim();
      };
      container.appendChild(btn);
    });
  }

  window.runSim = async function runSim() {
    const input = document.getElementById("simInput");
    const cadena = (input ? input.value : "").trim();
    if (!cadena) {
      return;
    }

    const res = await fetch("/api/" + AUTO_ID + "/validar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ cadena: cadena })
    });

    const data = await res.json();
    renderResult(data);
  };

  function renderResult(data) {
    const box = document.getElementById("simResult");
    if (!box) {
      return;
    }

    box.style.display = "block";

    if (data.error && (!data.historial || data.historial.length <= 1)) {
      box.className = "result-box rejected";
      box.innerHTML = '<div class="verdict fail">Aviso: ' + data.error + "</div>";
      return;
    }

    box.className = "result-box " + (data.aceptada ? "accepted" : "rejected");

    const verdict = data.aceptada
      ? "Cadena ACEPTADA"
      : "Cadena RECHAZADA" + (data.error ? " - " + data.error : "");

    const stepsHtml = (data.historial || []).map(function (p, i) {
      const isLast = i === data.historial.length - 1;

      if (p.paso === 0) {
        return '<div class="step">' +
          '<div class="snum">0</div>' +
          '<span class="sstate">Estado inicial: <strong>' + p.estado_actual + '</strong>' +
          '<span class="sdesc"> - ' + p.nombre_estado + "</span></span>" +
          "</div>";
      }

      return '<div class="step ' + (isLast ? (data.aceptada ? "final" : "error") : "") + '">' +
        '<div class="snum ' + (isLast && data.aceptada ? "ok" : "") + '">' + p.paso + "</div>" +
        '<span class="ssym">' + p.simbolo + "</span>" +
        '<span class="sdesc">(' + p.descripcion + ")</span>" +
        '<span class="sarrow">-></span>' +
        '<span class="sstate"><strong>' + p.estado_anterior + "</strong> -> <strong>" + p.estado_actual + "</strong>" +
        '<span class="sdesc"> ' + p.nombre_estado + "</span>" +
        "</span>" +
        (p.transicion_invalida ? '<span style="color:var(--danger);font-size:.72rem">invalida</span>' : "") +
        "</div>";
    }).join("");

    box.innerHTML =
      '<div class="verdict ' + (data.aceptada ? "ok" : "fail") + '">' + verdict + "</div>" +
      '<div class="result-meta">Estado final: ' + data.estado_final + " - " + data.nombre_estado_final + "</div>" +
      '<div class="steps">' + stepsHtml + "</div>";
  }

  function renderDiagram() {
    const diagramArea = document.getElementById("diagramArea");
    if (!diagramArea || typeof config.renderDiagram !== "function") {
      return;
    }

    const svg = config.renderDiagram(DEFINICION, {
      defs: DEFS,
      circle: circle,
      arrow: arrow,
      loop: loop
    });

    if (svg) {
      diagramArea.innerHTML = svg;
    }
  }

  initExamples();
  renderDiagram();
})();
