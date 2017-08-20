# CreateRoomDialog
## data
### ```apiRoot```
web address  
常量，指定api.js与服务器进行通信的地址；跟随服务器ip地址更改
### ```ImagePage```
const  
常量0，指定当前在弹窗的第一页，需要上传图片
### ```FormPage```
const  
常量1，指定当前在弹窗的第二页，需要填写房间介绍
### ```IdPage```
const  
常量2，指定当前在弹窗的第三页，获取分配到的房间id
### ```myCroppa```
组件vue-croppa的句柄，通过v-modal双向绑定
### ```nowView```
指定当前在弹窗的哪一页面
### ```step```
指定步骤条的进度，始终与nowView一致；最后一页在获得服务器分配的ID后进度再次加一
### ```choosedImg```
选择的图片，图片以base64编码形成的字符串
### ```roomId```
创建房间的ID，成功的情况下将为正值
### ```openFail```
创建房间失败，在该值为 false 的情况下，服务器未明确返回失败的消息，用户将在第三页看到“waiting”等字样；当服务器发回错误消息时，该值控制页面显示“fail”等字样。另外当 roomId 为正值时，将忽略该值，直接显示创建成功的信息

## component
### ```croppa```
来自于 [vue-croppa](https://www.npmjs.com/package/vue-croppa)，用于图片裁剪的组件，将所裁剪图片转化为以base64编码的字符串
### ```el-steps```
[element UI](http://element.eleme.io/#/zh-CN/component/tabs)所提供的步骤条组件

## function
### ```closeDialog```
关闭当前弹窗，由 vuex 实现；关闭时清空当前组件的各状态量

### ```checkFormInput```
检查房间名称和房间简介的填写，如果未填写房间名称将无法向下进行；如未填写房间简介，将自动赋值为“暂无描述”

### ```nextBtnFun```
按钮next点击后触发该方法，控制页面后翻。当位于表单结束的第二页时，触发提交表单的操作。

### ```createBtnClick```
表单提交前的操作，将表单中的值加入 formData，然后调用 API 进行 post 操作。

### ```generateImage```
在第一页点击 next 按钮时，将裁剪得到的值赋值给表单需要提交的变量。同时检查该值，若为空则说明未上传图片，拒绝继续操作。