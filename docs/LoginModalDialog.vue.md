# LoginModalDialog
自定义组件，注册弹窗，当未登录用户点击导航栏“注册”按钮时弹出。参考组件：  
[RegisterModalDialog](RegisterModalDialog.vue.md)  
[ForgetModalDialog](ForgetModalDialog.vue.md)  

## function
### ```closeDialog```
关闭注册弹窗，由 vuex 完成控制

### ```loginButtonClick```
检查账号密码是否填写，然后向服务器发出登录请求。密码经过前端 ```sha256``` 加密