

def string_list(words):
    result = [x[::-1]for x in words]
    return result


word_list = ["apple","anirudh","priyanka","trisha","anirudh"]
print(string_list(word_list))