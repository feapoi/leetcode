Create table If Not Exists Scores (Id int, Score DECIMAL(3,2));
Truncate table Scores;
insert into Scores (Id, Score) values ('1', '3.5');
insert into Scores (Id, Score) values ('2', '3.65');
insert into Scores (Id, Score) values ('3', '4.0');
insert into Scores (Id, Score) values ('4', '3.85');
insert into Scores (Id, Score) values ('5', '4.0');
insert into Scores (Id, Score) values ('6', '3.65');

SELECT s1.Score, COUNT(DISTINCT s2.score)+1 Rank
FROM scores s1 LEFT JOIN scores s2 ON s2.score > s1.score
GROUP BY s1.Score, s1.id
ORDER BY s1.score DESC