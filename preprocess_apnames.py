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

#create temporary table

SQL1 = "drop table if exists t1; \
        create table t1 \
        ( \
        id int, \
        apname text, \
        maploc text\
        );"

cur.execute(SQL1)

#get all access points
SQL2 =  "select distinct apname, maploc from wifilog"
cur.execute(SQL2)

result = cur.fetchall()
aps = [x[0] for x in result]
maplocs = [x[1] for x in result]

#function to get the id from the ap
def apname2id(apname):
    #get the building id by getting the 2 characters before the second '-' in apname
    i = apname.find("-",2)
    bld_id = apname[(i-2):(i)]
    if bld_id == 12 and apname[7] == 1:
        bld_id = 13
    if bld_id == 61:
        bld_id = 62
    return bld_id

#insert values in t1
for i in range(len(result)):
    ap_id = int(apname2id(aps[i]))
    maploc = maplocs[i]
    item = ap_id, aps[i], maploc
    statement = "insert into t1\
                values {}".format(item)
    cur.execute(statement)

#dump the building table from the wifi database into the sos database
dumpTable = "pg_dump -t buildings -C -h wifitracking.bk.tudelft.nl -U team2 wifi | psql -h localhost -U bdukai sos_wifitracking_core"
call(dumpTable, shell = True)

#create final table; access_points
SQL3 =  "drop table if exists access_points; \
        create table access_points \
        ( \
        id serial, \
        apname text,\
        maploc text, \
        geom geometry \
        )"
cur.execute(SQL3)

# insert values into access_points (and drop temporary table)
SQL4 =  "insert into access_points (apname, maploc, geom)\
         select distinct on (t1.apname) t1.apname, t1.maploc, geometry \
         from t1, buildings\
         where t1.id = buildings.id; \
         drop table t1;"
        
cur.execute(SQL4)

conn.commit()


