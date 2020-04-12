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
    tmp_W = [x for x in k]

    for i in tmp_W:

#        if tmp_W.index(i) == 0:

            if i in S_ls:
                tmp_S_ind = S_ls.index(i)

                if tmp_S_ind != 0:
                    for j in range(tmp_S_ind):
                        S_ls.remove(S_ls[j])
                else:
                    S_ls.remove(S_ls[0])

            tmp_W.pop(tmp_W.index(i))



                        try:
                            S_ls.remove(S_ls[j])
                        except:
                            IndexError
        
        if tmp_W.index(i) != 0:

            tmp_S_ind = 0

            if i in S_ls:
                tmp_S_ind = S_ls.index(i)
            
            if tmp_S_ind > 0:
                for j in range(tmp_S_ind):

                