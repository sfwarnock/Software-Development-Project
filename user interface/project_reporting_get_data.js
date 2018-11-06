{
    "Budget at Complete": 571200.0,
    "BCWP": 195400.0,
    "Percent Complete": 0.34208683473389356,
    "Bugeted Cost of Work Remaining": 375800.0,
    "BCWS": 190400.0,
    "ACWP": 240600.0,
    "EAC": 616400.0,
    "TCPI": 0.9266709928617781,
    "CPI": 0.8121363258520365,
    "SPI": 1.0262605042016806,
    "CV": -45200.0,
    "SV": 5000.0,
    "Performance ETC": 545800.8312551953,
    "Performance EAC": 786400.8312551953,
    "Perfromance TCPI": 0.7263471467702959,
    "VAC": -45200.0
}


var txt = '{
    "BAC": 571200.0,
    "BCWP": 195400.0,
    "Percent Complete": 0.34208683473389356,
    "Bugeted Cost of Work Remaining": 375800.0,
    "BCWS": 190400.0,
    "ACWP": 240600.0,
    "EAC": 616400.0,
    "TCPI": 0.9266709928617781,
    "CPI": 0.8121363258520365,
    "SPI": 1.0262605042016806,
    "CV": -45200.0,
    "SV": 5000.0,
    "Performance ETC": 545800.8312551953,
    "Performance EAC": 786400.8312551953,
    "Perfromance TCPI": 0.7263471467702959,
    "VAC": -45200.0}'
var obj = JSON.parse(txt);
document.getElementByID("python_data").innnerHTML = obj.BAC;
