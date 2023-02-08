document.getElementById("postForm").addEventListener("submit", async function (e) {
    
    e.preventDefault();
    
    var first_name = document.getElementById("first_name").value;
        if (!first_name) {
            alert("Please add your First Name")
            return first_name;
        }
    
        var last_name = document.getElementById("last_name").value;
        if (!last_name) {
            alert("Please add your Last Name");
            return last_name
        }
        var gender = document.getElementById("gender").value;
        if (!gender) {
            alert("Select your gender");
            return gender;
        }
        
    
        var data = {
            first_name, last_name, gender
        } 
        var config = {
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken,
                        mode:'same-origin'
                    }
                };
                
        var body= JSON.stringify(data)
                try { 
                    var response = await axios.post("/student_profile_update", body, config);
                    if (response.data == "Ok") {
                        alert("Profile updated successfully");
                        location.reload();
                    }
                    
                        }
                        catch (error) {
                            alert("Could not save student profile")
                        }
    })
    