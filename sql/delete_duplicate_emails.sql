--delete join 的应用

Create table if not exists person (id int(11), Email varchar(512));
truncate person;
insert into person (id, Email) values (1, 'john@example.com');
insert into person (id, Email) values (2, 'bob@example.com');
insert into person (id, Email) values (3, 'john@example.com');

select p2 from person p1 join person p2 where p1.email = p2.email and p2.id > p1.id;

把ID大的删除