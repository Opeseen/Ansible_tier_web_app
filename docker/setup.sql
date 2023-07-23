-- create the user
CREATE USER 'admin'@'%' IDENTIFIED BY 'admin4045';

-- create the database
CREATE DATABASE IF NOT EXISTS flaskdb;

-- Grant all priviledge for the user
GRANT ALL ON *.* TO 'admin'@'%';

FLUSH PRIVILEGES;