let form = document.getElementById('form');
btn.addEventListener("click",function(){
    let age = form.elements.age.value;
    let name = form.elements.name.value;
    let password = form.elements.password.value;
    profile = {
        userName: name,
        userAge: age,
        userPassword: password
    }
    console.log(profile);
})