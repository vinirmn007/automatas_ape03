window.AUTOMATA_CONFIG = {
  ejemplos: [
    ["bot user cmd", true],
    ["bot cmd", true],
    ["user cmd", false],
    ["bot user help", true]
  ],
  renderDiagram: function () {
    return '<svg viewBox="0 0 520 180" xmlns="http://www.w3.org/2000/svg">' +
      '<rect x="8" y="8" width="504" height="164" rx="12" fill="#131720" stroke="#1e2535"/>' +
      '<text x="260" y="78" text-anchor="middle" font-family="Syne" font-size="16" fill="#a855f7">AFND #1</text>' +
      '<text x="260" y="106" text-anchor="middle" font-family="Space Mono" font-size="11" fill="#5a6480">Diagrama en construccion</text>' +
      "</svg>";
  }
};
