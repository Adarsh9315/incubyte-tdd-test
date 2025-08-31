import re

class StringCalculator:

    def __init__(self):
        self._count = 0

    def add(self, numbers: str) -> int:
        self._count += 1
        
        # Empty string should return 0.
        if numbers == "":
            return 0
        
        delimiters = [",", "\n"]

        # Handle custom delimiters
        if numbers.startswith("//"):
            header, numbers = numbers.split("\n", 1)
            if header.startswith("//["):
                # Multiple or multi-char delimiters
                delimiters = re.findall(r"\[(.*?)\]", header[2:])
            else:
                delimiters = [header[2:]]

        # Split using regex
        pattern = "|".join(map(re.escape, delimiters))
        parts = re.split(pattern, numbers)
        values = [int(p) for p in parts if p]
        
        # negatives not allowed
        negatives = [v for v in values if v < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

        # Ignore numbers > 1000
        values = [v for v in values if v <= 1000]
        return sum(values)
    
    def get_called_count(self) -> int:
        return self._count
