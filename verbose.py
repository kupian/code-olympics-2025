number = input().split(" ")

DIGITS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "fourty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90
}

MAGNITUDES = {
    "hundred": 100,
    "thousand": 1000,
    "million": 1000000
}

MAGNITUDE_ORDER = {
    "million": 1,
    "thousand": 2,
    "hundred": 3,
}

final_number = 0
last_chunk_idx = -1

def get_further_multiplier(number, a, multiplier):
    for i in range(a,len(number)):
        further_word = number[i]
        if further_word in MAGNITUDES and MAGNITUDE_ORDER.get(further_word) < MAGNITUDE_ORDER.get(multiplier):
           return MAGNITUDES.get(further_word)
    return 1

def point_to_multiply_from(number, a, multiplier):
    for i in range(a, 0, -1):
        prev_word = number[i]
        if prev_word in MAGNITUDES and MAGNITUDE_ORDER.get(prev_word) < MAGNITUDE_ORDER.get(multiplier):
            return i+1
    return 0
    

for i,word in enumerate(number):
    if word in MAGNITUDES:
        number_to_add = 0
        multiplier = 1
        
        if i == len(number)-1:
            chunk = number[point_to_multiply_from(number, i, word):]
            multiplier = MAGNITUDES.get(word)
        else:
            if number[i+1] in MAGNITUDES:
                next_word = number[i+1]
                magnitude = MAGNITUDES[word] * MAGNITUDES[next_word]
                chunk = number[last_chunk_idx+1 : i]
                i += 1
            else:
                magnitude = MAGNITUDES[word]
                chunk = number[last_chunk_idx+1 : i]
                multiplier = get_further_multiplier(number, i, word)

        last_chunk_idx = i
        
        for digit in chunk:
            number_to_add += DIGITS.get(digit,0) * magnitude
        
                
        final_number += number_to_add * multiplier
            
for remaining_digit in number[last_chunk_idx+1:]:
    final_number += DIGITS.get(remaining_digit, 0)
    
final_number = [char for char in str(final_number)]
for i in range(len(final_number)-3, 0, -3):
    final_number.insert(i, ",")
    
final_number = "".join(final_number)
    

print(final_number)