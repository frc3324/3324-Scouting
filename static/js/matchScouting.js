boolean cookieCheck;

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

// make a cookie if this is the first input this page, then set currentCookie to true and update data
function bakeCookies() {
    if (cookieCheck == false)
	document.cookie = "currentCookie";
    cookieCheck = true;
    else {
	currentCookie = ;
    }
	}

// set currentCookie to false so that a new one will be created, and reset page to default values
function newPage() {
    
}

// sets variables values equal to html values in JSON
function htmlToVar(var var1) {

    var var2 = variablesName(var1) + ": " + var1;

    return var2;
}
