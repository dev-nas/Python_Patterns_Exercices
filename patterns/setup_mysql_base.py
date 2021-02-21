import pymysql
import re
# CREATE DATABASE api_users CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
# (CREATE | ALTER) USER 'stagiaire'@'localhost' IDENTIFIED BY 'a123456!';
# GRANT ALL PRIVILEGES ON api_users.* TO 'stagiaire'@'localhost';
# INSERT INTO users 
# (id, name, email, gender, status, updated_at) VALUES ('153', 'Daiwik Rana CPA', 
# 'rana_daiwik_cpa@metz-wunsch.net', 'Female', 'Inactive', '2021-02-02 03:50:06')

# connexion db
try:
    conn = pymysql.connect(host="localhost", user="stagiaire", password="a123456!", database="api_users", autocommit=True)
    with conn.cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT,
            name VARCHAR (100) DEFAULT NULL,
            email VARCHAR (255) DEFAULT NULL,
            gender VARCHAR (10) DEFAULT NULL,
            status VARCHAR (10) DEFAULT NULL,
            updated_at DATETIME DEFAULT NULL,
            PRIMARY KEY (id)
        ) ENGINE=innodb""")
    
        sql = "INSERT INTO users \
(id, name, email, gender, status, updated_at) VALUES ('153', 'Daiwik Rana CPA', \
'rana_daiwik_cpa@metz-wunsch.net', 'Female', 'Inactive', '2021-02-02 03:50:06')"
        print(sql)
        cur.execute(sql)
    conn.close()
except pymysql.MySQLError as e:
    # revenir à un état stable de la db ante execution
    print(e)
    conn.close()