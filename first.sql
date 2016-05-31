-- SQL statement 1
drop table if exists t1;
create table t1
( 
    id int, 
    apname text, 
    maploc text
);
-- SQL statement 2
select distinct apname, maploc 
from wifilog;