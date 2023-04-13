import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database = "chinook")


# build cursor object (sset/list)
cursor = connection.cursor()


# fetch results (multiple)
results = cursor.fetchall()


# fetch results (single)
# results = cursor.fetchone()


# close conneection
connection.close()


#print results
for result in results:
    print(result)