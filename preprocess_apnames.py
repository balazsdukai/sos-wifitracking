import psycopg2
import numpy as np
from subprocess import *
import sys

#make connection with the database
#make sure the parameters are correct

def main():
    #dump the building table from the wifi database into the sos database
    cur.execute(open("create_wifilog_table.sql", "r").read())
    conn.commit()
    limit = raw_input('Row limit for the wifilog: ')
    dumpTable = 'psql -c "\copy (select * from wifilog limit {}) TO STDIN" -h wifitracking.bk.tudelft.nl -d wifi -U team2 | psql -c "\copy wifilog FROM STDOUT" -U {} -d {}'.format(limit, username, dbname)
    call(dumpTable, shell = True)
   
    # Create temporary table 
    cur.execute(open("first.sql", "r").read())
    result = cur.fetchall()
    aps = [x[0] for x in result]
    maplocs = [x[1] for x in result]

    # Insert values in t1
    for i in range(len(result)):
        ap_id = int(apname2id(aps[i]))
        maploc = maplocs[i]
        item = ap_id, aps[i], maploc
        statement = "insert into t1\
                    values {}".format(item)
        cur.execute(statement)
    # Dump the building table from the wifi database into the sos database
    cur.execute('create table if not exists buildings (id integer, name text, geometry geometry, x double precision, y double precision)')
    conn.commit()
    dumpTable = 'psql -c "\copy (select * from buildings) TO STDIN" -h wifitracking.bk.tudelft.nl -d wifi -U team2 | psql -c "\copy buildings FROM STDOUT" -U {} -d {}'.format(username, dbname)
    call(dumpTable, shell = True)

    # Create final table; access_points
    cur.execute(open("second.sql", "r").read())
    conn.commit()
    print 'finished'

    
#function to get the id from the ap
def apname2id(apname):
    """get the building id by getting the 2 characters before the second '-' in apname"""
    i = apname.find("-",2)
    bld_id = apname[(i-2):(i)]
    if bld_id == '12' and apname[7] == '1':
        bld_id = '13'
    if bld_id == '61':
        bld_id = '62'
    return bld_id

if __name__ == '__main__':
    try:
        dbname = raw_input('Name of database: ')
        username = raw_input('Username: ')
        passw = raw_input('Password: ')
        conn = psycopg2.connect(database=dbname, user=username, password=passw, host="localhost", port="5432")
        cur = conn.cursor()
        print "Opened database successfully"
    except:
        print "I'm unable to connect to the database"
    main()
    


