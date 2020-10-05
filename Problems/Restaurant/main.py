import itertools

main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]

desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]

drinks = ['cola', 'wine']
price_drinks = [3, 10]

combinations = itertools.combinations(zip(main_courses,desserts,drinks),(zip(price_main_courses,price_desserts,price_drinks)))

for i,n in combinations:
    if sum(n) < 30:
        print(i,n)
