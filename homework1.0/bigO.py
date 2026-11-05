"""

Big O Detective
Part 1 - Classify These Functions
"""

# Function A
def get_first(data):
    return data[0]

# Big O: O(1)
# Reason: Accessing the first element of a list takes constant time
# regardless of the size of the list.


# Function B
def count_matches(data, target):
    count = 0
    for item in data:
        if item == target:
            count += 1
    return count

# Big O: O(n)
# Reason: The function examines every element in the list exactly once.


# Function C
def all_pairs(data):
    pairs = []
    for i in range(len(data)):
        for j in range(len(data)):
            pairs.append((data[i], data[j]))
    return pairs

# Big O: O(n²)
# Reason: Two nested loops each iterate n times, producing n² operations.


# Function D
def mystery(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count

# Big O: O(log n)
# Reason: The value of n is cut in half each iteration, so the number
# of iterations grows logarithmically.


# Function E
def process(data):
    total = sum(data)           # O(n)
    sorted_data = sorted(data)  # O(n log n)
    first = data[0]             # O(1)
    return total, sorted_data, first

# Big O: O(n log n)
# Reason: O(n log n) sorting dominates the O(n) summation and O(1)
# indexing operations.


"""
Part 2 - Pair Counting Functions
"""

import random
import time
import csv
import os
import platform
import subprocess


def count_pairs_quadratic(nums, target):
    """
    O(n²) solution using nested loops.
    Counts unique index pairs (i, j) where i < j.
    """
    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                count += 1

    return count


def count_pairs_linear(nums, target):
    """
    O(n) solution using a dictionary.
    Counts pairs as elements are processed.
    """
    seen = {}
    count = 0

    for num in nums:
        complement = target - num

        if complement in seen:
            count += seen[complement]

        seen[num] = seen.get(num, 0) + 1

    return count


import csv
import os
import platform
import random
import subprocess
import time
from datetime import datetime


def benchmark():
    sizes = [1000, 5000, 10000]
    target = 100

    detailed_results = []
    results = []

    print("\nPair Counting Benchmark")
    print("=" * 70)

    for size in sizes:
        nums = [random.randint(0, 100) for _ in range(size)]

        # O(n²) Benchmark
        start = time.perf_counter()
        count_pairs_quadratic(nums, target)
        quadratic_time = time.perf_counter() - start

        # O(n) Benchmark
        start = time.perf_counter()
        count_pairs_linear(nums, target)
        linear_time = time.perf_counter() - start

        speedup = quadratic_time / linear_time if linear_time > 0 else float("inf")

        detailed_results.append({
            "List Size": size,
            "Quadratic Time (s)": quadratic_time,
            "Linear Time (s)": linear_time,
            "Speedup Factor": speedup
        })
        results.append((size, quadratic_time, linear_time))

        print(f"\nInput Size: {size:,}")
        print(f"Quadratic Algorithm: {quadratic_time:.6f} sec")
        print(f"Linear Algorithm:    {linear_time:.6f} sec")
        print(f"Speed Improvement:   {speedup:.2f}x")

    # ------------------------------------------------------
    # Detailed Data CSV
    # ------------------------------------------------------

    with open("benchmark_results.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["PAIR COUNTING BENCHMARK RESULTS"])
        writer.writerow([f"Generated: {datetime.now()}"])
        writer.writerow([])

        writer.writerow([
            "Input Size",
            "O(n²) Runtime (seconds)",
            "O(n) Runtime (seconds)",
            "Speedup Factor"
        ])

        for result in detailed_results:
            writer.writerow([
                result["List Size"],
                f"{result['Quadratic Time (s)']:.8f}",
                f"{result['Linear Time (s)']:.8f}",
                f"{result['Speedup Factor']:.2f}x"
            ])

    # ------------------------------------------------------
    # Executive Summary CSV
    # ------------------------------------------------------

    largest_speedup = max(
        detailed_results,
        key=lambda x: x["Speedup Factor"]
    )

    avg_quad = sum(
        r["Quadratic Time (s)"] for r in detailed_results
    ) / len(detailed_results)

    avg_linear = sum(
        r["Linear Time (s)"] for r in detailed_results
    ) / len(detailed_results)

    with open("benchmark_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["BIG O PERFORMANCE ANALYSIS REPORT"])
        writer.writerow([f"Generated: {datetime.now()}"])
        writer.writerow([])

        writer.writerow(["Overview"])
        writer.writerow([
            "This benchmark compares two algorithms that count pairs whose sums equal a target value."
        ])
        writer.writerow([
            "Algorithm 1 uses nested loops and has O(n²) complexity."
        ])
        writer.writerow([
            "Algorithm 2 uses a dictionary and has O(n) complexity."
        ])

        writer.writerow([])
        writer.writerow(["Performance Statistics"])
        writer.writerow(["Average O(n²) Runtime", f"{avg_quad:.6f} seconds"])
        writer.writerow(["Average O(n) Runtime", f"{avg_linear:.6f} seconds"])

        writer.writerow([
            "Largest Observed Speedup",
            f"{largest_speedup['Speedup Factor']:.2f}x"
        ])

        writer.writerow([
            "Input Size with Largest Speedup",
            largest_speedup["List Size"]
        ])

        writer.writerow([])
        writer.writerow(["Conclusion"])
        writer.writerow([
            "Results demonstrate that the O(n) implementation scales significantly better as input size increases."
        ])
        writer.writerow([
            "As datasets grow, the runtime gap between O(n²) and O(n) becomes increasingly substantial."
        ])

    print("\nGenerated Files:")
    print(" - benchmark_results.csv")
    print(" - benchmark_summary.csv")

    # Open both files automatically
    try:
        system = platform.system()

        files = [
            "benchmark_results.csv",
            "benchmark_summary.csv"
        ]

        for file in files:
            if system == "Windows":
                os.startfile(file)
            elif system == "Darwin":
                subprocess.call(["open", file])
            else:
                subprocess.call(["xdg-open", file])

    except Exception as e:
        print(f"Could not automatically open files: {e}")
    return results


if __name__ == "__main__":
    results = benchmark()
    
    # Write results to CSV
    csv_filename = "benchmark_results.csv"
    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "List Size",
            "O(n²) Time (sec)",
            "O(n) Time (sec)"
        ])
        writer.writerows(results)

    print(f"Benchmark results saved to {csv_filename}")

    # Open the CSV automatically
    system = platform.system()

    try:
        if system == "Windows":
            os.startfile(csv_filename)
        elif system == "Darwin":  # macOS
            subprocess.call(["open", csv_filename])
        else:  # Linux
            subprocess.call(["xdg-open", csv_filename])
    except Exception as e:
        print(f"Could not automatically open the file: {e}")