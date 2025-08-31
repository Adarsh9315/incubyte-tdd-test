class StringCalculator:
    def add(self, numbers: str) -> int:
        # Empty string should return 0.
        if numbers == "":
            return 0
        
        delimiter = ","
        if numbers.startswith("//"):
            # Extract custom delimiter
            delimiter_line, numbers = numbers.split("\n", 1)
            delimiter = delimiter_line[2:]

        
        numbers = numbers.replace("\n", delimiter)
        parts = numbers.split(delimiter)
        values = [int(p) for p in parts if p]

        # negatives not allowed
        negatives = [v for v in values if v < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

        return sum(values)
