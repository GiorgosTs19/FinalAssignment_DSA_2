# Most Frequent Word

def findMostFrequentWord(inputList1: list[str], inputList2:list[str]) -> str:
    word_occurrences = {}
    # Loop through each word in the input list
    for index, word in enumerate(inputList1):
        # 1st constraint, check whether the word is excluded.
        # and ignore.
        if word in inputList2:
            continue
        else :
            # If we've already seen the word, increment its count
            if word not in word_occurrences:
                # We store both the count and the latest index of occurrence
                # to meet the tie constraints (return the latest one in case of a tie)
                word_occurrences[word] = [1, index]
            # Otherwise just add it to  the dictionary and set its count to 1
            else:
                word_occurrences[word] = [word_occurrences[word][0] + 1, index]
                
    # In order to find the 2nd most frequent word,
    # we need to somehow keep track of the 2nd max count
    most_frequent_word = ""
    max_count = 0
    latest_index = -1
    
    second_max_count_2 = 0
    max_count_2 = 0
    latest_index_2 = -1
    
    # Loop over the dictionary values
    for word, (count, index) in word_occurrences.items():
        if count > max_count:
            max_count = count
            most_frequent_word = word
            latest_index = index
        elif count > max_count_2 > max_count:
            max_count_2 = count
    
    return most_frequent_word
    
# Test
print(findMostFrequentWord(
  ["apple", "orange", "apple", "orange", "banana", "orange", "apple"],
  ["banana"]
))