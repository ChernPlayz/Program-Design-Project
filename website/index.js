async function getData(){
  /*
  Fetch() sends request
  Flask receives request
  Python runs main.exe
  C++ prints output
  Python capture output
  Flask sends JSON back
  JS display result
  */
  const response = await fetch("http://127.0.0.1:5000/get-cpp-data");
  const data = await response.json();
  document.getElementById("result").innerText = data.output;
}

window.onload = getData()