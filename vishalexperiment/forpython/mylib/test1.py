# import time

# def typing_test():
#     test_sentence='MAMAMAMATA  BAI CHUP BAITH VARNA TU SEE ME U GO TO ICE'
#     print(f'Type the below sentence \n'  f'{test_sentence}')
#     start = time.time()
#     user_input = input()
#     end = time.time()
#     time_taken = end - start
#     correct_chars=0
#     for i, j in zip(test_sentence, user_input):
#         if i == j:
#             correct_chars += 1
#     accuracy = correct_chars/len(test_sentence)
#     print(f'Your accuracy is {accuracy}')
#     print(f'Time taken to type: {time_taken} seconds')
# typing_test()
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
 
# using zip() to map values
mapped = zip(name, roll_no)
 
print(set(mapped))
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
 
# using zip() to map values
mapped = zip(name, roll_no)
 
print(set(mapped))
# List 
x = ['q', 'w', 'r', 'e', 't', 'y'] 
print(sorted(x)) 

# Tuple 
x = ('q', 'w', 'e', 'r', 't', 'y') 
print(sorted(x)) 

# String-sorted based on ASCII translations 
x = "python"
print(sorted(x)) 

# Dictionary 
x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6} 
print(sorted(x)) 

# Set 
x = {'q', 'w', 'e', 'r', 't', 'y'} 
print(sorted(x)) 

# Frozen Set 
x = frozenset(('q', 'w', 'e', 'r', 't', 'y')) 
print(sorted(x)) 

