# from collections import OrderedDict

sentence = input("Write your string! ").lower()
char_list = list(sentence)
count = {}

for char in char_list:
    if char not in count.keys():
        count[char] = 1
    else:
        count[char] += 1
count_ordered = sorted(count.items())
# # count_ordered = OrderedDict(sorted(count.items()))
for k,v in count_ordered:
    print(k,v)


