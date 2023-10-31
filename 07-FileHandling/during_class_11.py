film_titles = ["House of teh Dragon", "Game of Thrones", "Batman", "Spider-Man", "Avengers"]

file = open("films.txt", "w")
for tittle in film_titles:
    file.write(tittle)
    file.write("\n")
file.close()
    