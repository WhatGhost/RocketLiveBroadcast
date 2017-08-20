# ChatArea
## props
### ```httpServer```
用于与 socket.io 服务器进行数据通信

### ```roomInfo```
Object  
含有 roomId

### ```userInfo```
Object  
含有 user 的 nickname

## component
### ```ChatItem```
通过 ```v-for``` 语法渲染，详见 [ChatItem](ChatItem.vue.md) 组件

### ```BannedItem```
自定义组件，用于展示被单独禁言的学生，详见 [BannedItem](BannedList.vue.md)

## data
### ```messageList```
Object Array  
每个对象分别含有 message, nickname, room id, highlight，分别代表消息内容、发送者昵称、房间号、是否高亮。房间号用于服务端的消息配送。该数组用于 chatItem 的渲染

### ```emojis``` 😄
String Array
用于 emoji 表情

## function
### ```sendMessage```
发送消息，并将当前消息推入消息队列 ```messageList```