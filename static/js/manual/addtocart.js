//function Delete(e){
//  let items = [];
//  JSON.parse(localStorage.getItem('items')).map(data=>{
//      if(data.id != e.parentElement.parentElement.children[0].textContent){
//          console.log(e.parentElement.parentElement.children[0].textContent)
//          items.push(data);
//
//      }
//      else if (data.no != []){
//        localStorage.removeItem('items');
//      }
//  });
//  localStorage.setItem('items',JSON.stringify(items));
//
//  window.location.reload();
//};
//
//
//const attToCartBtn = document.getElementsByClassName('addTocart');
//var title=document.getElementsByClassName('titles');
//var price=document.getElementsByClassName('price');
//var destination=document.getElementsByClassName('destination');
//let city_currentl=document.getElementById('city_currentl');
//
//// console.log(title)
//// console.log(attToCartBtn)
//// console.log(attToCartBtn)
//let items = [];
//let single_cities=JSON.parse(localStorage.getItem('cities_obj'))
//for(let i=0; i<attToCartBtn.length; i++){
//  let updateitems=[];
// attToCartBtn[i].addEventListener("click",function(e){
//
//// console.log(city_currentl)
//
//
//console.log(single_cities)
//if(single_cities=='[]'){
//  alert('You cant any Cities')
//}
//
//
//// console.log(updateitems)
////   window.onload = function()
////   {document.getElementById('').style.display="block";
//// };
//
//
//   if(typeof(Storage) !== 'undefined'){
//
//    // for(var titleI=0; titleI<title.length; titleI++ ){
//    //   // console.log(title[titleI].innerHTML);
//    //   var titleresult=title[titleI].innerHTML;
//    //   // console.log(titleresult)
//    // }
//    // for(var priceI=0; priceI<price.length; priceI++ ){
//    //     var priceresult=price[priceI];
//    //     // console.log(priceresult)
//    // }
//    // for(var destinationI=0; destinationI<destination.length; destinationI++ ){
//    //     var destinationresult=destination[destinationI].innerHTML;
//    //     // console.log(destinationresult)
//    // }
//
//    // console.log(e.target.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.children[0]);
//    // console.log(e.target.parentElement.parentElement.children[3]);
//     let item = {
//         id:i+1,
//         serverid:e.target.parentElement.parentElement.parentElement.children[0].textContent,
//         image:e.target.parentElement.parentElement.parentElement.parentElement.parentElement.children[1].children[0].children[0].children[0].children[0].src,
//         title:e.target.parentElement.parentElement.parentElement.children[1].textContent,
//         room: e.target.parentElement.parentElement.parentElement.children[2].textContent,
//         price:e.target.parentElement.parentElement.children[0].children[2].textContent,
//         room_numb:e.target.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.children[0].textContent,
//        capacity:e.target.parentElement.parentElement.children[3].value,
//         no:1,
//
//       };
//      //  let pop={
//      //   pop:hiddenDiv,
//      //  }
//      let current_people_str=JSON.parse(localStorage.getItem('adult2'))
//      console.log(current_people_str)
//  if(e.target.parentElement.parentElement.children[3].value<=current_people_str){
//    let updatecurrent=0;
//    current_people_str-=e.target.parentElement.parentElement.children[3].value;
//
//    localStorage.setItem('adult2', JSON.stringify(current_people_str));
//  }
//  if(single_cities[0].title==city_currentl.innerHTML.trim() && current_people_str===0){
//    single_cities.splice(0, 1);
//  //   let k=JSON.parse(localStorage.getItem('adult2'))
//  // k=0;
//  // localStorage.setItem('adult2',JSON.stringify(k))
//    localStorage.setItem('cities_obj',JSON.stringify(single_cities));
//  }
//
//      let exampleModalsingle=document.getElementById('some')
//      JSON.parse(localStorage.getItem('cities_obj')).map(data=>{
//        console.log(data[0])
//      let k=`
//       <div class="modal show fade" id="exampleModalsingle" data-keyboard="false" data-backdrop="static" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
//    <div class="modal-dialog" role="document">
//      <div class="modal-content">
//        <div class="modal-header">
//          <h5 class="modal-title" id="exampleModalLabel">Please Choose Other City</h5>
//          <button  onclick="javascript:window.location.reload()" type="button" class="close" data-dismiss="modal" aria-label="Close">
//            <span aria-hidden="true">&times;</span>
//
//          </button>
//        </div>
//        <div class="modal-body">
//        <span> Please Choose Other City: </span>
//        <a href="http://127.0.0.1:8000/archiveaccommodation"> ${single_cities[0].title} </a>
//        <span> You Can choose also ${current_people_str} People </span>
//        </div>
//        <div class="modal-footer">
//
//        </div>
//      </div>
//    </div>
//  </div>
//      `
//      localStorage.setItem('usermessage', k)
//      // $('#exampleModalsingle').modal('show')
//      exampleModalsingle.innerHTML=localStorage.getItem('usermessage')
//
//      })
//
//
//      //  //  console.log(hiddenDiv)
//      if(localStorage.getItem("item") == null){
//        // Page has already loaded earlier
//        // $("#hidden_div").css("display","block");
//        localStorage.mytime = document.getElementById('hidden_div').innerHTML;
//        // $('#exampleModalsingle').modal('show')
//        exampleModalsingle.innerHTML=localStorage.getItem('usermessage')
//      }
//      else if(localStorage.getItem("item") =='[]'){
//        localStorage.removeItem("mytime", "");
//
//      }
//        // if(localStorage.getItem('mytime')!= null){
//        //   var go_to=document.getElementById('go_to');
//        //   go_to.style.visibility="visible";
//        // }
//
//     if(JSON.parse(localStorage.getItem('items')) === null
//         ){
//
//       items.push(item);
//       localStorage.setItem("items",JSON.stringify(items));
//       $('#exampleModalsingle').modal('show')
//       exampleModalsingle.innerHTML=localStorage.getItem('usermessage')
//       window.location.reload();
//      // item.pop.style.display="block"
//
//
//
//     }
//     else if(single_cities[0].title!==city_currentl.innerHTML.trim()){
//      JSON.parse(localStorage.getItem('cities_obj')).map(data=>{
//
//      let message_not=`
//       <div class="modal show fade" id="message_not_pop" data-keyboard="false" data-backdrop="static" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
//    <div class="modal-dialog" role="document">
//      <div class="modal-content">
//        <div class="modal-header">
//          <h5 class="modal-title" id="exampleModalLabel">Please Choose Other City</h5>
//
//
//          </button>
//        </div>
//        <div class="modal-body">
//        <span> Please Choose Other City: </span>
//        <a href="http://127.0.0.1:8000/archiveaccommodation"> ${single_cities[0].title} </a>
//        <span> You Can choose also ${current_people_str} People </span>
//        </div>
//        <div class="modal-footer">
//
//        </div>
//      </div>
//    </div>
//  </div>
//      `
//      console.log(message_not)
//      document.getElementById('message_not').innerHTML=message_not
//
//      $('#message_not_pop').modal('show')
//
//
//      })
//     }
//     else {
//
//       const localItems = JSON.parse(localStorage.getItem("items"));
//       localItems.map(data=>{
//
//         if(item.serverid == data.serverid){
//           item.no = data.no + 1;
//         }
//         else{
//           items.push(data);
//         }
//       });
//
//       items.push(item);
//
//       exampleModalsingle.innerHTML=localStorage.getItem('usermessage')
//      //  window.localStorage.getItem('items.pop');
//       localStorage.setItem('items',JSON.stringify(items));
//      //  var hiddenDiv=document.getElementById('hidden_div');
//      //  hiddenDiv.style.display="block"
//      //  console.log(hiddenDiv)
//      //  window.location.reload();
//      //  window.localStorage.setItem('pops', JSON.stringify(pop));
//      $('#exampleModalsingle').modal('show')
//      //  document.getElementById('go_to').innerHTML =localStorage.getItem("pops")
//
//
//     }
//   }else{
//     alert('local storage is not working on your browser');
//   }
//
// });
//}
//
// // adding data to shopping cart
//const iconShoppingP = document.querySelector('.iconShopping p');
//let no = 0;
//JSON.parse(localStorage.getItem('items')).map(data=>{
// no = no+data.no
//;	});
//// iconShoppingP.innerHTML = no;
//
//
////adding cartbox data in table
//const cardBoxTable = document.querySelector('.cart_table');
//let tableData = '';
//tableData += '';
//if(JSON.parse(localStorage.getItem('items'))[0] === null){
// tableData += '<tr><td colspan="5">No items found</td></tr>'
//}else{
// JSON.parse(localStorage.getItem('items')).map(data=>{
//   var pricee=parseInt(data.price);
//  //  var noo=parseInt(data.no);
//  //  var result=pricee;
//  // console.log(result);
//  // console.log(pricee);
//tableData +=  '  <div class="items"> <div class="row">   <div class="col-md-6 left_side"> <img src="' + data.image + ' ">' + '</div> <div class="col-md-6 right_side"> <div style="display:none">' +data.id + ' </div> <h5 id="test">'  + data.title + '</h5>' +
//   ' <div class="description">' + data.room +'<h6>Price</h6> <p class="price_order">' + data.price + '<input type="hidden" name="room_id" class="localstorage_id" value="'+ data.serverid +'">' + '</p>' +' <a href="#" class="delete_checkitems" onclick=Delete(this);>X</a></div> </div>  </div> </div>';
// });
//}
//
//cardBoxTable.innerHTML = tableData;
//
//
//
//
//// checkout page
//
//var reservation_total=document.getElementsByClassName ("reservation_price");
//console.log(reservation_total)
//
//var reservation_order=document.getElementsByClassName ("number_order");
//var arr='';
//var sum =0;
//var reservation_price=document.getElementsByClassName ("price_order");
//for(var reser_i=0; reser_i<reservation_price.length; reser_i++){
//sum+=parseInt(reservation_price[reser_i].innerHTML);
//
//}
//
//
// reservation_total[0].innerHTML+=sum
//// var reservation_totall=document.getElementsByClassName ("reservation_pricee");
//// console.log(reservation_total)
//
//// var reservation_orders=document.getElementsByClassName ("number_order");
//// var arr='';
//// var sum =0;
//// var reservation_pricee=document.getElementsByClassName ("price_orderr");
//// for(var reser_i=0; reser_i<reservation_pricee.length; reser_i++){
//// sum+=parseInt(reservation_pricee[reser_i].innerHTML);
//
//// }
//
//
//// reservation_totall[0].innerHTML+=sum
//
//
//
//let localid=document.getElementsByClassName('localstorage_id');
//// let localid=document.getElementsByClassName('personalCheckout');
//
//console.log(localid)
//
//let result_id='';
//console.log(typeof(result_id))
//// console.log(result_id)
//for(let id=0; id<localid.length; id++){
//  result_id+=localid[id].value + ' '
//// check_server+=result_id;
//}
//console.log(result_id)
//// document.getElementById('checkout_server').value='11';
//// console.log(check_server)
//// check_server.setAttribute('value',result_id )
//// let form_check=document.getElementById('checkout_form');
//
//
//
//  // let create=(value, name)=>{
//  //   let input=document.createElement('input');
//  //   input.setAttribute('type', 'text');
//  //   input.setAttribute('name', name);;
//  //   input.setAttribute('value', value);
//  //   form_check.appendChild(input)
//
//
//  // }
//
//  // create(localid[id].value,id);
//  let test1=document.getElementById('personalCheckout');
//
//  test1.setAttribute('value',result_id);
//
//  let personalcheck=document.getElementById('personalCheckout');
//  localStorage.setItem('input_id', personalcheck.value);
//
//
//
//
//console.log(single_cities[0].title)