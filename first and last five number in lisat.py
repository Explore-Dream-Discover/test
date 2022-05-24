import numpy as np                                                                                                                                                                                                                  
generate_numbers = np.arange(1,30)


def square_first5_last5(generate_numbers):
    first5 = generate_numbers[0:5]
    last5 = generate_numbers[-5:]
    return {"generate_number":generate_numbers,"first5":first5,"last5":last5}


print(square_first5_last5(generate_numbers))
