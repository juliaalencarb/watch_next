# Importing spacy.
import spacy


def find_next_movie(description):
    """Receives a movie description and returns the most similar movie in 'movies.txt' using spacy.similarity."""
    with open("movies.txt", "r") as f:  # Reading 'movies.txt' lines.
        movies = f.readlines()

        model_sentence = nlp(description)  # Establishing which sentence will be the reference.
        highest_similarity = 0  # Creating helper variables.
        chosen_movie = ''
        for movie_description in movies:  # Looping through all movies and finding the most similar title.
            similarity = nlp(movie_description[9:]).similarity(model_sentence)
            if similarity >= highest_similarity:
                highest_similarity = similarity
                chosen_movie = movie_description
    return f"Your next movie is '{chosen_movie[:7]}' with a similarity of {highest_similarity}!"


# Specifying the model to be used.
# IMPORTANT: this model must be installed:
# >>> python -m spacy download en_core_web_md
nlp = spacy.load('en_core_web_md')

# Declaring variable holding the movie's reference to be analyzed to find next similar title.
previously_watched = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet Sakaar where he is sold into slavery 
and trained as a gladiator."""


# Calling find_next_movie() function and printing out the result.
print(find_next_movie(previously_watched))
