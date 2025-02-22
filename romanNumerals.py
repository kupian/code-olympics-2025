numeralDict = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

def optimiseNumerals(n):
    optimisedNumeral = ""
    for numeral, value in numeralDict.items():
        while n >= value:
            optimisedNumeral += numeral
            n -= value
    return optimisedNumeral

unoptimisedString = input().strip()

num = sum(numeralDict[c] for c in unoptimisedString)
optimisedString = optimiseNumerals(num)

print(optimisedString)
