# Task 1
food = "Japanese curry"
print(food[:3])
print(food[-3:])

first_last = food[0] + food[-1]
print(first_last)

food_list = food.split()
print(food_list)

food_join = ' '.join(food_list)
print(food_join)

# Task 2
number_list = [1, 2, 3, 4, 5]
number_list.append(6)
number_list.insert(2, 2.5)
number_list.pop()
number_list.remove(2)
print(number_list)

print(number_list[:3])
print(number_list[-3:])

# Task 3
books = {'J.K. Rowling': 'Harry Potter', 'Suzanne Collines': 'Hunger Games', 'Fonda Lee': 'Jade City', 'Pierce Brown': 'Red Rising'}
print(books.keys())
print(books.values())
print(books.get('J.K. Rowling'))

books.pop('Fonda Lee')
print(books)

del books['J.K. Rowling']
print(books)