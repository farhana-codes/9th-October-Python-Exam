'''
Question 6: Hospital Patient Queue A hospital maintains a list of patients waiting for consultation.
 Write a function that removes the first patient after consultation,
   adds a new patient to the queue, and displays the updated queue. 
'''


def patient(a):
    print("Original queue:", a)  
    print(" removes the first patient after consultation:", a.pop(0))
    new = input("Enter new patient name: ")
    a.append(new)
    print("Updated queue:", a)


a = ['Farhana', 'Salma', 'Amitava', 'Amit']

patient(a)