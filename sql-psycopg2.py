import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database= "chinook")


# build cursor object (sset/list)
cursor = connection.cursor()

# Query1 - Select all records from artist table
# cursor.execute('SELECT * FROM "Artist"')

# Query2 - Select only name from artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query3 - Select only Queen from artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s,' ["Queen"])

# Query4 - Select only artistId-51 from artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s,' [51])

# Query5 - Select only albums with "ArtistId"-51 from album table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s,' [51])

# Query6 - Select all tracks with composer queen
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s,' ["Queen"])




# fetch results (multiple)
# results = cursor.fetchall()


# fetch results (single)
results = cursor.fetchone()


# close conneection
connection.close()


# print results
for result in results:
    print(result)