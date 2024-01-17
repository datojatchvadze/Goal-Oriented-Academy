let submit = document.getElementById('submit');
let userName = document.getElementById('name');
let userSurname = document.getElementById('surname');
let userAge = document.getElementById('age');
submit.addEventListener("click", function () {
    userProfile = {
        name: userName.value,
        surname: userSurname.value,
        age: Number(userAge.value)
    };
    console.log(userProfile);
});