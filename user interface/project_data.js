//let project_todate = $.getJSON( "cum_json.json", function(data) {
//	console.log(data);
//});

var project_todate = {
    "ACWP": 240600.0,
    "BCWP": 195400.0,
    "BCWS": 190400.0,
    "Budget at Complete": 571200.0,
    "Bugeted Cost of Work Remaining": 375800.0,
    "CPI": 0.812136325852036,
    "CV": -45200.0,
    "EAC": 616400.0,
    "Percent Complete": 0.34208683473389356,
    "Performance EAC": 786400.8312551953,
    "Performance ETC": 545800.8312551953,
    "Perfromance TCPI": 0.7263471467702959,
    "SPI": 1.0262605042016806,
    "SV": 5000.0,
    "TCPI": 0.9266709928617781,
    "VAC": -45200.0
};

var acwp = document.getElementById('acwp');
acwp.textContent = project_todate['ACWP'];

var bcwp = document.getElementById('bcwp');
bcwp.textContent = project_todate['BCWP'];

var bcws = document.getElementById('bcws');
bcws.textContent = '$' + project_todate['BCWS'];

var bac = document.getElementById('bac');
bac.textContent = project_todate['Budget at Complete'];

var bcwr = document.getElementById('bcwr');
bcwr.textContent = project_todate['Budget Cost of Work Remaining'];

var cpi = document.getElementById('cpi');
cpi.textContent = project_todate['CPI'];

var cv = document.getElementById('cv');
cv.textContent = project_todate['CV'];

var eac = document.getElementById('eac');
eac.textContent = project_todate['EAC'];

var percentcom = document.getElementById('percentcom');
percentcom.textContent = project_todate['Percent Complete'];

var peac = document.getElementById('peac');
peac.textContent = project_todate['Performance EAC'];

var petc = document.getElementById('petc');
ptec.textContent = project_todate['Performance ETC'];

var ptcpi = document.getElementById('ptcpi');
tcpi.textContent = project_todate['Perfromance TCPI'];

var spi = document.getElementById('spi');
spi.textContent = project_todate['SPI'];

var sv = document.getElementById('sv');
sv.textContent = project_todate['SV'];

var tcpi = document.getElementById('tcpi');
tcpi.textContent = project_todate['TCPI'];

var vac = document.getElementById('vac');
vac.textContent = '$' + project_todate['VAC'];
