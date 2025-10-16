# math.py

import os
from mcp.server.fastmcp import FastMCP
from starlette.responses import JSONResponse

mcp = FastMCP(host=os.getenv("HOST", "0.0.0.0"), stateless_http=True)

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers together"""
    return a * b

@mcp.tool()
def divide_numbers(a: int, b: int) -> float:
    """Divide two numbers"""
    return a / b

@mcp.tool()
def subtract_numbers(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
