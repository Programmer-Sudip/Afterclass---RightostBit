def find_rightmost_set_bit_position(n):
    # If n is 0, there are no set bits
    if n == 0:
        return -1
    
    position = 1  # Start counting positions from 1
    while (n & 1) == 0:  # Check if the least significant bit is 0
        n >>= 1          # Right shift n to check the next bit
        position += 1    # Move to the next bit position
    
    return position

# Example usage
num = int(input("Enter a number: "))
position = find_rightmost_set_bit_position(num)

if position != -1:
    print(f"The rightmost set bit of {num} is at position {position}.")
else:
    print(f"The number {num} has no set bits.")
