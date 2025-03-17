#Exercise 1

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'];
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9];
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Exercise 2

capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

# Exercise 3

vowels = "aeiouAEIOU"

fruits_with_more_than_two_vowels = [
    fruit for fruit in fruits if sum(1 for char in fruit if char in vowels) > 2
]
print(fruits_with_more_than_two_vowels)


# Exercise 4

fruits_with_only_two_vowels = [
    fruit for fruit in fruits if sum(1 for char in fruit if char in vowels) == 2
]
print(fruits_with_only_two_vowels)

# Exercise 5 - Fruits with more than 5 characters
fruits_with_more_than_5_chars = [fruit for fruit in fruits if len(fruit) > 5]
print(fruits_with_more_than_5_chars)

# Exercise 6 - Fruits with exactly 5 characters
fruits_with_exactly_5_chars = [fruit for fruit in fruits if len(fruit) == 5]
print(fruits_with_exactly_5_chars)

# Exercise 7 - Fruits with less than 5 characters
fruits_with_less_than_5_chars = [fruit for fruit in fruits if len(fruit) < 5]
print(fruits_with_less_than_5_chars)

# Exercise 8 - List of the number of characters in each fruit
fruit_name_lengths = [len(fruit) for fruit in fruits]
print(fruit_name_lengths)

# Exercise 9 - Fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit.lower()]
print(fruits_with_letter_a)

# Exercise 10
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Exercise 11 - Odd numbers
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)

# Exercise 12 - Positive numbers
positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)

# Exercise 13 - Negative numbers
negative_numbers = [number for number in numbers if number < 0]
print(negative_numbers)



