import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database = "chinook")


# build cursor object (sset/list)
cursor = connection.cursor()

# Query1 - Select all records from artist table
cursor.execute('SELECT * FROM "Artist"')

# fetch results (multiple)
results = cursor.fetchall()


# fetch results (single)
# results = cursor.fetchone()


# close conneection
connection.close()


#print results
for result in results:
    print(result)