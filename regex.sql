select* from ps15;
select * from ps15 where state_ut like '%*' ;
select state_ut,rural_government_hospitals,rural_government_beds,urban_government_hospitals,urban_government_beds,last_updated,total_beds,total_hospitals,population,
(total_beds*100/population) as clc from ps15 where state_ut like '%*' order by clc asc;
create table ps_15 as select state_ut,rural_government_hospitals,rural_government_beds,urban_government_hospitals,urban_government_beds,last_updated,total_beds,total_hospitals,population,
(total_beds*100/population) as clc from ps15 where state_ut like '%*' order by clc  asc fetch first 3 rows only;
select* from ps_15;
select * from ps_15 order by total_hospitals asc;