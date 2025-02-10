/*--    Authors:   			Eric Bridgens | Joshua Dickens | Sunny He | Kyle Willoughby     --*/
/*--    Creation Date:  	August 15, 2024                                                 --*/
/*--    Project Name:   	StatVision                                                      --*/

// Define arrays for supported leagues and content types
const leagues = ['mlb', 'nba', 'nfl'];
const content_types = ['player', 'team'];

// Define the host, key, and base url for the api
const api_host = 'sports-information.p.rapidapi.com';
const api_key = '57d0de8e70msh8dfd6aa90a4f540p1056dejsn93b82d089ef1';
const api_url = new URL(`https://${api_host}`);

// Define the options object for the fetch call, including method and headers
const options = {
    method: 'GET',
    headers: {
        'x-rapidapi-host': api_host,
        'x-rapidapi-key': api_key
    }
};

// Define maximum number of autocomplete options to display
max_autocomplete_options = 5



// Retrieve the input element reference from the document
const searchInput = document.getElementById('search-input')

// Retrieve the container element for the autocomplete list
const autocompleteList = document.getElementById('autocomplete-list')

// Save the default html content of the autocomplete list defined in html file
const defaultSuggestions = Array.from(autocompleteList.querySelectorAll('#autocomplete-item'));



// Define an asynchronous function to fetch suggestions based on the query
async function fetchSuggestion(query) {

    // Create a fresh url object by appending search api endpoint to the base api url
    const search_url = new URL('search', api_url);

    // Append the query parameter and value to the api search parameters
    search_url.searchParams.append('query', query);
    
    // Log the complete url being used for the fetch request
    console.log("Fetching from:", search_url.href);
    
    // Perform the fetch request with the provided options, then parse the response as json
    let data = await fetch(search_url, options).then(response => response.json());

    // Log the raw api response data
    console.log("API Results:", data);
    
    // Filter the api results to only include supported data
    data = (data.results || [])
    
    // Filter The results to only include results that are related to supported content types
    .filter(result =>
        content_types.some(content_type =>
            result.type.toLowerCase() === content_type.toLowerCase()
        )
    )

    // Filter The results to only include results that are related to supported leagues
    .map(result => {
        return {...result, contents: result.contents.filter(content =>
            leagues.some(league =>
                content.defaultLeagueSlug && content.defaultLeagueSlug.toLowerCase() === league.toLowerCase()
            )
        )};
    })

    // Initialize array to results
    let results = [];

    // Loop through filtered data results
    data.forEach( result => {

        // loop through result contents and add to list of results
        result.contents.forEach( content => { 
            results.push(content)
        });
    });
    
    // Log the filtered results after processing
    console.log("Filtered Results:", results);
    
    
    // Return a new promise that resolves after a slight delay
    return new Promise(resolve => {

        // Set a timeout to simulate a delay
        setTimeout(() => {

            // Resolve the promise with an array of length up to the maximum number of autocomplete options
            resolve(results.slice(0,max_autocomplete_options));

        }, 300);
    });
}



// Define an asynchronous function to update the autocomplete list based on user input
async function updateAutocompleteOptions() {

    // Log that update autocomplete options has been triggered
    console.log("Update Autocomplete Options Triggered");

    // Get the trimmed value of the search input
    const query = searchInput.value.trim();

    // Check if the input query string is empty
    if (query === '') {

        // Restore the default suggestions and return control
        autocompleteList.replaceChildren(...defaultSuggestions.map(li => li.cloneNode(true)));
        return;
    }
    
    try {

        // Wait for autocomplete options to be fetched based on the query
        const autocompleteOptions = await fetchSuggestion(query);

        // Log the autocomplete options
        console.log("Autocomplete Options:", autocompleteOptions);

        // Get a list of the current list item elements in the autocomplete list
        const autocompleteItems = Array.from(autocompleteList.querySelectorAll('#autocomplete-item'));

        // Loop through each autocomplete option in the list of autocomplete options
        autocompleteOptions.forEach((autocompleteOption, index) => {

            // Create a new list item element for the autocomplete list
            const li = document.createElement('li');
            li.id = 'autocomplete-item';

            // Create a new a element
            const a = document.createElement('a');

            // Check if the current autocomplete option contains a link
            if (autocompleteOption.link) {

                // Add an href link to the a element
                a.href = autocompleteOption.link.web;
            }

            // If the autocompletion option has an image url
            if (autocompleteOption.image) {

                // Create a new img element and define img source url
                const img = document.createElement('img');
                img.src = autocompleteOption.image.default;

                // Append an img element as a child element of the a element
                a.appendChild(img);
            }
            else {

                // Create a new i element for and define icon sport
                const i = document.createElement('i');
                i.className = `fa-solid fa-${autocompleteOption.sport}-ball fa-xl`;

                // Append an i element as a child element of the a element
                a.appendChild(i);
            }

            // Append a text element as a child element of the a element
            a.appendChild(document.createTextNode(autocompleteOption.displayName));

            // Append the a element as a child element of the new list item element
            li.appendChild(a);


            // Check if there is an existing list item at this index
            if (index < autocompleteItems.length) {

                // Update the existing list item element in the autocomplete list
                autocompleteList.replaceChild(li, autocompleteItems[index]);

            } else {
                // Append the list item element as a child element of the autocomplete list
                autocompleteList.appendChild(li);
            }
        });
        
        // Remove old autocomplete options from the autocomplete list
        while (autocompleteList.children.length != autocompleteOptions.length) {
            autocompleteList.removeChild(autocompleteList.lastElementChild);
        }

        // Check if the default suggestions can be added to autocomplete list without exceeding limit
        if (autocompleteOptions.length + defaultSuggestions.length <= max_autocomplete_options) {

            // Loop through default suggestions
            for (let index = 0; index < defaultSuggestions.length; index++) {

                // Append the default suggestion to the autocomplete list
                autocompleteList.appendChild(defaultSuggestions[index]);
            }
        }
        
        // Log the final autocomplete list
        console.log("autocomplete-list: ", autocompleteList);
    
    } catch (err) {

        // Log any errors that occur
        console.error(err);

        // Revert the autocomplete list to the default suggestions
        autocompleteList.replaceChildren(...defaultSuggestions.map(li => li.cloneNode(true)))
    }
}



// Listen for a click event on the element with class "clear-icon" to clear the search input
document.querySelector('#clear-icon').addEventListener(

    // Specify the event type as 'click' and define the callback function that runs when the clear icon is clicked
    'click', function() {

        // Retrieve the search input element by its id "search-input"
        const input = document.getElementById('search-input');

        // Clear the search input value by setting it to an empty string
        input.value = '';  

        // Set focus back to the search input so the user can start typing immediately
        input.focus();
        
        // Dispatch an 'input' event on the search input to trigger any associated event listeners
        input.dispatchEvent(new Event('input'));
    }
);



// Listen for input events and update suggestions as the user types.
searchInput.addEventListener('input', updateAutocompleteOptions);
