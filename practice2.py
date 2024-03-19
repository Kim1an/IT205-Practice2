def count_character_frequency(string):
    frequency_dict = {}

    for char in string:
        if char != ' ':
            frequency_dict[char] = frequency_dict.get(char, 0) + 1

    return frequency_dict

def print_frequency(frequency_dict):
    print("Character frequency:")
    for char, frequency in frequency_dict.items():
        print(f"'{char}': {frequency}")

input_string = input("Enter a string: ")
frequency = count_character_frequency(input_string)
print_frequency(frequency)
