const updateButton = document.getElementById("update_header");

updateButton.addEventListener("click", (event) => {
  document.querySelector("header").textContent = "New Header!!!"
});
