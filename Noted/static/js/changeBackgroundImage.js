// функция для смены фонового изображения на сайте в зависимости от даты
// в нужном блоке разместить идентификатор id="main-back"
// в папке images должны находиться картинки 1.jpg, 2.jpg ... 31.jpg
window.onload = function() {
    var today=new Date();
    var day=today.getDate();
    document.getElementById('main-back').style.backgroundImage = 'url('+'/static/images/'+day+'.jpg'+')';
    document.getElementById('main-back').style.backgroundRepeat = "no-repeat";
    document.getElementById('main-back').style.backgroundPosition = "center center";
    document.getElementById('main-back').style.backgroundSize = "contain";
    document.getElementById('main-back').style.backgroundAttachment = "fixed";
}