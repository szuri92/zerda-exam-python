# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the original list.
# It should raise an error if the parameter is not a list.
# Example: with the input [1, 2, 3, 4, 5] it should return [2, 4].


def even_list(my_list):
    result = []
    if type(my_list) == list:
        for i in range(len(my_list)):
            if i % 2 == 1:
                result.append(my_list[i])
        return result
    else:
        raise TypeError

even_list(3)
