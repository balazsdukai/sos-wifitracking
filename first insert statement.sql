-- Run from here
insert into codespace
select nextval('codespaceid_seq'), 'tudelft-wlan';

insert into featureofinteresttype
select nextval('featureofinteresttypeid_seq'), 'http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint';

--run script that created access points table before inserting
insert into featureofinterest 
select nextval('featureofinterestid_seq'), 'F', 1, apname, 1, apname, 1, maploc, geom, NULL, NULL
from access_points

insert into observableproperty
select nextval('observablepropertyid_seq'), 'F', 'mac_address', 1, 'Mac', 1, 'Mac addresses scanned by wifi access point';
insert into observableproperty
select nextval('observablepropertyid_seq'), 'F', 'netid', 1, 'NetID', 1, 'NetID of user on device scanned by wifi access point';
insert into observableproperty
select nextval('observablepropertyid_seq'), 'F', 'rssi', 1, 'Received Signal Strenght Indicator', 1, 'RSSI of device scanned by wifi access point';
insert into observableproperty
select nextval('observablepropertyid_seq'), 'F', 'snr', 1, 'Signal to Noise Ratio', 1, 'SNR of device scanned by wifi access point';

insert into proceduredescriptionformat
select nextval('procdescformatid_seq'), 'http://www.opengis.net/sensorML/1.0.1';

insert into procedure
select nextval('procedureid_seq'), 'F', 1, 'wifi_access_point', 1, 'Scan', 1, 'WiFi Scan', 'F', 'F';

insert into unit
select nextval('unitid_seq'), 'mac address';
insert into unit
select nextval('unitid_seq'), 'db';
insert into unit
select nextval('unitid_seq'), 'netid';

insert into observationtype
select nextval('observationtypeid_seq'), 'http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement';

insert into offering
select nextval('offeringid_seq'), 'F', 'wifi_access_points', 1, 'WiFi Access Points', 1, 'Network of all WiFi Access Points';



--ONLY FOR OLD MODEL--
insert into observation(
observationid, 
featureofinterestid, 
observablepropertyid,
procedureid,
phenomenontimestart,
phenomenontimeend,
resulttime,
codespace,
name,
description,
samplinggeometry,
unitid,
codespaceid)
select nextval('observationid_seq'), featureofinterestid, 1, 1, asstime, asstime+sesdur, asstime+sesdur, 1, 'Scan', 'WiFi Scan', featureofinterest.geom, 1, 1
from featureofinterest, wifilog
where featureofinterest.identifier = wifilog.apname
------------------------------------------------------------

---for series model---
INSERT INTO series (
	seriesid,
	featureofinterestid,  
    observablepropertyid,
    procedureid)
SELECT nextval('seriesid_seq'), *
from (SELECT DISTINCT featureofinterestid, 1 ,1
    FROM featureofinterest, wifilog
    WHERE identifier=apname) as hola
 
--observation
--RUN SCRIPT  
    
INSERT INTO observationhasoffering
SELECT observationid, 1 
FROM observation;

INSERT INTO observationconstellation (
    observationconstellationid,
    observablepropertyid,
    procedureid,
    observationtypeid,
    offeringid)
SELECT nextval('observationconstellationid_seq'), 1, 1, 1, 1;

---ONLY FOR OLD MODEL---
---TEXT VALUE---
insert into textvalue
select observationid, mac
from observation, wifilog, featureofinterest
where phenomenontimestart=asstime and phenomenontimeend = (asstime+sesdur) 
and observation.featureofinterestid = featureofinterest.featureofinterestid


