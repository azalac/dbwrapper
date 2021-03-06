
# dbwrapper

## Note: this library is pre-alpha.

This version of dbwrapper is highly subject to change. Due to this, I won't be documenting a lot of the API. I tried to make the code fairly readable and code-suggestion friendly. I'm not planning on changing the structure of the major classes, but function arguments will definitely change and features will definitely be removed or addded.

dbwrapper is a lightweight python library designed to simplify interacting with databases of all kinds. This is not an ORM, and I have no plans to make it one. dbwrapper allows programmers to easily create queries using a fluent API. The primary focus of this library is to make data persistance database-agnostic while keeping query overhead low.

## Supported Databases

- SQLite
- PostgreSQL

## Databases with planned support

- SQL Server
- MySQL
- MongoDB

## Features

- SELECT, UPDATE, INSERT, DELETE statements
- Table Creation (via a Builder)
- Migrations
    - Note: Migrations are not automatically created, you have full control over these!
- List Tables
- List Table Columns
- 'Type Safe' Table and Column retreival
    - Only the presence of tables & columns is validated. Verifying the datatype would incur too much overhead.
- Aliasing for Tables and Columns
- SQL Functions (partially implemented)
- Connection Pooling
- Built in logging and query profiling (just enable it using logging.basicConfig)
- Common Table Expressions & Subqueries

## Simple Example Usage

```Python
from dbwrapper import sqlite # or postgresql

# If using PostgreSQL, the connection string will need to be changed
connection = sqlite.Connection("data.db")

db = connection.database(sqlite.MASTER_DB)

if "test" not in db.tables:
    with db.table("test").builder() as builder:
        builder.column("id", db.dtypes.integer)
        builder.column("a", db.dtypes.varchar)
        builder.column("b", db.dtypes.float)
        
        builder.primary_key("id", autoincrement=True)

test = db.tables.test

test.delete().execute() # delete everthing

for i in range(5):
    test.insert_one({
        test.columns.a: "hello world!",
        test.columns.b: i / 5
    })

# no parameters for select() = all columns
results = test.select(
        test.columns.id,
        test.columns.a,
        test.columns.b
    ) \
    .where(test.columns.b <= 0.5) \
    .execute()

print(results)

connection.close() # optional, but good practice
```
