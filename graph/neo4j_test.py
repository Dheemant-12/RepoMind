from neo4j import GraphDatabase

URI = "neo4j+s://66a8e799.databases.neo4j.io"
AUTH = (
    "66a8e799",
    "2VPsUy1NUlJwxk7qHSpzFgiBh3XNWypUjQq__2K1y68"
)

driver = GraphDatabase.driver(URI, auth=AUTH)

try:
    with driver.session(database="66a8e799") as session:
        result = session.run("RETURN 1 AS num")
        print(result.single()["num"])

except Exception as e:
    print(type(e))
    print(e)

finally:
    driver.close()