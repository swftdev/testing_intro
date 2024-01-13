from getpass import getpass 
from service.flixnet import Flixnet
from service.user import UserService

def movieMenu(user, flixnet):
    while True:
        print("""
1. create movie
2. list movies
3. watch movie
4. favorite movie
5. exit""")
        inp = input("> ")

        match inp:
            case "1":
                title = input("title: ")
                rating = input("rating: ")
                flixnet.createMovie(title, rating)
            case "2":
                print(flixnet.getMovies())
            case "3":
                print("What would you like to watch?")
                print(flixnet.getMovies())
                title = input("title: ")
                success = flixnet.watchMovie(user, title)
                if not success:
                    print("can't find a movie with that title to watch")
            case "4":
                pass
            case "5":
                exit()

def getUser(userService):
    while True:
        print("""
    1. login
    2. sign-up
    3. exit
    """)
        inp = input("> ")

        match inp:
            case "1":
                username = input("username: ")
                password = getpass("password: ")
                user = userService.signIn(username, password)
                if user:
                    return user

                print("Failed to find matching user/password combo")

            case "2":
                username = input("username: ")
                password = getpass("password: ")
                userService.signUp(username, password)

            case "3":
                exit()

if __name__ == "__main__":
    flixnet = Flixnet()
    userService = UserService()

    user = getUser(userService)
    movieMenu(user, flixnet)