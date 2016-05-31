import psycopg2
import numpy as np
from subprocess import call

#make connection with the database
#make sure the parameters are correct

try:
    conn = psycopg2.connect(database="sos_wifitracking_core", user="bdukai", password="ERBAgoNd1#", host="localhost", port="5432")
    print "Opened database successfully"
except:
    print "I'm unable to connect to the database"
cur = conn.cursor()

seriesid = 0
phenemenontimestart = 1
phenemenontimeend = 2
resulttime = 3
samplinggeometry = 7
mac = 8

SQL1 = '''
    select 
    series.seriesid, 
    asstime as phenomenontimestart, 
    asstime+sesdur as phenomenontimeend, 
    asstime+sesdur as resulttime, 
    1 as codespace, 
    'description' as description, 
    1 as unitid, 
    st_asewkt(geom) as samplinggeometry,
    mac

    from series, (
    --join wifilog and featureofinterest
    select *
    from wifilog, featureofinterest
    where wifilog.apname=featureofinterest.identifier) as a
    --join with series table
    where series.featureofinterestid = a.featureofinterestid'''
cur.execute(SQL1)
result = cur.fetchall()

for i in result:
    SQL3 = '''SELECT nextval('observationid_seq');'''
    cur.execute(SQL3)
    obs_id = cur.fetchall()[0][0]

    print obs_id, i[seriesid], type(i[phenemenontimestart]), i[phenemenontimeend], i[samplinggeometry], i[mac]
    SQL2 = '''insert into observation(
    observationid,
    seriesid,
    phenomenontimestart,
    phenomenontimeend,
    resulttime,
    codespace,
    description,
    unitid,
    samplinggeometry) values(
    {}, {}, '{}', '{}', '{}', 1, 'description', 1, st_geomfromewkt('{}'))'''.format(obs_id, i[seriesid], i[phenemenontimestart], i[phenemenontimeend], i[resulttime],i[samplinggeometry])  
    cur.execute(SQL2)

    SQL3 = '''insert into textvalue(
    observationid,
    value) values ({}, '{}');'''.format(obs_id, i[mac])
    cur.execute(SQL3)
    conn.commit()


    
