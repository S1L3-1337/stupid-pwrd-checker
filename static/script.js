document.getElementById('sendBtn').addEventListener('click', function () {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (email && password) {
        fetch('/hash', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        })
            .then(response => response.json())
            .then(data => {
                document.getElementById('hashResult').textContent = data.hash;
                document.getElementById('output').style.display = 'block';
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById('hashResult').textContent = 'Error: ' + error.message;
                document.getElementById('output').style.display = 'block';
            });
    } else {
        alert('Please fill in both email and password fields');
    }
});
