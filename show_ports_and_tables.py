from sqlalchemy import create_engine, text

# Replace with your actual MySQL username and password
USER = "root"
PASSWORD = "password"
HOST = "localhost"

# Common MySQL ports to check
ports = [3306, 33060]

for port in ports:
    try:
        engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{port}/")
        with engine.connect() as conn:
            result = conn.execute(text("SHOW DATABASES;"))
            dbs = [row[0] for row in result]
            print(f"\nPort {port} has databases: {dbs}")
            if "PythonTable" in dbs:
                print(f"✅ Found 'PythonTable' on port {port}!")
    except Exception as e:
        print(f"\nCould not connect on port {port}: {e}")