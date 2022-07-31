-- FROM THE TWO MOST COMMONLY APPEARING REGIONS, WHICH IS THE LATEST DATASOURCE?

WITH most_common_region AS (
    SELECT
        a.region_id
    FROM (
        SELECT
            region_id,
            COUNT(1) as rows_num
        FROM trips
        GROUP BY region_id
        ORDER BY rows_num DESC
        LIMIT 2
    ) a
),

latest_datasource AS (

    SELECT
        a.datasource_id
    FROM (
        SELECT
            datasource_id
        FROM trips
        WHERE 1 = 1
        AND region_id in (
            SELECT
                region_id
            FROM most_common_region
        )
        ORDER BY trip_datetime DESC
        LIMIT 1
    ) a

)

SELECT b.name_desc as datasource_name
FROM latest_datasource a
LEFT JOIN sources b
ON a.datasource_id = b.id;

-- WHAT REGIONS HAS THE "CHEAP_MOBILE" DATASOURCE APPEARED IN?

SELECT
    DISTINCT c.name_desc as region_name
FROM trips a
INNER JOIN sources b
ON a.datasource_id = b.id
LEFT JOIN regions c
ON a.region_id = c.id
WHERE 1 = 1
AND b.name_desc = 'cheap_mobile';