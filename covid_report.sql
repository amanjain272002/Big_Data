select * from covid_report;

create table updaterep as select country,indicator,rdate,substr(year_week, 1,4) ryear,substr(year_week, 6) rweak ,value from covid_report;

select * from updaterep;