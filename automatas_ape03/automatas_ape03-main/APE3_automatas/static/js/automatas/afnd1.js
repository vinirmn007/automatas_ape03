window.AUTOMATA_CONFIG = {
  ejemplos: [
    ["BWC", true],
    ["BWWWC", true],
    ["WC", false]
  ],
  renderDiagram: function (definicion, h) {
    const n = definicion.nombres_estados;
    return '<svg viewBox="0 0 560 220" xmlns="http://www.w3.org/2000/svg">' + h.defs +
      h.circle(60, 110, 32, "q0", false, false, true, n) +
      h.circle(200, 110, 32, "q1", false, false, false, n) +
      h.circle(350, 110, 32, "q2", false, false, false, n) +
      h.circle(490, 110, 32, "q3", true, false, false, n) +
      h.arrow(60, 110, 200, 110, "B", 32, false, 0) +
      h.arrow(200, 110, 350, 110, "W", 32, false, 0) +
      h.arrow(350, 110, 490, 110, "C", 32, false, 0) +
      '<path d="M 220 142 Q 280 185 330 142" fill="none" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arr)" opacity="0.8"/>' +
      '<text x="275" y="182" text-anchor="middle" font-family="Space Mono" font-size="10" fill="#a855f7">ε</text>' +
      "</svg>";
  }
};
