function downloadFile() {
  var obj = [];
  var names = [];
  var inputs = document.getElementsByTagName('input');
  for (var i = 0; i < inputs.length; i++) {
    if (inputs[i].type !== "radio") {
      obj[i] = inputs[i].value;
      names[i] = inputs[i].name;
    } else {
      if (inputs[i].checked) {
        obj[i] = inputs[i].value;
        names[i] = inputs[i].name;
      }
    }
  }
  var data = "data:text/csv;charset=utf-8,";
  data = names.join() + "\n" + obj.join();
  document.getElementById("submitButton").href = "data:" + data;
  document.getElementById("submitButton").download = "data.csv";
}
