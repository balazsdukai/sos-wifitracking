-- SQL statement 3
drop table if exists access_points;
create table access_points
(
    id int,
    apname text,
    maploc text,
    geom geometry
);
insert into access_points
select t1.id, apname, t1.maploc, geometry
from t1, buildings as bld
where t1.id = bld.id;
drop table t1;