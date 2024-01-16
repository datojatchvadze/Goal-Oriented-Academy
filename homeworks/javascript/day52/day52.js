const me = {
    name: "dato",
    surname: 'jatchvadze',
    age:16,
    birthday:"27september",
    studingAt:"goa",
    livingIn:"rustavi",
    engine:function(){
        this.name.textcontent = "nika"
    }
}

const car = {
    color: "red",
    produceDate: "2019",
    brend: "porshe",
    doors: 2,
    horsepower: 250,
    engine: {   
    DisplacementInLiters: 3,
    FuelType: "gasoline",
    Aspiration:'Naturally Aspirated' 
    },
    engine:function(){
        console.log(engine)
    }

}


//creating objects from user inputs
let submit = document.getElementById('btn');
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

//woring with one function from another
const academy = {
    name:"GOA",
    peopleAmount:350,
    lectorsAmount:2,
    ranking:"number 1"
}
const change = {
    peopleChange:function(){
        console.log(academy.peopleAmount +=1)
    },
    lectorsChange:function(){
        console.log(academy.lectorsAmount +=1)
    }
    
}