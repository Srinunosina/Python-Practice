
items = [('avocado', 2.2, 170), ('pamelo', 8, 1500), ('durian', 22, 1500), ('cucamelon', 0.26, 15), ('lychee', 0.4, 20),
        ('star apple', 1, 200)]

#items = sorted(items,key=lambda item : item[1], reverse=True)
#print(items)

def get_knapsack_greedy(items, capacity):
    total_profit = 0
    selected_items = {}

    items = sorted(items,key=lambda item : item[1], reverse=True)

    for i in range(len(items)):
        name, profit, weight = items[i]
        num_of_fruit = (capacity - capacity % weight) / weight
        # capcity = 9 weight = 2 = ( 9 - 9%2 ) / 2 = 4
        selected_items[name] = num_of_fruit
        capacity = capacity % weight
        total_profit += num_of_fruit * profit
    
    return round(total_profit, 2), selected_items


def get_knapsack_greedy_by_dantzig(items, capacity):
    total_profit = 0
    selected_items = {}

    items = sorted(items,key=lambda item : item[1] / item[2], reverse=True)

    for i in range(len(items)):
        name, profit, weight = items[i]
        num_of_fruit = (capacity - capacity % weight) / weight
        # capcity = 9 weight = 2 = ( 9 - 9%2 ) / 2 = 4
        selected_items[name] = num_of_fruit
        capacity = capacity % weight
        total_profit += num_of_fruit * profit
    
    return round(total_profit, 2), selected_items


#print(get_knapsack_greedy(items, 2000))
#print('Optimal Solutions would be: -----------')
#print(get_knapsack_greedy_by_dantzig(items, 2000))


def get_knapsack_no_fraction_dp_tabulization(weights : list, profits : list, capacity: int):
    n = len(profits)
    bag = [[0 for i in range(capacity +1)] for col in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                # list index starting with zero, so profits and weights are indexed accordingly (i-1)
                bag[i][w] = max(profits[i-1] + bag[i-1][w-weights[i-1]], bag[i-1][w])
            else:
               bag[i][w] = bag[i-1][w]
    return bag[n][capacity]


profits = [1, 2, 5, 6] # [6, 10, 12]
weights = [2, 3, 4, 5] #[1, 2, 3]
capacity = 8           #5
#print(get_knapsack_no_fraction_dp_tabulization(weights, profits, capacity))


# knapSack_brute_force_recursion
def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
 
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1) 
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))
 

#Driver Code
val = [6, 10, 12]
wt = [1, 2, 3]
W = 5
n = len(val)
print(knapSack(W, wt, val, n))