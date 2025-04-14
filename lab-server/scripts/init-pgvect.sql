
-- PGVector Extension
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS embeddings (
  id SERIAL PRIMARY KEY,
  embedding vector,
  text text,
  created_at timestamptz DEFAULT now()
);

-- Create the langfuse database
CREATE DATABASE langfuse;

-- Create the langfuse user with the specified password
CREATE USER langfuse WITH ENCRYPTED PASSWORD 'langfuse';

-- Grant all privileges on the langfuse database to the langfuse user
GRANT ALL PRIVILEGES ON DATABASE langfuse TO langfuse;

-- Connect to the langfuse database
\c langfuse;

-- Grant usage and all privileges on the public schema to the langfuse user
GRANT ALL PRIVILEGES ON SCHEMA public TO langfuse;

-- Alter default privileges for tables created in the public schema
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO langfuse;

\! touch /var/lib/postgresql/data/db_init_completed
