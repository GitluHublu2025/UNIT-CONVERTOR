
import json
from collections import deque

# Load conversions from JSON
with open("conversions.json") as f:
    conversions = json.load(f)

def convert(value, from_unit, to_unit):
    from_unit, to_unit = from_unit.strip(), to_unit.strip()

    # Handle temperature separately
    if from_unit in ["C", "F", "K"] and to_unit in ["C", "F", "K"]:
        if from_unit == "C" and to_unit == "F":
            return value * 9/5 + 32
        if from_unit == "F" and to_unit == "C":
            return (value - 32) * 5/9
        if from_unit == "C" and to_unit == "K":
            return value + 273.15
        if from_unit == "K" and to_unit == "C":
            return value - 273.15
        if from_unit == "F" and to_unit == "K":
            return (value - 32) * 5/9 + 273.15
        if from_unit == "K" and to_unit == "F":
            return (value - 273.15) * 9/5 + 32

    # Direct conversion
    if to_unit in conversions.get(from_unit, {}):
        return value * conversions[from_unit][to_unit]

    # Multi-step conversion using BFS
    queue = deque([(from_unit, value)])   # (current_unit, current_value)
    visited = set([from_unit])

    while queue:
        current_unit, current_value = queue.popleft()

        for next_unit, factor in conversions.get(current_unit, {}).items():
            if next_unit in visited:
                continue

            new_value = current_value * factor
            if next_unit == to_unit:
                return new_value

            queue.append((next_unit, new_value))
            visited.add(next_unit)

    raise ValueError(f"No conversion path found from {from_unit} to {to_unit}")
