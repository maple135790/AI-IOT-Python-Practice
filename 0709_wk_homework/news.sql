BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "news" (
	"id"	INTEGER,
	"title"	TEXT UNIQUE,
	"date"	TEXT,
	"link"	TEXT,
	"context"	TEXT,
	PRIMARY KEY("id")
);
COMMIT;
