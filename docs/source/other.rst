其他 API
========

class **CsrfExemptSessionAuthentication(SessionAuthentication)**

继承自RestFrameWork的SessionAuthentication，重写其ensure\_csrf函数，用以解决跨域访问的问题，在需要跨域访问的viewset中，用\ ``authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)``\ 语句来指定登录类
