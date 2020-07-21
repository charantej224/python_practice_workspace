with open('actuals.txt', 'r') as f:
    actuals = f.readlines()
    f.close()

with open('references.txt', 'r') as f:
    lookup = f.readlines()
    f.close()

for i in len(len(actuals)):
    actuals[i] = actuals[i].lower().strip('\n')

for i in len(len(lookup)):
    lookup[i] = lookup[i].lower().strip('\n')

match_list = []

for each in lookup:
    each_list = each.split()
    for each_in_list in each_list:
        for actual in actuals:
            if each_in_list in actual:
                match_list


