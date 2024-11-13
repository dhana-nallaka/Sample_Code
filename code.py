def sort(width, height, length, mass):
    #volume calculation
    volume = width * height * length
    
    # Checking bulk or heavy 
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    
    # Determining type
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

width, height, length, mass = map(int, input().split(",")) #taking input eg:1,2,3,4
result = sort(width, height, length, mass)
print(f"Package {result}") #printing it 
