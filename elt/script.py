import subprocess
import time



def wait_for_postgres(host, max_reties=5, delay_seconds=5):
    #This allows to become available during wait
    retries=0
    while retries < max_reties:
        try:
            result= subprocess.run(
                ["pg_isready", "-h", host], check=True, capture_output=True, text=True
            )
            if "accepting connections" in result.stdout:
                print("Sucessfully conected to PostgreSQL!")
                return True
        except subprocess.CalledProcessError as e:
            print(f"Error connecting to PostgreSQL: {e}")
            retries += 1
            print(
                f"Retry in {delay_seconds} seconds... (Attempt {retries/{{max_reties}}})"
            )
            time.sleep(delay_seconds)
    print("Max retries reached. Exiting...")
    return False

if not wait_for_postgres(host= "source_postgres"):
    exit(1)

    print("Starting ELT script...")

#Config for source PostgreSQL DB
source_config = {
    "dbname": "source_db",
    "user": "postgres",
    "password": "secret",
    "host": "source_postgres"
}

#Config for destination PostgreSQL DB
destination_config = {
    "dbname": "destination_db",
    "user": "postgres",
    "password": "secret",
    "host": "destination_postgres"
}

#Dump source db
dump_command = [
    'pg_dump',
    '-h', source_config['host'],
    '-U', source_config['user'],
    '-d', source_config['dbname'],
    '-f', 'data_dump.sql',
    '-w'
]

subprocess_env = dict(PGPASSWORD=source_config["password"])

subprocess.run(dump_command, env=subprocess_env, check=True)

#Prepare Load command
load_command = [
    'psql',
    '-h', destination_config['host'],
    '-U', destination_config['user'],
    '-d', destination_config['dbname'],
    '-a', '-f', 'data_dump.sql',
]


subprocess_env = dict(PGPASSWORD=destination_config["password"])

subprocess.run(load_command, env=subprocess_env, check=True)

print("Ending ETL Script...")