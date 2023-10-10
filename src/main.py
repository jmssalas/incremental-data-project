import os
import sqlite3
from neo4j import GraphDatabase

URI = os.getenv("NEO4J_DB_HOST") + ":" + os.getenv("NEO4J_DB_PORT")
AUTH = (os.getenv("NEO4J_DB_USER"), os.getenv("NEO4J_DB_PASS"))

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    try: 
        driver.verify_connectivity()
        print("Connected to Neo4j database")
    except Exception as error:
        print("ERROR Connecting to Neo4j database:", error)

    driver.close()

con = sqlite3.connect(os.getenv("SQLITE_DB"))
print("Connected to sqlite database")

con.close()