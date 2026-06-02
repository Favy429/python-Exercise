def analyze_numbers(numbers):
    """Return summary statistics for a list of numbers."""
    
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

def main():
    numbers = []
    # Collect 5 numbers
    for i in range(5):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Analyze the numbers
    stats = analyze_numbers(numbers)

    print("\n--- Statistics Report ---")

    for key, value in stats.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()