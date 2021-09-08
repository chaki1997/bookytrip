let kas=document.querySelector('.cities_chousen');
let gocheck=document.getElementById('save_localstorage');
let localdiv=document.getElementById('my_items_save');
let localdivv=document.getElementById('result_city');
let mycities=document.querySelector('.myCities');
console.log(gocheck)
console.log(typeof(localdiv.innerHTML))
if(mycities==null){
  gocheck.setAttribute('disabled', '')
}


function Delet(e){
  let items = [];
  JSON.parse(localStorage.getItem('cities_obj')).map(data=>{
      if(data.id != e.parentElement.parentElement.parentElement.children[1].textContent){
          console.log(e.parentElement.parentElement.parentElement.children[1].textContent)
          items.push(data);
          window.location.reload();
          localdiv.style.display="none";
          localStorage.removeItem('cities_obj');
      }

       if (localStorage.getItem('cities_obj',JSON.stringify(items))==[]){
        localStorage.clear();
        
        window.location.reload();
        localStorage.removeItem('cities_obj');
        
      }
    
  });
 
  console.log(items)

  localStorage.setItem('cities_obj',JSON.stringify(items));
  
  window.location.reload();
  localStorage.removeItem('cities_obj');


};
if(localStorage.getItem("cities_obj") === '[]' ){
  localStorage.removeItem('cities_obj');
  }


var diffDays;


let result_city=document.getElementById('result_city');
let k=document.getElementById('title_map');
// let button_add=document.getElementById('add_city');
console.log(k)
let counter=1;
let arrcities=[];
function add_city(e){

    let title_map=document.getElementById('title_map');
    $('.modal').modal('hide');
    let cities_chousen=document.createElement('div');
    cities_chousen.setAttribute('class', 'cities_chousen');
    let title_form=document.createElement('div');
    title_form.setAttribute('class', 'title_form');
    title_form.innerHTML=title_map.innerHTML;

    let input_citiess=document.createElement('div');
    input_citiess.setAttribute('class', 'input_cities');
    let start_date_input_class=document.createElement('div');
    start_date_input_class.setAttribute('class', 'start_date_input');

    let start_date_input_class_label=document.createElement('label');
    start_date_input_class_label.setAttribute('for', 'textfield9');
    start_date_input_class_label.innerHTML='Start Date';
    start_date_input_class.appendChild(start_date_input_class_label); // append start date label
    let start_date_input_form=document.createElement('input');
    start_date_input_form.setAttribute('type', 'date');
    start_date_input_form.setAttribute('id', 'textfield9');
    start_date_input_form.setAttribute('class', 'textfield9 start_date_input_form date_input');
    start_date_input_form.setAttribute('autocomplete', 'off');
    start_date_input_form.setAttribute('required', '');
    start_date_input_form.setAttribute('onkeydown', 'return false');
    start_date_input_class.appendChild(start_date_input_form); // append start date input
// console.log(start_date_input_form)

    let end_date_input_class=document.createElement('div'); //start div end date
    end_date_input_class.setAttribute('class', 'end_date_input');
    let end_date_input_class_label=document.createElement('label');
    end_date_input_class_label.setAttribute('for', 'textfield10');
    end_date_input_class_label.innerHTML='End Date'
    end_date_input_class.appendChild(end_date_input_class_label); // append start date input
    let end_date_input_form=document.createElement('input');
    end_date_input_form.setAttribute('type', 'date');
    end_date_input_form.setAttribute('id', 'textfield10');
    end_date_input_form.setAttribute('class', 'textfield10  end_date_input_form  date_input');
    end_date_input_form.setAttribute('autocomplete', 'off');
    end_date_input_form.setAttribute('required', '');
    end_date_input_form.setAttribute('onkeydown', 'return false');
    // end_date_input_form.setAttribute('min', start_date_input_form.value );
    // console.log(end_date_input_form)
    end_date_input_class.appendChild(end_date_input_form); // append start date input
    input_citiess.appendChild(start_date_input_class)
    input_citiess.appendChild(end_date_input_class)
    cities_chousen.appendChild(title_form)
    cities_chousen.appendChild(input_citiess)



    result_city.appendChild(cities_chousen);

    // object


    let start_local=document.getElementById('textfield9');
    start_local.setAttribute('value', localStorage.getItem('txtValue20'))
    start_local.setAttribute('min', localStorage.getItem('txtValue20'))
    let end_local=document.getElementById('textfield10');
    end_local.setAttribute('min', start_local.value)
    let startsta= document.getElementsByClassName('textfield9');
    let endsta= document.getElementsByClassName('textfield10');
    var date_input = document.getElementsByClassName('date_input');
    console.log(result_city)
    for(let i=0; i<endsta.length; i++){
      // date_input[i].valueAsDate = new Date();
      // console.log( endsta[i]);
      endsta[i].onchange = function(){
      //  console.log(this.parentElement.previousElementSibling.children[1].value);
       if(this.value<=this.parentElement.previousElementSibling.children[1].value || this.value<=this.parentElement.parentElement.parentElement.previousElementSibling.children[1].
        children[1].children[1].value  ){
         alert('You Cant Make this')
         this.value='';
       }
       else{

       }
    }
    }
    for(let j=0; j<startsta.length; j++){
      // date_input[i].valueAsDate = new Date();

      startsta[j].onchange = function(){
       console.log(this.parentElement.parentElement.parentElement.previousElementSibling.children[1].
        children[0].children[1].value);
       if( this.value<=this.parentElement.parentElement.parentElement.previousElementSibling.children[1].
        children[0].children[1].value || this.value<=this.parentElement.parentElement.parentElement.previousElementSibling.children[1].
        children[1].children[1].value   ){
         alert('You Cant Make this')
         this.value='';
       }
       else{

       }
    }
    }

    let objcities={
      start_date:start_date_input_form.value,
      end_date:end_date_input_form.value,
      title:title_map.innerHTML
    }
    arrcities.push(objcities)
    // console.log(arrcities)
    // date_input.onchange = function(){
    //    console.log(this.value);
    // }
    // var d1 = new Date(start_local);
    // var d2 = new Date(endsta);
    // console.log(d1)
    // console.log(d2)
    // for(let end=0; end<endsta.length; end++){
    //   endsta[end].onchange=function(){


    //     console.log(this.parentElement.parentElement.parentElement.nextElementSibling.children[2].children[1].children[1].value)


    //     this.parentElement.parentElement.parentElement.nextElementSibling.children[2].children[0].children[1].setAttribute('min',  this.value);


    //   }
    // }



//   $('#textfield9').on('change', function()
// {
//     var checkInDate = $(this).val();
//     console.log(checkInDate)
//     var split = checkInDate.split('-');

//     console.log(checkInDate)
//     var tomorrow = new Date(split[0], split[1]-1, parseInt(split[2])+2, 0,0,0,0);

//     console.log(tomorrow)
//     $('#textfield10')[0].valueAsDate = tomorrow;

//     $('#textfield10')[0].attr('min', tomorrow);

// });

    $(function(){

      var dtToday = new Date();

      var month = dtToday.getMonth() + 1;

      var day = dtToday.getDate();
      var year = dtToday.getFullYear();
      if(month < 10)
          month = '0' + month.toString();
      if(day < 10)
          day = '0' + day.toString();

      var maxDate = year + '-' + month + '-' + day;

      // or instead:
      // var maxDate = dtToday.toISOString().substr(0, 10);


      $('.date_input').attr('min', maxDate);
    });
    gocheck.removeAttribute('disabled', '')
    // let sta= document.getElementsByClassName('textfield9');
    // for(let start=0; start<=sta.length; start++){
    //   sta[start].onchange=function(){

    //     console.log(this.parentElement)
    //     this.parentElement.parentElement.children[1].children[1].setAttribute('min',  this.value);
    //     this.parentElement.parentElement.parentElement.nextElementSibling.children[2].children[0].children[1].setAttribute('min',  this.value);
    //   }
    // }
    let closebtn=document.getElementById('Close');
    if(localdivv.innerHTML!=''){
      closebtn.style.display="block";
      closebtn.style.textAlign="right";

      closebtn.style.color="#562443";
      closebtn.style.fontSize="21px";
    }
    if(e.previousElementSibling.innerHTML==cities_chousen.previousElementSibling.children[0].innerHTML){
      cities_chousen.remove();
      $('#myModalcountry.modal').modal('show');

      let closebtn=document.getElementById('close_modal_map');
      closebtn.addEventListener('click', function(){
        $('#myModalcountry.modal').modal('hide');
      })
    }

}

function delete_items(e){
  console.log(e.parentNode.parentNode)
  e.parentNode.parentNode.remove(e.parentNode);
  if(localdivv.innerHTML==''  ){

    gocheck.setAttribute('disabled', '')
   }
  // gocheck.setAttribute('disabled', '')
}
    let localcheckout=document.getElementById('save_localstorage');
    let citiarr=[];
localcheckout.addEventListener('click', function(e){

//   localStorage.setItem("cities_obj",JSON.stringify(citiarr));
let cities_chousen=document.getElementsByClassName('cities_chousen');
let title=document.getElementsByClassName('title_form');
let end_date_input_value=document.getElementsByClassName('end_date_input_form');
let start_date_input_value=document.getElementsByClassName('start_date_input_form');



  for(var titleI=0; titleI<cities_chousen.length; titleI++ ){
    // console.log(title[titleI].innerHTML);
    document.getElementsByClassName('onetwo').innerHTML=titleI
    var titleresult=title[titleI].innerHTML;
    console.log(titleresult)

  var enddate=end_date_input_value[titleI];
  var startdate=start_date_input_value[titleI];
 console.log(enddate)


//   let cities_obj=localStorage.getItem("cities_obj");
//   let cities_objj=localStorage.getItem("cities_objj");
//  if(cities_obj){
//   citiarr= JSON.parse(cities_obj);
//  }
//  if(cities_objj){
//   citiarrr= JSON.parse(cities_objj);
//  }


  let qala_obj={
id: titleI+1,
title: titleresult.trim(),
start_date: startdate.value,
end_date: enddate.value,
}

console.log("-------------------------------------")
citiarr.push(qala_obj);
console.log(citiarr)



  }
  var postData = JSON.stringify({ cities: citiarr });
const url = "http://127.0.0.1:8000/accomodationmiddle";
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
console.log(csrftoken)
    console.log(postData);
    $.ajax({

      type: "GET",
      url: url,
      headers: {'X-CSRFToken': csrftoken},
      data: postData,
      async:false,
      contentType: "application/json; charset=utf-8",
      dataType: "json",

  });
}, {once : true})

// add localhost in middle mao
if(localStorage.getItem('cities_obj')!=null){
  let my_items_save=document.getElementById('my_items_save');
  my_items_save.style.display="block";

  let tableData = '';
  tableData += '';
  JSON.parse(localStorage.getItem('cities_obj')).map((data, index)=>{
    tableData +=  `<div class="myCities">  <div class="num_city"> ${index+1} </div> <div style="display:none"> ${data.id} </div>
   <div class="myciti_inner"> ${data.title} <input type="hidden" name="title" value="${data.title}"> </div> 
   <div class="my_inputs"> 
   <p> <span style="font-weight:bold"> Start Date: </span> <span class="input_date_start_ac"> ${data.start_date} </span> <input type="hidden" name="start_date" value="${data.start_date}">  </span>
   </p>
    <p style="margin:10px 0;"><span style="font-weight:bold"> End Date </span> <span class="input_date_start_ac"> ${data.end_date} </span> <input type="hidden" name="end" class="end_date_local" value="${data.end_date}">  </p> <p>   
       </div> <hr>`;
  });
  my_items_save.innerHTML+=tableData + `<a href="#" class="delete_map_item" onclick=Delet();>X</a>`
  my_items_save.appendChild(buttonDelete)
 }
 let deleteItems=document.getElementById('Delete_items');
 deleteItems.addEventListener('click', function(){
  localStorage.removeItem('cities_obj');
  window.location.reload();
 })



 function Delet(e){

      
       if (localStorage.getItem('cities_obj',JSON.stringify(items))==[]){
        localStorage.clear();
        window.location.reload();
      }

  console.log(items)
  localStorage.setItem('cities_obj',JSON.stringify(items));
  window.location.reload();

  
};

 