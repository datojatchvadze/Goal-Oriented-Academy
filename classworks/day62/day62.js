const me = {
    name: 'dato',
    surname: 'jatchvadze',
    age:15,
}
me.age = 16;
me.studyingPlace = 'GOA';
console.log(me)


const car = {
    name:'mercedes',
    weight:900,
    model:102,
    start: function(){
        console.log('car is starting')
    },
    break: function(seconds){
        for(i = Number(seconds);i>0;i = i-1){
            console.log('car will break in'+i+'seconds')
        }
    }
}
car.start = function(){
    console.log('hello world')
}
car.break(5)

let form = document.getElementById('form');
let btn = document.getElementById('btn');
btn.addEventListener('click',function(){
    userName = form.elements.name.value;
    user = {
        name: userName
    }
    console.log(user)
})