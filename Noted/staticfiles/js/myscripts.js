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
    var url = "/main/tasks/" + date + "/edit/" + task_id;
    window.location.replace(url);
    }

function DateUnpin(note_id) {
    date = GetDatestring();
    var path = window.location.pathname
    var url = "/main/" + date + "/unpin/" + note_id +'?next=' + path;
    window.location.replace(url);
    }

function DatePin(note_id) {
    date = GetDatestring();
    var path = window.location.pathname
    var url = "/main/" + date + "/pin/" + note_id +'?next=' + path;
    window.location.replace(url);
    }

function submitbtn() {
    document.getElementById("task_submit").style.display= "none";
    setTimeout(function(){document.getElementById("task_submit").style.display= "block";},3000);
}