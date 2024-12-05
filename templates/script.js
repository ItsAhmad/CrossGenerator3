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


        if (!model) {
            alert('Please provide the model part number.');
            return;
        }
        
        if (!mounting) {
            alert('Please provide the mounting part number.');
            return;
        }
        
        if (!diffuser) {
            alert('Please provide the diffuser part number.');
            return;
        }
        
        if (!lamp) {
            alert('Please provide the lamp part number.');
            return;
        }
        
        if (!driver) {
            alert('Please provide the driver part number.');
            return;
        }
        
        if (!voltage) {
            alert('Please provide the voltage part number.');
            return;
        }
        
        if (!doorframe) {
            alert('Please provide the doorframe part number.');
            return;
        }
        
        if (!options) {
            alert('Please provide the options part number.');
            return;
        }

        if (!accessories) {
            alert('Please provide the accessories part number.');
            return;
        }
        

        try {
            // Send data to the server
            const response = await fetch('/api/search-part', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 
                  model,
                  mounting,
                  diffuser,
                  lamp,
                  driver,
                  voltage,
                  doorframe,
                  options,
                  accessories
                }),
            });

            console.log("Response status:", response.status);
            console.log("Response body (raw):", await response.text());

            if (!response.ok) {
              // Handle non-200 responses
              const errorData = await response.json();
              alert(`Error: ${errorData.error}`);
              return;
          }
  
          const responseText = await response.text(); // Read as plain text first
          if (responseText.trim() === '') {
              alert('Error: Empty response from the server.');
              return;
          }
  
          const data = JSON.parse(responseText); // Parse JSON only if non-empty
          resultsContainer.innerHTML = ''; // Clear previous results
  
          if (Object.keys(data).length > 0) {
              for (const [key, value] of Object.entries(data)) {
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
});

  
