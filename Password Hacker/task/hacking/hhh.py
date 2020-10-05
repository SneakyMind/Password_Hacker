import itertools
teams = ['Best-ever', 'Not-so-good', 'Amateurs']
my_iter = itertools.combinations(teams, 2)
for i in range(len(teams)):
    print(next(my_iter))
