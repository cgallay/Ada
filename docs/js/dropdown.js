function setIframeSource() {
    var theSelect = document.getElementById('genre');
    var theIframe = document.getElementById('myIframe');
    var theUrl;

    theUrl = theSelect.options[theSelect.selectedIndex].value;
    theIframe.src = theUrl;
}