import sys

def parse_file(input_file):
    """
    Read file line by line and return list of contents.
    """
    with open(input_file) as f:
       file_content = [int(value) for value in f] 
    return file_content


def find_three_sum(value_list, target_value):
    """
    Determine three numbers within a list that sum to a given value. 
    """
    for i in range(0, len(value_list)-1):
        remaining_sum = target_value - value_list[i]

        num1, num2 = find_two_sum(value_list[i:], remaining_sum)

        if num1 and num2:
            return value_list[i], num1, num2
    return None, None, None

def find_two_sum(value_list, target_value):
    """
    Determine two numbers within a list that sum to a given value.
    """
    values_seen = set()

    for val in value_list:
        value_to_find = target_value - val

        if value_to_find in values_seen:
            return val, value_to_find
        
        values_seen.add(val)

    return None, None

def find_product_of_three_sum(value_list, target_value):
    """
    Determine the product of three numbers that sum to a given value 
    """
    num1, num2, num3 = find_three_sum(value_list, target_value)

    if num1 and num2 and num3: 
        print(f"The product of the three sum is: {num1*num2*num3}")
    

def find_product_of_two_sum(value_list, target_value):
    """
    Determine the product of two numbers that sum to a given value 
    """
    num1, num2 = find_two_sum(value_list, target_value)

    if num1 and num2: 
        print(f"The product of the two sum is: {num1*num2}")
    

if __name__ == "__main__":
    input_file = sys.argv[1]
    input_list = parse_file(input_file)
    find_product_of_two_sum(input_list, 2020)
    find_product_of_three_sum(input_list, 2020)
