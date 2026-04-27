window.AUTOMATA_CONFIG = {
  ejemplos: [["CFC", true], ["FFF", false], ["FFCF", true], ["CCF", true]],
  renderDiagram: function (definicion, h) {
    const n = definicion.nombres_estados;
    return '<svg viewBox="0 0 480 200" xmlns="http://www.w3.org/2000/svg">' + h.defs +
      h.circle(70, 100, 32, "q0", true, false, true, n) + h.circle(200, 100, 32, "q1", true, false, false, n) +
      h.circle(330, 100, 32, "q2", true, false, false, n) + h.circle(440, 100, 32, "q3", false, true, false, n) +
      h.loop(70, 100, 32, "C", "top") + h.arrow(70, 100, 200, 100, "F", 32, false, 0) +
      h.arrow(200, 100, 330, 100, "F", 32, false, 0) + h.arrow(330, 100, 440, 100, "F", 32, false, 0) +
      h.loop(440, 100, 32, "C,F", "top") +
      h.arrow(200, 100, 70, 100, "C", 32, true, 1) + h.arrow(330, 100, 70, 100, "C", 32, true, 1) +
      "</svg>";
  }
};
