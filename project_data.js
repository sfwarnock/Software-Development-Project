//let project_todate = $.getJSON( "cum_json.json", function(data) {
//	console.log(data);
//});

var project_todate = {
    "ACWP": 240600.0,
    "BCWP": 195400.0,
    "BCWS": 190400.0,
    "Budget at Complete": 571200.0,
    "Bugeted Cost of Work Remaining": 375800.0,
    "CPI": 0.8121363258520365,
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
acwp.textContent = '$ ' + parseFloat(Math.round(project_todate['ACWP']*100) / 100).toFixed(2);

var bcwp = document.getElementById('bcwp');
bcwp.textContent = '$ ' + parseFloat(Math.round(project_todate['BCWP']*100) / 100).toFixed(2);

var bcws = document.getElementById('bcws');
bcws.textContent = '$ ' + parseFloat(Math.round(project_todate['BCWS']*100) / 100).toFixed(2);

var bac = document.getElementById('bac');
bac.textContent = '$ ' + parseFloat(Math.round(project_todate['Budget at Complete']*100) / 100).toFixed(2);

var totalbudget = document.getElementById('totalbudget');
totalbudget.textContent = '$ ' + parseFloat(Math.round(project_todate['Budget at Complete']*100) / 100).toFixed(2);

var bcwr = document.getElementById('bcwr');
bcwr.textContent = '$ ' + parseFloat(Math.round(project_todate['Bugeted Cost of Work Remaining']*100) / 100).toFixed(2);

var cpi = document.getElementById('cpi');
cpi.textContent = parseFloat(Math.round(project_todate['CPI']*100)/100).toFixed(2);

var cv = document.getElementById('cv');
cv.textContent = '$ ' + parseFloat(Math.round(project_todate['CV']*100) / 100).toFixed(2);

var eac = document.getElementById('eac');
eac.textContent = '$ ' + parseFloat(Math.round(project_todate['EAC']*100) / 100).toFixed(2);

var percentcom = document.getElementById('percentcom');
percentcom.textContent = parseFloat(Math.round(project_todate['Percent Complete'] *100) / 100).toFixed(4) * 100;

var peac = document.getElementById('peac');
peac.textContent = '$ ' + parseFloat(Math.round(project_todate['Performance EAC']*100) / 100).toFixed(2);

var petc = document.getElementById('petc');
petc.textContent = '$ ' + parseFloat(Math.round(project_todate['Performance ETC']*100) / 100).toFixed(2);

var ptcpi = document.getElementById('ptcpi');
ptcpi.textContent = parseFloat(Math.round(project_todate['Perfromance TCPI']*100) / 100).toFixed(2);

var spi = document.getElementById('spi');
spi.textContent = parseFloat(Math.round(project_todate['SPI']*100) / 100).toFixed(2);

var sv = document.getElementById('sv');
sv.textContent = '$ ' + parseFloat(Math.round(project_todate['SV']*100) /100).toFixed(2);

var tcpi = document.getElementById('tcpi');
tcpi.textContent = parseFloat(Math.round(project_todate['TCPI']*100) / 100).toFixed(2);

var vac = document.getElementById('vac');
vac.textContent = '$' + parseFloat(Math.round(project_todate['VAC']*100) / 100).toFixed(2);

var etc = document.getElementById('etc');
etc.textContent = '$ ' + parseFloat(Math.round(project_todate['Bugeted Cost of Work Remaining']*100) / 100).toFixed(2);
