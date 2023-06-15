def forecast(*raw_data):
    weather_data = {'Sunny': [], 'Cloudy': [], 'Rainy': []}
    for (location, weather) in raw_data:
        weather_data[weather].append(location)

    end_result = ''
    for (key, value) in weather_data.items():
        for location in sorted(value):
            end_result += f'{location} - {key}\n'

    return end_result
