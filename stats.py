def number_of_words(text):
    #lists how many words there are in a text
    words = text.split()
    return len(words)

def counting_letters(text):
    #lists how many times a letter occurs in the text
    char_count = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
    return char_count
        
def sorted_list(char_count):
    result = []
    for char, count in char_count.items():
        char_info = {'char': char, 'count': count}
        result.append(char_info)
    
    # Now we need to sort the list by the 'count' key
    # We'll use a helper function to tell sort() which value to use
    def sort_on(dict):
        return dict['count']
    
    # Sort in descending order (reverse=True)
    result.sort(reverse=True, key=sort_on)
    
    return result
    