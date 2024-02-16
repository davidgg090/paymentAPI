#!/bin/bash

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=


psql -h $DB_HOST -U $DB_USER -d $DB_NAME -f create_users.sql
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -f create_tokens.sql
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -f create_customers.sql
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -f create_merchants.sql
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -f create_transactions.sql
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -f create_audit_log.sql

echo "The tables have been created successfully."