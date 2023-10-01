Select * from ps16;
Insert into ps16(State_UT,total_beds,population) values('National',(Select sum(total_beds) from ps16),(Select sum(population) from ps16));
create table ps_16 as select * from ps16;
Select * from ps_16;