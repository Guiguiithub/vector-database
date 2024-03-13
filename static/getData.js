document.addEventListener('DOMContentLoaded', async function() {
    // Function to load initial games
    async function loadInitialGames() {
        const response = await fetch('http://localhost:8000/api/getall');
        if (response.ok) {
            const data = await response.json();
            console.log(data)
            displayResults(data);
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
        displayResults(data);
    } else {
        alert('Error searching. Please try again later.');
    }
}

// Function to display search results
function displayResults(results) {

    const searchResults = document.getElementById('searchResults');
    searchResults.innerHTML = '';

    console.log(results)
    const firstResult = results.result.splice(0, 5);

    firstResult.forEach(result => {
        const li = document.createElement('li');
        li.className = 'result-item';
        li.innerHTML = `
            <img src=${result.img_url}>
            <h3>${result.name}</h3>
            <p>price: ${result.price}</p>
            <p>${result.score}</p>
        `;
        searchResults.appendChild(li);
    });
}