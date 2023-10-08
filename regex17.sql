select * from newps_17;
select state_ut,rural_government_beds + urban_government_beds as total_beds,rural_government_hospitals+urban_government_hospitals as total_hospitals 
from newps_17;
select * from newps_15;

create table updated_ps_17 as select newps_17.state_ut,newps_17.rural_government_beds + newps_17.urban_government_beds as total_beds,
newps_17.rural_government_hospitals+newps_17.urban_government_hospitals as total_hospitals 
,newps_15.population from newps_17 inner join newps_15 on newps_17.state_ut = newps_15.state_ut;

select * from updated_ps_17;
select sum(TOTAL_BEDS) from updated_ps_17;
select sum(TOTAL_HOSPITALS) from updated_ps_17;
select sum(POPULATION) from updated_ps_17;

insert into updated_ps_17(TOTAL_BEDS,TOTAL_HOSPITALS,POPULATION) select sum(TOTAL_BEDS),sum(TOTAL_HOSPITALS),sum(POPULATION)  
from updated_ps_17;

update updated_ps_17 set state_ut = 'National' where total_hospitals = 23582;
