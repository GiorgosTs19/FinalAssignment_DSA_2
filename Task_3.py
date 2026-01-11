# 2nd most Frequent Word
# Constraints :
#   - Words in the second input array are excluded from the "search"
#   - If there's a tie, we need the latest word occurrence in the array.
import string


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
    
    max_count_2 = -1
    latest_index_2 = -1
    most_frequent_word_2 = ""
    
    # Loop through words to find most and second-most frequent
    # Could've also sorted the dictionary by the occurrences and indexes,
    # but the single-loop approach is more efficient, though slightly more work.
    for word, (count, index) in word_occurrences.items():
        # If we find a new max, or we have a tie with latest index
        if count > max_count or (count == max_count and index > latest_index):
            # Shift current max to second-max
            if most_frequent_word:
                most_frequent_word_2 = most_frequent_word
                max_count_2 = max_count
                latest_index_2 = latest_index
            most_frequent_word = word
            max_count = count
            latest_index = index
        # If we find a new second-max or a tie with second-latest index
        elif count > max_count_2 or (count == max_count_2 and index > latest_index_2):
            most_frequent_word_2 = word
            max_count_2 = count
            latest_index_2 = index
    
    return most_frequent_word_2
    
# Test
print(findMostFrequentWord(
  ["apple", "orange", "apple", "orange", "banana", "orange", "apple"],
  ["banana"]
))

# Most frequent word
# Hard-coded excluded words list -> “a”, “the”, “in”, “of”, “and”, “to”, “be”, “is”.
excluded_words = ['a', 'the', 'in', 'of', 'and', 'to', 'be', 'is']
# No tie constraints

def findMostFrequentWordInText(text: str) -> str:
    # There might be punctuation included in the string, so this needs to be stripped away.
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    
    word_occurrences = {}
    # Loop through each word in the input list
    for index, word in enumerate(words):
        # 1st constraint, check whether the word is excluded.
        # and ignore.
        if word in excluded_words:
            continue
        else:
            # If we've already seen the word, increment its count
            if word not in word_occurrences:
                # We store both the count and the latest index of occurrence
                # to meet the tie constraints (return the latest one in case of a tie)
                word_occurrences[word] = 1
            # Otherwise just add it to  the dictionary and set its count to 1
            else:
                word_occurrences[word] += 1
    
    # Now we need to find the most frequent word.
    # Way simpler than before, since we don't have tie constraints.
    most_frequent_word = ""
    max_count = 0
    
    # Loop through words to find the most frequent
    for word, count in word_occurrences.items():
        # Update the word every time we find a new max.
        if count > max_count :
            most_frequent_word = word
            max_count = count
    
    return most_frequent_word

print(findMostFrequentWordInText('This is the way. The way is shut. The door is the end.'))