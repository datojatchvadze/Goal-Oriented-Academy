//1
let i = 0
while(True){
    if(i===20){
        break
    }
    else{
        console.log(i);
        i = i + 1
    }

}

//2
let number = 1
while(number <= 100){
    console.log(number);
    number = number + 1
}
//3
let age = Number(prompt('enter your age:'));
if(age < 15){
    console.log("under 15")
}
else if(age === 15){
    console.log('is 15')
}
else{
    console.log('over 15')
}