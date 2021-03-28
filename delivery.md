# deliverables:

Create a data architecture diagram to visualize how you will ingest and migrate the data into 
Staging, Operational Data Store (ODS) and DWH.

```
(0)-snowflake-etl-template/docs/0-data-architecture.png
```

Create a staging environment (schema) in Snowflake.  
Upload all Yelp and Climate data to the staging environment. (Screenshots 1,2)  
1.Screenshot of 6 tables created upon upload of YELP data  
2.Screenshot of 2 tables created upon upload of climate data
```
(1,2) snowflake-etl-template/docs/1-2-yelp-weather.png
```

Create an ODS schema.  
Draw an entity-relationship (ER) diagram to visualize the data structure.   
Migrate the data into the ODS environment. (Screenshots 3,4,5,6)  
3.SQL queries code that transforms staging to ODS. (include all queries)  
4.SQL queries code that specifically uses JSON functions   
6.SQL queries code to integrate climate and Yelp data    
5.Screenshot of the table with three columns: raw files, staging, and ODS. (and sizes)

```
(0) - snowflake-etl-template/docs/0-ods-conceptual-erd.png

(3,4,6) - check files:
snowflake-etl-template/src/etl/ods_ddl.sql
snowflake-etl-template/src/etl/ods_etl.sql

(5) - snowflake-etl-template/docs/5-dimension-comparison.png
```

Draw a STAR schema for the Data Warehouse environment Migrate the data to the Data Warehouse. (Screenshot 7)  
7.SQL queries code necessary to move the data from ODS to DWH.

```
(0) - snowflake-etl-template/docs/0-dwh-physical-ERD.pdf
(7) - check queries:
snowflake-etl-template/src/etl/dwh_ddl.sql
snowflake-etl-template/src/etl/dwh_etl.sql
```

Query the Data Warehouse to determine how weather affects Yelp reviews. (Screenshot 8)  
8.SQL queries code that reports the business name, temperature, precipitation, and ratings.

```
(8) - check queries:
snowflake-etl-template/src/etl/dwh_query.sql
```
