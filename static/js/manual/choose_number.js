//add to cart modal box
let acommodation_id=document.getElementById('acommodation_id');
let total_hotel_price=document.getElementById('total_hotel_price');
let total_car_price=document.getElementById('total_car_price');
total_hotel_price.style.display="none";
total_car_price.style.display="none";
if(acommodation_id.classList.contains('active')){
    total_hotel_price.style.display="inline-block";
    total_car_price.style.display="none";
    }
    else{
     total_hotel_price.style.display="none";
    total_car_price.style.display="inline-block"
    }
function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";

    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
    if(acommodation_id.classList.contains('active')){
    total_hotel_price.style.display="inline-block";
    total_car_price.style.display="none";
    }
    else{
     total_hotel_price.style.display="none";
    total_car_price.style.display="inline-block"
    }

  }
//  end====

let login_but=document.getElementById('login_button');
let regustbut=document.getElementById('sign_up_button');
let login_form=document.getElementById('login_form');
let regist_form=document.getElementById('registration_form');
let forgot = document.getElementById('forgot_password');
let password = document.getElementById('login_form');
let mypassword = document.getElementById('mypassword');
login_but.addEventListener('click', function(){
    login_form.style.display="flex";
    regist_form.style.display="none";
    mypassword.style.display = "none";
    this.classList.add('active');
    regustbut.classList.remove('active')
})
regustbut.addEventListener('click', function(){
    regist_form.style.display="flex";
    login_form.style.display="none";
    mypassword.style.display = "none";
    this.classList.add('active');
    login_but.classList.remove('active')
});


// forgot password============

forgot.addEventListener('click', function(){
    login_form.style.display = "none";
    mypassword.style.display = "block";
})

// forgot password end ============


jQuery('.dropdown-toggle').on('click', function (e) {
    $(this).next().toggle();
});
jQuery('.dropdown-menu.keep-open').on('click', function (e) {
    e.stopPropagation();
});


function increaseValue() {
    var value = parseInt(document.getElementById('number').value, 10);
    value = isNaN(value) ? 0 : value;
    var room = parseInt(document.getElementById('room').innerHTML, 10);
    room = isNaN(value) ? 0 : value;
    // Get the modal
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function () {
        modal.style.display = "none";
    }
    if (value <= 9) {

        value++;

        room++;

    } else {
        modal.style.display = "block";
        // alert("the number of Bookytriper    being more than 10, please contact our services at 0X XX XX XX XX or schedule a call with a Booky    administrator&quot");
    }
    console.log(value);
    console.log(room);
    document.getElementById('number').value = value;
    document.getElementById('room').innerHTML = room;
}

function decreaseValue() {
    var value = parseInt(document.getElementById('number').value, 10);
    value = isNaN(value) ? 2 : value;
    value <= 2 ? value = 2 : '';
    var room = parseInt(document.getElementById('room').innerHTML, 10);
    room = isNaN(value) ? 2: value;

    value--;
    room--
    document.getElementById('number').value = value;
    document.getElementById('room').innerHTML = room;

}

function increaseValuee() {
    var value = parseInt(document.getElementById('numbers').value, 10);
    value = isNaN(value) ? 0 : value;
    var room = parseInt(document.getElementById('adult').innerHTML, 10);
    room = isNaN(value) ? 0 : value;
    // Get the modal
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function () {
        modal.style.display = "none";
    }
    if (value <= 9) {
        room++;
        value++;
    } else {
        modal.style.display = "block";
        // alert("the number of Bookytriper    being more than 10, please contact our services at 0X XX XX XX XX or schedule a call with a Booky    administrator&quot");
    }
    document.getElementById('numbers').value = value;
    document.getElementById('adult').innerHTML = room;
}

function decreaseValuee() {
    var value = parseInt(document.getElementById('numbers').value, 10);
    value = isNaN(value) ? 0 : value;
    value < 1 ? value = 1 : '';
    var room = parseInt(document.getElementById('room').innerHTML, 10);
    room = isNaN(value) ? 0 : value;
    value--;
    room--
    document.getElementById('numbers').value = value;
    document.getElementById('adult').innerHTML = room;
}

function increaseValueee() {
    var value = parseInt(document.getElementById('numberss').value, 10);
    value = isNaN(value) ? 0 : value;
    var room = parseInt(document.getElementById('rooms').innerHTML, 10);
    room = isNaN(value) ? 0 : value;
    // Get the modal
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function () {
        modal.style.display = "none";
    }
    if (value <= 9) {
        room++;
        value++;
    } else {
        modal.style.display = "block";
        // alert("the number of Bookytriper    being more than 10, please contact our services at 0X XX XX XX XX or schedule a call with a Booky    administrator&quot");
    }
    document.getElementById('numberss').value = value;
    document.getElementById('rooms').innerHTML = room;
}

function decreaseValueee() {
    var value = parseInt(document.getElementById('numberss').value, 10);
    value = isNaN(value) ? 2 : value;
    value <= 2 ? value = 2 : '';
    var room = parseInt(document.getElementById('rooms').innerHTML, 10);
    room = isNaN(value) ? 2: value;

    value--;
    room--
    document.getElementById('numberss').value = value;
    document.getElementById('rooms').innerHTML = room;
}


function increaseValuea() {
    var value = parseInt(document.getElementById('numberss').value, 10);
    value = isNaN(value) ? 0 : value;
    var room = parseInt(document.getElementById('rooms').innerHTML, 10);
    room = isNaN(value) ? 0 : value;
    // Get the modal
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function () {
        modal.style.display = "none";
    }
    if (value <= 9) {
        room++;
        value++;
    } else {
        modal.style.display = "block";
        // alert("the number of Bookytriper    being more than 10, please contact our services at 0X XX XX XX XX or schedule a call with a Booky    administrator&quot");
    }
    document.getElementById('numberss').value = value;
    document.getElementById('rooms').innerHTML = room;
}

function decreaseValuea() {
    var value = parseInt(document.getElementById('numbered').value, 10);
    value = isNaN(value) ? 0 : value;
    value < 1 ? value = 1 : '';
    var room = parseInt(document.getElementById('rooms').innerHTML, 10);
    room = isNaN(value) ? 0 : value;
    value--;
    room--
    document.getElementById('numberss').value = value;
    document.getElementById('rooms').innerHTML = room;
}




function  increaseValue1() {
    var value = parseInt(document.getElementById('number1').value, 10);
    value = isNaN(value) ? 0 : value;
    var room = parseInt(document.getElementById('room22').innerHTML, 10);
    room = isNaN(value) ? 0 : value;
    // Get the modal
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function () {
        modal.style.display = "none";
    }
    if (value <= 9) {
        room++;
        value++;
    } else {
        modal.style.display = "block";
        // alert("the number of Bookytriper    being more than 10, please contact our services at 0X XX XX XX XX or schedule a call with a Booky    administrator&quot");
    }
    document.getElementById('number1').value = value;
    document.getElementById('room22').innerHTML = room;
}

function decreaseValue1() {
    var value = parseInt(document.getElementById('number1').value, 10);
    value = isNaN(value) ? 2 : value;
    value < 2 ? value = 2 : '';
    var room = parseInt(document.getElementById('room22').innerHTML, 10);
    room = isNaN(value) ? 2 : value;
    value--;
    room--
    document.getElementById('number1').value = value;
    document.getElementById('room22').innerHTML = room;
}


function  increaseValuee2() {
    var value = parseInt(document.getElementById('numbers2').value, 10);
    value = isNaN(value) ? 0 : value;
    var room = parseInt(document.getElementById('room22').innerHTML, 10);
    room = isNaN(value) ? 0 : value;
    // Get the modal
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function () {
        modal.style.display = "none";
    }
    if (value <= 9) {
        room++;
        value++;
    } else {
        modal.style.display = "block";
        // alert("the number of Bookytriper    being more than 10, please contact our services at 0X XX XX XX XX or schedule a call with a Booky    administrator&quot");
    }
    document.getElementById('numbers2').value = value;
    document.getElementById('adult22').innerHTML = room;
}

function decreaseValuee2() {
    var value = parseInt(document.getElementById('numbers2').value, 10);
    value = isNaN(value) ? 0 : value;
    value < 1 ? value = 1 : '';
    var room = parseInt(document.getElementById('room22').innerHTML, 10);
    room = isNaN(value) ? 0 : value;
    value--;
    room--
    document.getElementById('numbers2').value = value;
    document.getElementById('adult22').innerHTML = room;
}

function  increaseValueee3() {
    var value = parseInt(document.getElementById('numberss3').value, 10);
    value = isNaN(value) ? 0 : value;
    var room = parseInt(document.getElementById('rooms22').innerHTML, 10);
    room = isNaN(value) ? 0 : value;
    // Get the modal
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function () {
        modal.style.display = "none";
    }
    if (value <= 9) {
        room++;
        value++;
    } else {
        modal.style.display = "block";
        // alert("the number of Bookytriper    being more than 10, please contact our services at 0X XX XX XX XX or schedule a call with a Booky    administrator&quot");
    }
    document.getElementById('numberss3').value = value;
    document.getElementById('rooms22').innerHTML = room;
}

function decreaseValueee3() {
    var value = parseInt(document.getElementById('numberss3').value, 10);
    value = isNaN(value) ? 2 : value;
    value < 2 ? value = 2 : '';
    var room = parseInt(document.getElementById('rooms22').innerHTML, 10);
    room = isNaN(value) ? 2 : value;
    value--;
    room--
    document.getElementById('numberss3').value = value;
    document.getElementById('rooms22').innerHTML = room;
}
// //////////////////////////////////////////////////////////////////////


// typewritter

    var app = document.getElementById('app');

var typewriter = new Typewriter(app, {
    loop: false
});

typewriter.typeString('Its Your Trip So Make It')
        .start();


// // choose Traveler in other page
    function optionCheck(){
    var option=document.getElementById('Travelers').value;
    console.log(option);
    if(option=="10+"){
    
    
    }
    }



    // accordion

    var accordion = document.getElementsByClassName("accordion");

for (let i = 0; i < accordion.length; i++) {
	accordion[i].addEventListener("click", function(){
		this.classList.toggle("active");
		var details = this.nextElementSibling;
		if (details.style.maxHeight) {
			details.style.maxHeight = null;
		} else {
			details.style.maxHeight = details.scrollHeight + "px";
		}
	});
}

function getData()
{
    //gettting the values
    var Destination = document.getElementById("Destination").value;
    var departure= document.getElementById("departure").value; 
    var depart_date= document.getElementById("depart_date").value; 
    var duration= document.getElementById("duration").value; 
    var adult1= document.getElementById("number").value; 
    var children1= document.getElementById("numbers").value; 
    var room1= document.getElementById("numberss").value; 
    //saving the values in local storage
    localStorage.setItem("txtValue", Destination);
    localStorage.setItem("txtValue1", departure);
    localStorage.setItem("txtValue2", depart_date);
    localStorage.setItem("txtValue3", duration);   
    localStorage.setItem("adult1", adult1);   
    localStorage.setItem("children1", children1);   
    localStorage.setItem("room1", room1);   
}




// personal tour


function getDataa()
{
   
    //gettting the values
    var Destinations = document.getElementById("Destinations").value;
    var start_date= document.getElementById("textfield7").value; 
   
    var adult2= document.getElementById("number1").value; 
    var children2= document.getElementById("numbers2").value; 
    var room2= document.getElementById("numberss3").value; 
    //saving the values in local storage
    localStorage.setItem("txtValue10", Destinations);
    localStorage.setItem("txtValue20", start_date);
   
    localStorage.setItem("adult2", adult2);   
    localStorage.setItem("children2", children2);   
    localStorage.setItem("room2", room2);   
}
