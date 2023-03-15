var today=new Date();
    var day=today.getDate();
    document.getElementById('tasks-notes').style.backgroundImage = 'url('+'/static/images/'+day+'.jpg'+')';
    document.getElementById('tasks-notes').style.backgroundRepeat = "no-repeat";
    document.getElementById('tasks-notes').style.backgroundPosition = "center";
    document.getElementById('tasks-notes').style.backgroundSize = "cover";
}