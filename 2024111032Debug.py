
# Online Python - IDE, Editor, Compiler, Interpreter

def is_narc(n):
    """Check if a number is narc."""
    num_str = str(n) #instead of assignment operator it was equality comparison operator
    num_digits = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str) # exponential operator ** was not used
    
    return sum_of_powers == n

def print_narcis_numbers(start, end):
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1):
        if is_narc(num): # is_narc was not used, instead is_narcisstic was used
            print(num)

print_narcis_numbers(1000, 5000) # print_narcis_numbers was not used properly
# in all of the functions, loop and if statement there was no colon used. so 
# proper interpretation was not able to be done
"""Submit your response here: https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u """
