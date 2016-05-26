import psycopg2
import numpy as np


try:
    conn = psycopg2.connect(database="sos_core", user="postgres", password="database2015", host="localhost", port="5432")
    print "Opened database successfully"
except:
    print "I'm unable to connect to the database"
cur = conn.cursor()



SQL1 = "drop table if exists t1; \
        create table t1 \
        ( \
        id int, \
        apname text, \
        maploc text\
        )"

cur.execute(SQL1)

SQL2 =  "select distinct apname, maploc from wifilog"
cur.execute(SQL2)

result = cur.fetchall()
aps = [x[0] for x in result]
print aps
maplocs = [x[1] for x in result]
print maplocs

def apname2id(apname):
    #get the building id by getting the 2 characters before the second '-' in apname
    i = apname.find("-",2)
    bld_id = apname[(i-2):(i)]
    if bld_id == 12 and apname[7] == 1:
        bld_id = 13
    if bld_id == 61:
        bld_id = 62
    return bld_id

for i in range(len(result)):
    ap_id = int(apname2id(aps[i]))
    print ap_id
    maploc = maplocs[i]
    item = ap_id, aps[i], maploc
    print item
    statement = "insert into t1\
                values {}".format(item)
    cur.execute(statement)

SQL3 =  "drop table if exists access_points; \
        create table access_points \
        ( \
        id int, \
        apname text,\
        maploc text, \
        geom geometry \
        )"
cur.execute(SQL3)

SQL4 =  "insert into access_points\
        select t1.id, apname, t1.maploc, geometry \
        from t1, bld\
        where t1.id = bld.id; \
        drop table t1"
cur.execute(SQL4)




conn.commit()


