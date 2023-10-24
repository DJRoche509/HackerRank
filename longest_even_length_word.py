'''
LONGEST EVEN LENGTH WORD

Consider a string, sentence, of words separated by spaces where each word is a substring consisting of English alphabetic letters only. FInd the first word in the sentence that has a length which is both an even number and greater than or equal to the length of any other word of even length in the sentence. If there are multiple words meeting the criteria, return the one which occurs first in the sentence. 
Example:  If the input, sentence = "Time to write great code", the output should be Time
Example2: If the input, sentence = "hey", the output should be "00"
Example3: If the input, sentence = "You can do it the way you like", the output should be "like".

'''

def longest_even_length_word(sentence):
    words = sentence.split()
    longest_word = ''

    longest_word = max ((word for word in words if len(word) % 2 == 0), default = None, key= len ) 
    return longest_word if longest_word else '00'


'''
ALTERNATE SOLUTION

def longest_even_length_word(sentence):
    words = sentence.split()
    even_length_words = [word for word in words if len(word) % 2 == 0]
    
    if even_length_words:
        even_length_words.sort(key=len,reverse=True)
        return even_length_words[0]
    else:
        return "00"
'''


# Example Usage
sentence1 = "Time to write great code"
sentence2 = "hey"
sentence3 = "You can do it the way you like"

result1 = longest_even_length_word(sentence1)
result2 = longest_even_length_word(sentence2)
result3 = longest_even_length_word(sentence3)

print(result1)  # Output: "Time"
print(result2)  # Output: "00"
print(result3)  # Output: "like"