select * from census;
select * from housing1;
select * from all_hospitals;
select  census.state_ut from census inner join housing1 on census.District = housing1.district;

create table table1 as select census.state_ut,census.district,census.population from census inner join 
all_hospitals on census.state_ut = all_hospitals.state_ut;

select * from table1;

create table table2 as select housing1.households_rural_toilet_premise,housing1.households_urban_toilet_premise,housing1.state_ut,housing1.district
,all_hospitals.hospitalbeds from housing1 inner join all_hospitals on all_hospitals.state_ut = housing1.state_ut;

select * from table2;

create table table3 as select table2.district,table2.state_ut,table2.households_rural_toilet_premise,table2.households_urban_toilet_premise,table2.hospitalbeds,table1.population from table2
inner join table1 on table2.district = table1.district;

select * from table3;

select table3.district,table3.state_ut,table3.hospitalbeds,table3.population ,table3.households_rural_toilet_premise , table3.households_urban_toilet_premise from table3 
where table3.households_rural_toilet_premise =0 or table3.households_urban_toilet_premise=0 ;


select table3.state_ut,table3.hospitalbeds,table3.district,sum(table3.population) from table3 
where table3.households_rural_toilet_premise =0 or table3.households_urban_toilet_premise=0 
group by table3.state_ut ,table3.hospitalbeds,table3.district;
