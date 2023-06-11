def movie_organizer(*movies_list):
    movies_library = {}
    for (movie, genre) in movies_list:
        if genre not in movies_library:
            movies_library[genre] = []
        movies_library[genre].append(movie)

    movies_library = dict(sorted(movies_library.items(), key=lambda x: (-len(x[1]), x[0])))

    end_result = ''
    for (genre, movies) in movies_library.items():
        end_result += f'{genre} - {len(movies)}\n'
        for movie in sorted(movies):
            end_result += f'* {movie}\n'
    return end_result
