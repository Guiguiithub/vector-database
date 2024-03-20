document.addEventListener('DOMContentLoaded', async function() {
    // Function to load initial games
    async function loadInitialGames() {
        const response = await fetch('http://localhost:8000/api/getall');
        if (response.ok) {
            const data = await response.json();
            displayResults(data, 100);
        } else {
            alert('Error loading games. Please try again later.');
        }
    }
    // Call the function to load initial games when the page loads
    loadInitialGames();
});
async function search() {
    const query = document.getElementById('searchInput').value.trim();
    if (query === '') {
        alert('Please enter a search query');
        return;
    }

    const response = await fetch(`http://localhost:8000/api/search?q=${encodeURIComponent(query)}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    });

    if (response.ok) {
        const data = await response.json();
        displayResults(data, 8);
    } else {
        alert('Error searching. Please try again later.');
    }
}

// Function to display search results
function displayResults(results, number) {

    console.log(results)
    const searchResults = document.getElementById('searchResults');
    searchResults.innerHTML = '';

    const firstResult = results.result.splice(0, number);

    firstResult.forEach(result => {
        const devcol = document.createElement('dev');
        devcol.className = 'col mb-4';
        devcol.innerHTML = `
            <div class="card" style="width: 18rem;">
              <img src=${result.img_url} class="card-img-top">
              <div class="card-body">
                <h5 class="card-title">${result.name}</h5>
                <h6 class="card-subtitle mb-2 text-muted">${result.price}</h6>
                <p class="card-text">${truncDescription(result.full_desc.desc)}</p>
                <button class="btn btn-danger" onclick="addDislike('${result.ident}')">No</button>
                <button class="btn btn-success" onclick="addLike('${result.ident}')">Like</button>
              </div>
            </div>
        `;
        searchResults.appendChild(devcol);
    });
}

let likeIds = []
let dislikeIds = []

function addLike(name){
    likeIds.push(name)
}

function addDislike(name){
    dislikeIds.push(name)
}

async function recommand(){
    const response = await fetch("http://localhost:8000/api/recommend", {
        method: 'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({
            likeIds: likeIds,
            dislikeIds: dislikeIds
        })
    });
    if(response.ok){
        const data = await response.json();
        displayResults(data, 8);
    }
    else {
        alert("error")
    }
}

function truncDescription(description){
    if(description.length > 200) {
        description = description.substring(0, 200) + '...';
    }
    if(description.substring(0, 16) === "About This Game "){
        description = description.substring(16, description.length)
    }
    if(description.substring(0, 19) === "About This Content "){
        description = description.substring(19, description.length)
    }
    return description
}