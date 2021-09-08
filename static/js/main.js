const alertBox = document.getElementById('ajax_alert');

const form = document.getElementById('login_form_ajax');
const email = document.getElementById('email');
const pswrd = document.getElementById('password');

const csrf = document.getElementsByName('csrfmiddlewaretoken');
const srff_login = document.querySelector('#srff_login input');
const booking_bottom = document.getElementById('booking_bottom');
const packid = document.getElementById('packid');

const url = "http://127.0.0.1:8000/login";
var a = "{% url 'themedTour:packorder' pack.id %}";
console.log(a)
const handleAlerts = (type, text) => {
    alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">${text}</div>`
};

form.addEventListener('submit', (e)=>{
    e.preventDefault();

    const fd = new FormData();
    fd.append('csrfmiddlewaretoken',srff_login.value);
    fd.append('email', email.value);
    fd.append('password', pswrd.value);
    $.ajax({
        type: 'POST',
        url: url,
        data: fd,
        success: function(response){
            console.log(response);
           
            if(response.user=="supplier"){
                window.location.href = "http://127.0.0.1:8000/supplieritems";
            }
            else if(response.user=="admin"){
                window.location.href = "http://127.0.0.1:8000/dashboard";
            }
            
            else{
                location.reload();
            }
            if(booking_bottom.innerHTML!=''){
                
             

                location.href = packid
            }
        },
        
        error: function(error){
            console.log(error)
            handleAlerts('danger', "email or password is incorrect");
        },
        cache: false,
        contentType: false,
        processData: false,

    });


});
// registration
const alertBoxSign = document.getElementById('ajax_alert_sign');

const form_sign_up = document.getElementById('registar_form');
const nameId = document.getElementById('id_name');
const id_surname = document.getElementById('id_surname');
const id_email = document.getElementById('id_email');

const phone = document.getElementById('phone');
const id_picture = document.getElementById('id_picture');
const id_password1 = document.getElementById('id_password1');
const id_password2 = document.getElementById('id_password2');
const date_inputtt = document.getElementById('date_inputtt');
const srff = document.querySelector('#srff input');
console.log(srff)


const urlsign = "http://127.0.0.1:8000/signup";

const handleAlertss = (type, text, pass) => {
    alertBoxSign.innerHTML = `<div class="alert alert-${type}" role="alert">${text} ${pass}</div>`
};

form_sign_up.addEventListener('submit', (event)=>{
    event.preventDefault();
    const message_pri = $(".type_input[name='user_type']:checked").val();
    console.log(message_pri)
  
    const sign = new FormData();
    sign.append('csrfmiddlewaretoken',srff.value);
    sign.append('name', nameId.value);
    sign.append('surname', id_surname.value);
    sign.append('email', id_email.value);
    sign.append('date', date_inputtt.value);
    sign.append('phone', phone.value);
    sign.append('picture', id_picture.files[0]);
    sign.append('password1', id_password1.value);
    sign.append('password2', id_password2.value);
    sign.append('user_type', message_pri);
    $.ajax({
        type: 'POST',
        url: urlsign,
        enctype: 'multipart/form-data',
        data: sign,

        success: function(response){      
            if(message_pri=="supplier"){
                alertBoxSign.innerHTML= alertBoxSign.innerHTML=`<div class="alert alert-primary" role="alert">Your request has been send in to admin </div>`
                setInterval(myTimer, 4000);
                function myTimer() {
                    
                   
                    location.reload();
                  }
              
            }
            else{
                location.reload();
                console.log(response)
            }
           
        },
        
        error: function(error){
            // alert()
            console.log(JSON.parse(error.responseText))
           
            let err=JSON.parse(error.responseText)

            if(id_password1.value!=id_password2.value){
               alertBoxSign.innerHTML=`<div class="alert alert-danger" id="passval" role="alert">${err.error.password2[0]}</div>`
            }
            if(id_password1.value!=id_password2.value && err.error.email[0]){
               alertBoxSign.innerHTML+=`<div class="alert alert-danger" id="passval" role="alert">${err.error.password2[0]}</div>`
               alertBoxSign.innerHTML+=`<div class="alert alert-danger" role="alert">${err.error.email[0]}</div> `
            }
             if(err.error.email[0]){
                alertBoxSign.innerHTML = `<div class="alert alert-danger" role="alert">${err.error.email[0]}</div> `
                
            }
           
            
        },
        cache: false,
        contentType: false,
        processData: false,

    });


});