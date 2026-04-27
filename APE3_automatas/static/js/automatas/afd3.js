window.AUTOMATA_CONFIG = {
  ejemplos: [["CPET", true], ["CPED", true], ["CPX", true], ["CPE", false]],
  renderDiagram: function (definicion, h) {
    const n = definicion.nombres_estados;
    return '<svg viewBox="0 0 700 240" xmlns="http://www.w3.org/2000/svg">' + h.defs +
      h.circle(50, 120, 30, "q0", false, false, true, n) + h.circle(165, 120, 30, "q1", false, false, false, n) +
      h.circle(280, 120, 30, "q2", false, false, false, n) + h.circle(395, 120, 30, "q3", false, false, false, n) +
      h.circle(520, 60, 30, "q4", true, false, false, n) + h.circle(520, 180, 30, "q5", true, false, false, n) +
      h.circle(640, 120, 30, "q6", true, false, false, n) +
      h.arrow(50, 120, 165, 120, "C", 30, false, 0) + h.arrow(165, 120, 280, 120, "P", 30, false, 0) +
      h.arrow(280, 120, 395, 120, "E", 30, false, 0) + h.arrow(395, 120, 520, 60, "T", 30, false, 0) +
      h.arrow(395, 120, 520, 180, "D", 30, false, 0) + h.arrow(165, 120, 640, 120, "X", 30, true, -1) +
      h.arrow(280, 120, 640, 120, "X", 30, true, -1) + h.arrow(520, 60, 520, 180, "D", 30, false, 0) +
      "</svg>";
  }
};
