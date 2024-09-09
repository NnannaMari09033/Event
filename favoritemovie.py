print("Welcome to the best movie selections!!!")

Favorite_movie = []

while True:
  command = input("Enter 'add' to add a movie (or 'remove' to remove a movie) (or 'view' to view all movies) (or'exit' to exit the program):")
  if command == "add":
    movie_title = input("enter the title of the movie: ")
    director = input("enter the director of the movie: ")
    release_year = int(input("enter the release year of the movie: "))
    Favorite_movie.append({"movie_title": movie_title, "director": director, "release_year": release_year})
    print("yo! congratulations the movie has been added succesfully")
  
  if command == "remove":
    movie_title = input("input the title of the movie you want: ")
    for movie in Favorite_movie:
      if movie["movie_title"] == movie_title:
        Favorite_movie.remove(movie)
        print("heyai! you have removed the movie o")
        break
  
  if command == "view":
    print("List of all the favorite movies: ")
    for movie in Favorite_movie:
      print(f"Title: {movie['movie_title']}, Director: {movie['director']}, Release Year: {movie['release_year']}")
  
  if command == "exit":
    break