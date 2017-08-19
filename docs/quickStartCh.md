# 快速上手
## 设置数据库
 - 首先，安装包依赖：  

     ```bash
. ./init.sh
```
 - 虚拟环境报错  
 如果你在执行时遇到错误，可能是因为python的问题，这种情况下不需要使用虚拟环境，请更换执行的shell文件：

     ```bash
. ./shell-py3/init.sh
```

 - 配置settings文件  
修改你的django配置的setting.py文件：将密码设置为你的mysql的密码。  
不过，你也可以直接将数据库的密码改为"root"：

     ```sql
mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('root');
```
 - 创建数据库  
 启动数据库　```mysql -u root -p```，执行：
 
     ```sql
create database live default character set utf8 collate utf8_unicode_ci; 
```

## 配置视频服务器
 - 找到 node_moudles/easyrtc/api 目录里的文件 ```easyrtc.js```和 ```easyrtc_int.js``` , 打开并搜索 **"serverPath"**   
 修改
```javascript
var serverPath = null
```
为
```javascript
var serverPath = 'http://localhost:8080;'
```
，修改
```javascript
serverPath = socketUrl;
```
为
```javascript
serverPath  = 'http://localhost:8080;'
```
 **如果你更改了你的视频服务器端口，请一同更改以上的端口**  

 完成上述步骤后，你还需要运行以下命令以启动服务器
```bash
node node_modules/easyrtc/server_example/server.js 
```
这个命令将启动一个位于8000端口的服务

## 运行其他服务器
 - 你还需要运行最后一个服务器：
 ```bash
 node server/server.js
 ```
 这个服务器将在3000端口运行
 
## 打开网页
 - 现在，如果一切顺利的话，你应该可以通过以下网址来访问网站
```
http://localhost:8000
```

## 其他问题{docsify-ignore}
老哥你自己看着办吧，好伐？