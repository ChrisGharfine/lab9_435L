"""Measure execution time for each workload line."""
import time
from line_profiler import LineProfiler


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


def profile_main():
    measurement = LineProfiler()
    for task in (slow_function, fast_function, memory_intensive_function):
        measurement.add_function(task)
    measurement.runcall(main)
    measurement.print_stats()


if __name__ == "__main__":
    profile_main()
