# Install Postgres and PostGIS on UBUNTU
---

Step 1: Add and Install the PostgreSQL 12 via your terminal.

>```
$ sudo apt update
$ sudo apt install postgresql-12 postgresql-client-12
```

Then, connect and change the “postgres” password.

>```
$ sudo -u postgres psql
$ password postgres
enter strong password twice!
```

Step 3: Install GnuPG 2.0 and PostGIS

>```
$ sudo sudo apt install gnupg2
$ sudo apt install postgis postgresql-12-postgis-3
```

Step 4: Set the Client Authentication & Connection

>``` 
# ========================================
# === Set Listening Port =================
# ========================================
$ nano /etc/postgresql/12/main/postgresql.conf
#  listen_addresses = '*' ==> Listen on all interfaces 
# listen_addresses = '<ip here>'==> Listen on specified IP address
# 
# ========================================
# === Set Client authentication ==========
# ========================================
#   
$ vi /etc/postgresql/12/main/pg_hba.conf
# TYPE  DATABASE     USER       ADDRESS             METHOD
# host  postgres     all        192.168.12.10/32     md5
host    all          all        localhost/0          md5
#host    all         all        0.0.0.0/0            md5
```
   
Step 4.1: Restart postgres service:

> ```
sudo /etc/init.d/postgresql restart
```

##### Connect and enjoy PostgreSQL via your favorite GUI!

* PostgreSQL: https://www.pgadmin.org/
* DBeaver: https://dbeaver.io/

---
### Create sample database and user


> ```
sudo -u postgres psql
;
postgres# create database test;
postgres# create user user1 with encrypted password 'te%$&st';
postgres# grant all privileges on database test to user1;
;
\q
```      
 
Now you can login using

> ```
psql -h localhost -U user1 -d test 
Password for user user1: 
psql (12.9 (Ubuntu 12.9-0ubuntu0.20.04.1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.
# 
#  Create some random table to test
#
test=> create table test( name varchar,value varchar,valid boolean,num1 int,num2 float8,num3 float8);
test=> insert into test values ('name1' , 'value', true, 0,0,0);
test=> select * from test;
.
``` 

---
### Connect from SQLDB (Ignore if you are not using python)

* install 
	sudo apt-get install libpq-dev
    
* pip install psycopg2-2.9.3

---
```
import services.gen.DBservices
from services.gen.DBservices import *

# Postgres
db  = getDB("db", "postgresql://user1:t&^$$est@localhost/test")
ret = db.Q(q="SELECT * from test")
#pd.DataFrame(ret[0]['values'], columns=ret[0]['columns'])
print(ret)‣
```
---- 


