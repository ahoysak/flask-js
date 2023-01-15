
function valid(form){
            var fail_form = false;

            var first_name = form.first_name.value;
            var last_name = form.last_name.value;
            var email = form.email.value;
            var login = form.login.value;
            var password = form.password.value;
            var password2 = form.password2.value;
            if(first_name == "" || first_name == " ")
                fail_form = "Введіть ваше ім.я";

            else if(last_name == "" || last_name == " ")
                fail_form = "Введіть ваше прізвище";

            else if(email == "" || email == " ")
                fail_form = "Введіть ваш електронний адрес";

            else if(login =="" || login == " ")
                fail_form = "Введіть логін"

            else if(password == "" || password == " ")
                fail_form = "Введіть ваш пароль";

            else if(password2 != password)
                fail_form = "Паролі не сходяться";
            if(fail_form)
                alert(fail_form);
//            else{
//                window.location = '/login';}

        }

    document.getElementById("btn_one").addEventListener('click', ()=>{
        console.log('Text JS')
        const first_name = document.getElementById('first_name').value
        const last_name = document.getElementById('last_name').value
        const email = document.getElementById('email').value
        const login = document.getElementById('login').value
        const password = document.getElementById('password').value
        console.log(document.getElementById('form').last_name.value )
        valid(document.getElementById('form'))
        fetch("/registration", {
            method: 'POST',
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            },
            body: JSON.stringify({ first_name: first_name, last_name: last_name, email: email, login: login,
                    password: password }),

    })
        .then((response) => {
         console.log(response.status)
         if(response.status === 200){
            window.location = '/login';
         }
    })
    })

