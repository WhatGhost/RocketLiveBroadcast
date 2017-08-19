# Room
## props
### ```room```
一个房间的详细信息，包括room_img, id, room_creater.nickname, room_name, room_introduction，分别为房间封面、房间id、房间创建者昵称、房间名称、房间简介

## data
### ```currentDate```
当前时间，暂未使用

## function
### ```enterRoom```
由vue-router进行路由，打开所点击的房间。包含身份验证，当以游客身份访问时会遭到拒绝