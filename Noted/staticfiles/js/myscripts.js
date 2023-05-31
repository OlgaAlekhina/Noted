function GetDatestring() {
    var today = new Date();
    var day = today.getDate();
    var d = (day<10 ? '0' : '') + day;
    var mon = today.getMonth() + 1;
    var m = (mon<10 ? '0' : '') + mon;
    var year = today.getFullYear();
    var date = d + '-' + m + '-' + year;
    return date;
}

function DateInsert(task_id) {
    date = GetDatestring();
    var url = "/main/tasks/" + date + "/edit/" + task_id + '#task' + task_id;
    window.location.replace(url);
    }

function DateUnpin(note_id) {
    date = GetDatestring();
    var path = window.location.href
    var url = "/main/" + date + "/unpin/" + note_id +'?next=' + path;
    window.location.replace(url);
    }

function DatePin(note_id) {
    date = GetDatestring();
    var path = window.location.href
    var url = "/main/" + date + "/pin/" + note_id +'?next=' + path;
    window.location.replace(url);
    }

function submitbtn() {
    document.getElementById("task_submit").style.display= "none";
    setTimeout(function(){document.getElementById("task_submit").style.display= "block";},3000);
}

// после нажатия на кнопку отправки формы убирает эту кнопку на 3 секунды
function subformbtn() {
    document.getElementById("form_submit").style.display= "none";
    setTimeout(function(){document.getElementById("form_submit").style.display= "block";},3000);
}

// меняет приоритет задачи с низкого на высокий при клике на белый флажок
function checkBox() {
    var check_on = '<a onclick="uncheckBox()" style="cursor: pointer;"><img src="/static/images/icons/flag_icon.svg" width="25px" height="25px"/></a><span style="padding-left: 4px;">Приоритет</span><input type="hidden" id="priority" name="priority" value="priority">';
    document.getElementById('prior_choice').innerHTML = check_on;
}

// меняет приоритет задачи с высокого на низкий при клике на красный флажок
function uncheckBox() {
    var check_on = '<a onclick="checkBox()" style="cursor: pointer;"><img src="/static/images/icons/flag_white.svg" width="25px" height="25px"/></a><span style="padding-left: 4px;">Приоритет</span>';
    document.getElementById('prior_choice').innerHTML = check_on;
}

// добавляет в урл для восстановления задачи текущую дату, чтобы поставить ее в качестве даты выполнения
function restoreTask(task_id) {
    date = GetDatestring();
    var url = "/main/task_restore/" + date + '/' + task_id;
    window.location.replace(url);
}

// показывает или скрывает пароль при нажатии на иконку глаза
function togglePassword() {
    const password = document.getElementById("password");
    const type = password.getAttribute('type') === "password" ? "text" : "password";
    password.setAttribute("type", type);
    const img = document.getElementById("togglePassword");
    const src = img.getAttribute('src') === "/static/images/icons/eye_closed.svg" ? "/static/images/icons/eye.svg" : "/static/images/icons/eye_closed.svg";
    img.setAttribute("src", src);
}

// кастомизация поля выбора файла
function fileinputChange() {
    var file = document.getElementById('note-file');
    var placeholder = document.getElementById('text_input_id');
    if (file.value == "")
    {
        placeholder.setAttribute("placeholder", "Файл не выбран");
    }
    else
    {
        var theSplit = file.value.split('\\');
        placeholder.setAttribute("placeholder", theSplit[theSplit.length-1]);
    }
}

// переводит текст поля выбора файлов на английский
function transAddfile() {
    var file_span = document.getElementById('text_input_span_id');
    var file_text = document.getElementById('text_input_id');
    var lang = document.getElementById('lang_select').value;
    if (lang == 'en') {
        file_span.innerHTML = 'Add file';
        file_text.setAttribute("placeholder", "No file chosen");
    }
}

