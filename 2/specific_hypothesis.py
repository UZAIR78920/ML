S=['sunny','warm','normal','strong']
new_example=['sunny','warm','high','strong']
print("Before generalizer:", S)
for i in range(len(S)):
    if S[i]!=new_example[i]:
        S[i]='?'
print("After generalize:", S)


# Before generalizer: ['sunny', 'warm', 'normal', 'strong']
# After generalize: ['sunny', 'warm', '?', 'strong']