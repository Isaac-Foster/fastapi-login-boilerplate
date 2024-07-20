const form = document.querySelector("form");

document.querySelector('form').addEventListener('submit', event => {
    event.preventDefault();
    const formData = new FormData(form);
    const formObject = {};
        formData.forEach((value, key) => {
            formObject[key] = value;
        });

        console.log(formObject)
    
        axios.post(
            'http://localhost:8000/api/users/signin',
            formObject
        )
        .then(response => {
            console.log('POST Response:', response.data);
        })
        .catch(error => {
            console.error('POST Error:', error);
        });
        
    }
)
