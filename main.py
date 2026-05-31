import random
from fastmcp import FastMCP

# create a fastmcp server instance

mcp = FastMCP(name='demoserver')


#1st tool
@mcp.tool
def roll_dice(n_dice: int =1) -> list[int]:
    """Roll n_dice 6-sded dice and return the results"""
    return [random.randint(1,6) for _ in range(n_dice)]


# 2nd tool

@mcp.tool
def add_two_numbers(a:float, b:float) -> float:
    """Add two numbers"""
    return a+b


if __name__ == "__main__":
    mcp.run()









