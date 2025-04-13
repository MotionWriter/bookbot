def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(words):
    lower = words.lower()
    result = {}

    for i in lower:
        if i in result:
            result[i] += 1 
        else:
            result[i] = 1
    return result

def sort_on(dict):
    return dict["count"]

def sorted_list(dict):
    new_list = []

    for char,count in dict.items():
        char_dict = {"char": char, "count": count}
        new_list.append(char_dict)
    
    new_list.sort(reverse=True, key=sort_on)

    return new_list
    

