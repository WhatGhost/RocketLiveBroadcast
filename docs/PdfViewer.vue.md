# PdfViewer
## props
### ```hide```
Boolean  
继承自 [LiveRoom](LiveRoom.vue.md)，与类hiding动态绑定。当该值为真是隐藏，反之显示。用于接受控制，使得LiveRoom界面同一时刻只有一个组件显示（另见 [CodeEditorPage](CodeEditorPage.vue.md), [WhiteboardPage](WhiteboardPage.vue.md)）

### ```httpServer```
用于与 socket.io 服务器进行数据通信

## data
### ```loadingItem```
element的loading组件服务的实例，获得该实例后可以通过
```JavaScript
loadingItem.close()
```
的方式关闭 loading 组件的显示

### ```pdfSource```
String    
与pdf组件的 src 绑定，被服务器资源URL的赋值

## component
### ```pdf```
组件 [vue-pdf](https://www.npmjs.com/package/vue-pdf)

### ```loading```
由 element UI 提供的加载效果组件，此处没有直接使用组件，而是使用了引入后注册在系统中的服务

### ```el-upload```
element UI库中的上传组件，含有回调函数，可以自定义上传目标、可选文件类型、是否支持拖拽等

## function
### ```created```
hook  
vue 的生命周期函数，发生在进入房间时，组件未完全装载(?)
```
this.getPdf()
```
向服务器请求PDF资源
```
this.httpServer.on('changePage', (obj) => {
	this.page = obj.page
})
```
通过 socket.io 服务器进行左侧面板同步

### ```emitPageChange```
教师向 socket.io 服务器发出左侧面板切换的请求，学生端将同步

### ```showErrorMes```
简单封装了 element UI 组件库中的message服务

### ```uploadSuccess```
教师端完成上传后的回调函数，启动 loading 组件，并向服务器发出进行格式转换的请求

### ```getPdf```
从服务器请求PDF资源的操作，发生在进入房间时或教师端获知服务器完成文档转换后