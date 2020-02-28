let answerArray = new Array(constants.questionIndexes.match.length).fill("0");
answerArray[1] = "1";
let scouterMatchNum = 0;
var currentDiv = 0;
var divNames = ["teamatch", "auto", "teleop"];
var edited = false;
    
function next() {
  for (var i = 0; i <= 2; i++){
    document.getElementById(divNames[i]).style.display = "none";
  }
  currentDiv += 1;
  if (currentDiv > 2){currentDiv = 2}
  document.getElementById(divNames[currentDiv]).style.display = "block";
}

function prev() {
  for (var i = 0; i <= 2; i++){
    document.getElementById(divNames[i]).style.display = "none";
  }
  currentDiv -= 1;
  if (currentDiv < 0){currentDiv = 0}
  document.getElementById(divNames[currentDiv]).style.display = "block";
}

function increase(ele) {
    let input = ele.parentNode.children[2];
    input.value = parseInt(input.value) + 1;
    if (parseInt(input.value) == parseInt(input.max)) {
        ele.parentNode.children[1].disabled = true;
    }
    if (ele.parentNode.children[3].disabled) {
        ele.parentNode.children[3].disabled = false;
    }
    updateArray(input);
}

function decrease(ele) {
    let input = ele.parentNode.children[2];
    input.value = parseInt(input.value) - 1;
    if (parseInt(input.value) == parseInt(input.min)) {
        ele.parentNode.children[3].disabled = true;
    }
    if (ele.parentNode.children[1].disabled) {
        ele.parentNode.children[1].disabled = false;
    }
    updateArray(input);
}



function updateArray(ele) {
    answerArray[constants.questionIndexes.match.indexOf(ele.name)] = ele.value
    edited = true;
}

function postData() {
    if (edited) {
            if (!confirm("Are you sure? The data you currently have in the form will not be submitted.")) {
                    return false;
            }
    }
    var xhr = new XMLHttpRequest();
    xhr.open('POST', "/submit?form=match", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) { //HTTP Success
            localStorage.clear();
            alert("Success! The data was transferred properly.");
        } 
    }
    xhr.onerror = function() { //HTTP error
        alert("Something went wrong.");
    }
    xhr.send(JSON.stringify(localStorage));
}

function resetForm(event) {
    if (confirm("Are you sure? This will finalize the data you have written.")) {
        localStorage.setItem("match"+String(scouterMatchNum), JSON.stringify(answerArray));
        document.getElementsByTagName("form")[0].reset()
        scouterMatchNum++;
        document.getElementById(divNames[currentDiv]).style.display = "none";
        currentDiv = 0;
        document.getElementById(divNames[currentDiv]).style.display = "block";

        for (var i=0; i<document.getElementsByClassName('downButton').length;i++) {
            document.getElementsByClassName('downButton')[i].disabled = true;
        }
        answerArray = new Array(constants.questionIndexes.match.length).fill("0");
        answerArray[1] = "1";
        edited = false;
    } else {
        event.preventDefault();
    }
}

window.onbeforeunload = function(event) {
        if (edited) {
            event.preventDefault();
        }
}
