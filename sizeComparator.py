thing, size = input(),input()

objects = [
    ["atom",0.0000000001],
    ["proton",0.000000000000001],
    ["milky way",10000000000000000000000],
    ["observable universe",440000000000000000000000000],
    ["earth",12756000],
    ["moon",2474800],
    ["sun",1391000000],
    ["light year", 461000000000000],
    ["solar system",9000000000],
]

print(thing + " is the same size as " + thing)
for object in objects:
    print(thing + " is " + str(int(size)/object[1]) + " times the size of the " + object[0])