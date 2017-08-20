# WhiteboardPage
## props
### ```hide```
Boolean  
继承自 [LiveRoom](LiveRoom.vue.md)，与类 hiding 动态绑定。当该值为真是隐藏，反之显示。用于接受控制，使得 LiveRoom 界面同一时刻只有一个组件显示（另见 [CodeEditorPage](CodeEditorPage.vue.md), [PdfViewerPage](PdfViewerPage.vue.md)）

### ```httpServer```
用于与 socket.io 服务器进行数据通信

## component
### ```literallyCanvas```
使用了开源项目 [literallyCanvas](http://literallycanvas.com/)

## data
### ```lc```
用于绑定白板对象

### ```drawing```
JSON 对象，用于暂存白板同步的内容。

## function
### ```created```
hook  
vue 的生命周期函数，发生在进入房间时，组件未完全装载。监听“changeDrawing”消息。如果画板未初始化，接收到的内容会被暂存至 drawing 中。如果画板已初始化，则会调用lc对应函数加载画板内容。

### ```updated```
hook
vue 的生命周期函数。发生在数据引起 DOM 更新时。此时若 lc 未加载，则会加载画板，并加载画板内容

### ```mountlc```
用于加载画板，并添加画板更改监听

### ```emitDrawingChange```
向 socket.io 服务器提交画板的状态
