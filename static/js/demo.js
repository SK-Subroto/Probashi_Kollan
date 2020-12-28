
var defaultTheme = 0

var today = new Date();


var week_date = [];

var curAdd, curRmv;


function getWeeksInMonth(a, b) {
    var c = [], d = new Date(b, a, 1), e = new Date(b, a + 1, 0), f = e.getDate();
    var g = 1;
    var h = 7 - d.getDay();
    while (g <= f) {
        c.push({
            start: g,
            end: h
        });
        g = h + 1;
        h += 7;
        if (h > f) h = f;
    }
    return c;
}

week_date = getWeeksInMonth(today.getMonth(), today.getFullYear())[2];

$(document).ready(function () {
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/meeting-list/',
        success: function (meetings) {
         var arrayList=[];
            $.each(meetings,function (i, meeting) {
                var obj={id:meeting.id,name:meeting.title,description:meeting.description,date:meeting.meeting_date,type:"event"};
                arrayList.push(obj);
            });
            // console.log(arrayList)
            $("#demoEvoCalendar").evoCalendar({
                format: "MM dd, yyyy",
                titleFormat: "MM",
                calendarEvents: arrayList
            });

            a($("[data-set-theme]")[defaultTheme]);
                function a(a) {
                    var b = a.dataset.setTheme;
                    $("#demoEvoCalendar").evoCalendar("setTheme", b);
                }
        }
    })
});


$('[data-go*="#"]').on("click", function(a) {
    a.preventDefault();
    var b = $(this).data().go;
    if ("#top" === b) {
        $("html, body").animate({
            scrollTop: 0
        }, 500);
        return;
    } else var c = $(b)[0].offsetTop - $("header")[0].offsetHeight - 10;
    $("html, body").animate({
        scrollTop: c
    }, 500);
});