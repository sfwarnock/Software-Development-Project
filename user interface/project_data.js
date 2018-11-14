var project_todate = $.getJSON( "cum_json.json", function(data) {
	console.log(data);
});

acwp = (project_todate)['ACWP'];
bcwp = (project_todate)['BCWP'];
bac = (project_todate)['Budget at Complete'];

document.write(acwp);
document.write(bcwp);
document.write(bac);
