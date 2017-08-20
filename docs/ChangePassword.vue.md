# ChangePassword
## function
### ```changepasswordClick```
点击“更该密码”按钮后触发。依次检查两次新密码是否一致、新密码是否为空、是否符合密码格式要求，如果出现不符则显示相应错误信息并拒绝操作；若通过检验，通过 vuex store 向服务器发送改密请求。