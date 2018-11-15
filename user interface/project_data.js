var project_todate = $.getJSON( "cum_json.json", function(data) {
	console.log(data);
});

acwp = (project_todate)['ACWP'];
bcwp = (project_todate)['BCWP'];
bcws = (project_todate)['BCWS'];
bac = (project_todate)['Budget at Complete'];
bcwr = (project_todate)['Budget Cost of Work Remaining'];
cpi = (project_todate)['CPI'];
cv = (project_todate)['CV'];
eac = (project_todate)['EAC'];
percentcom = (project_todate)['Percent Complete'];
peac = (project_todate)['Performance EAC'];
petc = (project_todate)['Performance ETC'];
ptcpi = (project_todate)['Performance TCPI'];
spi = (project_todate)['SPI'];
sv = (project_todate)['SV'];
tcpi = (project_todate)['TCPI'];
vac = (project_todate)['VAC'];

document.write(acwp);
document.write(bcwp);
document.write(bac);
document.write(bcws);
document.write(bcwr);



// progressbar.js@1.0.0 version is used
// Docs: http://progressbarjs.readthedocs.org/en/1.0.0/

var bar = new ProgressBar.Line(container_bar1, {
  strokeWidth: 4,
  easing: 'easeInOut',
  duration: 1400,
  color: '#FFEA82',
  trailColor: '#eee',
  trailWidth: 1,
  svgStyle: {width: '100%', height: '100%'},
  text: {
    style: {
      // Text color.
      // Default: same as stroke color (options.color)
      color: '#999',
      position: 'absolute',
      right: '0',
      top: '30px',
      padding: 0,
      margin: 0,
      transform: null
    },
    autoStyleContainer: false
  },
  from: {color: '#FFEA82'},
  to: {color: '#ED6A5A'},
  step: (state, bar) => {
    bar.setText(Math.round(bar.value() * 100) + ' %');
  }
});

bar.animate(.7);  // Number from 0.0 to 1.0

// progressbar.js@1.0.0 version is used
// Docs: http://progressbarjs.readthedocs.org/en/1.0.0/

var bar = new ProgressBar.Circle(container_circle, {
  color: '#aaa',
  // This has to be the same size as the maximum width to
  // prevent clipping
  strokeWidth: 4,
  trailWidth: 1,
  easing: 'easeInOut',
  duration: 1400,
  text: {
    autoStyleContainer: false
  },
  from: { color: '#aaa', width: 1 },
  to: { color: '#333', width: 4 },
  // Set default step function for all animate calls
  step: function(state, circle) {
    circle.path.setAttribute('stroke', state.color);
    circle.path.setAttribute('stroke-width', state.width);

    var value = Math.round(circle.value() * 100);
    if (value === 0) {
      circle.setText('');
    } else {
      circle.setText(value);
    }

  }
});
bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
bar.text.style.fontSize = '2rem';

bar.animate(.7);  // Number from 0.0 to 1.0
