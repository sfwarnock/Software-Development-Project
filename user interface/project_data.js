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
