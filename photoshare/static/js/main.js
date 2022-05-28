// $("#show").hover(
//   function () {
//     $("#hide").css("display", "none").slideDown(2000,function () {
//         $("#show").css("display", "none") 
//     });
//   },
//   function () {
//     $("#hide").css("display", "block").slideUp(3000);
//   }
// );

$("#show").click(function () {
    $("#hide").css("display",'none').slideDown(2000)
    $("#show").css("display",'none')
})
