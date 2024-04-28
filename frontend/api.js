// movies.js

document.addEventListener('DOMContentLoaded', function () {
    fetchMovies();
});

async function fetchMovies() {
    try {
        const response = await fetch('https://api. .com/movies');
        if (!response.ok) {
            throw new Error('Failed to fetch movies');
        }
        const data = await response.json();
        displayMovies(data);
    } catch (error) {
        console.error('Error fetching movies:', error.message);
    }
}

function displayMovies(movies) {
    const moviesContainer = document.querySelector('.movies'); 
    movies.forEach(movie => {
        const movieElement = createMovieElement(movie);
        moviesContainer.appendChild(movieElement);
    });
}

function createMovieElement(movie) {
    const movieElement = document.createElement('div');
    movieElement.classList.add('movie');
    movieElement.innerHTML = `
        <img src="${movie.poster}" alt="${movie.title}">
        <h3>${movie.title}</h3>
        <p>${movie.description}</p>
        <a href="#">Read More</a>
    `;
    return movieElement;
}










<script src="movies.js"></script>