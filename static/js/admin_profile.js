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
           
        var data = {
            first_name, last_name
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
                    var response = await axios.post("/admin_profile_update", body, config);
                    if (response.data == "Ok") {
                        alert("Profile updated successfully");
                        location.reload();
                    }
                    
                        }
                        catch (error) {
                            alert("Could not save profile")
                        }
    })
    