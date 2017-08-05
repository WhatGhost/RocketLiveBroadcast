# Live Video Boardcast

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

### New

**1. Set Your Database**

It seems great changes needed for the project, so the ```init.sh``` and ```deploy.sh``` may be not used anymore.

Whatever, here are tips to get your Django connect with database.

- No more need venv  
Some errors will happen when you config database within the venv, just use
```python3 [commands]``` instead.
- First, install the **PyMySQL**

```
pip3 install PyMySQL
```
- Second, config your settings file. Modify the password as yours.  
However, I suggest just modify your database password as follow:

```
mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('root');
```
The password "root" is written in the settings.py, no need to change it everytime.

**2. Install Requirements**

Updated requirments.txt, but this time run this:

```
pip3 install -r requirments.txt
```
No need to run venv.

**3. Common Commands**

Don't recommend using shell anymore, just run these commands:

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
```
//only frontend, but hot-loaded
npm run dev
```