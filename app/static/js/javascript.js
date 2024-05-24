const InputFirstName = document.querySelector("#first_name");

console.log(InputFirstName);

InputFirstName.addEventListener("keypress", function(e) {
    const keyCode = (e.keyCode ? e.keyCode : e.wich);

    if(keyCode > 47 && keyCode < 58) {
        e.preventDefault()
    }
});

const InputLastName = document.querySelector("#last_name");

console.log(InputLastName);

InputLastName.addEventListener("keypress", function(e) {
    const keyCode = (e.keyCode ? e.keyCode : e.wich);

    if(keyCode > 47 && keyCode < 58) {
        e.preventDefault()
    }
});

const InputUsuario = document.querySelector("#usuario");

console.log(InputUsuario);

InputUsuario.addEventListener("keypress", function(e) {
    const keyCode = (e.keyCode ? e.keyCode : e.wich);

    if(keyCode > 47 && keyCode < 58) {
        e.preventDefault()
    }
});

