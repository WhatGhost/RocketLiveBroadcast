# App.vue
## component
### ```nav-header```
导航条

### ```router-view```
用于vue-router进行页面切换的组件

## function
### ```changePage```
在房间内时，通过点击事件中的```$emit('goto')```触发changePage，跳转到主页。导航条作为bus

### ```doShowDialog```
导航条上的多个按钮均可触发，通过点击事件中的```$emit('show')```。由于携带参数，可以指定显示的模态窗口
