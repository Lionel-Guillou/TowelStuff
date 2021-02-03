def greet(first_name, *names):
    """This function greets all
    the person in the names tuple."""

    print("This is the first name", first_name)
    # names is a tuple with arguments
    print(names)
    print(type(names))
    print(type(names[0]))

    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John")