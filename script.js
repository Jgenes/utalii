var button = document.getElementById('hoverme');
var slideout = document.getElementById('notif');

button.onclick = function() {
  slideout.classList.toggle('visible');
};