document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('partNumberForm');
    const resultsContainer = document.getElementById('results');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); 

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

        const requiredFields = { model, mounting, diffuser, lamp, driver, voltage, doorframe };
        for (const [field, value] of Object.entries(requiredFields)) {
            if (!value) {
                alert(`Please provide the ${field} part number.`);
                return;
            }
        }

        const requestData = { 
          ...requiredFields, 
          options: options || '000',  
          accessories: accessories || '00'  
      };

        try {
          // use Axios for json requests
          const response = await axios.post('https://crossgeneratordynamic.onrender.com/api/search-part', requestData);
          console.log('Response data:', response.data);

          resultsContainer.innerHTML = ''; 

          if (Object.keys(response.data).length > 0) {
            const data = response.data;

            const formattedResult = [
              'L',
              data['Amico Model'],
              data['Amico Voltage'],
              data['Amico Function'],
              data['Amico CCT'],
              'A',
              data['Amico Mounting'], 
              data['Amico Switch'],
              data['Amico Options']
            ].join('-');

            const resultItem = document.createElement('li');
            resultItem.textContent = formattedResult;
            
            resultsContainer.appendChild(resultItem);

          } else {
            const resultItem = document.createElement('li');
            resultItem.textContent = 'No Equivalent Found'; 
            resultsContainer.appendChild(resultItem);
          }

      } catch (error) {
          console.error('Error:', error);
          if (error.response) {
              // If server responds with error code
              alert(`Error: ${error.response.data.error || 'Unknown error occurred.'}`);
          } else if (error.request) {
              // If request was sent, but server sends blank response 
              alert('Error: No response from the server.');
          } else {
              // Isusé Boze buddy it's chopped 
              alert(`Error: ${error.message}`);
          }
      }  
});
}); 


/* 

L-SEC22-120-E200-L30-A-F-000-00

*/ 

  
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