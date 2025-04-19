fetch('http://localhost:10000/')
  .then(response => response.json())
  .then(data => {
    console.log(data.message);  // Output: Welcome to PawPal!
    document.getElementById('output').innerText = data.message;
  })
  .catch(error => console.error('Error:', error));

