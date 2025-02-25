from enum import Enum

class Operations(Enum):
    PUSH = "Push"
    POP = "Pop"

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        prev_num = 0

        for current_num in target:
            # Calculate how many numbers we need to skip
            skipped_count = current_num - prev_num - 1

            # For each skipped number, add a PUSH followed by a POP
            for _ in range(skipped_count):
                result.append(Operations.PUSH.value)
                result.append(Operations.POP.value)
            
            # Add a PUSH for the current target number
            result.append(Operations.PUSH.value)

            # Update previous number
            prev_num = current_num

        return result