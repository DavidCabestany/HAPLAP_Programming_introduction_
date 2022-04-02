def super_anagrams(word1, word2):
    if word1[0] == word2[0] and word1[-1] == word2[-1] and len(word1) == len(word2):
        return 'Super Anagram!'
    else:
        return 'What?'