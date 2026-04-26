window.AUTOMATA_CONFIG = {
  ejemplos: [
    ["KGF", true],
    ["XKGFX", true],
    ["KGFGF", true],
    ["KGG", false]
  ],
  renderDiagram: function (definicion, h) {
    const n = definicion.nombres_estados;
    return '<svg viewBox="0 0 560 220" xmlns="http://www.w3.org/2000/svg">' + h.defs +
      h.circle(60, 110, 32, "q0", false, false, true, n) +
      h.circle(200, 110, 32, "q1", false, false, false, n) +
      h.circle(350, 110, 32, "q2", false, false, false, n) +
      h.circle(490, 110, 32, "q3", true, false, false, n) +
      h.loop(60, 110, 32, "K,G,X,F", "top") +
      h.arrow(60, 110, 200, 110, "K", 32, false, 0) +
      h.arrow(200, 110, 350, 110, "G", 32, false, 0) +
      h.loop(350, 110, 32, "K,G,X", "top") +
      '<path d="M 382 110 Q 430 70 458 110" fill="none" stroke="#3a4460" stroke-width="1.5" marker-end="url(#arr)"/>' +
      '<text x="422" y="72" text-anchor="middle" font-family="Space Mono" font-size="10" fill="#a0aec0">F</text>' +
      '<path d="M 382 124 Q 430 175 458 124" fill="none" stroke="#3a4460" stroke-width="1.5" marker-end="url(#arr)"/>' +
      '<text x="422" y="178" text-anchor="middle" font-family="Space Mono" font-size="10" fill="#a0aec0">F</text>' +
      "</svg>";
  }
};
