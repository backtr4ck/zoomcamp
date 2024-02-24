
{{
    config(
        materialized='view'
    )
}}


with 

source as (

    select * from {{ source('staging', 'fhv') }}
    where EXTRACT(YEAR FROM pickup_datetime) = 2019

),

renamed as (

    select
        {{ dbt_utils.generate_surrogate_key(['dispatching_base_num', 'pickup_datetime']) }} as tripid,
        dispatching_base_num,
        pickup_datetime,
        dropoff_datetime,
        pulocationid as pickup_locationid,
        dolocationid as dropoff_locationid,
        sr_flag,
        affiliated_base_number

    from source

)

select * from renamed


-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
