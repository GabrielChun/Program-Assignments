food = 'Japanese Curry'

print(food[:3])
print(food[-3:])

string = food[0] + food[-1]
print(string)

food_list = food.split()
print(food_list)

food_string = ' '.join(food_list)
print(food_string)

number_list = [1, 2, 3, 5, 7]
number_list.append(11)
number_list.insert(3, 4)
number_list.pop()
number_list.remove(2)
print(number_list)
print(number_list[:3])
print(number_list[-3:])

books = {'J.K. Rowling': 'Harry Potter',
         'Suzanne Collins': 'Six of Crows',
         'Fonda Lee': 'Jade City',
         'Pierce Brown': 'Red Rising'}
print(list(books.keys()))
print(list(books.values()))
print(books.get('J.K.Rowling'))
third_key = list(books.keys())[2]
books.pop(third_key)
print(books)
first_key = list(books.keys())[0]
del books[first_key]
print(books)