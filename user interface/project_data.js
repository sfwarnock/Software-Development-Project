var project_todate = $.getJSON( "cum_json.json", function(data) {
	console.log(data);
});

acwp = project_todate.ACWP;
bcwp = project_todate.BCWP;

document.write(acwp);
document.write(bcwp);
