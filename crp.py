import random

def chinese_restaurant_process(num_customers, alpha):
    if num_customers <= 0:
        return []

    table_assignments = [1]  # first customer sits at table 1
    next_open_table = 2  # index of the next empty table

    # now generate table assignments for the rest of the customers.
    for i in range(1, num_customers):
        r, p = random.random(), alpha / (alpha + i) # random() is in [0, 1]
        print(r, p)
        if  r < p:  
            # customer sits at a new table.
            table_assignments.append(next_open_table)
            next_open_table += 1
        else:
            # customer sits at an existing table.
            # he chooses which table to sit at by giving equal weight to each
            # customer already sitting at a table. 
            which_table = random.choice(table_assignments)
            table_assignments.append(which_table)

    return table_assignments

# usage example
print(", ".join(map(str, chinese_restaurant_process(10, 3))))