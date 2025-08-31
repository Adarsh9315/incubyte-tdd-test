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
        return sum(int(p) for p in parts if p)
