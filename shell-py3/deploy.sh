echo 'Make migrations'
python3 manage.py makemigrations

echo 'migrate'
python3 manage.py migrate
echo 'Migrate done...'

echo 'Running npm build'
npm run build
echo 'Done...'

echo 'Format index.html as Jinja template'
python3 format_index_html.py
echo 'Done...'

echo 'Collect static'
python3 manage.py collectstatic --noinput
echo 'Done...'

export PORT=8000
echo 'Server runnning on port ' $PORT
python3 manage.py runserver
