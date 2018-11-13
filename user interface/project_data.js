var project_todate = $.getJSON( "cum_json.txt", function(data) {
	console.log(data);
});


var projectKeyValue = JSON.parse(project_todate;
var bac, bcws, percentComplete, bcwp, acwp, sv, spi, cv, cpi;
acwp = projectKeyValue["ACWP"];
bac = projectKeyValue["Budget at Complete"];
percentComplete = projectKeyValue["percentComplete"];
bcwp = projectKeyValue["BCWP"];
sv = projectKeyValue["SV"];
spi = projectKeyValue["SPI"];
cv = projectKeyValue["CV"];
cpi = projectKeyValue["CPI"];

var elacwp = document.getElementById('ACWP');
elacwp.textContent = acwp;
var elbac = document.getElementById("BAC");
