var myPlot = document.getElementById('plot');
console.log(myPlot)
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
      container = document.getElementById('history');
      container.insertBefore(document.createElement('br'), container.childNodes[0])
      container.insertBefore(document.createTextNode(data.points[0].text.replace(/<br>/g, ' ')), container.childNodes[0])
    } else {
      showToast();
    }
});

function showToast() {
  var x = document.getElementById("snackbar")
  x.className = "show";
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}


function pause() {
  if(audio){
    audio.pause()
  }
}