document.getElementById('partNumberForm').addEventListener('submit', async (event) => {
    event.preventDefault();
  
    const formData = new FormData(event.target);
    const partNumber = formData.get('part_number');
  
    try {
        const response = await fetch(`/api/get-amico-part/${encodeURIComponent(partNumber)}`, {
            method: 'GET',
        });
  
        if (response.ok) {
            const result = await response.json();
            const resultsList = document.getElementById('results');
            resultsList.innerHTML = '';
            result.kenall_models.forEach((model) => {
                const listItem = document.createElement('li');
                listItem.textContent = model;
                resultsList.appendChild(listItem);
            });
        } else {
            alert('No equivalent parts found.');
        }
    } catch (error) {
        console.error('Error:', error);
    }
  });
  