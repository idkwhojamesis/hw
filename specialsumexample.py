# Prof. Kounavelis
# Sept. 27 2019
# more efficient special sum

arr = [3,8,13,2,17,18,10]

spsumStr = input("special sum")
spsum = int (spsumStr)

for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                continue
            temp = arr[i] + arr[j]
            if temp == spsum:
                print(arr[i],",",arr[j])
