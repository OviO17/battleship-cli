const express = require('express');
const app = express();
const path = require('path');
const { spawn } = require('child_process');

app.use(express.static('views'));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views/index.html'));
});

const server = require('http').createServer(app);
const io = require('socket.io')(server);

io.on('connection', (socket) => {
    const python = spawn('python3', ['run.py']);

    python.stdout.on('data', (data) => {
        socket.emit('output', data.toString());
    });

    python.stderr.on('data', (data) => {
        socket.emit('output', data.toString());
    });

    socket.on('input', (data) => {
        python.stdin.write(data + '\n');
    });
});

server.listen(process.env.PORT || 3000);