from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Boolean, MetaData


db_string = "postgres://your_username:@localhost/test"

db = create_engine(db_string)

db.execute("DROP TABLE IF EXISTS my_tests")

meta = MetaData(db)

# Create
tests = Table('my_tests', meta,
              Column('id', Integer, primary_key=True),
              Column('completed', Boolean, default=False, nullable=False))

with db.connect() as conn:
    tests.create()

    ins = tests.insert().values(
        id=1,
        completed=False
    )
    conn.execute(ins)

    # Read
    sel = tests.select()
    result_set = conn.execute(sel)

    for r in result_set:
        print(r)
