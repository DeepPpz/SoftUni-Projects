def add_songs(*songs_input):
    songs_data = {}

    for (song, lyrics) in songs_input:
        if song not in songs_data:
            songs_data[song] = []

        for line in lyrics:
            songs_data[song].append(line)

    end_result = ''
    for (song, lyrics) in songs_data.items():
        end_result += f'- {song}\n'
        for line in lyrics:
            end_result += f'{line}\n'
    return end_result
