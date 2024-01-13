class Movie:
    movieId = 0
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
        self.id = self.movieId
        self.movieId += 1

    def __repr__(self):
        return f"{self.title}, rated: {self.rating}"

# Flixnet handles all things movies, but doesn't manage a user session
class Flixnet:
    def __init__(self):
        self.movies = []
    
    def createMovie(self, title, rating):
        newMovie = Movie(title, rating)
        self.movies.append(newMovie)

    def getMovies(self):
        return self.movies

    # note with the way we have this setup flexnet has to know about the user watched array
    def watchMovie(self, user, title):
        for m in self.movies:
            if m.title == title:
                user.watched.append(m.id)
                return True
        return False

