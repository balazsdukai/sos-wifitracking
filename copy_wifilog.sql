\copy (SELECT * FROM wifilog limit 10) TO '/home/bdukai/Development/GEO1007_Main-Project/wifilog.csv' DELIMITER ',' CSV HEADER;