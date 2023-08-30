Сервис для создания и отправления рассылок "MAS".
Возможности сервиса:
- Создание клиентов, которым будут отправляться рассылки.
- Создание рассылок, которые содержат сообщения для отправки клиентам.
- Ведение блога (создание блога).

Как запустить сервис:
1.1. Открыть Ubuntu и выполнить "curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
".
1.2. Выполнить "sudo apt-get update".
1.3. Выполнить "sudo apt-get install redis".
1.4. Выполнить "sudo service redis-server start".

2.1. В терминале выполнить "python manage.py runserver" и перейти по ссылке.