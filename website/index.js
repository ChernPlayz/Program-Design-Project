async function getData(){
  const response = await fetch("https://program-design-project.onrender.com/get-backend-data");
  const data = await response.json();
  //document.getElementById("test").innerText = data.output;
}

window.onload = getData()

function toggleMode(){
  if(document.body.style.backgroundColor === "rgb(47, 53, 58)"){
    document.body.style.backgroundColor = "rgb(216, 223, 228)";
  }
}