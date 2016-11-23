//CRUD for TASK
$( "#addTask" ).on( "click", function() {
    var pathname = window.location.pathname;
    var course_id = pathname.match(/\d+/)[0];
    localStorage.setItem("courseId", course_id);
});

$( "#editTask" ).on( "click", function() {
    var pathname = window.location.pathname;
    var course_id = pathname.match(/\d+/)[0];
    localStorage.setItem("courseId", course_id);
});

if (window.location.pathname == '/tasks/create' || window.location.href.indexOf("/tasks/edit") > -1) {
    var id_course = localStorage.getItem("courseId");

    if (id_course == 0) {
        alert('Не выбран курс!');
        window.location.replace("http://127.0.0.1:8000/courses/");
    }
    else {
        $('#course_id').val( $('#course_id').val() + id_course );
    }
}

$( "#taskAddSubmit" ).on( "click", function() {
    localStorage.setItem("courseId", 0);
});

/*$( "#taskEditSubmit" ).on( "click", function() {
    localStorage.setItem("courseId", 0);
});*/

//CRUD for LAB
$( "#addLabwork" ).on( "click", function() {
    var pathname = window.location.pathname;
    var task_id = pathname.match(/\d+/)[0];
    localStorage.setItem("taskId", task_id);
});

$( "#editLabwork" ).on( "click", function() {
    var pathname = window.location.pathname;
    var task_id = pathname.match(/\d+/)[0];
    localStorage.setItem("taskId", task_id);
});

$( "#checkLabwork" ).on( "click", function() {
    var pathname = window.location.pathname;
    var task_id = pathname.match(/\d+/)[0];
    localStorage.setItem("taskId", task_id);
});

$( "#labAddSubmit" ).on( "click", function() {
    localStorage.setItem("taskId", 0);
});

/*$( "#labEditSubmit" ).on( "click", function() {
    localStorage.setItem("taskId", 0);
});*/

$( "#labEditSubmit" ).on( "click", function() {
    var comment = $('#editCommentLab').val();
    if (comment == '') {
        $('#editCommentLab').val( '...' );
    }
});

if (window.location.pathname == '/labworks/create' || window.location.href.indexOf("/labworks/edit") > -1) {
    var id_task = localStorage.getItem("taskId");

    if (id_task == 0) {
        alert('Не выбрано задание!');
        window.location.replace("http://127.0.0.1:8000/courses/");
    }
    else {
        $('#task_id').val( $('#task_id').val() + id_task );
    }
}

console.log('eto id taska!');
console.log(localStorage.getItem("taskId"));
console.log('eto id cursa!');
console.log(localStorage.getItem("courseId"));