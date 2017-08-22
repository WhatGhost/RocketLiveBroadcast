# Quick Start

## Set Your Database And Start

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

## start a server
 - you only need another server to run：
 ```bash
 node server/server.js
 ```
 this server is on port 3000
 
## open the webpage
 - Now, if everything well, you can visit this webpage:
```
http://localhost:8000
```