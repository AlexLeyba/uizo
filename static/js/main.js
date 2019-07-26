// $("#first").on("click", function() {
//   $("#text1").toggle("fide");
//   togglearoow1();
// });
//
// function togglearoow1() {
//   if ($(".arrow-list1").attr("src") == "../img/imgsite/arrow-btn.svg") {
//     $(".arrow-list1").attr("src", "../img/imgsite/arrow-up.svg");
//   } else {
//     $(".arrow-list1").attr("src", "../img/imgsite/arrow-btn.svg");
//   }
// }
//
// $("#second").on("click", function() {
//   $("#text2").toggle("fide");
//   togglearoow2();
// });
//
// function togglearoow2() {
//   if ($(".arrow-list2").attr("src") == "../img/imgsite/arrow-btn.svg") {
//     $(".arrow-list2").attr("src", "../img/imgsite/arrow-up.svg");
//   } else {
//     $(".arrow-list2").attr("src", "../img/imgsite/arrow-btn.svg");
//   }
// }
//
// $("#three").on("click", function() {
//   $("#text3").toggle("fide");
//   togglearoow3();
// });
//
// function togglearoow3() {
//   if ($(".arrow-list3").attr("src") == "../img/imgsite/arrow-btn.svg") {
//     $(".arrow-list3").attr("src", "../img/imgsite/arrow-up.svg");
//   } else {
//     $(".arrow-list3").attr("src", "../img/imgsite/arrow-btn.svg");
//   }
// }
//
// $("#four").on("click", function() {
//   $("#text4").toggle("fide");
//   togglearoow4();
// });
//
// function togglearoow4() {
//   if ($(".arrow-list4").attr("src") == "../img/imgsite/arrow-btn.svg") {
//     $(".arrow-list4").attr("src", "../img/imgsite/arrow-up.svg");
//   } else {
//     $(".arrow-list4").attr("src", "../img/imgsite/arrow-btn.svg");
//   }
// }


$('.faq_item_title_inner').on('click', function () {
        $(this).parents('.faq_item').find('.faq_item_body').slideToggle(300);
        $(this).toggleClass('open');
        if ($(this).hasClass('show_all')) {
            if ($(this).hasClass('open')) {
                $(this).html('Свернуть все');
                $('.faq_item_title_inner:not(.open)').trigger('click');
            } else {
                $(this).html('Смотреть все');
                $('.faq_item_title_inner.open').trigger('click');
            }
        }
    });
$("#mobail").on("click", function() {

  $("#nav").toggle("fide");
});
function qwer() {
  alert(1);
  $("#nav").toggle("fide");
}
