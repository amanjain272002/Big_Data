CREATE OR REPLACE FUNCTION get_population_district
           (DISTRICT1 IN VARCHAR2) 
          RETURN NUMBER
          IS
              TOTAL_POPULATION NUMBER(38):=0;
          BEGIN
              select population  INTO TOTAL_POPULATION from census where district = DISTRICT1;
              return TOTAL_POPULATION;
          END get_population_district;
          
          
CREATE OR REPLACE FUNCTION get_population
           (State_ut1 IN VARCHAR2) 
          RETURN NUMBER
          IS
              TOTAL_POPULATION NUMBER(38):=0;
          BEGIN
              select sum(population)  INTO TOTAL_POPULATION from census where state_ut = state_ut1;
              return TOTAL_POPULATION;
          END get_population;
          
          
CREATE OR REPLACE FUNCTION senior_citizen_population
           (State_ut1 IN VARCHAR2) 
          RETURN NUMBER
          IS
              TOTAL_POPULATION NUMBER(38):=0;
          BEGIN
              select sum(senior_citizen)  INTO TOTAL_POPULATION from census where state_ut = state_ut1;
              return TOTAL_POPULATION;
          END senior_citizen_population;
          
    
CREATE OR REPLACE FUNCTION get_govt_hospital_beds
           (State_ut1 IN VARCHAR2) 
          RETURN NUMBER
          IS
              TOTAL_GOV_BEDS NUMBER(38):=0;
          BEGIN
              select total_beds  INTO TOTAL_GOV_BEDS from gov_hos where state_ut = state_ut1;
              return TOTAL_GOV_BEDS;
          END get_govt_hospital_beds;

    
CREATE OR REPLACE FUNCTION govt_beds_per_lakh
           (State_ut1 IN VARCHAR2) 
          RETURN NUMBER
          IS
              TOTAL_GOV_BEDS_LAKH NUMBER(38):=0;
          BEGIN
              select (total_beds/population)*100000  INTO TOTAL_GOV_BEDS_LAKH from gov_hos where state_ut = state_ut1;
              return TOTAL_GOV_BEDS_LAKH;
          END govt_beds_per_lakh;
      