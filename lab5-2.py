lst = ['bgh','wer','yuy','1661']
count = 0

for i in range(len(lst)):
    leng = len(lst[i])
    if leng > 2:
        if lst[i][0] == lst[i][-1]:
            count += 1

print(count)
