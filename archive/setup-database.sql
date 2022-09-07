DROP TABLE IF EXISTS papers;

/* Create the paper table */
CREATE TABLE papers (
    code varchar(7) NOT NULL,
    year varchar(7),
    title varchar(50),
    points varchar(10),
    teaching_period varchar(10),
    subject varchar(20),
    pre_req varchar(30)

    PRIMARY KEY (code)
);

/* Populate papers table */
INSERT INTO papers VALUES ("COSC326", "2020","Effective Programming", "18", "S2", "compSCI", "somme 100lvl papers");
INSERT INTO papers VALUES ('COSC349', 'Cloud Computing Architecture');
INSERT INTO papers VALUES ('COMO303', 'Numerical Methods')