let checkBox =document.getElementById('accept');
let pElement =document.getElementById('result');
let btn =document.getElementById('btn');

btn.addEventListener ("click",function(){
    let value = checkBox.checked;
    console.log(value);
    if (value === true) {
        alert('payment succesful');
    }
    else{
        alert('payment failed');
    }


})