# BannedList
## props
### ```roomInfo```
继承自 ChatArea，用于教师提交解禁请求时的房间区别

### ```bannedUsers```
继承自 ChatArea，用于展示被禁言用户列表

## function
### ```unban```
向 socket.io 发送请求，携带房间 id 和用户 id，解禁某个用户发言
