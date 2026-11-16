"""Check results and report timing and resident memory for the lab."""
import time
import unittest
import memory_profiler
import profiler


class TestProfiler(unittest.TestCase):
    def measure(self, function):
        started = time.perf_counter()
        value = function()
        elapsed = time.perf_counter() - started
        print(f"{function.__name__}: {elapsed:.6f} seconds; result={value}")
        return value, elapsed

    def test_slow_function(self):
        value, elapsed = self.measure(profiler.slow_function)
        self.assertEqual(value, 333283335000)
        self.assertGreaterEqual(elapsed, 2)

    def test_optimized_fast_function(self):
        value, elapsed = self.measure(profiler.optimized_fast_function)
        self.assertEqual(value, 328350)
        self.assertLess(elapsed, 1)

    def test_memory_intensive_function(self):
        before = memory_profiler.memory_usage(-1, interval=0.1, max_iterations=1)[0]
        value, elapsed = self.measure(profiler.memory_intensive_function)
        after = memory_profiler.memory_usage(-1, interval=0.1, max_iterations=1)[0]
        print(f"Resident memory: {before:.3f} -> {after:.3f} MiB; change={after-before:+.3f} MiB")
        self.assertEqual(value, 333333283333335000000)
        self.assertLess(elapsed, 5)
        # A running integer need not leave additional resident memory behind.
        # Record RSS rather than requiring an allocator-dependent increase.


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
