let startdate=document.getElementById('startdate');
let endtdate=document.getElementById('endtdate');
let Quantity=document.getElementById('Quantity');
let pricethemed=document.getElementById('pricethemed');
let pricethemedTotal=document.getElementById('pricethemedTotal');
let packnumber_days=document.getElementById('packnumber_days');

let children1=parseInt(localStorage.getItem('children1'));
let adult1=parseInt(localStorage.getItem('adult1'));
Quantity.value=children1+adult1;
pricethemed.innerHTML=Quantity.value*50+'$'
pricethemedTotal.innerHTML=Quantity.value*50+'$'
Quantity.addEventListener('keyup', function(e){
   console.log(e.target.value)
   pricethemed.innerHTML=e.target.value*50 +'$';
   pricethemedTotal.innerHTML=e.target.value*50 +'$';
})

// dates start


startdate.value=localStorage.getItem('txtValue2');
console.log(startdate.value)
// enddate
var date = new Date(startdate.value);
var newdate = new Date(date);

newdate.setDate(newdate.getDate() + packnumber_days.innerHTML);

var dd = newdate.getDate();
var mm = newdate.getMonth() + 1;
console.log(mm)
var y = newdate.getFullYear();
if(mm<10){
    var someFormattedDate = y + '-' +'0' + mm + '-' + dd    
    console.log(someFormattedDate)
    endtdate.value = someFormattedDate;
}
else{
    var someFormattedDate = y + '-' + mm + '-' + dd;    
    console.log(someFormattedDate)
    endtdate.value = someFormattedDate;
}
