const express = require('express');
const ngrok = require('ngrok');
require("dotenv").config(); 
const app = express();
const PORT = 3000;
  
app.listen(PORT, (error) =>{
    if(!error)
        console.log("Server is Successfully Running, and App is listening on port "+ PORT)
    else 
        console.log("Error occurred, server can't start", error);
    }
);

(async function() {
    const url = await ngrok.connect(
        {
            proto: 'http', // http|tcp|tls, defaults to http
            addr: 8000, // port or network address, defaults to 80
            authtoken: process.env.AUTHTOKEN,
          }
    );
    console.log("url", url)
})();