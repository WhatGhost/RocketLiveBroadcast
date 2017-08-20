# LiveRoom
## component
### ```WhiteboardPage```
自定义组件，参见 [WhiteboardPage](WhiteboardPage.vue.md)

### ```CodeEditorPage```
自定义组件，参见 [CodeEditorPage](CodeEditorPage.vue.md)

### ```RecordVideo```
自定义组件，参见 [RecordVideo](RecordVideo.vue.md)

### ```ChatArea```
自定义组件，参见 [ChatArea](ChatArea.vue.md)

### ```PdfViewer```
自定义组件，参见 [PdfViewer](PdfViewer.vue.md)

### ```io```
引入 ```socket.io``` 模块，用于 ```httpServer``` 连接 socket.io 服务器，参见 [GitHub socket.io](https://github.com/socket.io/socket.io)

### ```RecordRTC```
开源项目 [RecordRTC](https://github.com/muaz-khan/RecordRTC)

## data
### ```isRecordingStarted```
Boolean  
记录录像是否开始

### ```isStoppedRecording```
Boolean  
记录录像是否已经停止

### ```canvas2d```
一个 canvas 对象，用于截屏，以实现录像

### ```recorder```
RecordRTC 对象，用于录像

### ```context```
用于获取 canvas 内容

### ```elementToShare```
用于标记要记录的区域

### ```showingComponent```
String  
用于计算当前左侧显示的组件

## function
### ```hidePdfViewer```
与 PdfViewer 的 hide 类属性动态绑定，返回值确定是否隐藏PdfViewer

### ```hideCodeEditor```
与 CodeEditor 的 hide 类属性动态绑定，返回值确定是否隐藏 CodeEditor

### ```hideWhiteBoard```
与 WhiteBoard 的 hide 类属性动态绑定，返回值确定是否隐藏 WhiteBoard

### ```roomMessage```
显示当前房间的信息，包括房间名、房间 id、教师名

### ```created```
hook
vue的生命周期钩子，在组件加载完成之前，调用 ```getRoomInfo```, ```getUserInfo```获取房间与用户信息；调用 ```connect``` 方法，与 socket.io 服务器建立连接，并绑定相关函数

### ```connect```
与 socket.io 建立联系的函数，在用户进入房间时触发。
向 socket.io 服务器发送 ```init``` 消息，传递用户进入房间的消息。  
进行匿名函数的定义与相关的事件绑定，包括控制面板切换的 ```switchPane```。

### ```appendCanvas```
waiting......

### ```getRoomInfo```
从 vuex store 中获取当前用户的信息

### ```switchPane```
切换左侧多功能面板

### ```startRecord```
用于开始录播

### ```stopRecord```
用于结束录播

### ```looper```
用于监听录像事件