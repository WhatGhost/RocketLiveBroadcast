# RoomList
## component
### ```Room```
自定义组件，使用v-for进行渲染，详见 [Room](Room.vue.md) 组件

## function
### ```rooms```
从vuex的store中获取的全部房间的列表

## CSS
### ```blur```
有高斯模糊效果的类，由store中的background_blur动态绑定。为真值时，全部房间列表出现高斯模糊效果，用于弹窗出现时的背景虚化