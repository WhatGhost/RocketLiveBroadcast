var app = require('express')()
var http = require('http').Server(app)
var io = require('socket.io')(http)

let ROOMDATA = {}

io.on('connection', function (socket) {
    console.log('新连接已创建 !')
    socket.on('init', function(obj) {
        console.log('enter' + obj.roomId)
        socket.join(obj.roomId)
        if (!ROOMDATA.hasOwnProperty(obj.roomId)) {
            ROOMDATA[obj.roomId] = {
                page: 1,
                code: '',
                showingComponent: 'codeEditor'
            }
        }
    })
    socket.on('message', function(obj) {
        this.to(obj.roomId).emit('message', obj)
    })
    socket.on('changePage', function(obj) {
        this.to(obj.roomId).emit('changePage', obj)
        ROOMDATA[obj.roomId].page = obj.page
    })
    socket.on('changeCode', function(obj) {
        this.to(obj.roomId).emit('changeCode', obj)
        ROOMDATA[obj.roomId].code = obj.code
    })
    socket.on('switchPane', function(obj) {
        this.to(obj.roomId).emit('switchPane', obj)
        ROOMDATA[obj.roomId].showingComponent = obj.showingComponent
    })
    socket.on('getCurrentData', function(obj) {
        io.in(socket.id).emit('switchPane', ROOMDATA[obj.roomId])
        io.in(socket.id).emit('changePage', ROOMDATA[obj.roomId])
        io.in(socket.id).emit('changeCode', ROOMDATA[obj.roomId])
    })
})

http.listen(3000, function () {
    console.log('监听端口:3000')
})
