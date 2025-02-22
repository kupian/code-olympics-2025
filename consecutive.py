try:
    ints = [int(i) for i in input().split(",")]
except ValueError:
    ints = []
ints = list(set(ints))

ints.sort()

sequences = []

def count_consecutive(arr, start):
    sequence = [arr[start]]
    i = start
    while i < len(arr)-1:
        i += 1
        if arr[i-1]+1 == arr[i]:
            sequence.append(arr[i])
        else:
            break
        
    sequences.append(sequence)
    return i
  
i = 0      
while i < (len(ints)-1):
    i = count_consecutive(ints, i)

largest_seq = 0
for i,seq in enumerate(sequences):
    if len(seq) > len(sequences[largest_seq]):
        largest_seq = i

if len(sequences) > 0:    
    print(sequences[largest_seq])
else:
    print([])