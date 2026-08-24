import json

# Imagine you asked a movie database API for info, and it 
# sent you back this giant block of raw text (a string).
raw_text_from_internet = """
{
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
    "imdb_rating": 8.8
}
"""

# Right now, Python just sees a giant string of letters.
# If you tried to print raw_text_from_internet["title"], Python would crash with an error!

print("Type BEFORE loads:", type(raw_text_from_internet)) # <class 'str'>


# --- THE MAGIC STEP ---
# We load the String (loads) and turn it into a Python dictionary
movie_data = json.loads(raw_text_from_internet)


print("Type AFTER loads:", type(movie_data)) # <class 'dict'>

# Now it is a real Python dictionary, and you can easily pull exactly what you want out of it:
print(f"The movie {movie_data['title']} was directed by {movie_data['director']}.")
print(f"The lead actor is {movie_data['cast'][0]}.")