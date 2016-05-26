-- Doesn't work yet
insert into textvalue 
select nextval('observationid_seq'), mac 
from wifilog;

-- Run from here
insert into codespace
select nextval('codespaceid_seq'), 'codespacetest';

insert into featureofinteresttype
select nextval('featureofinteresttypeid_seq'), 'http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint';

insert into proceduredescriptionformat
select nextval('procdescformatid_seq'), 'http://www.opengis.net/sensorML/1.0.1';

insert into unit
select nextval('unitid_seq'), 'mac address';

-- If related feature is pointing to AP, how to specify nearest AP?
insert into relatedfeature
select nextval('relatedfeature_seq'), #

-- I think this is correct
insert into observationtype
select nextval('observationtypeid_seq'), 'http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement';

-- Do we need to fill out name and description, and other assumptions?
insert into procedure
select nextval('procedureid_seq'), 'var', 1, 'eduroam_access_point', 1, 'name of procedure', 1, 'description', 'F', NULL, 'F'
