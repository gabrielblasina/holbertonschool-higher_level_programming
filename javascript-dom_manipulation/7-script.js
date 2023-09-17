const movies = document.querySelector("#list_movies")
let Res = fetch("https://swapi-api.hbtn.io/api/films/?format=json")
Res.then((res) => res.json()).then((d) => {
  console.log(d)
  for (const movie in d.results) {
    var newLi = document.createElement("li")
    newLi.appendChild(document.createTextNode(d.results[movie].title))
    movie.append(newLi)
  }
});
