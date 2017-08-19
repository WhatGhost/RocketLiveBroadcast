# NavHeader
## CSS
### ```blur```
参见 [RoomList](RoomList.vue.md) 中的 ```blur```

### ```isTeacher```
Boolean
由vuex store中的isTeacher决定，控制导航栏中的“创建房间”按钮显示

## component
### ```RegisterModalDialog```
自定义组件，点击注册按钮时弹出，参见 [RegisterModalDialog](RegisterModalDialog.vue.md)

### ```LoginModalDialog```
自定义组件，点击登录按钮时弹出，参见  [LoginModalDialog](LoginModalDialog.vue.md)

### ```InfoModalDialog```
自定义组件，点击个人昵称按钮时弹出，参见 [InfoModalDialog](InfoModalDialog.vue.md)

### ```ForgetModalDialog```
自定义组件，在登录弹窗中点击“找回密码”按钮时弹出，参见  [ForgetModalDialog](ForgetModalDialog.vue.md)

### ```CreateRoomModalDialog```
自定义组件，经授权的教师用户点击创建房间按钮时弹出，参见  [CreateRoomModalDialog](CreateRoomDialog.vue.md)

## function
### ```logout```
向服务器发送退出登录的请求

### ```showRoomList```
重新获取房间列表，并由vue router路由至房间列表主页

