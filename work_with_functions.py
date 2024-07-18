from typing import Callable, Dict

def add(a: int, b: int) -> int:
    return a + b

def multiplay(a: int, b: int) -> int:
    return a * b

def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)

result_add = apply_operation(5, 3, add)
result_multiplay = apply_operation(4, 9, multiplay)

print(result_add, result_multiplay)


def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base ** exponent
    return inner

square = power(3)
cube = power(2)

print(square(7))
print(cube(2))


operations: Dict[str, Callable] = {
    'add': add,
    'multiply': multiplay,
    'square': square,
    'cube': cube
} 

result_add = operations["add"](10, 20)
result_square = operations['square'](5)

print(result_add)
print(result_square)