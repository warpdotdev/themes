var svgns = "http://www.w3.org/2000/svg";
var xlinkns = "http://www.w3.org/1999/xlink";

console.log("loaded");

function getKey(key) {
  return key.replace("{", "").replace("}", "");
}

function getDictFromUrl() {
  var params = document.defaultView.location.href.split("?")[1].split("&");
  var paramsDict = {}
  for (var i = 0; i < params.length; i++) {
    var name = params[i].split('=')[0]
    var value = params[i].split('=')[1]
    paramsDict[name] = value;
  }
  console.log(paramsDict);
  return paramsDict;
}

function maybeUpdateAttributes(element, dict) {
    var attributes = element.getAttributeNames();
    console.log(attributes);
    for (var i = 0; i < attributes.length; i++) {
      var attribute = attributes[i];
      console.log(attribute);
      var value = element.getAttribute(attribute);
      if (dict[getKey(value)]) {
        element.setAttribute(attribute, dict[getKey(value)]);
      }
      console.log(value);
    }
}

function GetParams() {
  console.log("hello");
  var dynamicElements = document.getElementsByClassName('Dynamic');
  var paramsDict = getDictFromUrl();

  for (var i = 0; i < dynamicElements.length; i++) {
    maybeUpdateAttributes(dynamicElements[i], paramsDict);
  }

}

GetParams();
