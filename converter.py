import json

# Load conversions from JSON
with open("conversions.json") as f:
    conversions = json.load(f)

def convert(value, from_unit, to_unit):
    # Handle temperature conversions separately
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

    raise ValueError(f"Conversion from {from_unit} to {to_unit} not available")
