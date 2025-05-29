const express = require('express');
const axios = require('axios');
const app = express();

app.get('/', async (req, res) => {
    try {
        const response = await axios.get('http://backend-service:8080/api/message');
        res.send(`<h1>${response.data.message} AT FRONTEND</h1>`); // todo Add " AT FRONTEND" to the message
    } catch (error) {
        res.status(500).send('Error connecting to backend');
    }
});

app.listen(3000, () => {
    console.log('Frontend running on port 3000');
});