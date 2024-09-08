def find_anagrams(word, candidates):
    word_sorted = sorted(word.lower())  # Sort the word letters and make them lowercase
    anagrams = []

    for item in candidates:
        if item.lower() == word.lower():
            continue  # Skip exact matches
        if sorted(item.lower()) == word_sorted:  # Compare sorted letters
            anagrams.append(item)

    return anagrams


# Testing the function
print(find_anagrams("good", ["dog", "goody"]))  # Should return []
print(
    find_anagrams(
        "allergy", ["gallery", "ballerina", "regally", "clergy", "largely", "leading"]
    )
)  # Should return ["gallery", "regally", "largely"]
print(
    find_anagrams("Orchestra", ["cashregister", "Carthorse", "radishes"])
)  # Should return ["Carthorse"]
