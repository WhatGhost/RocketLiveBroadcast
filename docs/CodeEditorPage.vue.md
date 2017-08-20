# CodeEditorPage
## props
### ```hide```
Boolean  
继承自 [LiveRoom](LiveRoom.vue.md)，与类hiding动态绑定。当该值为真是隐藏，反之显示。用于接受控制，使得LiveRoom界面同一时刻只有一个组件显示（另见 [PdfViewer](PdfViewer.vue.md), [WhiteboardPage](WhiteboardPage.vue.md)）

### ```httpServer```
用于与socket.io服务器进行数据通信

## data
### ```code```
当前代码编辑器的内容，与代码编辑器组件动态绑定

### ```syncCode```
用于代码的缓冲，防止出现同步的死循环

### ```editorOptions```
json  
代码编辑器的设置项，与代码编辑器 ```option``` 属性动态绑定

## component
### ```CodeMirror```
第三方组件 [CodeMirror](https://codemirror.net/)

## function
### ```emitCodeChange```
由代码编辑器的内容改变事件触发，首先判断当前代码内容与缓冲驱的内容是否相同，若相同则返回以避免死循环；若不同则向sockIO服务器提交同步请求

### ```created```
hook  
vue 生命周期钩子函数，在页面组件加载时触发，此处进行：
- 根据用户身份变更代码编辑器的只读属性，非房间创建者不能进行代码编辑
- 定义匿名函数，该匿名函数用于使缓冲 syncCode 和 code 均与 socket.io 消息内容一致；绑定该匿名函数到 socket.io 接收消息的钩子函数