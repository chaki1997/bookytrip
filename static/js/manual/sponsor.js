$(document).ready(function(){
   $('input[name=customRadio1]').click(function () {
     if (this.id == "customRadio14") {
         $("#other").show('slow');
     } else {
         $("#other").hide('slow');
     }
   });




   var input = document.querySelector("#phone");
   window.intlTelInput(input, {
    allowDropdown: true,
    autoHideDialCode: false,
    autoPlaceholder: "on",
    // preferredCountries: ['ge'],
    autoPlaceholder:"polite",
    initialCountry: "auto",
    type: "",
    dropdownContainer: document.body,
    // excludeCountries: ["Af"],
    formatOnDisplay: true,
    geoIpLookup: function(callback) {
      $.get("http://ipinfo.io/", function() {}, "jsonp").always(function(resp) {
        var countryCode = (resp && resp.country) ? resp.country : "ge";
        callback(countryCode);
      });
    },
  // //   hiddenInput: "full_number",
    // initialCountry: "Ge",
  //   localizedCountries: { 'Ge': 'Georgia' },
  //   nationalMode: true,
   
  
  
    // onlyCountries: ['us', 'gb', 'ch', 'ca', 'do'],
    placeholderNumberType: "MOBILE",
    // preferredCountries: ['ge'],
    separateDialCode: false,
       utilsScript: "{% static 'js/manual/utils.js' %}",
   });

   
});
window.intlTelInputGlobals.loadUtils("{% static 'js/manual/utils.js' %}");