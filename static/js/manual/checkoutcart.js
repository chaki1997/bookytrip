   //adding cartbox data in table
   const cardBoxTablee = document.querySelector('.cart_tablee');
   let tableDataa = '';
   tableDataa += '';
   if(JSON.parse(localStorage.getItem('items'))[0] === null){
    tableData += '<tr><td colspan="5">No items found</td></tr>'
   }else{
    JSON.parse(localStorage.getItem('items')).map(data=>{
      var pricee=parseInt(data.price);
     //  var noo=parseInt(data.no);
     //  var result=pricee;
     // console.log(result);
     // console.log(pricee);
   tableDataa +=  `<span class="room_number"> ${data.price}</span>
         <span class="hotel">${data.title}</span>`;
    });
   }
   
   cardBoxTablee.innerHTML = tableDataa;
      
  

   let checkout=document.getElementsByClassName('deleteLocalsotrage');
   let number_room=document.getElementsByClassName('number_room');
   let hotel=document.getElementsByClassName('title_room');
   let serverid=document.getElementsByClassName('serverid');

   for(var i=0; i<checkout.length; i++){
     checkout[i].addEventListener('click', function(e){
    
       let items = [];
       JSON.parse(localStorage.getItem('items')).map(data=>{
        //  console.log(data.title )
      
       console.log(e.target.parentElement.parentElement.children[2].children[0].value)
      //  console.log(console.log(data.room))
    
         if(data.serverid.trim() == e.target.parentElement.parentElement.children[2].children[0].value
          
         ){
           
          //  alert()
          
           items.push(data);
           window.location.reload();
          
         }
         else if (data.serverid.trim() != [] && data.title.trim() != []){
           localStorage.clear();
           
         }
        
       })
       localStorage.setItem('items',JSON.stringify(items));
      //  e.preventDefault();
      window.location.reload();
      
     })
   }
  //  console.log(checkout)


// people in checkout personal
   let People_inner=document.getElementById('People_inner');

   let localPersonaladult=parseInt(localStorage.getItem('adult2'))
   let localchildren=parseInt(localStorage.getItem('children2'))
   People_inner.innerHTML=localPersonaladult+localchildren+ `
   <input type="hidden" name="number_treveler"
   class="hotel" value="${localPersonaladult+localchildren}"> `;


  //  dates in checkout for cities_obj
  let city_in_personal= document.getElementsByClassName('city_in_personal');
let arr_h4=[];

 
   let city_inner;
    for(let i=0; i<city_in_personal.length; i++){

      arr_h4.push(city_in_personal[i].innerHTML)
   
    }
   
   

let data_startend=document.querySelector('.data_startend')
let siblingTitle=document.getElementsByClassName('siblingTitle')


for(let siblingTitlei=0; siblingTitlei<siblingTitle.length; siblingTitlei++){

// console.log(siblingTitle[siblingTitlei].innerHTML)

    JSON.parse(localStorage.getItem('cities_objj')).map(data=>{
      
   
   arr_h4.forEach(element =>{
    if(data.title==element ){
   
      if(siblingTitle[siblingTitlei].innerHTML==data.title){
        // console.log( siblingTitle[siblingTitlei].nextElementSibling)
        siblingTitle[siblingTitlei].nextElementSibling.innerHTML= `
        
        <div class="date_end" style="width:50%">
        <h4>End Date  </h4>
       <span class="siblingTitle" style="display: none;">{{ hotel.hotel_name.city.city }}</span>
      ${data.start_date}
      <input type="hidden" name="start_date" value=" ${data.start_date}" >
      </div>
        <div class="date_end">
        <h4>End Date  </h4>
       <span class="siblingTitle" style="display: none;">{{ hotel.hotel_name.city.city }}</span>
      ${data.end_date}
      <input type="hidden" name="start_date" value=" ${data.end_date}" >
      </div>
        ` 
      }
     }
   
   })

    });
  }


  // checkout total price


  let checkout_price=document.getElementsByClassName('checkout_price');
  let reservation_pricee=document.getElementById('reservation_pricee');
  let price_hidden=document.getElementById('price_hidden');
  let sumtotal=0;
  let peop_sum= People_inner.innerHTML.trim();
  console.log(peop_sum)
for(let price=0; price<checkout_price.length; price++){
  // console.log(parseInt(checkout_price[price].innerHTML))
 
  sumtotal=sumtotal+(parseInt(checkout_price[price].innerHTML)  * parseInt(peop_sum))
 console.log( sumtotal)
  reservation_pricee.innerHTML=sumtotal + ' $'
  price_hidden.value=sumtotal
}