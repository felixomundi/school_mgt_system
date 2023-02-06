const express = require('express');
  
const app = express();
const PORT = 3000;
  
app.listen(PORT, (error) =>{
    if(!error)
        console.log("Server is Successfully Running, and App is listening on port "+ PORT)
    else 
        console.log("Error occurred, server can't start", error);
    }
);

const ngrok = require('ngrok');
(async function() {
    const url = await ngrok.connect(
        {
            proto: 'http', // http|tcp|tls, defaults to http
            addr: 8000, // port or network address, defaults to 80
            authtoken: '2KDznS6M2OIUiVCOmpz69kG19Hx_4adr25MU4ps6PYpXt8VkA',
          }
    );
    console.log("url", url)
})();