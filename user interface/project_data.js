function loadData(project_todate) {
  var acwp = document.getElementById('acwp');
  acwp.textContent = '$ ' + parseFloat(project_todate['ACWP']).toLocaleString('en');

  var bac = document.getElementById('bac');
  bac.textContent = '$ ' + parseFloat(project_todate['BAC']).toLocaleString('en');

  var bcwp = document.getElementById('bcwp');
  bcwp.textContent = '$ ' + parseFloat(project_todate['BCWP']).toLocaleString('en');

  var bcwr = document.getElementById('bcwr');
  bcwr.textContent = '$ ' + parseFloat(project_todate['BCWR']).toLocaleString('en');

  var bcws = document.getElementById('bcws');
  bcws.textContent = '$ ' + parseFloat(project_todate['BCWS']).toLocaleString('en');

  var cpi = document.getElementById('cpi');
  cpi.textContent = parseFloat(Math.round(project_todate['CPI']*100)/100).toFixed(2);

  var cv = document.getElementById('cv');
  cv.textContent = '$ ' + parseFloat(project_todate['CV']).toLocaleString('en');

  var eac_CPI = document.getElementById('EAC_CPI');
  eac_CPI.textContent = '$ ' + parseFloat(project_todate['EAC_CPI']).toLocaleString();

  var eac_comp = document.getElementById('EAC_Composite');
  eac_comp.textContent = parseFloat(project_todate['EAC_Composite']).toLocaleString();

  var eac_gen = document.getElementById('eac_gen');
  eac_gen.textContent = '$ ' + parseFloat(project_todate['EAC_General']).toLocaleString('en');

  var etc = document.getElementById('etc');
  etc.textContent = '$ ' + parseFloat(project_todate['ETC']).toLocaleString('en');

  var etc = document.getElementById('etc');
  etc.textContent = '$ ' + parseFloat(project_todate['ETC']).toLocaleString('en');

  var percentcom = document.getElementById('percentcom');
  percentcom.textContent = parseFloat(Math.round(project_todate['PerComp'] *100) / 100).toFixed(4) * 100;

  var spi = document.getElementById('spi');
  spi.textContent = parseFloat(project_todate['SPI']).toLocaleString('en');

  var sv = document.getElementById('sv');
  sv.textContent = '$ ' + parseFloat(project_todate['SV']).toLocaleString('en');

  var tcpi_bac = document.getElementById('tcpi_bac');
  tcpi_bac.textContent = parseFloat(Math.round(project_todate['TCPI_BAC']*100) / 100).toFixed(2);

  var tcpi_eac = document.getElementById('tcpi_eac');
  tcpi_eac.textContent = parseFloat(Math.round(project_todate['TCPI_EAC']*100) / 100).toFixed(2);

  var vac = document.getElementById('vac');
  vac.textContent = '$' + parseFloat(project_todate['VAC']).toLocaleString('en');

  var totalbudget = document.getElementById('totalbudget');
  totalbudget.textContent = '$ ' + parseFloat(project_todate['BAC']).toLocaleString('en');

  var reportingpercent = document.getElementById('reportingpercent');
  reportingpercent.textContent = parseFloat(Math.round(project_todate['PerComp'] *100) / 100).toFixed(4) * 100 + '%';
}

$.getJSON( "cum_json.json", function(data) {
  console.log(data);
  loadData(data);
});
