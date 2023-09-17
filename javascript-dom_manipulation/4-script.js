const button = document.getElementById("header");
const myList = document.querySelector("#toggle_header");

button.addEventListener("click", function(){
  const new_item = document.createElement("li");
  new_item.textContent = "Item"

  myList.appendChild(new_item);
});
