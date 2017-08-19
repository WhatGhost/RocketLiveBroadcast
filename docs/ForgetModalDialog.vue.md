# ForgetModalDialog
自定义组件，注册弹窗，当未登录用户点击导航栏“注册”按钮时弹出。参考组件：  
[RegisterModalDialog](RegisterModalDialog.vue.md)  
[LoginModalDialog](LoginModalDialog.vue.md) 

## function
### ```closeDialog```
关闭注册弹窗，由vuex完成控制

### ```isRightPhoneNum```
检查是否是格式正确的手机号

### ```isRightEmail```
检查是否是格式正确的电子邮箱

### ```isPassword```
检查是否是规定格式的密码，即8至20位的数字、字母和下划线组合

### ```checkInput```
分别检查账号格式是否正确、昵称是否填写、两次密码是否一致、密码格式是否符合规定、是否填写验证码，如果不符合条件则发出错误反馈

### ```changePassword```
点击确认改密按钮触发，首先调用```checkInput```方法检查各项输入是否符合格式，然后将数据以json发送给服务器。其中密码在前端经过```sha256```加密