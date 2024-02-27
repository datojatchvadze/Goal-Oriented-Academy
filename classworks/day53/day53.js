const me = {
    name: "dato",
    surname: "jatchvadze",
    age: 16,
    title: "student",
    bankEqaunt: {
        produceDate: 2017,
        cardCode: 249383921,
        balanceInDollars: 500,
    },
    getName: function(){
        console.log(you.name)
    }
}

const you = {
    name: "luka",
    surname: "tskhvaradze",
    age: 17,
    title: "lector",
    bankEqaunt: {
        produceDate: 2019,
        cardCode: 105964835,
        balanceInDollars: 50000000,
    },
    getName: function(){
        console.log(you.name)
    }
}

let form = document.getElementById('numbers');
let btn = document.getElementById('btn');
btn.addEventListener('click', function () {
    let num1 = Number(form.elements.num1.value);
    let num2 = Number(form.elements.num2.value);
    console.log(num1 + num2);
});