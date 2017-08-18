# Live Video Boardcast

### New README

**1. Set Your Database**

Whatever, here are tips to get your Django connect with database.

- **venv ERROR**  
If within the venv you meet errors, just run shells inside the ```shell-py3``` folder or use ```python3 [commands]``` instead.
- **First, install the requirements** ( **PyMySQL** new added)

```
. ./init.sh
```
or run ```. ./shell-py3/init.sh```

- **Second, config your settings file.**  
Modify the password as yours in settings.py.  
However, I suggest just modify your database password as follow:

```
mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('root');
```
The *password "root" is written in the settings.py* , no need to change it everytime.

- **Finally Create Database**  
Start your mysql or MariaDB, 

```
create database live default character set utf8 collate utf8_unicode_ci; 
```

**2. Common Commands**

You can run this when only writing front end:

```
//no backend, but hot-loaded, port 8080
npm run dev
```

For fully server run:

```
. ./deploy.sh
```
or ```. ./shell-py3/deply.sh```

If not using shell:

```
//prepare your database
pip install balabala
python manage.py makemigrations
python manage.py migrate
```
```
//run whole frontend server and backend server, slow
npm run build
python manage.py runserver
```
**3.Config the video server**
find file ```easyrtc.js```and ```easyrtc_int.js```in ./node_moudles/easyrtc/api , then open them and search **serverPath** in them 
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
```
node node_modules/easyrtc/server_example/server.js 
```
This command will open a server on port 8080
<br>
<br>
### old README
>### To init the project
After clone the project from git, use command below to init  your project:
```shell
cd Group2
. ./init.sh
```
Notice that **the first point** cannot be ignored.  
### To run the server
Then you can use this:
```shell
. ./deploy.sh
```
Similarly you should use a point at first.
