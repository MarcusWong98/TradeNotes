import mysql.connector
from mysql.connector import errorcode


TABLES = {}



TABLES['user_roles'] = """
CREATE TABLE user_roles(
    `role_id` int(10) NOT NULL AUTO_INCREMENT,
    `role_name` varchar(16) NOT NULL,
    `enable_block` boolean NOT NULL,
    `enable_reset_pwd` boolean NOT NULL,
    `enable_sql` boolean NOT NULL,
    PRIMARY KEY(`role_id`),
    UNIQUE(`role_name`)
)
ENGINE=InnoDB
"""

TABLES['users'] = """
CREATE TABLE users (
    `user_id` int(10) NOT NULL AUTO_INCREMENT,
    `user_name` varchar(16) NOT NULL,
    `role_name` varchar(16) NOT NULL DEFAULT 'user',
    `email` varchar(50) NOT NULL,
    `password` varchar(50) NOT NULL,
    `created_date` date NOT NULL,
    PRIMARY KEY(`user_id`),
    UNIQUE (`user_name`),
    CONSTRAINT `users_ibfk1` FOREIGN KEY (`role_name`) references `user_roles` (`role_name`) on delete cascade
)
ENGINE=InnoDB
"""