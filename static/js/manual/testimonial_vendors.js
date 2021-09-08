$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
        items:6,
  //      autoplay:false,
        margin:30,
        loop:false,
        dots:true,
        responsive:{
            0:{
                items:1,
                nav:true
            },
            100:{
                items:2,
                nav:true
            },
            200:{
                items:3,
                nav:true
            },
            300:{
                items:4,
                nav:true
            },
          
        }
  //      nav:true,
  //      navText:["<i class='fas fa-long-arrow-alt-left'></i>","<i class='fas fa-long-arrow-alt-right'></i>" ]
   
});
  });