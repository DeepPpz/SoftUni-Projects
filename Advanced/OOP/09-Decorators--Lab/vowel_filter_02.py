def vowel_filter(function):
    def wrapper():
        all_letters = function()
        all_vowels = list(filter(lambda x: x.lower() in "aeiouy", all_letters ))
        return all_vowels
    
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters())
