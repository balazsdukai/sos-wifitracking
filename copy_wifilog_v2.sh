#!/bin/sh

psql -c "\copy (select * from wifilog limit 200) TO STDIN" -h wifitracking.bk.tudelft.nl -d wifi -U team2 | psql -c "\copy wifilog FROM STDOUT" sos_wifitracking_core




