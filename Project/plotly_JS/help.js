var myPlot = document.getElementById('plot');
//Plotly.newPlot(myPlot, data, layout);
audio = null;
myPlot.on('plotly_click', function(data){
    console.log(data);
    //alert(data.points[0].customdata)
    if(data.points[0].customdata) {
      if(audio){
        audio.pause()
      }
      audio = new Audio(data.points[0].customdata);
      audio.play();
    } else {
      showToast();
    }
    //container = document.getElementById('selection');
    //container.appendChild(document.createTextNode(data.points[0].text));
});

function showToast() {
  var x = document.getElementById("snackbar")
  x.className = "show";
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

$('#theButton').click(function() {
  console.log('clicked');
  $('#plot').css({
      position: 'fixed',
      top: 0,
      right: 0,
      bottom: 0,
      left: 0,
      zIndex: 999
  });
});