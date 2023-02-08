var attendanceBtn = document.getElementById("fetch-attendance-dates");      
attendanceBtn.addEventListener("click", async function (e) {
    e.preventDefault();
    var unit = document.getElementById("unit").value;
    var session = document.getElementById("session").value;
    var data = {
        unit, session,
    }
    let body = JSON.stringify(data);
   
    var config = {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
            mode: 'same-origin'
        }
    };
    try {
        var response = await axios.post("/get_attendance_dates", body, config);
        var json_data = JSON.parse(response.data);
        console.log(json_data);
        if (json_data.length>0) {
            var html_data = "";
            for (key in json_data) {
                html_data += "<option value='" + json_data[key]["id"] + "'>" + json_data[key]["attendance_date"] + "</option>"
            }
            $("#error_attendance").html("");
            $("#error_attendance").hide();
            $("#attendance_block").show();
            $("#fetch_student_block").show();
            $("#attendance_date").html(html_data);
        } else {
            $("#error_attendance").html("No Attendance Data Found.");
            $("#error_attendance").show();
            $("#attendance_block").hide();
            $("#fetch_student_block").hide();
            $("#attendance_date") = "" 
        }
    }
    catch (error) {
        console.log(error);
        // alert("Error in getting Attendance Dates.")
        $("#error_attendance").html("Error or No Attendance Data Found.");
        $("#fetch_student_block").hide();
        $("#attendance_block").hide();
    }
});


var fetchStudentBtn = document.getElementById("fetch_student");
fetchStudentBtn.addEventListener("click", async function (e) {
    e.preventDefault();
    var attendance_date = document.getElementById("attendance_date").value;
    if (!student_data) {
       
        alert("Select student");
        return attendance_date;
    }
    let body = JSON.stringify(attendance_date);
    var config = {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
            mode: 'same-origin'
        }
    };
    let url = 'get_attendance_student';
    try {
        var response = await axios.post(url, body, config);
        alert(response.data);
        console.log(response.data);
    }
    catch (error) {
        console.log(error);
    }

});



