1) Установка brew
	brew.sh

2) Установка СУБД neo4j
	brew install neo4j

3)
neo4j-admin server migrate-configuration

4)
neo4j start
neo4j stop

5)
neo4j-admin dbms set-initial-password <password>


6) изменить название бд в файле `neo4j.conf`
# The name of the default database
initial.dbms.default_database=neo4j
