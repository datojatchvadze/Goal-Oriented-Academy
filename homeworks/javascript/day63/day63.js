//1
function Student(name, surname, score) {
    this.name = name;
    this.surname = surname;
    this.score = score;
  }
let student1 = new Student('david','jatchvadze',10);
console.log(student1);

//2
function Engine(model, weight, releaseDate) {  //2.1
    this.model = model;
    this.weight = weight;
    this.releaseDate = releaseDate;
  }

function phone(memory,model) {  //2.2
    this.memory = memory;
    this.model = model;
  }

function Car(weight,model,produceDate) {  //2.3
    this.weight = weight;
    this.model = model;
    this.produceDate = produceDate;
  }

function Id(name,email,password) {  //2.4
    this.name = name;
    this.email = email;
    this.password = password;
  }
  
function Game(score,level,timeSpent) {  //2.5
    this.score = score;
    this.level = level;
    this.timeSpent = timeSpent;
  }