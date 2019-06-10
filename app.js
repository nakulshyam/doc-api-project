const express = require('express');
const app = express();

app.get('/', function(req, res) {
     res.send('This is the root route');
});

app.listen(8080, function() {
     console.log('Server started on localhost:8080');
});


