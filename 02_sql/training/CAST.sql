create table one (
col1 char(3)
)

create table two (
coluna char(6)
)


insert into two (coluna)
values ('123'), ('487'), ('498')

insert into one (col1)
values ('123'), ('145'), ('189')

select * from one
select * from two

select a.*, b.* 
from one as a
inner join two as b on a.col1 = cast(b.coluna as char(3))

select a.*, b.* 
from one as a
inner join two as b on a.col1 = b.coluna
