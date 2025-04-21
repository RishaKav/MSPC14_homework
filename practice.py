fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

vowels = ['a', 'e', 'i', 'o', 'u']

uppercased_fruits = [fruits.upper() for fruits in fruits]
print(uppercased_fruits)

capitalized_fruits = [fruits.capitalize() for fruits in fruits]
print(capitalized_fruits)


fruits_with_more_than_two_vowels = [fruit for fruit in fruits if sum(1 for letter in fruit.lower() if letter in vowels)>2]
print(fruits_with_more_than_two_vowels)

fruits_with_only_two_vowels = [fruit for fruit in fruits if sum(1 for letter in fruit.lower() if letter in vowels)==2]
print(fruits_with_only_two_vowels)

fruits_with_more_than_five_char = [fruit for fruit in fruits if len(fruit)>5]
print(fruits_with_more_than_five_char)

fruits_with_exactly_five_char = [fruit for fruit in fruits if len(fruit)==5]
print(fruits_with_exactly_five_char)

fruits_with_less_than_five_char = [fruit for fruit in fruits if len(fruit)<5]
print(fruits_with_less_than_five_char)

#fruit_char_num = [len(fruit) for fruit in fruits]
#print(fruit_char_num)
fruit_char_num = [len(fruit.replace(" ","")) for fruit in fruits]
print(fruit_char_num)

fruits_with_letter_a = [fruit for fruit in fruits if "a" in fruit]
print(fruits_with_letter_a)

even_numbers = [number for number in numbers if number%2==0]
print(even_numbers)

odd_numbers = [number for number in numbers if number%2!=0]
print(odd_numbers)

positive_numbers = [number for number in numbers if number>0]
print(positive_numbers)

negative_numbers = [number for number in numbers if number<0]
print(negative_numbers)



