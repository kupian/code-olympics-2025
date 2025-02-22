nums = [int(x.strip("[]")) for x in input().split(",")]
target = nums[-1]
nums = nums[:-1]

def get_pair():
    for i,num in enumerate(nums):
        for j,other_num in enumerate(nums):
            if num + other_num == target and i != j:
                return [i,j]

a,b = get_pair()
print(f"[{a},{b}]")