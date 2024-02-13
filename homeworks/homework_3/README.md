Loaded everything into a parquet file in GCS and did this query to load in BQ:

```sql
CREATE OR REPLACE EXTERNAL TABLE ny_taxi_data.green_taxi_data
OPTIONS (
  format='parquet',
  uris=['gs://zoomcamp_homework3_bucket/ny_taxi_green_data.parquet']
)
```

for partitioned and clustered did this query:

```sql
create or replace table ny_taxi_data.green_taxi_data_partitioned
partition by lpep_pickup_date
cluster by PULocationID as
select * from `ny_taxi_data.green_taxi_data`
```

for querying the data for PULocationID did this query:

```sql
SELECT distinct PULocationID FROM `zoomcamp-0.ny_taxi_data.green_taxi_data_partitioned`
WHERE lpep_pickup_date >= "2022-06-01" and lpep_pickup_date <= "2022-06-30"
```
