select * from table1;
select * from table2;
select * from table3;
select * from census;
desc census;

select get_population_district('Chamba') "POPULATION_DISTRICT" from dual;

select get_population('Dadra and Nagar Haveli') "POPULATION_STATE" from dual;

select senior_citizen_population('Himachal Pradesh') "POPULATION_SENIOR_CITIZEN_STATE" from dual;

select * from gov_hos;

update gov_hos set population = 41974218 where STATE_UT = 'ODISHA';
update gov_hos set STATE_UT = 'DADRA AND NAGAR HAVELI' where population = 0;
update gov_hos set STATE_UT ='ORISSA' where population = 41974218;
update gov_hos set population = 343709 where STATE_UT = 'DADRA AND NAGAR HAVELI';


select get_govt_hospital_beds('ORISSA') "HOSPITAL_BEDS" from dual;

select govt_beds_per_lakh('DADRA AND NAGAR HAVELI') "HOSPITAL_BEDS" from dual;