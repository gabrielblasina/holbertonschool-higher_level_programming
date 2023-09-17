const header = document.querySelector("header");
const toggle = document.querySelector("#toggle_header")
toggle.addEventListener("click", (event) =>{
  if (header.classList.contains("red")){
    header.classList.remove("red");
    header.classList.add("green");
  }
  else {
    header.classList.remove("green");
    header.classList.add("red");
  }
});
