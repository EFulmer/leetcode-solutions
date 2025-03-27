select
    p.firstName as firstName, p.lastName as lastName, a.city, a.state
from
    person p
left outer join
    address a
    on p.personId = a.personId;
