document.addEventListener("DOMContentLoaded", function(event) {
  var teamAverages = {};
  function onlyUnique(value, index, self) {
    return self.indexOf(value) === index;
  }
  var teamList = [];
  for (var j = 0; j < JSON.parse(data.match).length; j++) {
    teamList[j] = JSON.parse(data.match)[j][0]
  }
  teamList = teamList.filter(onlyUnique);
  if (teamList.length > 0) {
    var least = 0;
    var most = 0;
    for (var i = -1; i < teamList.length; i++) {
      var matches = JSON.parse(data.match).filter(function(x){ return x[0] == teamList[i]; });
      var row = document.createElement('tr')
      for (var j = 0; j < constants.dataCalculationHeaders.length; j++) {
        if (i == -1) {
          var item = document.createElement("th");
          item.innerHTML = constants.dataCalculationHeaders[j];
          item.id = j;
          item.addEventListener('click', function(){sort(this);});
          row.style.backgroundColor = "#b10003";
          row.style.cursor = "pointer";
        } else {
          var item = document.createElement('td');
          switch (j) {
            case 0:
              item.innerHTML = teamList[i]
              break;
            case 1://GETTING MATCHES OBSERVED 0
              item.innerHTML = matches.length;
              break;
            case 2://GETTING AVG START POINT
            case 3://GETTING AVG CARGO HIGH
            case 4://GETTING AVG CARGO MID
            case 5://GETTING AVG CARGO LOW
              item.innerHTML = arraySum(getColData(matches, [j])) / getColData(matches, [j]).length
              break;
            case 6: //GETTING LEAST CARGO CYCLES
              item.innerHTML = Math.min(...getColData(matches, [3, 5]));
              break;
            case 7://GETTING MOST CARGO CYCLES
              item.innerHTML = Math.max(...getColData(matches, [3, 5]));
              break;
            case 8://GETTING AVG CARGO PLACED
              item.innerHTML = arraySum(getColData(matches, [3, 5])) / getColData(matches, [3, 5]).length
              break;
            case 9://GETTING STD DEV CARGO
              item.innerHTML = stdDev(getColData(matches, [3, 5]))
              break;
            case 10://GETTING AVG HATCH HIGH
            case 11://GETTING AVG HATCH MID
            case 12://GETTING AVG HATCH LOW
              item.innerHTML = arraySum(getColData(matches, [j-4])) / getColData(matches, [j-4]).length
              break;
            case 13://GETTING LEAST HATCH CYCLES
              item.innerHTML = Math.min(...getColData(matches, [6, 8]));
              break;
            case 14://GETTING MOST HATCH CYCLES
              item.innerHTML = Math.max(...getColData(matches, [6, 8]));
              break;
            case 15://GETTING AVG HATCH PLACED
              item.innerHTML = arraySum(getColData(matches, [6, 8])) / getColData(matches, [6, 8]).length
              break;
            case 16://GETTING STD DEV HATCH
              item.innerHTML = stdDev(getColData(matches, [6, 8]))
              break;
            case 17://GETTING LEAST CYCLES
              item.innerHTML = Math.min(...getColData(matches, [3, 8]));
              break;
            case 18://GETTING MOST CYCLES
              item.innerHTML = Math.max(...getColData(matches, [3, 8]));
              break;
            case 19://GETTING AVERAGE CYCLES
              item.innerHTML = arraySum(getColData(matches, [3, 8])) / getColData(matches, [3, 8]).length
              break;
            case 20://GETTING STD DEV CYCLES
              item.innerHTML = stdDev(getColData(matches, [3, 8]))
              break;
            case 21://GETTING BEST CLIMB
              item.innerHTML = Math.max(...getColData(matches, [11]));
              break;
            case 22://GETTING % OF MATCHES BEST CLIMB ACHIEVED
              item.innerHTML = String(getColData(matches, [11]).reduce(function(a, b) {
                  return a + (b === Math.max(...getColData(matches, [11])));
              }, 0)/getColData(matches, [11]).length * 100) + "%";

              break;
          }
          if (item.innerHTML.length > 4) {
            item.innerHTML = Math.round(100*parseFloat(item.innerHTML))/100;
          }
        }
        row.appendChild(item)
      }
      document.getElementById('averagesTable').appendChild(row)
    }
  } else {
    p = document.createElement("p");
    h5 = document.createElement("h5")
    h5.className = "noDataIcon";
    h5.innerHTML = "&#xe002;";
    p.innerHTML = "No Data Found";
    p.style.marginTop = "2px";
    document.getElementById('averagesTable').parentNode.appendChild(h5);
    document.getElementById('averagesTable').parentNode.appendChild(p);
  }

});

function arraySum(array) {
  return array.reduce(function(a,b){
    return a + parseFloat(b)
  }, 0);
}

function stdDev(array) {
  var mean = arraySum(array)/array.length;
  var devArray = []
  array.forEach(function(item) {
    devArray.push(Math.pow(item-mean, 2));
  });
  return Math.sqrt(arraySum(devArray)/devArray.length);
}

function getColData(array, colArray) {
  var colData = []
  if (colArray.length == 1) {
    for (var c = 0; c < array.length; c++) {
      colData.push(parseFloat(array[c][colArray[0]]))
    }
    return colData;
  } else {
    for (var c = 0; c < array.length; c++) {
      colData.push(parseFloat(arraySum(array[c].slice(Math.min(...colArray), Math.max(...colArray)+1))))
    }
    return colData;
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
