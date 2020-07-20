USE maindatabase;

Create table PokeChallenge(
DexNumber varchar(3),
Pokemon varchar(20),
TypeMain varchar(20),
TypeSec varchar(20),
Adder varchar(30)
)

INSERT INTO PokeGen1(DexNumber,Pokemon,TypeMain,TypeSec,Adder) 
VALUES ('010','CATERPIE','BUG','BUG','NULL');


INSERT INTO PokeGen1 
VALUES ('019','RATTATA','NORMAL','NORMAL','NULL');

INSERT INTO PokeGen1 
VALUES ('020','RATICATE','NORMAL','NORMAL','NULL');

INSERT INTO PokeGen1 
VALUES ('021','SPEAROW','NORMAL','FLYING','NULL');

INSERT INTO PokeGen1 
VALUES ('022','FEAROW','NORMAL','FLYING','NULL');

INSERT INTO PokeGen1 
VALUES ('018','PIDGEOT','NORMAL','FLYING','NULL');
