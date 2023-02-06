var button = document.getElementById("fetch-student");
button.addEventListener("click", async function (e) {
    e.preventDefault()
    var unit = document.getElementById("unit").value;
    var session = document.getElementById("session").value;
    // console.log("unit", unit)
    
    var body = JSON.stringify({ "unit": unit, "session": session });
     console.log("body",body)
        // var config = {
        //     headers: {
        //         'Content-Type': 'application/json',               
        //         mode:'same-origin'
        //     }
        // };
    try {
        var url = "get_students";
        const response = await axios.post(url,
            // config,
            body);
        console.log(response);
    } catch (error) {
        console.log(error)
    }
})

// const FetchStudent = async() => {
//     var unit = document.getElementById("unit").value;
//     var session = document.getElementById("session").value;
    
//     var body = JSON.stringify({ "unit":unit, "session":session });
//         var config = {
//             headers: {
//                 'Content-Type': 'application/json',               
//                 mode:'same-origin'
//             }
//         };
//     try {
//         var url = "get_students";
//         const response = await axios.post(url, config, body);
//         console.log(response);
//     } catch (error) {
        
//     }
// }