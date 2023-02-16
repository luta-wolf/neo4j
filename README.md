1) Установка brew
	brew.sh

2) Установка СУБД neo4j
	brew install neo4j

3) изменить название бд в файле `neo4j.conf`
При запуске neo4j пишется где находится конфиг файл
# The name of the default database
initial.dbms.default_database=neo4j


4) запускаем конфиг файл
neo4j-admin server migrate-configuration

5)
neo4j-admin dbms set-initial-password <password>

6) создаем миграции
python manage.py install_labels

7)
neo4j start - запуск бд

neo4j stop - остановка бд

8) по этому адресу смотрим бд
http://localhost:7474




