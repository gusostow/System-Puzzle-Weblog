#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username $POSTGRES_USER --dbname $POSTGRES_DB <<-EOSQL
        CREATE TABLE  weblogs (
               day    date,
               source varchar(6),
               status varchar(3)
               );
EOSQL
