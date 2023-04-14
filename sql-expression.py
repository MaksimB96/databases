import sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing from local database 'chinook'
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# Create Var for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)


# Create Var for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)


# Create Var for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)



# making the connection
with db.connect() as connection:

    # Query 1 - select all records from artist table
    # select_query = artist_table.select()

    # Query2 - Select only name from artist table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query3 - Select only Queen from artist table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen" )

    # Query4 - Select only artistId-51 from artist table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51 )

    # Query5 - Select only albums with "ArtistId"-51 from album table
    # select_query = album_table.select().where(artist_table.c.ArtistId == 51 )

    # Query6 - Select all tracks with composer queen
    select_query = track_table.select().where(track_table.c.Composer == "Queen" )



    results = connection.execute(select_query)
    for result in results:
        print(result)

