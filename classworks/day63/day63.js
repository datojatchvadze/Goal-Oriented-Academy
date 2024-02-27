const rocket = {
    weight: 2000,
    height: 100,
    width: 30,
    builtDate: 13,
    engine: {
        model: 16,
        power: 500,
        weight: 500
    },
    launch: function(){
        console.log('rocket is launching in 10seconds!')
    }

}
let firstName = 'giorgi';
let secondName = firstName;



function Flight(code,status) {
    this.code = code;
    this.status = status;
  }

let code1 = 32443;
let status1 = 'delayed';
let flight1 = new Flight(code1,status1);
console.log(flight1)