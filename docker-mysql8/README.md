

## Docker

```
MYSQL_ROOT_PASSWORD= make docker-run
```


## Commands

```
apt update
apt install mysql-server
apt install mysql-client
```


```
mysqld -D
```

```
mysql -u root -h localhost -P 3306 <<EOF
ALTER USER 'root'@'localhost' IDENTIFIED BY '<password>';
EOF
```

## Reference
- https://github.com/docker-library/mysql/blob/master/8.0/Dockerfile.debian
