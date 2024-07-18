from collections import Counter, defaultdict

letter_count = Counter("чукапабра")
print(len(letter_count))
print(letter_count)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)
word_count = Counter(words)
for word, count in word_count.items():
    print(f"{word}: {count}")

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

d = defaultdict(int)

# Збільшення значення для кожного ключа
d['a'] += 2
d['b'] += 1
d['a'] += 1

print(d)

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}

for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)

print(grouped_words)


words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(dict(grouped_words))
