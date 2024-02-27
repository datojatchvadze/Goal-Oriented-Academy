//1
for(let i=0; i<=100; i++){
    console.log(i);
}

//2
for(let i=100; i>0; i--){
    console.log(i);
}

//3
for(let i=0; i<=20; i++){
    if(i % 2 == 0){
        console.log(i+"is even number")
    }
    else{
        console.log(i+'is odd number')
    }
}


//4
let myFriend = prompt('whats your name?');

if(myFriend === 'dato' || myFriend === 'nika'){
    console.log('hello friend')
}
else{
    console.log('you are not my friend')
}


//5
i = 0;
while(i <= 100){
    console.log(i);
    i+=5;
}
