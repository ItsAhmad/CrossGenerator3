document.getElementById('partNumberForm').addEventListener('submit', async (event) => {
    event.preventDefault();
  
    const formData = new FormData(event.target);
    const partNumber = formData.get('part_number');
  
    async function fetchAmicoPart(partNumber, category) {
        try {
            const response = await fetch('/api/get-amico-part', {
                method: 'POST',  // Change to POST
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    part_number: partNumber,  // Send part number in body
                    category: category        // Send category in body
                }),
            });
    
            if (response.ok) {
                const result = await response.json();
                const resultsList = document.getElementById('results');
                resultsList.innerHTML = ''; // Clear the list
                const partNumber = result.kenall_part_number;
                const amicoPartNumber = result.amico_part_number;
                const listItem = document.createElement('li');
                listItem.textContent = `Kenall Part: ${partNumber}, Amico Part: ${amicoPartNumber}`;
                resultsList.appendChild(listItem);
            } else {
                alert('No equivalent parts found.');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    }
  });
  