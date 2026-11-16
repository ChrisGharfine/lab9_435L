"""Lab 9 computational workload."""
import time


def slow_function():
    """Include the lab's deliberate wait before the small calculation."""
    time.sleep(2)
    result = 0
    for number in range(10_000):
        result += number ** 2
    return result


def fast_function():
    """Return the sum of squares from zero through ninety-nine."""
    result = 0
    for number in range(100):
        result += number ** 2
    return result


def memory_intensive_function():
    """Run the large workload without retaining the individual squares."""
    result = 0
    for number in range(10_000_000):
        result += number ** 2
    return result


def main():
    slow_function()
    fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    main()
