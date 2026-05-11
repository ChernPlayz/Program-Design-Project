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
  const response = await fetch("https://program-design-project.onrender.com/get-backend-data");
  const data = await response.json();
  document.getElementById("title").innerText = data.output;
}

window.onload = getData()