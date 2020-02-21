let answerArray = new Array(19).fill("0");
let scouterMatchNum = 0;

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
    localStorage.setItem("match"+String(scouterMatchNum), JSON.stringify(answerArray));
}

function postData() {
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

function resetForm() {
    if (confirm("Are you sure? This will finalize the data you have written.")) {
        document.getElementsByTagName("form")[0].reset()
        scouterMatchNum++;
    }
}
