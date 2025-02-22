current_score = int(input())
singles = [s for s in range (1,21)] + [25]
doubles = [2 * i for i in range(1, 21)] + [50]
triples = [3 * i for i in range(1,21)]

def get_combinations(score, darts_thrown):
    combinations = 0
    
    if darts_thrown == 3:
        return combinations
    
    for single_throw in scores:
        new_score = score - single_throw
        if new_score >= 2:
            combinations += get_combinations(new_score, darts_thrown+1)
    
    for double_throw in scores:
        new_score = score - double_throw*2
        if new_score == 0:
            combinations += 1
        elif new_score >= 2:
            combinations += get_combinations(new_score, darts_thrown+1)
            
    for triple_throw in scores:
        new_score = score - triple_throw*3
        if new_score >= 2:
            combinations += get_combinations(new_score, darts_thrown+1)
    
    return combinations

print(get_combinations(current_score, 0))