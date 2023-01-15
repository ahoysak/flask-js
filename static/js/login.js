
function validation (form) {
        var fail = false;
        var email = form.email.value;
        var password = form.password.value;
        if(email == "" || email == " ")
            fail = "Не вірний email!";
        else if (password == "" || password == " ")
            fail = "Не вірний пароль!";

        if (fail)
            alert(fail);
    }

    document.getElementById("btn_two").addEventListener('click', ()=>{
        console.log('Text for JS')
        const email = document.getElementById('email').value
        const password = document.getElementById('password').value

        validation(document.getElementById('test_form'))
        fetch("/login", {
            method: 'POST',
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            },
            body: JSON.stringify({ email: email, password: password }),
    })
        .then((response) => {
         console.log(response.status)
         if(response.status === 200){
            window.location = '/';
         }
    })
    })