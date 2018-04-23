'''
 - Enter 'a' to add a movie, 'l' to see yout mivies, 'f' to fin a movie, and 'q; to quit:

 -Add movies
 - See movies
 - Find a movie
 -Stop running the program '''


movies = []

# Showing the menu to user and adding required main functions
def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to fin a movie, and 'q; to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input =='f':
            find_movies()
        else:
            print('Unknown command - please try again.')
        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to fin a movie, and 'q; to quit: ")
    if user_input =='q':
        print("You bastard I'm exiting the program! :)")

# Adding movie into database
def add_movie():
    movie_name = input('What is the name of the movie: ')
    movie_director = input('Who is the director of the movie: ')
    movie_year = int(input('What is the year of the movie: '))

    movies.append({
        'name': movie_name,
        'director': movie_director,
        'year': movie_year
    })

def show_movies():
    for i in movies:
        print(f"Name: {movie['name']}")
        print(f"Director: {movies['director']}")
        print(f"Release Year: {movies['year']}")

def find_movies():



menu()











