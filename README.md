# learning_site
## Для запуска приложения выполните следующие действия:


в settings.py заполнить свои конфиги DATABASES


```bash
pip install -r req.txt
```
```bash
cd educationit
```
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
python manage.py create_admin (login: admin, pass:admin)
```
```bash
python manage.py runserver
```

## Было добавлено:
1) Консольная команда "create_admin" для создания суперпользователя
2) Теперь можно запустить базу postgresql в докере командой
```bash
docker compose up -d
```