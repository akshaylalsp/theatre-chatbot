import sqlite3
from modules.get_movie import get_movies
from modules.get_theatre_detail import get_theatre_details

class SetupDb:
    def __init__(self,location) -> None:       
        self.insert_into_db(location=location)


    def insert_into_db(self,location):
        self.delete_all_entries()
        conn = sqlite3.connect("movie.db")
        cursor = conn.cursor()
        self.movies_data = get_movies("kochi")
        self.theatre_data = get_theatre_details("kochi")
        for movie in self.movies_data:
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

        for theater, theater_data in self.theatre_data.items():
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

    def delete_all_entries(self):
        conn = sqlite3.connect("movie.db")
        cursor = conn.cursor()
        tables = ['Movies', 'Theaters', 'Showtimes']
        # Delete all entries from each table
        for table in tables:
            cursor.execute(f"DELETE FROM {table};")
            conn.commit()
        conn.close()
        