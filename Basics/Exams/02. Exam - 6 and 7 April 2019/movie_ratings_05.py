total_movies = int(input())
average_rating = 0
best_movie, highest_rating = "", 0
worst_movie, lowest_rating = "", 100

for i in range(total_movies):
    movie_name = input()
    movie_rating = float(input())

    average_rating += movie_rating

    if movie_rating > highest_rating:
        best_movie = movie_name
        highest_rating = movie_rating
    if movie_rating < lowest_rating:
        worst_movie = movie_name
        lowest_rating = movie_rating

average_rating /= total_movies

print(f"{best_movie} is with highest rating: {highest_rating:.1f}")
print(f"{worst_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
