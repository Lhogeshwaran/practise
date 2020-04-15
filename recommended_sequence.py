D = {"able", "ale", "apple", "bale", "kangaroo"}
S = "abppplee"

# Edge-cases
D.add("thisistocheck")  # Words longer than S.
D.add("abppp")  # Multiple correct words.
### D = {"no", "possible", "words"}  # No combinations.

# Word longer than S can be automatically ignored.
#E = {x: len(x) for x in D if len(x)<=len(S)}

# As the goal is to find the longest word, let's sort the words in descending order.
# However, as Google only offers python 3.5 for the challenge, ordering within dict is not an option!! 
#F = {k: v for k, v in sorted(E.items(), key=lambda item: item[1], reverse=True)}
E = [x for x in sorted(D, key=lambda i: len(i), reverse=True) if len(x) <= len(S)]

present_words = {}

for i in E:

  checked_indexes = []

  for j in i:

    if i.index(j) == 0:
      if j in S:
        checked_indexes.append(S.index(j))
      else:
        checked_indexes = [0]

    else:
      if j in S[checked_indexes[-1]+1:]:
        checked_indexes.append(S[checked_indexes[-1]+1:].index(j)+checked_indexes[-1]+1)

    word = ''.join([S[x] for x in checked_indexes])

    if word == i:
      present_words[word] = len(word)

''' Replacing dict with list to reduce memory usage.
for k, v in F.items():

    checked_indexes = []

    for i in k:

        if k.index(i) == 0:
            if i in S:
                checked_indexes.append(S.index(i))
            else:
                checked_indexes = [0]

        else:
            if i in S[checked_indexes[-1]+1:]:
                checked_indexes.append(S[checked_indexes[-1]+1:].index(i)+checked_indexes[-1]+1)

        word = ''.join([S[x] for x in checked_indexes])

        if word == k:
            present_words[word] = len(word)
'''

if bool(present_words):
    answer = [key for m in [max(present_words.values())] for key,val in present_words.items() if val == m]
else:
    answer = ""

print(f"The word is: {', '.join([x for x in answer])}")


def sleep_in(weekday, vacation):
  
  if (weekday == False and vacation == False):
    return True
  else if (weekday == False and vacation == True):
    return True
  else:
    return False

def parrot_trouble(talking, hour):
  if (hour < 7 or hour  > 20):
    trouble = True
  else:
    trouble = False
    
  return talking == trouble


ls = [1, 4, 7, 13, 43, 23, 52, 19, 0]


def has22(nums):
  
  check =  False
  case = False
  
  for i in nums:
    
    if i == 2 and not check:
      check = True
      continue
    
    if i == 2 and check:
      case = True
      
  return case or check


D = {"able", "ale", "apple", "bale", "kangaroo"}
S = "abppplee"

# Check and eliminate words in D longer than S
# Sort the list based on length of string
D = sorted([x for x in D if len(x) <= len (S)], key=len, reverse=True)

for i in D:

  for j in range(len(i)):
    if i[j] == S[j]



def balcheck(ls):

  bal_l = 0
  bal_r = 0

  for i in range(len(ls)):

    bal_l = sum(ls[:i])
    bal_r = sum(ls[i:])

    if bal_l == bal_r:
      return True, i, bal_l, bal_r, ls[:i], ls[i:]
      break

    bal_l = 0
    bal_r = 0
    
  return False


def withoutString(base, rem):

  return ''.join([x for x in base.lower() if x not in rem.lower()])


def sumNumbers(str):

  digit = False
  num = []
  nums = [0]

  for i in str:

    if i.isdigit():
      num.append(i)
      digit = True
      continue

    digit = False
    try:
      nums.append(int(''.join(num)))
    except:
      ValueError
    num = []

  return sum(nums)
