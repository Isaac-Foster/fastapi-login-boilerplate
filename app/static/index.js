const form = document.querySelector("form");

document.querySelector('form').addEventListener('submit', event => {
    event.preventDefault();
    const formData = new FormData(form);
    const formObject = {};
        formData.forEach((value, key) => {
            formObject[key] = value;
        });

    
        axios.post('http://localhost:8000/api/users/signin', formObject)
        .then(response => {
            console.log('POST Response:', response.data);
        })
        .catch(error => {
            console.error('POST Error:', error);
        });



        /* fetch('http://127.0.0.1:8000/api/users/signin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formObject)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro HTTP, status ' + response.status);
            }
            return response.json();
        })
        .then(data => {
            console.log('Resposta:', data);
        })
        .catch(error => {
            console.error('Erro ao fazer requisição:', error);
        });*/




        /* axios.delete('/your-endpoint', {
            data: {
                id: 12345
            }
        })
        .then(response => {
            console.log('DELETE Response:', response.data);
        })
        .catch(error => {
            console.error('DELETE Error:', error);
        }); */
        
        
    }
)
