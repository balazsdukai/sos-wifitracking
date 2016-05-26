-- Doesn't work yet
insert into textvalue 
select nextval('observationid_seq'), mac 
from wifilog;

-- Run from here
insert into codespace
select nextval('codespaceid_seq'), 'tudelft-access-points';

insert into featureofinteresttype
select nextval('featureofinteresttypeid_seq'), 'http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint';

insert into proceduredescriptionformat
select nextval('procdescformatid_seq'), 'http://www.opengis.net/sensorML/1.0.1';

--need to update this with rssi, snr, netid
insert into unit
select nextval('unitid_seq'), 'mac address';

/*
-- If related feature is pointing to AP, how to specify nearest AP?
insert into relatedfeature
select nextval('relatedfeature_seq'), #;
*/

-- I think this is correct
insert into observationtype
select nextval('observationtypeid_seq'), 'http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement';

insert into "procedure"
select nextval('procedureid_seq'), 'F', 1, 'wifi_access_point', 1, 'Scan', 1, 'WiFi Scan', 'F', 'F';

insert into observableproperty
select nextval('observablepropertyid_seq'), 'F', 'mac_address', 1, 'Mac', 1, 'Mac addresses scanned by wifi access point';

