var app = require('express')()
var http = require('http').Server(app)
var io = require('socket.io')(http)

io.on('connection', function (socket) {
    console.log('新连接已创建 !')
    socket.on('init', function(obj) {
        console.log('enter' + obj.roomId)
        socket.join(obj.roomId)
    })
    socket.on('message', function(obj) {
        this.to(obj.roomId).emit('message', obj)
    })
})

http.listen(3000, function () {
    console.log('监听端口:3000')
})
