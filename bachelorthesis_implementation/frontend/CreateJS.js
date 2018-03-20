//Require latest version of jQuery and the Bootstrap popover plugin
require(['jquery-noconflict', 'bootstrap-popover'], function (jQuery) {
  //Ensure MooTools is where it must be
  Window.implement('$', function (el, nc) {
    return document.id(el, nc, this.document);
  });
  
  var $ = window.jQuery;
  
  //Begin tooltip popovers: http://getbootstrap.com/2.3.2/javascript.html#popovers
  $('.b1_tip').popover({
    html:true,
    trigger:'hover',
    title:'Intermediate English (B1)',
    content:'<p>You understand the main points of a discussion and can deal with most situations. You can describe experiences and briefly give explanations.</p>', 
  });
  
  $('.b2_tip').popover({
    html:true,
    trigger:'hover',
    title:'Upper-Intermediate English (B2)',
    content:'<p>You understand the main ideas of complex text on both concrete and abstract topics. You can interact with a degree of fluency and spontaneity that makes regular interaction with native speakers quite possible without strain for either party.</p>',
  });
  
  $('.c1_tip').popover({
    html:true,
    trigger:'hover',
    title:'Advanced English (C1)',
    content:'<p>You understand a wide range of demanding, longer texts, and recognise implicit meaning. You can use language flexibly and effectively for social, academic and professional purposes.</p>',
  });
  
  
  $('.c2_tip').popover({
    html:true,
    trigger:'hover',
    title:'Proficiency (C2) / Native Speaker',
    content:'<p>You understand with ease hardly everything heard or read. You can express yourself spontaneously and precisely, differentiating finer shades of meaning even in more complex situations.</p>',
  });
   $('.input_tip').popover({
    html:true,
    trigger:'hover',
    placement:'left',
    title:'Requirements of your input',
    content:'<p> Your input has to be at least three characters long, but should not extend more than 20 characters or more than 5 words. You can use both words from the single document and words that are not already in this abstract.</p>',
  });
 
   
  $("#submit_english_questions").click(function(){
    var allRight = true;
    $("english_skills.check").each(function(){
      if (this.checked) {
        return true;
      }
      else {
        allRight = false;
        return false;
      }
        });
    
    /* var allRight = true;
    $(".english_skills.right").each(function(){
      if (this.checked) {
        return true;
      }
      else {
        allRight = false;
        return false;
      }
        });
 
    
    if (allRight) { */
    if (allRight) {
    $("#all").css("display", "block");
    $(".english_skills").hide();
    $(".abstracts").show();
    $(".individual_keywords").show();
    $(".class_generated_keywords_sim").hide();
    $(".given_keywords").hide();
    $(".generated_keywords_diff").hide();
    $(".generated_keywords_dissim").hide();
    $(".feedback").hide();
    $("#submit_english_questions").hide();
    $("#submit_general_keywords").hide();
    }
   
    
    /* //Change setting for all forms: Deactivate due to to platform restrictions
  $.validator.setDefaults({
    ignore: [],
  });
    else {
         alert("Sorry, your answers didn't meet our requirements. Unfortunately, you can't take part in this task. Thank you anyway! ");
         $(".english_skills").hide();
         $("#submit_english_questions").hide();
    }
    */
   
  });
  
  $("#submit_individual_keywords").click(function(){
    $(".individual_keywords").hide();
    $(".class_generated_keywords_sim").show();
    $(".generated_keywords_diff").show();
    $(".generated_keywords_dissim").show();
         $(".given_keywords").show();
    $(".feedback").hide();
    $("#submit_individual_keywords").hide();
    $("#submit_general_keywords").show();
  });
  
  $("#submit_general_keywords").click(function(){
    $(".abstracts").hide();
        $(".given_keywords").hide();
    $(".class_generated_keywords_sim").hide();
    $(".generated_keywords_diff").hide();
    $(".generated_keywords_dissim").hide();
    $(".feedback").show();
    $("#submit_general_keywords").hide();
  });

});
