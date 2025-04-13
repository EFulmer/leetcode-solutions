select
    Visits.customer_id
    , COUNT(Visits.visit_id) as count_no_trans
from Visits
where
    Visits.visit_id not in (select Transactions.visit_id from Transactions)
group by customer_id;
