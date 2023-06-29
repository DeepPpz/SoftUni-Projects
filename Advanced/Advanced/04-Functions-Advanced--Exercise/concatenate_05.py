def concatenate(*args, **kwargs):
    concatenated_string = ''.join(args)
    for (key, value) in kwargs.items():
        if key in concatenated_string:
            concatenated_string = concatenated_string.replace(key, value)

    return concatenated_string
