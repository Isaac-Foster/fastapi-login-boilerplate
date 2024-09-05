
const formRegister = document.getElementById("register");

document.getElementById('register').addEventListener('submit', event => {
    event.preventDefault();
    const formData = new FormData(formRegister);
    
    const formObject = {};
        formData.forEach((value, key) => {
            formObject[key] = value;
        });
    
    if (formData.passwd == formData.confirmPasswd) {
        console.log("senhas iguais");

        delete formObject.confirmPasswd;
        console.log(formObject);

        axios.post(
        '/api/users/signup', formObject, { withCredentials: true}
        ).then(
            response => {
                console.log('POST Response:', response.data);
                window.location.href = "/";
            }
        ).catch(error => {console.error('POST Error:', error);}
        )
    } else {
        console.log("senhas diferentes");
        console.log(formObject);
    }
    }
);