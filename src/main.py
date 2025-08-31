class StringCalculator:
    def add(self, numbers: str) -> int:
        # Step 1: Empty string should return 0.
        if numbers == "":
            return 0
        
        # Step 2: return the number itself if only one
        # Step 3: step 2 now extended to handle two numbers using split
        # Step 4: This will also work for Unknown count of numbers

        # Step 5: Treat newline as another delimiter
        numbers = numbers.replace("\n", ",")
        
        parts = numbers.split(",")
        if len(parts) == 1:
            return int(parts[0])
        return sum(int(p) for p in parts)
