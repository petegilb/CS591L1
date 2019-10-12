var Neptune = require('neptune-notebook');

const javascriptDependencies = [
  'dependencies/carousels/lib/imparse.js',
  'dependencies/carousels/lib/carousels.js',
  'dependencies/carousels/lib/costs.js',
  'dependencies/carousels/lib/metric.js',
  'dependencies/carousels/lib/plot.js',
  'dependencies/carousels/lib/setup.js',
  'dependencies/lodash.core.min.js',
  'dependencies/jquery-2.1.1.js',
  'dependencies/babel.min.js',
  'dependencies/randomColor.min.js',
  'dependencies/plotly-latest.min.js',
  'dependencies/polynomium.js'
];

var neptune = new Neptune();
neptune.addDocument('carousels', __dirname + '/notes/carousels_lecture.md', true, javascriptDependencies);
neptune.start(8080);

neptune.writeHTML('carousels', __dirname + '/../website/html/lecture-04-babel-carousels.html');
