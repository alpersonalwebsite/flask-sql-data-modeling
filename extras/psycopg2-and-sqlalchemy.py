from sqlalchemy import create_engine

db_string = "postgres://your_username:@localhost/test"

db = create_engine(db_string)

# Create
db.execute("DROP TABLE IF EXISTS my_tests")
db.execute(
    "CREATE TABLE my_tests (id INTEGER PRIMARY KEY, completed BOOLEAN NOT NULL DEFAULT False)")
db.execute("INSERT INTO my_tests (id, completed) VALUES (1, False)")

# Read
result_set = db.execute("SELECT * FROM my_tests")

for r in result_set:
    print(r)
