D = {"able", "ale", "apple", "bale", "kangaroo"}
S = "abppplee"

# Word longer than S can be automatically ignored.
D.add("thisistocheck")
E = {x: len(x) for x in D if len(x)<=len(S)}

# As the goal is to find the longest word, let's sort the words in descending order.
# However, as Google only offers python 3.5 for the challenge, ordering within dict is not an option!! 
F = {k: v for k, v in sorted(E.items(), key=lambda item: item[1], reverse=True)}

S_ls = [x for x in S]

for k, v in F.items():

    S_ls = [x for x in S]
    tmp_W = [x for x in k]

    tmp_hold = []
    
    for i in tmp_W:

            if i in S_ls:
                tmp_S_ind = S_ls.index(i)

                if tmp_S_ind != 0:
                    for j in range(tmp_S_ind):
                        tmp_hold.append(S_ls[j])
                        S_ls.remove(S_ls[j])
                else:
                    tmp_hold.append(S_ls[0])
#                    S_ls.remove(S_ls[0])

#                tmp_W.pop(tmp_W.index(i))


for k, v in F.items():

    S_ls = [x for x in S]
    tmp_W = [x for x in k]
    
    tmp_S_ind = {}

    for i in tmp_W:

            if i in S_ls:
                tmp_S_ind.setdefault(i, [])
                tmp_S_ind[i].append(S_ls.index(i))

                if tmp_S_ind != 0:
                    for j in range(S_ls.index(i)):
                        S_ls.remove(S_ls[j])
                else:
                    S_ls.remove(S_ls[0])

#                tmp_W.pop(tmp_W.index(i))


for k, v in F.items():

    tmp_W = [x for x in k]

    checked_indexes = []

    for i in tmp_W:

        if tmp_W.index(i) == 0:
            if i in S_ls:
                checked_indexes.append(S_ls.index(i))

        else:
            if i in S_ls[checked_indexes[-1]+1:]:
                checked_indexes.append(S_ls[checked_indexes[-1]+1:].index(i)+checked_indexes[-1]+1)

        word = [S_ls[x] for x in checked_indexes]

        print(word)