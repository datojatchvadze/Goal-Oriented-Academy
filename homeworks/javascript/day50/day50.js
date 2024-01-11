// creating variables to get values from html file to js file
let withdraw =document.getElementById('withdraw');
let deposit =document.getElementById('deposit');
let num = document.getElementById('num');
let balance = document.getElementById('balance');
withdraw.addEventListener('click',function(){
    let value = num.value; //variable to get x amount of money from input
    let currentBalance = Number(balance.textContent); // variable to check current balance in numbers
    let updatedBalance = currentBalance + Number(value); // addition of current balance and added amount
    balance.textContent = updatedBalance;
})
deposit.addEventListener('click',function(){
    let value = num.value; //variable to get x amount of money from input
    let currentBalance = Number(balance.textContent); // variable to check current balance in numbers
    let updatedBalance = currentBalance - Number(value); //substraction of current balance and deposit money
    if(currentBalance > value) {
        balance.textContent = updatedBalance;
    }
    else{
        alert('not enough money in balance');
    }
})