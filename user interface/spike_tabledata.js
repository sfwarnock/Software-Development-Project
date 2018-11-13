var jsonProjectEVM = {
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
}

var projectKeyValue = JSON.parse(jsonProjectEVM);
var bac, bcws, percentComplete, bcwp, acwp, sv, spi, cv, cpi;
acwp = projectKeyValue["ACWP"];
bac = projectKeyValue["Budget at Complete"];
percentComplete = projectKeyValue["percentComplete"];

var elacwp = document.getElementById('ACWP');
elacwp.textContent = acwp
var elbac = document.getElementById("BAC");

var bcwr, etc, petc, eac, peac, tcpi, ptcpi, bac, vac;

var periodBudget, periodBcws, periodPercentComplete, periodBCWP, periodACWP;
