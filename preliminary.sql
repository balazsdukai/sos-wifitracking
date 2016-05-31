-- Create wifilog table
CREATE TABLE if NOT exists wifilog 
(
 username text not null,
 mac text not null,
 asstime timestamp without time zone not NULL, 
 apname text not NULL,
 maploc text not NULL,
 sesdur INTERVAL not NULL,
 snr real,
 rssi integer, 
 importfile text
 );