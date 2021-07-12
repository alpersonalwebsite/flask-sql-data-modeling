import psycopg2

connection = psycopg2.connect('dbname=test')
# If you want to use a different user conn = psycopg2.connect('dbname=test user=your_username')


# Open a cursor to perform database operations
# A cursor is an interface that allows us to start queing up work and transactions
cursor = connection.cursor()

# drop any existing my_tests table
cursor.execute("DROP TABLE IF EXISTS my_tests")

# (re)create the my_tests table
# (note: triple quotes allow multiline text in python)
cursor.execute("""
  CREATE TABLE my_tests (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
""")

cursor.execute('INSERT INTO my_tests (id, completed) VALUES (1, False);')

cursor.execute('SELECT * from my_tests')

result = cursor.fetchall()

print(result)

# commit, so it does the executions on the db and persists in the db
connection.commit()

cursor.close()
connection.close()