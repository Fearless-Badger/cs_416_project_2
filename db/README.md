Docker MySQL container

name = cs-416-db
ROOT password = micah


run with "-p 3333:3306" so we can connect to db
expose port 3333 from container, 3306 from DB

docker run --name cs-416-db -p 3333:3306 -e MYSQL_ROOT_PASSWORD=micah -d mysql
