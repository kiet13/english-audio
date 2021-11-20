function showRemoveButton() {
    if (document.getElementById("search").value.length > 0) {
        document.getElementById("btnRemove").style.visibility = "visible";
    }
    else {
        document.getElementById("btnRemove").style.visibility = "hidden";
    }
}

function removeInput() {
    let inputField = document.getElementById("search");
    inputField.value = "";
    inputField.focus();
}

function submitWord() {
    let form = document.getElementById("form");
    form.submit.click();
}

function createUploadButton() {
    // Remove old button if possible
    let btnUpload = document.getElementById("btnUpload");
    if (btnUpload !== null) {
        btnUpload.remove();
    }

    btnUpload = document.createElement("input");
    btnUpload.type = "file";
    btnUpload.style.display = "none";
    btnUpload.setAttribute("id", "btnUpload");
    btnUpload.setAttribute("name", "file");

    let form = document.getElementById("form");
    form.appendChild(btnUpload);
    btnUpload.click();
    btnUpload.addEventListener("change", uploadFile);
}
  
function handleFileLoad(event) {
    console.log(event.target.result);
}

function uploadFile(event) {
    let btnUpload = document.getElementById("btnUpload");
    const fileName = btnUpload.value.split(/[\\/]/).pop();
    
    let uploadDiv = document.getElementsByClassName("upload")[0];
    uploadDiv.querySelector("p").innerText = fileName;
    uploadDiv.className += " show";

    const reader = new FileReader()
    reader.onload = handleFileLoad;
    reader.readAsText(event.target.files[0])
}

function removeFileUpload() {
    let btnUpload = document.getElementById("btnUpload");
    if (btnUpload !== null) {
        btnUpload.remove();
    }

    let uploadDiv = document.getElementsByClassName("upload")[0];
    uploadDiv.classList.remove("show");

    removeInput();
}

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

