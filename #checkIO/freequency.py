line = 'pritpraaaaaaaAaaaaaaaaaaaOOOOOOOOOOOeitpoefffffffffffffffffffriLSDKJFSDIUOSERUNOSEIUCNOEIUNOWEIUCNMWVECWVECWVECtpoeritpoeirtpoeitpowioqwiuyenxcnbvsdfnbsvnbvasndbvas'

dict_char_frequencies = {}
total_chars = 0
different_chars = 0
lst_top_chars = []

for char in line:
    if char.lower() in dict_char_frequencies.keys():
        dict_char_frequencies[char.lower()] += 1
        total_chars += 1
    else:
        if char.isalpha():
            dict_char_frequencies[char.lower()] = 1
            different_chars += 1
            total_chars += 1

lst_frequencies = sorted(dict_char_frequencies.items(), key=lambda item: item[1], reverse=True)

first_frequency = lst_frequencies[0][1]
for i in range(different_chars):
    print(lst_frequencies[i][0], lst_frequencies[i][1])
    if first_frequency == lst_frequencies[i][1]:
        lst_top_chars.append(lst_frequencies[i][0])

lst_top_chars.sort()

print(len(line))
print(lst_top_chars[0])


