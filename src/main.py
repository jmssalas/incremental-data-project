import os
import sqlite3
from neo4j import GraphDatabase
from create_raw_layer import create_raw_layer

URI = os.getenv("NEO4J_DB_HOST") + ":" + os.getenv("NEO4J_DB_PORT")
AUTH = (os.getenv("NEO4J_DB_USER"), os.getenv("NEO4J_DB_PASS"))
AIRBYTE_TABLE_BY_PLATFORM = {
    "netflix": "_airbyte_raw_netflix",
    "amazon_prime": "_airbyte_raw_amazon_prime",
    "disney_plus": "_airbyte_raw_disney_plus",
}
RAW_LAYER_TABLE = "raw_layer_unified_platforms"

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    try:
        driver.verify_connectivity()
        print("Connected to Neo4j database")
    except Exception as error:
        print("ERROR Connecting to Neo4j database:", error)

    driver.close()

con = sqlite3.connect(os.getenv("SQLITE_DB"))
print("Connected to sqlite database")

create_raw_layer(con, AIRBYTE_TABLE_BY_PLATFORM, RAW_LAYER_TABLE)

con.close()
