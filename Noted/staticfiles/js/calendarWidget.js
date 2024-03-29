var Cal = function(divId1, divId2) {
  //Сохраняем идентификатор div
  this.divId1 = divId1;
  this.divId2 = divId2;
  // Дни недели с понедельника
  this.DaysOfWeek = [
    'ПН',
    'ВТ',
    'СР',
    'ЧТ',
    'ПТ',
    'СБ',
    'ВС'
  ];
  this.DaysOfWeek2 = [
    'MO',
    'TU',
    'WE',
    'TH',
    'FR',
    'SA',
    'SU'
  ];
  // Месяцы начиная с января
  this.Months =['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'];
  this.Months2 =['January', 'Fabruary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  //Устанавливаем текущий месяц, год
  var d = new Date();
  this.currMonth = d.getMonth();
  this.currYear = d.getFullYear();
  this.currDay = d.getDate();
};
// Переход к следующему месяцу
Cal.prototype.nextMonth = function() {
  if ( this.currMonth == 11 ) {
    this.currMonth = 0;
    this.currYear = this.currYear + 1;
  }
  else {
    this.currMonth = this.currMonth + 1;
  }
  this.showcurr();
};
// Переход к предыдущему месяцу
Cal.prototype.previousMonth = function() {
  if ( this.currMonth == 0 ) {
    this.currMonth = 11;
    this.currYear = this.currYear - 1;
  }
  else {
    this.currMonth = this.currMonth - 1;
  }
  this.showcurr();
};
// Показать текущий месяц
Cal.prototype.showcurr = function() {
  this.showMonth(this.currYear, this.currMonth);
};
// Показать месяц (год, месяц)
Cal.prototype.showMonth = function(y, m) {
  var d = new Date()
  // Первый день недели в выбранном месяце
  , firstDayOfMonth = new Date(y, m, 7).getDay()
  // Последний день выбранного месяца
  , lastDateOfMonth =  new Date(y, m+1, 0).getDate()
  // Последний день предыдущего месяца
  , lastDayOfLastMonth = m == 0 ? new Date(y-1, 11, 0).getDate() : new Date(y, m, 0).getDate();

  var html1 = '';
  var lang = document.getElementById('lang_select').value;
  if (lang === 'ru') {
  // Запись выбранного месяца и года
    html1 += this.Months[m] + ', ' + y;
  }
  else {
    html1 += this.Months2[m] + ', ' + y;
  }
  var html = '<table>';

  // заголовок дней недели
  html += '<tr class="days">';
  if (lang === 'ru') {
      for(var i=0; i < this.DaysOfWeek.length;i++) {
        html += '<td>' + this.DaysOfWeek[i] + '</td>';
      }
  }
  else {
      for(var i=0; i < this.DaysOfWeek2.length;i++) {
        html += '<td>' + this.DaysOfWeek2[i] + '</td>';
      }
  }
  html += '</tr>';
  // Записываем дни
  var i=1;
  do {
    var dow = new Date(y, m, i).getDay();
    // Начать новую строку в понедельник
    if ( dow == 1 ) {
      html += '<tr>';
    }
    // Если первый день недели не понедельник, показать последние дни предыдущего месяца
    else if ( i == 1 ) {
      html += '<tr>';
      var k = lastDayOfLastMonth - firstDayOfMonth+1;
      for(var j=0; j < firstDayOfMonth; j++) {
        var m0 = (m<10 ? '0' : '') + m;
        html += '<td class="not-current"><a href=/main/' + k + '-' + (m==0 ? '12' : m0) + '-' + (m==0 ? y-1 : y) + '/>' + k + '</td>';
        k++;
      }
    }
    // Записываем текущий день в цикл
    var chk = new Date();
    var chkY = chk.getFullYear();
    var chkM = chk.getMonth();
    var day = (i<10 ? '0' : '') + i;
    var mon = m+1;
    var mon0 = (mon<10 ? '0' : '') + mon;
    if (chkY == this.currYear && chkM == this.currMonth && i == this.currDay) {
      html += '<td><span class="today"><a href=/main/' + day + '-' + mon0 + '-' + y + '/>' + i + '</span></td>';
    } else {
      html += '<td class="normal"><a href=/main/' + day + '-' + mon0 + '-' + y + '/>' + i + '</td>';
    }
    // закрыть строку в воскресенье
    if ( dow == 0 ) {
      html += '</tr>';
    }
    // Если последний день месяца не воскресенье, показать первые дни следующего месяца
    else if ( i == lastDateOfMonth ) {
      var k=1;
      var m1 = m+2;
      var m0 = (m1<10 ? '0' : '') + m1;
      for(dow; dow < 7; dow++) {
        var k0 = (k<10 ? '0' : '') + k;
        html += '<td class="not-current"><a href=/main/' + k0 + '-' + (m==11 ? '01' : m0) + '-' + (m==11 ? y+1 : y) + '/>' + k + '</td>';

	k++;
      }
    }
    i++;
  }while(i <= lastDateOfMonth);
  // Конец таблицы
  html += '</table>';
  // Записываем HTML в div

  document.getElementById(this.divId2).innerHTML = html;
  document.getElementById(this.divId1).innerHTML = html1;

};

  // Начать календарь
  var c = new Cal("headCal", "divCal");
  c.showcurr();
  // Привязываем кнопки «Следующий» и «Предыдущий»
  getId('btnNext').onclick = function() {
    c.nextMonth();
  };
  getId('btnPrev').onclick = function() {
    c.previousMonth();
  };

// Получить элемент по id
function getId(id) {
  return document.getElementById(id);
}



