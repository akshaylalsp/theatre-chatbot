let btn = document.querySelector("body");
// let api_key = "04a03760452fdabea07d13c24071c6e3";

let toggleMenu = document.querySelector(".toggle");
toggleMenu.addEventListener("click", () => {
  console.log("clicked");
  let ul = document.querySelector(".bottomHeader");
  ul.classList.toggle("show");
  toggleMenu.classList.toggle("fa-xmark");
  ul.classList.add("bg");
});
let tv = document.getElementById("tv");
var container = document.getElementsByClassName("container");
let url;
let i = 1;
let api_key = "04a03760452fdabea07d13c24071c6e3";
url = `https://api.themoviedb.org/3/movie/popular?api_key=${api_key}&language=en-US&page=${i}`;


  fetchData();
  let more = document.querySelector("#showMore");
  more.addEventListener("click", showMore);

  function showMore() {
    url = `https://api.themoviedb.org/3/movie/popular?api_key=${api_key}&language=en-US&page=${i}`;
    i++;
    fetchData();
    console.log(i)
  }

function fetchData() {
  fetch(url)
    .then((response) => {
      if (!response.ok) {
        i++;
        const message = `An error has occured: ${response.status}`;
        throw new Error(message);
        console.log(Error(message));
      }
      return response.json();
    })
    .then((movies) => {
      let container = document.querySelector(".container");
      // console.log(movies.results[i].postser_path)
      console.log(movies);
      let myLen = movies.results.length;
      showMovies();

      function showMovies() {
        for (var j = 0; j < myLen; j++) {
          let movie = movies.results[j];
          container.innerHTML += `<div class="box">
      <img src="http://image.tmdb.org/t/p/w500/${movie.poster_path}" alt="img" />
  <div class="moviesDetails">
    <div class="leftDetails">
      <h5>${movie.original_title}</h5>
      <p>${movie.release_date}</p>
    </div>
    <div class="rightDetails rating">${movie.vote_average}</div>
  </div>
</div>`;
        }
      }
    })
    .catch((error) => {
      error.message; // 'An error has occurred: 404'
      console.log(error);
    });
}
