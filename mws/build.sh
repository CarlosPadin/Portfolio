

# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collestatic --no-input
python manage.py migrate