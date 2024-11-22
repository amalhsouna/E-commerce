export PGUSER="postgres"
psql -C "CREATE DATABASE fkcommerce"
psql fkcommerce -C "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"