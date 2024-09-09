
print("Hello and welcome to the Uni_global favorite movies manager!!!")

favorite_movies = []

while True:
    command = input("enter: 'add' to add a movie 'remove' to remove a movie 'view' to view all movies 'exit' to exit: ")
        
    if command == "add":
        title = input("what is the title of the movie you want to add?: "),
        director = input("who is the movie director?: "),
        year = int(input("what year was the movie released? (dd/mm/yyyy): ")),
        favorite_movies.append({"title" : title, "director" : director, "year" : year})
        print("you have successfully added your movie")

    if command == "remove":
        title = input("what is the title of the movie you want to remove?: ")
        for movie in favorite_movies:
            if movie["title"] == title:
                favorite_movies.remove(movie)
        print("you have successfully removed this movie")
    
    if command == "view":
        print("these are the movies details: ")
        for movie in favorite_movies:
           
            
           print(f"title : {movie['title']}, director : {movie['director']}, year: {movie['year']} ")
                
                 
    if command == "exit":
        
     break
    print("thank you for visiting uni_global, we hope to see you soon, bye!!!")
      