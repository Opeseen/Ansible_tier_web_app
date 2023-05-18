const express = require('express');
const bodyParser = require('body-parser');
const handlers = require('./lib/handlers');
app = express();
// const {postUser,loginUser} = require('./model/userModel')

app.use(bodyParser.urlencoded({
  extended: true
}));

app.use(express.json())

app.use(bodyParser.json());

PORT = 3000;

app.use(express.static(__dirname + '/public'))

app.get('/', (req, res) => {
  handlers.index((statusCode,finalOutput) => {
    res.status(statusCode).send(finalOutput);
  });
});

app.get('/create-user', (req, res) => {
  handlers.createUser((statusCode,finalOutput) => {
    res.status(statusCode).send(finalOutput);
  });
});

app.get('/login-user', (req, res) => {
  handlers.loginUser((statusCode,finalOutput) => {
    res.status(statusCode).send(finalOutput);
  });
});

// app.post('/users',postUser);

// app.get('/login',loginUser);



app.listen(PORT, () => {
  console.log('App is listening on Port:',PORT);
});

