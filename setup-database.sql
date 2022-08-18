
/* Create the paper table */
CREATE TABLE papers (
    code varchar(7),
    name varchar(50) NOT NULL,
    PRIMARY KEY (code)
);

/* Populate papers table */
INSERT INTO papers VALUES ("COSC326", "Effective Programming");
INSERT INTO papers VALUES ('COSC349', 'Cloud Computing Architecture')