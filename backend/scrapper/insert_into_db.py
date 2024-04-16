import sqlite3
from get_movie import get_movies
from get_theatre_detail import get_theatre_details

# Create a connection to the database
conn = sqlite3.connect("real_movie_shit.db")
cursor = conn.cursor()

# tables = ['Movies', 'Theaters', 'Showtimes']

# # Delete all entries from each table
# for table in tables:
#     cursor.execute(f"DELETE FROM {table};")
#     conn.commit()

# List of movie data
movies_data = get_movies("kochi")
theatre_data = get_theatre_details("kochi")


print(movies_data)
# Insert each movie data into the table
for movie in movies_data:
    try:
        cursor.execute(
            "INSERT INTO Movies (name, image, inLanguage, duration, datePublished, movie_detail_link, summary, genre, casts, rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                movie["name"],
                movie["image"],
                movie["inLanguage"],
                movie["duration"],
                movie["datePublished"],
                movie["movie_detail_link"],
                movie["summary"],
                movie["genre"],
                movie["casts"],
                movie["rating"],
            ),
        )
    except sqlite3.IntegrityError:
        pass


# Commit the changes and close the connection
conn.commit()

for theater, theater_data in theatre_data.items():
    address = theater_data['address']
    try:
        cursor.execute("INSERT INTO Theaters (name, address) VALUES (?, ?)", (theater, address))
        conn.commit()  # Commit after each insertion
    except sqlite3.IntegrityError:
        pass

    # Insert data into the Showtimes table
    for movie, showtimes in theater_data['showtimes'].items():
        for showtime in showtimes:
            try:
                cursor.execute("INSERT INTO Showtimes (theater, movie, showtime) VALUES (?, ?, ?)", (theater, movie, showtime))
                conn.commit()
            except sqlite3.IntegrityError:
                pass

conn.close()
