from collections import Counter
def topKFrequent(words, k):
    word_counts = Counter(words)  # Count the frequency of each word
    sorted_words = sorted(word_counts.keys(), key=lambda word: (-word_counts[word], word))

    return sorted_words[:k] 


    # Example usage:
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
result = topKFrequent(words, k)
print(result)  # Output: ["i", "love"]

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
result = topKFrequent(words, k)
print(result)  # Output: ["the", "is", "sunny", "day"]