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

function checkBox() {
    var check_on = '<a onclick="uncheckBox()" style="cursor: pointer;"><img src="/static/images/icons/flag_icon.svg" width="25px" height="25px"/></a><span style="padding-left: 4px;">Приоритет</span><input type="hidden" id="priority" name="priority" value="priority">';
    document.getElementById('prior_choice').innerHTML = check_on;
}

function uncheckBox() {
    var check_on = '<a onclick="checkBox()" style="cursor: pointer;"><img src="/static/images/icons/flag_white.svg" width="25px" height="25px"/></a><span style="padding-left: 4px;">Приоритет</span>';
    document.getElementById('prior_choice').innerHTML = check_on;
}

function restoreTask(task_id) {
    date = GetDatestring();
    var url = "/main/task_restore/" + date + '/' + task_id;
    window.location.replace(url);
}