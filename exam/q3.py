'''
Question 3: Shopping Cart Management A customer adds products to a shopping cart. Write a function that accepts a list of product names and performs the following operations: 
• Add a new product. 
• Remove a purchased or unwanted product. 
• Display the final cart.
• Count the total number of products.
'''

def add_shopping_cart(a):
  new=input("add any product : ")
  a.append(new)
  print(a)

def remove_shopping_cart(a):
  prod=input('write a product name to remove : ')
  if prod in a:
    a.remove(prod)
    print(f'new product list is{a}')
  else:
    print("product isn't found")
    print('____________________________________')

def display_count(a):

  print(f'displaying the whole product list is : {a}')
  print(f'the number of the product is : {len(a)} ')  


a=['dal','choco','chips','coffee','biscuit']
add_shopping_cart(a)
remove_shopping_cart(a)
display_count(a)
