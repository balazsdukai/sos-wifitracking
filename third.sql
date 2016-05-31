-- SQL statement 3
drop table if exists access_points;
create table access_points
(
    id int,
    apname text,
    maploc text,
    geom geometry
);