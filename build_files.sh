python3 -m pip install -r requirements.txt
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py makemigrations --database=second_db --noinput
python3 manage.py migrate --database=second_db --noinput
python3 manage.py collectstatic --noinput --clear
