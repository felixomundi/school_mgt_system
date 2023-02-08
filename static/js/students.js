var productForm = document.getElementById('postForm')
var token = document.querySelector('[name=csrfmiddlewaretoken]').value;
productForm.addEventListener('submit', async function getStudents(e) {
    e.preventDefault();
    var formData = new FormData();
    formData.append('unit', document.getElementById('unit').value);
    formData.append('session', document.getElementById('session').value);
    formData.append('csrfmiddlewaretoken', token)
    
    try {
        
        const response = await axios.post("/get_students", formData);
        var json_data=JSON.parse(response.data);
        // console.log(json_data);
        //Displaying Attendance Date Input and Students Attendance
        var div_data="<div class='form-group'><label>Attendance Date: </label> <input type='date' required='true' name='attendance_date' id='attendance_date' class='form-control' /></div>"
        // div_data+="<div class='form-group'><div class='row'>"
        // div_data += "<div class='form-group'><div class='row'><div class='col-lg-12'><select id='mySelect' class='form-control' onchange='myFunction()'>"
        div_data += "<div class='form-group'><div class='row'><div class='col-lg-12'><select id='mySelect' class='form-control'> <option value=''>Select Student</option>"
       
        for(key in json_data)
        {
            // div_data+="<div class='col-lg-12'><input type='radio' onchange='onStudentChange(e)' name='student' class='mb-2' id='"+ json_data[key]['id'] +"' value='"+ json_data[key]['id']+"'>"+ json_data[key]['name']+"</input></div> ";
            div_data += "<option value='"+ json_data[key]['id'] +"'>"+ json_data[key]['name'] +"</option>"
            
        }
        div_data+="</select></div></div></div>";
        // div_data+="</div></div>";
        div_data+="<div class='form-group'>";
        div_data+="<button id='save_attendance' class='btn btn-success' type='button'>Save Attendance Data</button>";
        div_data+="</div>";
        $("#append-data").html(div_data);

        
    }
    catch (error) {
        console.log(error);
    };
            
        var saveButton = document.getElementById("save_attendance");      
        saveButton.addEventListener("click", async function () { 
            $(this).attr("disabled", "disabled");
            $(this).text("Saving Attendance Data...");
            var unit = document.getElementById("unit").value;                
            var session = document.getElementById("session").value;
            var attendance = document.getElementById("attendance_date").value;
            
          
            if (!attendance) {
                saveButton.removeAttribute("disabled");
                $(this).text("Save Attendance Data");
                    alert("Choose Attendance Date")
                    return attendance;
                }
                var student_data = document.getElementById("mySelect").value;
            if (!student_data) {
                saveButton.removeAttribute("disabled");
                $(this).text("Save Attendance Data");
                    alert("Select student");
                    return student_data;
                }
                            
            var data = {
                unit, session, attendance, student_data    
                    }    
                    let body = JSON.stringify(data);
                var config = {
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken,
                        mode:'same-origin'
                    }
                };
                try { 
                    const response = await axios.post("/save_attendance_data", body, config);
                    alert(response.data);
                     location.reload();

                }
                catch (error) {
                    alert("Error no student to save to attendance.");
                     location.reload();
                }
        
        
        })
});

