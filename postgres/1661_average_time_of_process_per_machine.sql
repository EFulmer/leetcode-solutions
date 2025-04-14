with durations as (
    select
        starts.machine_id
        , starts.process_id
        , (ends.timestamp - starts.timestamp) as duration
    from (
        select *
        from activity
        where activity_type = 'start'
    ) as starts, (
        select *
        from activity
        where activity_type = 'end'
    ) as ends
    where
        starts.machine_id = ends.machine_id
        and starts.process_id = ends.process_id
)
select
    machine_id
    , round(avg(duration)::decimal, 3) as processing_time
from durations
group by machine_id
;
