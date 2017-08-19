# ChatArea
## props
### ```httpServer```
???

### ```roomInfo```
Object  
含有roomId

### ```userInfo```
Object  
含有user的nickname

## component
### ```ChatItem```
component  
通过```v-for```语法渲染，详见 [ChatItem](ChatItem.vue.md) 组件

## data
### ```messageList```
Object Array  
每个对象分别含有message, nickname, room id, highlight，分别代表消息内容、发送者昵称、房间号、是否高亮。房间号用于服务端的消息配送。该数组用于chatItem的渲染

### ```emojis``` 😄
String Array
用于emoji表情

## function
### ```sendMessage```
发送消息，并将当前消息推入消息队列```messageList```