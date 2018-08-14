import sqlite3

db = sqlite3.connect('db/MercyCorps.db')

# Get a cursor object
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE "Student" (
    	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    	`personid`	INTEGER,
    	`legal_rep`	INTEGER,
    	FOREIGN KEY(`personid`) REFERENCES `Person`(`id`),
    	FOREIGN KEY(`legal_rep`) REFERENCES Legal_rep(id)
    );
''')

cursor.execute('''
    CREATE TABLE "School" (
    	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    	`name`	TEXT,
    	`address`	TEXT,
    	`phone`	NUMERIC
    );
''')

cursor.execute('''
    CREATE TABLE "Person" (
    	`firstname`	TEXT,
    	`lastname`	TEXT,
    	`nationalid`	TEXT,
    	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    	`phone`	NUMERIC,
    	`email`	TEXT,
    	`address`	TEXT
    );
''')

cursor.execute('''
    CREATE TABLE "Payment" (
    	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    	`value`	INTEGER,
    	`currency`	INTEGER,
    	`date`	INTEGER
    );
''')

cursor.execute('''
    CREATE TABLE "Legal_rep" (
    	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    	`personid`	INTEGER,
    	`studentid`	INTEGER,
    	FOREIGN KEY(`personid`) REFERENCES `Person`(`id`),
    	FOREIGN KEY(`studentid`) REFERENCES Student(id)
    );
''')

cursor.execute('''
    CREATE TABLE "Attendance" (
    	`studentid`	INTEGER,
    	`date`	TEXT,
    	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    	FOREIGN KEY(`studentid`) REFERENCES Student(id)
    );
''')
db.commit()

db.close()
