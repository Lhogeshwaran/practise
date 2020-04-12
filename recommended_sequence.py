D = {"able", "ale", "apple", "bale", "kangaroo"}
S = "abppplee"

# Edge-cases
D.add("thisistocheck")  # Words longer than S.
D.add("abppp")  # Multiple correct words.
D = {"no", "possible", "words"}  # No combinations.

# Word longer than S can be automatically ignored.
E = {x: len(x) for x in D if len(x)<=len(S)}

# As the goal is to find the longest word, let's sort the words in descending order.
# However, as Google only offers python 3.5 for the challenge, ordering within dict is not an option!! 
F = {k: v for k, v in sorted(E.items(), key=lambda item: item[1], reverse=True)}

S_ls = [x for x in S]

present_words = {}

for k, v in F.items():

    tmp_W = [x for x in k]
    checked_indexes = []

    for i in tmp_W:

        if tmp_W.index(i) == 0:
            if i in S_ls:
                checked_indexes.append(S_ls.index(i))
            else:
                checked_indexes = [0]

        else:
            if i in S_ls[checked_indexes[-1]+1:]:
                checked_indexes.append(S_ls[checked_indexes[-1]+1:].index(i)+checked_indexes[-1]+1)

        word = [S_ls[x] for x in checked_indexes]

        if word == tmp_W:
            present_words["".join(word)] = len("".join(word))

if bool(present_words) == True:
    answer = [key for m in [max(present_words.values())] for key,val in present_words.items() if val == m]
else:
    answer = ""

print(f"The word is: {answer}")
