DROP TABLE IF EXISTS Event;
DROP TABLE IF EXISTS USERS;

CREATE TABLE "Event" (
	"eventid"	INTEGER NOT NULL UNIQUE,
	"difficulty"	TEXT NOT NULL,
	"duration"	TEXT NOT NULL,
	"userid"	INTEGER NOT NULL,
	"result"	INTEGER NOT NULL,
	FOREIGN KEY("userid") REFERENCES "USERS"("userid"),
	PRIMARY KEY("eventid" AUTOINCREMENT)
);


CREATE TABLE "Users" (
	"userid"	INTEGER NOT NULL UNIQUE,
	"username"	TEXT NOT NULL UNIQUE,
	"firstname"	TEXT NOT NULL,
	"lastname"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("userid" AUTOINCREMENT)
);