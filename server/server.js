'use strict'
const app = require('express')()
const http = require('http').Server(app)
const io = require('socket.io')(http)

let ROOMDATA = {}
let SOCKETINFO = {}
let sysMessageTemplate = {
    content: '',
    userInfo: {
        nickname: '系统消息',
        isRoomCreator: true,
        account: '',
        isTeacher: true
    },
    roomId: null,
    status: 403
}

const findUser = (users, userToFind) => {
    for (let i = 0; i < users.length; i = i + 1) {
        if (users[i].account === userToFind.account) {
            return i
        }
    }
    return -1
}

const initRoom = (roomId) => {
    ROOMDATA[roomId] = {
        page: 1,
        code: '',
        showingComponent: 'codeEditor',
        bannedUsers: [],
        kickedoutUsers: [],
        allBanned: false,
        drawing: null,
        users: []
    }
}

const kickoutUser = (roomId, user, message) => {
    let userIndex = findUser(ROOMDATA[roomId].users, user)
    // 倒序踢出 防止奇怪的事情发生
    for (let i = ROOMDATA[roomId].users[userIndex].socketIds.length - 1; i >= 0; i = i - 1) {
        io.in(ROOMDATA[roomId].users[userIndex].socketIds[i]).emit('kickout', message)
    }
}

const addUser = (roomId, user, socketId) => {
    let userIndex = findUser(ROOMDATA[roomId].users, user)
    if (userIndex === -1) {
        user.socketIds = []
        user.socketIds.push(socketId)
        ROOMDATA[roomId].users.push(user)
    } else {
        // 一般来讲socketid是不会重复的
        ROOMDATA[roomId].users[userIndex].socketIds.push(socketId)
    }
}

io.on('connection', function (socket) {
    console.log('新连接已创建 !')

    socket.on('init', function (obj) {
        console.log(socket.id + ' ' + obj.userInfo.account + ' enter room ' + obj.roomId)
        socket.join(obj.roomId)
        if (!ROOMDATA.hasOwnProperty(obj.roomId)) {
            initRoom(obj.roomId)
        }
        addUser(obj.roomId, obj.userInfo, socket.id)
        SOCKETINFO[socket.id] = {
            roomId: obj.roomId,
            userInfo: obj.userInfo
        }
        if (findUser(ROOMDATA[obj.roomId].kickedoutUsers, obj.userInfo) !== -1) {
            kickoutUser(obj.roomId, obj.userInfo, '您已被踢出')
            return
        }
        io.in(obj.roomId).emit('userCountChange', ROOMDATA[obj.roomId].users.length)
    })

    socket.on('disconnect', function () {
        let socketInfo = SOCKETINFO[socket.id]
        if (!socketInfo) {
            return
        }
        let userIndex = findUser(ROOMDATA[socketInfo.roomId].users, socketInfo.userInfo)
        if (userIndex !== -1) {
            let socketIndex = ROOMDATA[socketInfo.roomId].users[userIndex].socketIds.indexOf(socket.id)
            if (socketIndex !== -1) {
                // remove socketId from socketIds
                ROOMDATA[socketInfo.roomId].users[userIndex].socketIds.splice(socketIndex, 1)
                if (ROOMDATA[socketInfo.roomId].users[userIndex].socketIds.length === 0) {
                    // remove user if there is no socket for him
                    ROOMDATA[socketInfo.roomId].users.splice(userIndex, 1)
                    if (socketInfo.userInfo.isRoomCreator) {
                        socket.to(socketInfo.roomId).emit('kickout', '教师已停止直播')
                    }
                }
            }
        }
        io.in(socketInfo.roomId).emit('userCountChange', ROOMDATA[socketInfo.roomId].users.length)
    })

    socket.on('message', function (obj) {
        if (obj.userInfo.isRoomCreator) {
            io.in(obj.roomId).emit('message', obj)
        } else if (ROOMDATA[obj.roomId].allBanned) {
            let bannedMessage = sysMessageTemplate
            bannedMessage.content = '当前处于全局禁言'
            bannedMessage.roomId = obj.roomId
            io.in(socket.id).emit('message', bannedMessage)
        } else if (findUser(ROOMDATA[obj.roomId].bannedUsers, obj.userInfo) !== -1) {
            let bannedMessage = sysMessageTemplate
            bannedMessage.content = '您已被禁言'
            bannedMessage.roomId = obj.roomId
            io.in(socket.id).emit('message', bannedMessage)
        } else {
            io.in(obj.roomId).emit('message', obj)
        }
    })

    socket.on('changePage', function (obj) {
        this.to(obj.roomId).emit('changePage', obj)
        ROOMDATA[obj.roomId].page = obj.page
    })

    socket.on('changeCode', function (obj) {
        this.to(obj.roomId).emit('changeCode', obj)
        ROOMDATA[obj.roomId].code = obj.code
    })

    socket.on('switchPane', function (obj) {
        this.to(obj.roomId).emit('switchPane', obj)
        ROOMDATA[obj.roomId].showingComponent = obj.showingComponent
    })

    socket.on('ban', function (obj) {
        if (findUser(ROOMDATA[obj.roomId].bannedUsers, obj.userInfo) === -1) {
            ROOMDATA[obj.roomId].bannedUsers.push(obj.userInfo)
            let bannedMessage = sysMessageTemplate
            bannedMessage.content = '用户' + obj.userInfo.nickname + '已被房主禁言'
            bannedMessage.roomId = obj.roomId
            io.in(obj.roomId).emit('message', bannedMessage)
        } else {
            let bannedMessage = sysMessageTemplate
            bannedMessage.content = '用户' + obj.userInfo.nickname + '已被您禁言'
            bannedMessage.roomId = obj.roomId
            io.in(socket.id).emit('message', bannedMessage)
        }
        io.in(socket.id).emit('getBannedList', ROOMDATA[obj.roomId].bannedUsers)
    })

    socket.on('unban', function (obj) {
        let i = findUser(ROOMDATA[obj.roomId].bannedUsers, obj.userInfo)
        if (i !== -1) {
            ROOMDATA[obj.roomId].bannedUsers.splice(i, 1)
            let bannedMessage = sysMessageTemplate
            bannedMessage.content = '用户' + obj.userInfo.nickname + '已被房主解除禁言'
            bannedMessage.roomId = obj.roomId
            io.in(obj.roomId).emit('message', bannedMessage)
        } else {
            let bannedMessage = sysMessageTemplate
            bannedMessage.content = '用户' + obj.userInfo.nickname + '未被禁言'
            bannedMessage.roomId = obj.roomId
            io.in(socket.id).emit('message', bannedMessage)
        }
        io.in(socket.id).emit('getBannedList', ROOMDATA[obj.roomId].bannedUsers)
    })

    socket.on('kickout', function (obj) {
        let i = findUser(ROOMDATA[obj.roomId].users, obj.userInfo)
        if (i !== -1) {
            kickoutUser(obj.roomId, obj.userInfo, '您已被踢出')
            ROOMDATA[obj.roomId].kickedoutUsers.push(obj.userInfo)
            let kickoutMessage = sysMessageTemplate
            kickoutMessage.content = '用户' + obj.userInfo.nickname + '已被房主踢出'
            kickoutMessage.roomId = obj.roomId
            io.in(obj.roomId).emit('message', kickoutMessage)
        } else {
            let kickoutMessage = sysMessageTemplate
            kickoutMessage.content = '用户' + obj.userInfo.nickname + '不在房间内'
            kickoutMessage.roomId = obj.roomId
            io.in(socket.id).emit('message', kickoutMessage)
        }
        io.in(socket.id).emit('getBannedList', ROOMDATA[obj.roomId].bannedUsers)
    })

    socket.on('getBannedList', function (obj) {
        io.in(socket.id).emit('getBannedList', ROOMDATA[obj.roomId].bannedUsers)
    })

    socket.on('banAll', function (obj) {
        if (!ROOMDATA[obj.roomId].allBanned) {
            ROOMDATA[obj.roomId].allBanned = true
            let bannedMessage = sysMessageTemplate
            bannedMessage.content = '房主已开启全体禁言'
            bannedMessage.roomId = obj.roomId
            io.in(obj.roomId).emit('message', bannedMessage)
        } else {
            let bannedMessage = sysMessageTemplate
            bannedMessage.content = '全体禁言已开启'
            bannedMessage.roomId = obj.roomId
            io.in(socket.id).emit('message', bannedMessage)
        }
        io.in(socket.id).emit('getBannedStatus', ROOMDATA[obj.roomId].allBanned)
    })

    socket.on('unbanAll', function (obj) {
        if (ROOMDATA[obj.roomId].allBanned) {
            ROOMDATA[obj.roomId].allBanned = false
            let bannedMessage = sysMessageTemplate
            bannedMessage.content = '房主已解除全体禁言'
            bannedMessage.roomId = obj.roomId
            io.in(obj.roomId).emit('message', bannedMessage)
        } else {
            let bannedMessage = sysMessageTemplate
            bannedMessage.content = '全体禁言未开启'
            bannedMessage.roomId = obj.roomId
            io.in(socket.id).emit('message', bannedMessage)
        }
        io.in(socket.id).emit('getBannedStatus', ROOMDATA[obj.roomId].allBanned)
    })

    socket.on('changeDrawing', function (obj) {
        this.to(obj.roomId).emit('changeDrawing', obj)
        ROOMDATA[obj.roomId].drawing = obj.drawing
    })

    socket.on('getCurrentData', function (obj) {
        io.in(socket.id).emit('changeCode', ROOMDATA[obj.roomId])
        io.in(socket.id).emit('changePage', ROOMDATA[obj.roomId])
        io.in(socket.id).emit('switchPane', ROOMDATA[obj.roomId])
        io.in(socket.id).emit('changeDrawing', ROOMDATA[obj.roomId])
    })
})

http.listen(3000, function () {
    console.log('监听端口:3000')
})
