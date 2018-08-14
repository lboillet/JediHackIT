BEGIN TRANSACTION;
CREATE TABLE "Student" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`personid`	INTEGER,
	`legal_rep`	INTEGER,
	FOREIGN KEY(`personid`) REFERENCES `Person`(`id`),
	FOREIGN KEY(`legal_rep`) REFERENCES Legal_rep(id)
);
CREATE TABLE "School" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`name`	TEXT,
	`address`	TEXT,
	`phone`	NUMERIC
);
CREATE TABLE "Person" (
	`firstname`	TEXT,
	`lastname`	TEXT,
	`nationalid`	TEXT,
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`phone`	NUMERIC,
	`email`	TEXT,
	`address`	TEXT,
	`att_percent`	TEXT,
	`payment`	TEXT
);
CREATE TABLE "Payment" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`value`	INTEGER,
	`currency`	INTEGER,
	`date`	INTEGER
);
CREATE TABLE "Legal_rep" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`personid`	INTEGER,
	`studentid`	INTEGER,
	FOREIGN KEY(`personid`) REFERENCES `Person`(`id`),
	FOREIGN KEY(`studentid`) REFERENCES Student(id)
);
CREATE TABLE "Attendance" (
	`studentid`	INTEGER,
	`date`	TEXT,
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	FOREIGN KEY(`studentid`) REFERENCES Student(id)
);
COMMIT;
