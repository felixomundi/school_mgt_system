var token = document.querySelector('[name=csrfmiddlewaretoken]').value;
document.getElementById('postForm').addEventListener("submit", async function (e) {
    e.preventDefault();
    var formData = new FormData();
    formData.append('unit', document.getElementById('unit').value);
    formData.append('session', document.getElementById('session').value);
    formData.append('csrfmiddlewaretoken', token);
    try {
        const response = await axios.post("/get_students", formData);
        var json_data = JSON.parse(response.data);        
        if (json_data.length == 0) {
            // document.getElementById("append-data").innerHTML += "<p class='text-danger m-3'>No students found</p>"
            $("#append-data").html("<p class='text-danger m-3'>No students found</p>")
        } else {
            var div_data = "<div class='form-group'><div class='row'><div class='col-lg-12'><select id='mySelect' class='form-control m-3'> <option value=''>Select Student</option>"
       
            for (key in json_data) {
            
                div_data += "<option value='" + json_data[key]['id'] + "'>" + json_data[key]['name'] + "</option>"
            
            }
            div_data += "</select></div></div></div>";
            div_data += "<div class='form-group'><div class='row'>";

            div_data += "<div class='col-lg-6'>";
            div_data += "<label>Assignment Marks : </label><input  type='number' min='0' max='30' step='0.01' id='assignment_marks'  class='form-control' placeholder='Assignment Marks' />";
            div_data += "</div>";

            div_data += "<div class='col-lg-6'>";
            div_data += "<label>Exam Marks : </label><input type='number' min='0' max='70' step='0.01' id='exam_marks' class='form-control' placeholder='Exam Marks' />";
            div_data += "</div>";

            div_data += "</div></div>";

            div_data += "<div class='form-group'>";
            div_data += "<button id='save-result' class='btn btn-success' type='submit'>Save Result</button>";
            div_data += "</div>";
        
            $("#append-data").html(div_data);
      
        }
    }
    catch (error) {
        console.log(error);
        alert("Error in getting students");
    };

    document.getElementById("save-result").addEventListener("click", async function (e) {
    
        e.preventDefault();
        var unit = document.getElementById("unit").value;
        var student = document.getElementById("mySelect").value;
        if (!student) {
            alert("Select student");
            return student;
        }
        var assignment_marks = document.getElementById("assignment_marks").value;
        if (!assignment_marks) {
            alert("Add assignment marks");
            return assignment_marks;
       } 
        var exam_marks = document.getElementById("exam_marks").value;
        if (!exam_marks) {
            alert("Add exam marks");
            return exam_marks;
        }

        var new_data = {
            unit, student, assignment_marks, exam_marks
        }
        var new_body = JSON.stringify(new_data);
        const axios_config = {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
                mode: 'same-origin'
            }
        };
        const body = new_body;
        try {
            const response = await axios.post("save_marks", body, axios_config);
            var serverResponse = response.data;
            if (serverResponse == "Ok") {
                document.querySelector("#success").classList.remove("hidden");
                $("#success").html("<p class='text-success'>Result added successfully</p>")
            } else if (serverResponse == "Updated") {
                document.querySelector("#success").classList.remove("hidden");
                $("#success").html("<p class='text-dark'>Result updated successfully</p>")
            }
            return response.data;
        }
        catch (error) {
            document.querySelector("#error").classList.remove("hidden");
            $("#error").html("<p class='text-danger'>Failed to add result</p>")
            console.log(error)
            
        }
    });
   

});



