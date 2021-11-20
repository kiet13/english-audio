function forceDownload(blob, filename) {
    var a = document.createElement('a');
    a.setAttribute('type', 'hidden');
    a.download = filename;
    a.href = blob;
    a.innerText = "Click here!";
    // For Firefox https://stackoverflow.com/a/32226068
    document.body.appendChild(a);
    a.click();
    a.remove();
}
  
// Current blob size limit is around 500MB for browsers
function downloadResource(url, filename) {
    if (!filename) filename = url.split('\\').pop().split('/').pop();
    console.log(filename)
    fetch(url, {
        headers: new Headers({
            'Origin': location.origin
        }),
        mode: 'cors'
        })
        .then(response => response.blob())
        .then(blob => {
        let blobUrl = window.URL.createObjectURL(blob);
        forceDownload(blobUrl, filename);
        })
        .catch(e => console.error(e));
}