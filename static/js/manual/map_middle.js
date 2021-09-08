// accomodation
let see_mode_btn=document.getElementsByClassName('see_mode_btn');
let adult_number=document.getElementById('room');

for(let see=0; see<see_mode_btn.length; see++){


  if(adult_number.innerHTML===0){
    see_mode_btn[see].setAttribute('href', '#')
    see_mode_btn[see].addEventListener('click', function(e){
      e.preventDefault()
      console.log(e.currentTarget.previousElementSibling)
      alert("You Must Choose Adult")

     })
 }

 else{
  see_mode_btn[see].addEventListener('click', function(e){

    console.log(e.currentTarget.previousElementSibling)

    see_mode_btn[see].setAttribute('href', e.currentTarget.previousElementSibling.innerHTML)
   })
  
 }

 

}

// ------------------------
let adult2=JSON.parse(localStorage.getItem('adult2'))
let children2=localStorage.getItem('children2')
let getcapacity=document.getElementsByClassName('getcapacity')
let capacity_value_id=document.getElementsByClassName('capacity_value_id')
console.log(adult2)
let changecurr=adult2;
localStorage.setItem('current_peoplee', changecurr);
let current_people_str=JSON.parse(localStorage.getItem('current_peoplee'))
console.log(current_people_str)
let current=0;

for(let capa=0; capa<getcapacity.length; capa++){
  let adultresult=[]
  console.log(getcapacity[capa])
  getcapacity[capa].addEventListener('change', function(e){
    // console.log(e.currentTarget.value)
    // console.log(e.currentTarget.previousElementSibling.innerHTML)
    if( e.currentTarget.value>=e.currentTarget.previousElementSibling.innerHTML.trim()
    &&e.currentTarget.value>adult2){
      alert()
      let k=`
      <div class="modal show fade" id="exampleModalsingleval" data-keyboard="false" data-backdrop="static" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
   <div class="modal-dialog" role="document">
     <div class="modal-content">
       <div class="modal-header">
         <h5 class="modal-title" id="exampleModalLabel">Please Choose Other City</h5>
         <button  onclick="javascript:window.location.reload()" type="button" class="close" data-dismiss="modal" aria-label="Close">
           <span aria-hidden="true">&times;</span>
         </button>
       </div>
       <div class="modal-body">
       <span> You Must Choose </span>
       <a href="http://127.0.0.1:8000/archiveaccommodation"> ${adult2} </a>
       </div>
       <div class="modal-footer">
        
       </div>
     </div>
   </div>
 </div>
     `
     
     let exampleModalsinglevalmain=document.getElementById('exampleModalsinglevalmain');
     exampleModalsinglevalmain.innerHTML=k;
     $('#exampleModalsingleval').modal('show');
      e.currentTarget.value=''
    }
    else  if(e.key === "Backspace" || e.key === "Delete"){
      adult2=parseInt(adult2)+parseInt(current)
    console.log(parseInt(current) + ' deleteee')
   
    }
    else{
      adult2=adult2-e.currentTarget.value
      current=e.currentTarget.value;
      console.log(adult2  + ' adult deleteee')
      console.log(current  + ' current -')
     
    }
   
  })

}
// $('.getcapacity').on('keyup keydown change', function(e){
//   console.log($(this).val() > adult2)
//       if ($(this).val() > $('.capacity_value_id').html
//           && e.keyCode !== 46
//           && e.keyCode !== 8
//          ) {
//          e.preventDefault();     
//          $(this).val($('.capacity_value_id').html);
//       }
//   });
// add localhost in middle mao
if(localStorage.getItem('cities_obj')!=null){
  let my_items_save=document.getElementById('my_items_sav');
  my_items_save.style.display="block";
  let buttonDelete=document.createElement('button');
  buttonDelete.setAttribute('type', 'button')
  buttonDelete.setAttribute('id', 'Delete_items');
  buttonDelete.innerHTML="X"

  let tableData = '';
  tableData += '';
  JSON.parse(localStorage.getItem('cities_obj')).map(data=>{
    tableData +=  `<div class="">
   <div class="fixed_sub"> <a href="#" class="fixed_sub "> 
   <div>
   ${data.title}
   </div> <div style="font-size:11px; padding:5px"> <span class="input_date_start_ac">${data.start_date}, </span>
   <span class="input_date_end_ac">  ${data.end_date} </span>
    </div>
    <div style="font-size:10px"> </div> </a> </div> 
   
   </div>
   `;
  });
  my_items_save.innerHTML+=tableData
  my_items_save.appendChild(buttonDelete)
 }
 let start=document.getElementsByClassName('input_date_start_ac');
 let end=document.getElementsByClassName('input_date_end_ac');
 for(let i=0; i<start.length; i++){
  let k=start[i].innerHTML.trim();
  let re=k.slice(2);

 re=re.replaceAll('-', '/')
  re=re.split('/');
  console.log(k)
  console.log(re)
  
  start[i].innerHTML=re[2]+'/'+re[1]+'/'+re[0];

}
for(let i=0; i<end.length; i++){
  let k=end[i].innerHTML.trim();
  let re=k.slice(2);

 re=re.replaceAll('-', '/')
  re=re.split('/');
  console.log(k)
  console.log(re)
  end[i].innerHTML=re[2]+'/'+re[1]+'/'+re[0];
}
 let deleteItems=document.getElementById('Delete_items');
 deleteItems.addEventListener('click', function(){
  localStorage.removeItem('cities_obj');
  window.location.reload();
 })

 if(localStorage.getItem('cities_obj')!=null){
  let filter_city_input=document.getElementById('filter_city_input');


  let tableDataaa = '';
  tableDataaa += '';
  let obj_citiess=JSON.parse(localStorage.getItem('cities_obj'))
    console.log('------------==================----------------------' )
    console.log(obj_citiess[0] )
    tableDataaa +=  `<input type="text" name="city" value="${obj_citiess[0].title}">
    <input type="text" name="st_date" value="${obj_citiess[0].start_date}">
    <input type="text" name="en_date" value="${obj_citiess[0].end_date}">
    
        <hr>`
    filter_city_input.innerHTML+=tableDataaa

  }

 if(localStorage.getItem('cities_obj')!=null){
  let my_items_save_filtwe=document.getElementById('accomodation_section_inner');
  my_items_save_filtwe.style.display="block";

  let tableDataa = '';
  tableDataa += '';
  let obj_cities=JSON.parse(localStorage.getItem('cities_obj'))
    console.log('----------------------------------' )
    console.log(obj_cities[0] )
    tableDataa +=  `<a href="">
    <h3 class="active"><span>${obj_cities[0].title}
        <i class="fas fa-angle-double-right" style="position:relative; left:4px; "></i>
    </span></h3>
    </a> <hr>`;

  my_items_save_filtwe.innerHTML+=tableDataa
  my_items_save_filtwe.appendChild(buttonDelete)
 }


//  shared romm capacity

