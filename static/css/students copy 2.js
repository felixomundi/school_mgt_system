var button = document.getElementById("fetch-student");
button.addEventListener("click", async function (e) {
    e.preventDefault()
    try {
        
    var unit = document.getElementById("unit").value;
    var session = document.getElementById("session").value;
    var unitElement = document.getElementById("unit-error");
    var sessionElement = document.getElementById("session-error");
    let error = ""
    if (!unit) {
        error = "Choose a unit"
        unitElement.innerHTML += error 
     return false   
    } else if (!session) {
        error = "Fill all fields"
        sessionElement.innerHTML += error;
        return false;
    } else {
        document.classList()
        var body = JSON.stringify({ "unit": unit, "session": session });
        var url = "get_students";
            const response = await axios.post(url, body);
    }
} catch (error) {
        console.log(error)
}

    // var body = JSON.stringify({ "unit": unit, "session": session });
    
    // try {
    //     var url = "get_students";
    //     const response = await axios.post(url,
           
    //         body);
    //     console.log(response);
    // } catch (error) {
    //     console.log(error)
    // }
   
    
    
})
