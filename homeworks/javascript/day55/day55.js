let sumResult = document.getElementById('sum');
let multiplyResult = document.getElementById('multiply');


let firstNumber = Number(prompt('insert first number:'));
let secondNumber = Number(prompt('insert second number'));


let sum = firstNumber + secondNumber;
let multiply = firstNumber * secondNumber;


sumResult.textContent = sum;
multiplyResult.textContent = multiply;

console.log((sum > multiply) || (sum === multiply));
console.log((sum < multiply) && (firstNumber > secondNumber));


