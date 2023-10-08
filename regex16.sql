Select * from ps16;
Insert into ps16(State_UT,total_beds,population) values('National',(Select sum(total_beds) from ps16),(Select sum(population) from ps16));
create table ps_16 as select * from ps16;
Select * from ps_16;

Select * from ps_17;
Insert into ps_17(State_UT,total_beds,population,total_hospitals)
values('National',(Select sum(total_beds) from ps_17),(Select sum(population) from ps_17),(Select sum(total_hospitals) from ps_17));
create table ps17 as select * from ps_17;
Select * from ps17;