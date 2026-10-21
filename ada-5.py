
from dataclasses import dataclass
from typing import List


# Fractional Knapsack
def fractional_knapsack(
    weights: List[int],
    values: List[int],
    capacity: int
) -> float:
    if len(weights) != len(values):
        raise ValueError("Weights and values must have equal lengths")

    if capacity < 0 or any(w <= 0 for w in weights):
        raise ValueError("Capacity must be non-negative and weights positive")

    items = sorted(
        zip(weights, values),
        key=lambda item: item[1] / item[0],
        reverse=True
    )

    profit = 0.0

    for weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            profit += value
            capacity -= weight
        else:
            profit += value * (capacity / weight)
            capacity = 0

    return profit


# Job class
@dataclass
class Job:
    id: int
    deadline: int
    profit: int


# Job Scheduling with Deadlines
def job_scheduling(jobs: List[Job]) -> List[int]:
    if not jobs:
        return []

    jobs = sorted(jobs, key=lambda job: job.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)
    slots = [None] * (max_deadline + 1)

    for job in jobs:
        for slot in range(min(job.deadline, max_deadline), 0, -1):
            if slots[slot] is None:
                slots[slot] = job
                break

    return [job.id for job in slots[1:] if job is not None]


# Main Program
if __name__ == "__main__":
    # Test Fractional Knapsack
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    print("Fractional Knapsack Profit:",
          fractional_knapsack(weights, values, capacity))

    # Test Job Scheduling
    jobs = [
        Job(1, 2, 100),
        Job(2, 1, 19),
        Job(3, 2, 27),
        Job(4, 1, 25),
        Job(5, 3, 15)
    ]

    sequence = job_scheduling(jobs)

    print("Optimal Job Sequence:", sequence)
    print("Maximum Job Profit:",
          sum(job.profit for job in jobs if job.id in sequence))
