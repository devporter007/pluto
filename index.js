const btn = document.getElementById('btn');
const result = document.getElementById('result');
btn.addEventListener('click', function onClick() {
if (btn.style.backgroundColor == "green"){
  result.style.backgroundColor = 'salmon';
  result.style.color = 'white';}
});


var i = 0;
function change() {
  var color = ["black", "blue", "brown", "green"];
  btn.style.backgroundColor = color[i];
	btn.style.color = "white";
  i = (i + 1) % color.length;
}
setInterval(change, 2000);

