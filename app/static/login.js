
document.addEventListener('DOMContentLoaded', () => {

    const formLogin = document.getElementById("login");

    document.getElementById('login').addEventListener('submit', event => {
        event.preventDefault();
        const formData = new FormData(formLogin);

        const formObject = {};
            formData.forEach((value, key) => {
                formObject[key] = value;
            });

        console.log(formObject)
    
        axios.post(
            '/api/users/signin',
            formObject,
            {
                withCredentials: true
            }
        )
        .then(response => {
            console.log('POST Response:', response.data);
            window.location.href = "/profile";

        })
        .catch(error => {
            console.error('POST Error:', error);
        });        
            
        }
    );
}); 


