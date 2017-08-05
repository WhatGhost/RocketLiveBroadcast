echo 'Init venv'
python3 -m venv ./.venv
echo 'Init venv done...'

echo 'Start venv'
source ./.venv/bin/activate
echo 'Start venv done...'

echo 'Install python modules'
pip install -r requirements.txt
echo 'Install done...'

echo 'Run npm install'
npm install
echo 'Npm isntall done'