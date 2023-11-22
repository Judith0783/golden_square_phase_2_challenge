def get_most_common_letter(text):
    counter = {}
    for char in text:
        print(counter)
        counter[char] = counter.get(char, 0) + 1
    counter.pop(" ")
    most_common = max(counter, key=counter.get)
    return most_common


"""def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), key=lambda item: item[1])[0][1]
    return letter
"""

print(f"""
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
