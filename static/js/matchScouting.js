function increase(ele) {
  var input = ele.parentNode.children[2];
  input.value = parseInt(input.value) + 1;
  if (parseInt(input.value) == parseInt(input.max)) {
    ele.parentNode.children[1].disabled = true;
  }
  if (ele.parentNode.children[3].disabled) {
    ele.parentNode.children[3].disabled = false;
  }
}

function decrease(ele) {
  var input = ele.parentNode.children[2];
  input.value = parseInt(input.value) - 1;
  if (parseInt(input.value) == parseInt(input.min)) {
    ele.parentNode.children[3].disabled = true;
  }
  if (ele.parentNode.children[1].disabled) {
    ele.parentNode.children[1].disabled = false;
  }
}
