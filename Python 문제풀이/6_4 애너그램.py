# A.    입력 예시 
#lst = ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

lst = ['eat','tea','tan','ate','nat','bat']

def group_anagrams(lst):
    result = {}
    for words in lst:
        sorted_words = str(sorted(words))
        

        if sorted_words in result:
                result[sorted_words].append(words)
        else:  
            result[sorted_words] = [words]

    return(list(result.values()))

print(group_anagrams(lst))










