$(document).ready(function(){
    $("#fetch-student").click(function(event){

        // Displaying Students Based on Staff, Course and Session Enrolled
        event.preventDefault()
        var unit = $("#unit").val();
        var session = $("#session").val();
        var year = $("#year_of_study").val();
        console.log("first",year)
        var new_url = "get_students";
        $.ajax({
             url:new_url,
            type:'POST',
            data: {
                unit: unit,
                session: session,
                year_of_study:year,
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
        })

        
            .done(function (response) {
            console.log(response)
            // var json_data=JSON.parse(response);
            // console.log(json_data)
            // //Displaying Attendance Date Input and Students Attendance
            // var div_data="<div class='form-group'><label>Attendance Date: </label> <input type='date' name='attendance_date' id='attendance_date' class='form-control' /></div>"
            // div_data+="<div class='form-group'><div class='row'>"

            // for(key in json_data)
            // {
            //     div_data+="<div class='col-lg-2'><div class='form-check'><input type='checkbox' checked='checked' name='student_data[]' value='"+ json_data[key]['id'] +"' />  <label class='form-check-label'>"+ json_data[key]['name']+" </label></div></div> ";

            // }
            // div_data+="</div></div>";
            // div_data+="<div class='form-group'>";
            // div_data+="<button id='save_attendance' class='btn btn-success' type='button'>Save Attendance Data</button>";
            // div_data+="</div>";
            // $("#student_data").html(div_data);

        })
        .fail(function(){
           console.log(error)
        })

      

    })
})