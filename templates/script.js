document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('partNumberForm');
    const resultsContainer = document.getElementById('results');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent default form submission

        // Collect input data
        const model = document.getElementById('model').value;
        const mounting = document.getElementById('mounting').value;
        const diffuser = document.getElementById('diffuser').value;
        const lamp = document.getElementById('lamp').value;
        const driver = document.getElementById('driver').value; 
        const voltage = document.getElementById('voltage').value;
        const doorframe = document.getElementById('doorframe').value;
        const options = document.getElementById('options').value;
        const accessories = document.getElementById('accessories').value;

        const requiredFields = { model, mounting, diffuser, lamp, driver, voltage, doorframe, options, accessories };
        for (const [field, value] of Object.entries(requiredFields)) {
            if (!value) {
                alert(`Please provide the ${field} part number.`);
                return;
            }
        }

        try {
          // Axios POST request
          const response = await axios.post('/api/search-part', requiredFields);
          console.log('Response data:', response.data);

          resultsContainer.innerHTML = ''; // Clear previous results

          if (Object.keys(response.data).length > 0) {
              for (const [key, value] of Object.entries(response.data)) {
                  const resultItem = document.createElement('li');
                  resultItem.textContent = `${key}: ${value || 'No equivalent found'}`;
                  resultsContainer.appendChild(resultItem);
              }
          } else {
              resultsContainer.textContent = 'No equivalent part found.';
          }
      } catch (error) {
          console.error('Error:', error);
          if (error.response) {
              // The request was made, and the server responded with a status code outside 2xx
              alert(`Error: ${error.response.data.error || 'Unknown error occurred.'}`);
          } else if (error.request) {
              // The request was made but no response received
              alert('Error: No response from the server.');
          } else {
              // Something else caused the error
              alert(`Error: ${error.message}`);
          }
      }  
});
}); 

  
/* try {
  const response = await fetch('/api/search-part', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(requiredFields),
  });

  console.log('Response status:', response.status);
  console.log('Response headers:', Array.from(response.headers.entries()));

  if (!response.ok) {
    const errorData = await response.json();
    console.error('Backend error:', errorData);
    alert(`Error: ${errorData.error || 'Unknown error occurred.'}`);
    return;
}

  /* const responseText = await response.text(); // Read as plain text first
  if (!responseText.trim()) {
      alert('Error: Empty response from the server.');
      return;
  }
  const data = JSON.parse(responseText); // Parse JSON after checking for content
  

  const results = await response.json(); 
  console.log('Response data:', results)
  resultsContainer.innerHTML = ''; // Clear previous results

  if (Object.keys(results).length > 0) {
      for (const [key, value] of Object.entries(results)) {
          const resultItem = document.createElement('li');
          resultItem.textContent = `${key}: ${value || 'No equivalent found'}`;
          resultsContainer.appendChild(resultItem);
      }
  } else {
      resultsContainer.textContent = 'No equivalent part found.';
  }
} catch (error) {
  console.error('Error:', error);
  alert('An error occurred while searching for the part.');
}
});

*/ 