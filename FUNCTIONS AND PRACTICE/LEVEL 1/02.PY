'''ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both
words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False '''

#Solution -

def animal_crackers(str):
    text= str.lower().split()
    #print(text)
    return text[0][0]==text[1][0]

print(animal_crackers('Clever rat'))
print(animal_crackers('Pink Parrot'))
    