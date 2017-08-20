房间与PPT API
=============

class **LiveRoomViewSet(viewsets.ModelViewSet)**


该类继承自viewsets.ModelViewSet类，包含了房间的各种函数

**方法：**
| **create(self, request)**

-  创建房间函数,重写其自带的create函数
-  以此判断其是否登录与是否为学生，均符合条件则成功创建房间，返回房间信息，否则返回失败信息

