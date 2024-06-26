from collections import Counter
word = str(input())
lister = []
for i in word:
    lister.append(i)

counts = Counter(lister)
print(counts.most_common())
