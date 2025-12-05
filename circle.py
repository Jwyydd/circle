"""
    Prompts the user for a radius, converts the input to an integer,
    and calculates and prints the area of the circle using Pi * r^2.
    """
    print("\n--- Area of a Circle ---")
    
    # 1. User input (returns a string)
    radius_str = input("Please enter the radius of the circle: ")
    
    try:
        # 2. Convert from string to integer
        radius = int(radius_str)
        
        # Calculation: Area = π * r^2
        area = math.pi * radius * radius
        
        # 3. Concatenation and conversion (using an f-string for simplicity)
        # The float area is automatically converted to a string for printing.
        print(f"\nThe circle has a radius of {radius}.")
        print(f"The calculated Area is: {area}")
        
    except ValueError:
        print("Invalid input. Please enter a whole number for the radius.")
