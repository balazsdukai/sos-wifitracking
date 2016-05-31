-- SQL statement 3
drop table if exists access_points;
create table access_points
(
    id serial,
    apname text,
    maploc text,
    geom geometry
);
/*
insert into access_points
select t1.id, apname, t1.maploc, geometry
from t1, buildings as bld
where t1.id = bld.id;
drop table t1;
 */


insert into access_points (apname, maploc, geom)
         select distinct on (t1.apname) t1.apname, t1.maploc, geometry 
         from t1, buildings
         where t1.id = buildings.id; 
         drop table t1;