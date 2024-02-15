
try:
    num=int(input("enter a number"))

    result=10/num
except ZeroDivisionError:

    print("Cannot divide by zero.")

except ValueError:

    print("Invalid input. Please enter a number.")

else:

    print("Result:", result)

finally:

    print("Exception handling complete.")


    # copy an objects
    import copy

original_list = [[1, 2, 3], [4, 5, 6]]

shallow_copied_list = copy.copy(original_list)

original_list[0] = 1  # Modifying the original list

print(shallow_copied_list)  # Changes are reflected in the shallow copy