
drop database trail;

CREATE DATABASE walnut
  WITH OWNER = jeffstrickler
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_US'
       LC_CTYPE = 'en_US'
       CONNECTION LIMIT = -1;




drop table
  if exists users
 cascade;


create table
  users
  (
    id serial primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    email varchar(50) unique not null,
    username varchar(50) unique not null,
    password varchar(50) not null,
    last_modified timestamp DEFAULT current_timestamp,
    created timestamp DEFAULT current_timestamp
  );
