# %%
def CollatzSeq(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        yield n

# example usage
for num in CollatzSeq(12):
    print(num)
# %%
def look_and_say():
    num = '1'
    while True:
        yield num
        i = 0
        new_num = ''
        while i < len(num):
            count = 1
            while i+1 < len(num) and num[i] == num[i+1]:
                count += 1
                i += 1
            new_num += str(count) + num[i]
            i += 1
        num = new_num
# example usage
count = 1
for num in look_and_say():
    print(num)
    if count == 6:
        break
    count += 1
# %%
