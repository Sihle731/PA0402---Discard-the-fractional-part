##Question 1.1

import math

def min_rooms_needed(guests: int) -> int:
    if guests < 0:
        raise ValueError("Number of guests cannot be negative")
    return math.ceil(guests / 3)


##Question 1.2

def generate_subnets():
    return [f"192.168.1.{i*32}/27" for i in range(8)]

for subnet in generate_subnets():
    print(subnet)
