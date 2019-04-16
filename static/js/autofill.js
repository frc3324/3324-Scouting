var data;
var element;

function loadJSON(callback) {
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    var url = "/teamInformation.json";
    xobj.onreadystatechange = function () {
        if (this.status == 200 && this.readyState == 4) {
          data = JSON.parse(this.responseText);
          autocomplete(element, data);
        }
    };

    xobj.open("GET", url, true);
    xobj.send();
 }


function autocomplete(inp, arr) {
  arr = arr.teams
  var currentFocus;
  inp.addEventListener("input", function(e) {
      debugger;
      document.getElementById("teamNumberInput").style.marginBottom = "0px";

      var a, b, i, val = this.value;
      var resultsNumber = 0
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-item-lists");
      this.parentNode.appendChild(a);

      for (i = 0; i < arr.length; i++) {
        if (String(arr[i].teamNumber).substr(0, val.length).toUpperCase() == String(val).toUpperCase()) {
          resultsNumber++
          b = document.createElement("DIV");
          b.setAttribute("class", "autocomplete-items")
          b.innerHTML = "<strong>" + String(arr[i].teamNumber).substr(0, val.length) + "</strong>";
          b.innerHTML += String(arr[i].teamNumber).substr(val.length);
          b.innerHTML += "<input type='hidden' value='" + String(arr[i].teamNumber) + "'>";
              b.addEventListener("click", function(e) {
              inp.value = this.getElementsByTagName("input")[0].value;
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
      if (resultsNumber == 0) {
        b = document.createElement("p");
        b.setAttribute("class", "autocompleteEmptyText");
        b.innerHTML = "No Results"
        a.appendChild(b);
      }
});

  function addActive(x) {
    if (!x) return false;
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    var x = document.getElementsByClassName("autocomplete-item-lists");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
      x[i].parentNode.removeChild(x[i]);
    }
  }
}


document.addEventListener("click", function (e) {
    closeAllLists(e.target);
});
}

window.addEventListener("beforeUnload", function() {
  closeAllLists();
});


document.addEventListener("DOMContentLoaded", function(event) {
element = document.getElementById("teamNumberInput");
loadJSON();
});
