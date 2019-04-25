document.addEventListener("DOMContentLoaded", function(event) {
//Scouting Table Creation
for (var t = 0; t < constants.tables.length; t++) {
  var tableVar = constants.tables[t]
  if (JSON.parse(window.data[tableVar]).length > 0) {
    for (var i = -1; i < JSON.parse(window.data[tableVar]).length; i++) {
      var row = document.createElement("tr");
      for (var j = 0; j < JSON.parse(window.data[tableVar])[0].length; j++) {
        if (i == -1) {
          var item = document.createElement("th");
          item.innerHTML = window.constants.questions[tableVar][j];
          item.id = j;
          item.addEventListener('click', function(){sort(this);});
          item.style.cursor = "pointer";
          row.style.backgroundColor = "#b10003"
          row.appendChild(item);
        } else {
          row.addEventListener('click', function(){selectRow(this)});
          row.style.cursor = "pointer"
          var item = document.createElement("td");
          if (window.constants.questions[tableVar][j] == "Other") { //Testing if the item is the "other" section (which can be lengthy)
            var div = document.createElement("div");
            div.className = "otherNotes";
            div.innerHTML = JSON.parse(window.data[tableVar])[i][j];
            item.appendChild(div);
            row.appendChild(item);
          } else {
            item.innerHTML = JSON.parse(window.data[tableVar])[i][j];
            row.appendChild(item);
          }
        }
      }
      document.getElementById(tableVar + "Table").appendChild(row);
    }
  } else {
    p = document.createElement("p");
    h5 = document.createElement("h5")
    h5.className = "noDataIcon";
    h5.innerHTML = "&#xe002;";
    p.innerHTML = "No Data Found";
    p.style.marginTop = "2px";
    document.getElementById(tableVar + 'Table').parentNode.appendChild(h5);
    document.getElementById(tableVar + 'Table').parentNode.appendChild(p);
  }

}
});



function collapse(ele) {
  if (ele.parentNode.children[2].style.display !== "none") { //Closing
    ele.parentNode.children[0].style.margin = "0";
    ele.parentNode.children[2].style.display = "none";
    ele.innerHTML = "&#xe5c5;";
  } else { //Opening
    ele.parentNode.children[0].style.margin = "";
    ele.parentNode.children[2].style.display = "block";
    ele.innerHTML = "&#xe5c7;";
  }
}

function selectRow(ele) {
  debugger;
  for (var i = 0; i < ele.parentNode.children.length; i++) {
    if (ele.parentNode.children[i] == ele && !ele.classList.contains("selectedRow")) {
      ele.classList.add("selectedRow");
    } else {
      ele.parentNode.children[i].classList.remove("selectedRow");
    }
  }
}

function sort(ele) {
  debugger;
  var i;
  var col = ele.id
  var switching = true;
  var dir = 1;
  var makeSwitch = false;
  var switchCount = 0;
  var table = document.getElementsByTagName('table')[0]
  while (switching) {
    switching = false;
    for (i = 1; i < (table.rows.length-1); i++) {
      if (dir == 1) {
        if (parseInt(table.rows[i].children[col].innerHTML) < parseInt(table.rows[i+1].children[col].innerHTML)) {
          makeSwitch = true;
          break;
        }
      } else if (dir == 0) {
        if (parseInt(table.rows[i].children[col].innerHTML) > parseInt(table.rows[i+1].children[col].innerHTML)) {
          makeSwitch = true;
          break;
        }
      }
    }
    if (makeSwitch) {
      table.rows[i].parentNode.insertBefore(table.rows[i + 1], table.rows[i]);
      switching = true;
      switchCount++;
    } else {
      if (switchCount == 0 && dir == 1) {
        dir = 0;
        switching = true;
      }
    }
  }
}
