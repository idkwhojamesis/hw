# James Park
# Oct. 28 2019
# example dictionary

exDict = {
    "Boston": "biggest city in chicago",
    "NYC": "ey im walkin ere"
}
for i in range(5):
    cityIn = input("city:")
    descIn = input("desc:")
    exDict[cityIn] = descIn;
for x in exDict:
    print(x)
    print(exDict[x])
