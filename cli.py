from main import solution

_is_debug_input = input("Turn on debug mode (y/n)? ")

if _is_debug_input == "y":
    is_debug = True

_n_times_input = int(input("Enter the quantity of times to run the algorithm: "))
_size_of_field_input = int(input("Enter the size of field: "))
_probability = solution(_n_times_input, _size_of_field_input)
print(f"The posterior probability of escaping the field is {_probability}")

