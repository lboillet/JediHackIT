BEGIN TRANSACTION;
CREATE TABLE "Student" (
	FOREIGN KEY(studentpersonid) REFERENCES Person(id),
	FOREIGN KEY(studentschoolid) REFERENCES School(id),
	FOREIGN KEY(legalrepid) REFERENCES Person(id),
	`id`	INTEGER UNIQUE,
	PRIMARY KEY(`id`)
);
CREATE TABLE `School` (
	`id`	INTEGER UNIQUE,
	`name`	TEXT,
	`address`	TEXT,
	`phone`	NUMERIC,
	PRIMARY KEY(`id`)
);
CREATE TABLE "Person" (
	`firstname`	TEXT,
	`lastname`	TEXT,
	`nationalid`	TEXT,
	`id`	INTEGER UNIQUE,
	`phone`	NUMERIC,
	`email`	TEXT,
	`address`	TEXT,
	PRIMARY KEY(`id`)
);
CREATE TABLE `Payment` (
	`id`	INTEGER UNIQUE,
	`value`	INTEGER,
	`currency`	INTEGER,
	`date`	INTEGER,
	FOREIGN KEY(legalrepid) REFERENCES Legalrep(id)
	PRIMARY KEY(`id`)
);
CREATE TABLE `Legal_rep` (
	`ID`	INTEGER UNIQUE,
	`Person`	INTEGER,
	`Student`	INTEGER,
	PRIMARY KEY(`ID`)
);
CREATE TABLE "Attendance" (
	`Student ID`	INTEGER,
	`Date/Time`	TEXT,
	`ID`	INTEGER UNIQUE,
	PRIMARY KEY(`ID`)
);
COMMIT;
