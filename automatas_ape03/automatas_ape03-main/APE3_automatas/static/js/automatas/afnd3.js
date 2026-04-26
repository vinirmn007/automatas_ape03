window.AUTOMATA_CONFIG = {
  ejemplos: [
    ["HSC", true],
    ["HSSC", true],
    ["HSHSC", true],
    ["HS", false]
  ],
  renderDiagram: function (definicion, h) {
    const n = definicion.nombres_estados;
    return '<svg viewBox="0 0 560 220" xmlns="http://www.w3.org/2000/svg">' + h.defs +
      h.circle(60, 110, 32, "q0", false, false, true, n) +
      h.circle(200, 110, 32, "q1", false, false, false, n) +
      h.circle(350, 110, 32, "q2", false, false, false, n) +
      h.circle(490, 110, 32, "q3", true, false, false, n) +
      h.arrow(60, 110, 200, 110, "H", 32, false, 0) +
      h.arrow(200, 110, 350, 110, "S", 32, false, 0) +
      h.loop(200, 110, 32, "S", "top") +
      h.arrow(350, 110, 490, 110, "C", 32, false, 0) +
      "</svg>";
  }
};
