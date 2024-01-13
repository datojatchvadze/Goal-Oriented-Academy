let bought = document.getElementsByClassName('bought');
let currentlyspent = document.getElementById('spent');
for (let i = 0; i < bought.length; i++) { //function for addition of total spent money
    bought[i].addEventListener('click', function () {
        let spent = Number(currentlyspent.textContent);
        currentlyspent.textContent = (spent + 100);
    });
}


let reset = document.getElementById('reset'); 
reset.addEventListener('click',function(){ //function for reseting spent money
    spent.textContent = 0;
})



let balance = document.getElementById('balance');
let num = document.getElementById('num');
let finish = document.getElementById('finish');
finish.addEventListener('click',function(){ //function for confirming purchase
    let spent = Number(currentlyspent.textContent);
    let currentBalance = Number(balance.textContent);
    if(spent>currentBalance){
        alert('not enough money in balance');
    }
    else{
        let updatedBalance = (currentBalance-spent);
        balance.textContent = updatedBalance;
        alert('payment succesful');
        
    }
})



let withdraw =document.getElementById('submitbtn');
withdraw.addEventListener('click',function(){ //function for witdrawing money from card
    let value = num.value; 
    let currentBalance = Number(balance.textContent); 
    let updatedBalance = currentBalance + Number(value); 
    balance.textContent = updatedBalance;
})