(function($) {
  "use strict"; // Start of use strict

  // Toggle the side navigation
  $("#sidebarToggle, #sidebarToggleTop").on('click', function(e) {
    $("body").toggleClass("sidebar-toggled");
    $(".sidebar").toggleClass("toggled");
    if ($(".sidebar").hasClass("toggled")) {
      $('.sidebar .collapse').collapse('hide');
    };
  });
  // $(document).ready(function($) {
 
  //   $('.select').change(function() {
     
  //     var selection = $(this).val();
  //     var dataset = $('table').find('tr');
    
  //     dataset.show();
      
  //     dataset.filter(function(index, item) {
  //       return $(item).find('td:first-child').text().split(',').indexOf(selection) === -1;
  //     }).hide();
  
  //   });
  // });

  // Close any open menu accordions when window is resized below 768px
  $(window).resize(function() {
    if ($(window).width() < 768) {
      $('.sidebar .collapse').collapse('hide');
    };
    
    // Toggle the side navigation when window is resized below 480px
    if ($(window).width() < 480 && !$(".sidebar").hasClass("toggled")) {
      $("body").addClass("sidebar-toggled");
      $(".sidebar").addClass("toggled");
      $('.sidebar .collapse').collapse('hide');
    };
  });

  // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
  $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function(e) {
    if ($(window).width() > 768) {
      var e0 = e.originalEvent,
        delta = e0.wheelDelta || -e0.detail;
      this.scrollTop += (delta < 0 ? 1 : -1) * 30;
      e.preventDefault();
    }
  });

  // Scroll to top button appear
  $(document).on('scroll', function() {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 100) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }
  });

  // Smooth scrolling using jQuery easing
  $(document).on('click', 'a.scroll-to-top', function(e) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: ($($anchor.attr('href')).offset().top)
    }, 1000, 'easeInOutExpo');
    e.preventDefault();
  });

})(jQuery); // End of use strict

// menu hidden div
function main(target){
           
  var artz = document.getElementsByClassName('hidden_div');
  var targ = document.getElementById(target);  
  var isVis = targ.style.display=='block';
    
  // hide all
  for(var i=0;i<artz.length;i++){
     artz[i].style.display = 'none';
  }
  // toggle current
  targ.style.display = isVis?'none':'block';
    
  return false;
}

// table check

$(document).ready(function() {
  $(".checkAll").on("click", function() {
    $(this)
      .closest("table")
      .find("tbody :checkbox")
      .prop("checked", this.checked)
      .closest("tr")
      .toggleClass("selected", this.checked);
  });
 
  $("tbody :checkbox").on("click", function() {
    // toggle selected class to the checkbox in a row
    $(this).closest("tr").toggleClass("selected", this.checked);
 


    // add selected class on check all
    $(this).closest("table").find(".checkAll").prop("checked",$(this).closest("table")
          .find("tbody :checkbox:checked").length ==
          $(this)
            .closest("table")
            .find("tbody :checkbox").length
      );
  });
});

// table pagination

getPagination('#table-id');
$('#maxRows').trigger('change');
function getPagination (table){

    $('#maxRows').on('change',function(){
      $('.pagination').html('');						// reset pagination div
      var trnum = 0 ;									// reset tr counter 
      var maxRows = parseInt($(this).val());			// get Max Rows from select option
      
      var totalRows = $(table+' tbody tr').length;		// numbers of rows 
     $(table+' tr:gt(0)').each(function(){			// each TR in  table and not the header
       trnum++;									// Start Counter 
       if (trnum > maxRows ){						// if tr number gt maxRows
         
         $(this).hide();							// fade it out 
       }if (trnum <= maxRows ){$(this).show();}// else fade in Important in case if it ..
     });											//  was fade out to fade it in 
     if (totalRows > maxRows){						// if tr total rows gt max rows option
       var pagenum = Math.ceil(totalRows/maxRows);	// ceil total(rows/maxrows) to get ..  
                             //	numbers of pages 
       for (var i = 1; i <= pagenum ;){			// for each page append pagination li 
       $('.pagination').append('<li data-page="'+i+'">\
                    <span>'+ i++ +'<span class="sr-only">(current)</span></span>\
                  </li>').show();
       }											// end for i 
   
       
    } 												// end if row count > max rows
    $('.pagination li:first-child').addClass('active'); // add active class to the first li 
      
      
      //SHOWING ROWS NUMBER OUT OF TOTAL DEFAULT
     showig_rows_count(maxRows, 1, totalRows);
      //SHOWING ROWS NUMBER OUT OF TOTAL DEFAULT

      $('.pagination li').on('click',function(e){		// on click each page
      e.preventDefault();
      var pageNum = $(this).attr('data-page');	// get it's number
      var trIndex = 0 ;							// reset tr counter
      $('.pagination li').removeClass('active');	// remove active class from all li 
      $(this).addClass('active');					// add active class to the clicked 
      
      
      //SHOWING ROWS NUMBER OUT OF TOTAL
     showig_rows_count(maxRows, pageNum, totalRows);
      //SHOWING ROWS NUMBER OUT OF TOTAL
      
      
      
       $(table+' tr:gt(0)').each(function(){		// each tr in table not the header
         trIndex++;								// tr index counter 
         // if tr index gt maxRows*pageNum or lt maxRows*pageNum-maxRows fade if out
         if (trIndex > (maxRows*pageNum) || trIndex <= ((maxRows*pageNum)-maxRows)){
           $(this).hide();		
         }else {$(this).show();} 				//else fade in 
       }); 										// end of for each tr in table
        });										// end of on click pagination list
  });
                    // end of on select change 
   
              // END OF PAGINATION 
  
}	


    

// SI SETTING
$(function(){
// Just to append id number for each row  
default_index();
        
});

//ROWS SHOWING FUNCTION
function showig_rows_count(maxRows, pageNum, totalRows) {
 //Default rows showing
      var end_index = maxRows*pageNum;
      var start_index = ((maxRows*pageNum)- maxRows) + parseFloat(1);
      var string = 'Showing '+ start_index + ' to ' + end_index +' of ' + totalRows + ' entries';               
      $('.rows_count').html(string);
}

// CREATING INDEX
function default_index() {
$('table#table-id tr:eq(0)').prepend('<th> ID </th>')

        var id = 0;

        $('table#table-id tr:gt(0)').each(function(){	
          id++
          $(this).prepend('<td class="number_c">'+id+'</td>');
        });
}

// All Table search script
function FilterkeyWord_all_table() {

// Count td if you want to search on all table instead of specific column

var count = $('.table#table-id').children('tbody').children('tr:first-child').children('td').length; 

      // Declare variables
var input, filter, table, tr, td, i;
input = document.getElementById("search_input_all");
var input_value =     document.getElementById("search_input_all").value;
      filter = input.value.toLowerCase();
if(input_value !=''){
      table = document.getElementById("table-id");
      tr = table.getElementsByTagName("tr");

      // Loop through all table rows, and hide those who don't match the search query
      for (i = 1; i < tr.length; i++) {
        
        var flag = 0;
         
        for(j = 0; j < count; j++){
          td = tr[i].getElementsByTagName("td")[j];
          if (td) {
           
              var td_text = td.innerHTML;  
              if (td.innerHTML.toLowerCase().indexOf(filter) > -1) {
              //var td_text = td.innerHTML;  
              //td.innerHTML = 'shaban';
                flag = 1;
              } else {
                //DO NOTHING
              }
            }
          }
        if(flag==1){
                   tr[i].style.display = "";
        }else {
           tr[i].style.display = "none";
        }
      }
  }else {
    //RESET TABLE
    $('#maxRows').trigger('change');
  }
}


function myFunction() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("select");
  filter = input.value;
  table = document.getElementById("table-id");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[2];
    if (td) {
      if (td.innerHTML.indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}


$('.confirmation').on('click', function () {
  return confirm('Are you sure to Delete?');
});
function myFunction(){
  confirm('Are you sure to Delete?');
}

// capacity

let id_room_type=document.getElementById('id_room_type');
let capacity_id=document.getElementById('capacity_id');
let bed_id=document.getElementById('bed_id');
id_room_type.addEventListener('change', function(){
   if(id_room_type.value=='2' || id_room_type.value=='4'){
       capacity_id.style.display="contents";    
       bed_id.style.display="none";    
   }
   else{
    capacity_id.style.display="none";
    bed_id.style.display="contents";      
   }
})

if(id_room_type.value=='2'){
  capacity_id.style.display="contents";    
  bed_id.style.display="none";  
}