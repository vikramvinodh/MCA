print("Hello, I am Vikram Vinodh(2347263) from 1 MCA 'B' and this is my First Lab Exercise in Python")
intro="Hello, I am Vikram Vinodh and I My domain is Web hosting using Python."
#Data Types
def count_word_frequency(paragraph, target_word):
    words = paragraph.split()
    word_count = 0
    for word in words:
        word = word.strip('.,!?()[]{}"\'')
        if word.lower() == target_word.lower():
            word_count += 1
    return word_count
paragraph = input("Kindly Enter your paragraph:")
target_word = input("enter the you want to count:")
frequency = count_word_frequency(paragraph, target_word)
print(f"The word '{target_word}' appears {frequency} times in the paragraph.")


num=["0","1","2","3","4","5","6","7","8","9"]
spld_word=intro.split(" ")
for i in spld_word:
    for j in i:
        if j in num:
            if "." in i:
                print(i," is float")
                break
            else:
                print(i,"is int")
                break
        else:
            print(i," : is string")
            break
def count_characters(paragraph):
    alphabets = 0
    numerics = 0
    specials = 0

    for char in paragraph:
        if char.isalpha():
            alphabets += 1
        elif char.isnumeric():
            numerics += 1
        else:
            specials += 1

    return alphabets, numerics, specials
paragraph = "Introducing Kavaskar, a passionate programmer with a roll number of 2347230. He scored 95.5 marks in the year 2023."

alphabets, numerics, specials = count_characters(paragraph)

print(f"Alphabets: {alphabets}")
print(f"Numeric characters: {numerics}")
print(f"Special symbols: {specials}")


#sorting the set
def set_operations_example():
    string_set = {"Java","Python","Web-Satck","Database_tech"}
    print("Initial Set:", string_set)
    sorted_set = sorted(string_set, reverse=True)
    print("Sorted Set (Descending Order):", sorted_set)
set_operations_example()

#packing and unpacking of tuple
def slicing_and_negative_indexing(domain):
    print("Original Domain Name:", domain)
    print("\nPositive Slicing:")
    print("1. Slicing from index 3 to 9:", domain[3:10])
    print("2. Slicing from index 0 to 7:", domain[:8])
    print("3. Slicing from index 5 to the end:", domain[5:])
    print("4. Slicing from index 2 to 11 with step 2:", domain[2:12:2])
    print("\nNegative Slicing:")
    print("1. Slicing from the end -8 to the end -3:", domain[-8:-2])
    print("2. Slicing from the end -11 to the end -1 with step 2:", domain[-11:-1:2])
    print("\nNegative Indexing:")
    print("Last character:", domain[-1])
    print("Second to last character:", domain[-2])
domain = "Web-Hosting"
slicing_and_negative_indexing(domain)

#Word Count


dmn_name=("W","E","B","H","O","S","T","I","N","G")
count=0
for i in dmn_name:
    count=count+1
print("count of Names:",count)

#tuple slicing

def slicing_and_negative_indexing(domain):
    print("Original Domain Name:", domain)
    print("\nPositive Slicing:")
    print("1. Slicing from index 3 to 9:", domain[3:10])
    print("2. Slicing from index 0 to 7:", domain[:8])
    print("3. Slicing from index 5 to the end:", domain[5:])
    print("4. Slicing from index 2 to 11 with step 2:", domain[2:12:2])
    print("\nNegative Slicing:")
    print("1. Slicing from the end -8 to the end -3:", domain[-8:-2])
    print("2. Slicing from the end -11 to the end -1 with step 2:", domain[-11:-1:2])
    print("\nNegative Indexing:")
    print("Last character:", domain[-1])
    print("Second to last character:", domain[-2])
domain = "Web-Hosting"
slicing_and_negative_indexing(domain)


#Pop

def set_operations_example():
    set = {1, "Python", 2.263, True, (1, 2)}
    print("Initial Set:", set)
    popped_element = set.pop()
    print("\nElement popped:", popped_element)
    print("Updated Set after pop:", set)
    set.clear()
    print("\nSet after clear:", set)
    set.add(42)
    set.add("Python")
    set.add("World")
    set.add(False)
    set.add((3, 4))
    set.update(["Java","Python","C++","Mongodb"])  
    print("Set after adding elements:", set)
    set.discard("World")
    print("\nSet after discarding 'World':", set)
    del set
set_operations_example()