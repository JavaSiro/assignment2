#b
# list=list(range(0, 100))
####################################I still can't get the logic behind the below code(for i,value)
# for i, value in enumerate(list):
#     if i>0 and i%20==0:
#         print(value)
########################################## How can i get rid of the 0 in output from the following, and wahts the difference between using the above and below codes
# list=list(range(2,100))
# for i in range(0,100,20):
#     print(i)



#c
# subject=['calculus', 'statistics', 'algorithms']
# score=['A+', 'B+', 'C+']
# for a, b in zip(subject,score):
#     if a%2==0:
#         print(f'for {a} Java got {b}')

#d and e
#the problem is it's counting 0 as even, but do we need that zero index data?
#also, same thing,what's the logic of for i, (a,b) in 
# subject=['calculus', 'statistics', 'algorithms']
# score=['A+', 'B+', 'C+']
# for i,(a,b) in enumerate(zip(subject,score)):
#     if i % 2 == 1:##in case of e practise it must be 0
#         print(f'for {a} Java got {b}')

#f
# Adele = {'data structures': 'A', 'algorithms': 'B', 'OOP': 'C'}
# Mumtoza = {'data structures': 'C', 'algorithms': 'B', 'OOP': 'A'}
# Fati = {'data structures': 'C', 'algorithms': 'A', 'OOP': 'B'}
# students = {'Adele': Adele, 'Mumtoza': Mumtoza, 'Fati': Fati}

# for name, grades in students.items():
#     print(f"{name}'s grades:")
#     for subject, grade in grades.items():
#         print(f"  {subject}: {grade}")