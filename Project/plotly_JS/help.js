var myPlot = document.getElementById('plot');
//Plotly.newPlot(myPlot, data, layout);
audio = null;
myPlot.on('plotly_click', function(data){
    console.log(data);
    //alert(data.points[0].customdata)
    if(audio){
      audio.pause()
    }
    audio = new Audio(data.points[0].customdata);
    audio.play();
});