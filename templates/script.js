document.getElementById('partNumberForm').addEventListener('submit', async (event) => {
  event.preventDefault();

  const formData = new FormData(event.target);
  const data = Object.fromEntries(formData.entries());

  try {
      const response = await fetch('/api/get-amico-part', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
      });

      if (response.ok) {
          const result = await response.json();
          const resultsList = document.getElementById('results');
          resultsList.innerHTML = '';
          result.part_numbers.forEach((part) => {
              const listItem = document.createElement('li');
              listItem.textContent = part;
              resultsList.appendChild(listItem);
          });
      } else {
          alert('No equivalent parts found.');
      }
  } catch (error) {
      console.error('Error:', error);
  }
});
