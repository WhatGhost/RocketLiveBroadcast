# Live Video Boardcast

### New

**1. Set Your Database**

Whatever, here are tips to get your Django connect with database.

- **No more venv !**  
Some errors will happen when you config database within the venv, just use
```python3 [commands]``` instead.
- First, install the **PyMySQL**

```
. ./init.sh
```
- Second, config your settings file. Modify the password as yours.  
However, I suggest just modify your database password as follow:

```
mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('root');
```
The **password "root" is written in the settings.py**, no need to change it everytime.

**2. Common Commands**

You can run this when only writing front end:

```
//no backend, but hot-loaded, port 8080
npm run dev
```

Due to lack of venv, run these commands if needed:

```
//prepare your database
pip3 install balabala
python3 manage.py makemigrations
python3 manage.py migrate
```
```
//run whole frontend server and backend server, slow
npm run build
python3 manage.py runserver
```


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
