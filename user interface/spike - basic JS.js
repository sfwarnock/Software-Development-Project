var today = new Date();
var hourNow = today.getHours();
var gretting;

if (hourNow > 18){
  greeting = 'Good evening!';
} else if (hoursNow > 12) {
  greeting = 'Good afternoon!';
} else if (hours > 0) {
  gretting = 'Good morning!';
} else {
  greeting = "Welcome!";
}

document.write('<h3>' + greeting + '<h3>')
