//1
const person = {
    name: 'dato',
    age: 16,
    city: 'rustavi',
    greet: function(name){
        console.log('welcome back,'+name+'!')
    }
}
//2
let pName = person.name
//3
person.age = 17;
//4
person.country = 'georgia'

//5
person.greet('Luka')
//6
const car1 = {
    produceDate: 2017,
    speed: 220,
    cost: 45000
}
const car2 = {
    produceDate: 2017,
    speed: 220,
    cost: 45000
}
console.log(car1 === car2);
//7
const school = {
    name: 'gimnazium',
    students: [
        {name: "nika", age: 12},
        {name: "gio", age: 15},
        {name: "luka", age: 14}
    ]
}
console.log(school.students[0])
//8
const calculator = {
    substract:function(num1,num2){
        console.log(num1-num2)
    },
    add:function(num1,num2){
        console.log(num1+num2)
    },
    multiply:function(num1,num2){
        console.log(num1*num2)
    },
    division:function(num1,num2){
        console.log(num1/num2)
    }
}
console.log(calculator.division(16,2));
//9
let btn = document.getElementById('btn');
let form = document.getElementById('form');
btn.addEventListener('click',function(){
        if (form.elements.name.value.length >= 5 && form.elements.password.value.length >= 8){
            let user = {
                name: form.elements.name.value,
                password: form.elements.password.value
            };
            console.log(user);
        }
        else{
            alert('not enough letters!')
        }
})