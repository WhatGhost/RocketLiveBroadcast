## Visit [online docs](https://wangleto.github.io/Rocket.github.io/#/)

# Quick start - English

**1. Set Your Database And Start**

Whatever, here are tips to get your Django connect with database.

- **venv ERROR**  
If within the venv you meet errors, just run shells inside the ```shell-py3``` folder or use ```python3 [commands]``` instead.
- **First, install the requirements** ( **PyMySQL** new added)
```bash
. ./init.sh
```
or run ```. ./shell-py3/init.sh```

- **Second, config your settings file.**  
Modify the password as yours in settings.py.  
However, I suggest just modify your database password as follow:
```sql
mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('root');
```
The *password "root" is written in the settings.py* , no need to change it everytime.

- **Finally Create Database**  
Start your mysql or MariaDB, 
```sql
create database live default character set utf8 collate utf8_unicode_ci; 
```

**2. View the doc page Locally**
 - You need to run this command to start a server for doc visiting:
 
  ```bash
  docsify serve ./docs
  ```
 then visit all the doc web pages at:
 ```
 http://localhost:3000
 ```

**3. Config the video server**
 - find file ```easyrtc.js```and ```easyrtc_int.js```in ./node_moudles/easyrtc/api , then open them and search **serverPath** in them 
then replace 
```javascript
var serverPath = null
```
to
```javascript
var serverPath = 'http://localhost:8080;'
```
and
replace
```javascript
serverPath = socketUrl;
```
to
```javascript
serverPath  = 'http://localhost:8080;'
```
 **if you change the port in video server , you need to change the above code too**  

 After doing that above , you need to run the server before you visit the website
you need to run
```bash
node node_modules/easyrtc/server_example/server.js 
```
This command will open a server on port 8080

**4. another server**
 - you only need another server to run：
 ```bash
 node server/server.js
 ```
 this server is on port 3000
 
**5. open the webpage**  
 - Now, if everything well, you can visit this webpage:
```
http://localhost:8000
```

# 快速上手 - 中文
**1. 设置数据库与其他**
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

**2. 访问文档网页**
 - 在bash中运行以下命令以启动文档网站:
 
  ```bash
  docsify serve ./docs
  ```
 让后访问以下网址来查看全部文档
 ```
 http://localhost:3000
 ```

**3. 配置视频服务器**  
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

**4. 运行其他服务器**
 - 你还需要运行最后一个服务器：
 ```bash
 node server/server.js
 ```
 这个服务器将在3000端口运行
 
**5. 打开网页**  
 - 现在，如果一切顺利的话，你应该可以通过以下网址来访问网站
```
http://localhost:8000
```