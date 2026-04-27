window.AUTOMATA_CONFIG = {
  ejemplos: [["ACL", true], ["AL", false], ["AC", false], ["AACL", false]],
  renderDiagram: function (definicion, h) {
    const n = definicion.nombres_estados;
    return '<svg viewBox="0 0 580 200" xmlns="http://www.w3.org/2000/svg">' + h.defs +
      h.circle(60, 100, 32, "q0", false, false, true, n) + h.circle(180, 100, 32, "q1", false, false, false, n) +
      h.circle(300, 100, 32, "q2", false, false, false, n) + h.circle(420, 100, 32, "q3", true, false, false, n) +
      h.circle(300, 182, 28, "q4", false, true, false, n) +
      h.arrow(60, 100, 180, 100, "A", 32, false, 0) + h.arrow(180, 100, 300, 100, "C", 32, false, 0) +
      h.arrow(300, 100, 420, 100, "L", 32, false, 0) +
      '<path d="M 92 110 Q 170 158 272 182" fill="none" stroke="#3a4460" stroke-width="1.2" marker-end="url(#arr)" stroke-dasharray="3,2" opacity=".6"/>' +
      '<text x="140" y="162" font-size="9" fill="#5a6480" font-family="Space Mono">C,L</text>' +
      '<path d="M 212 110 Q 258 156 272 182" fill="none" stroke="#3a4460" stroke-width="1.2" marker-end="url(#arr)" stroke-dasharray="3,2" opacity=".6"/>' +
      '<text x="244" y="156" font-size="9" fill="#5a6480" font-family="Space Mono">A,L</text>' +
      '<path d="M 332 110 Q 342 148 328 180" fill="none" stroke="#3a4460" stroke-width="1.2" marker-end="url(#arr)" stroke-dasharray="3,2" opacity=".6"/>' +
      '<text x="356" y="150" font-size="9" fill="#5a6480" font-family="Space Mono">A,C</text>' +
      '<path d="M 452 100 Q 510 100 510 168 Q 510 188 328 185" fill="none" stroke="#3a4460" stroke-width="1.2" marker-end="url(#arr)" stroke-dasharray="3,2" opacity=".6"/>' +
      '<text x="514" y="136" font-size="9" fill="#5a6480" font-family="Space Mono">A,C,L</text>' +
      h.loop(300, 182, 28, "A,C,L", "top") +
      "</svg>";
  }
};
