class StringCalculator:
    def add(self, numbers: str) -> int:
        # Step 1: Empty string should return 0.
        if numbers == "":
            return 0
        
        # Step 2: return the number itself if only one
        return int(numbers)
