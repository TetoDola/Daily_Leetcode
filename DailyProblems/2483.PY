class Solution:
    def bestClosingTime(self, customers: str) -> int:
        openpenalty = customers.count('Y') #penalty for staying closed from 0h
        min_penalty = openpenalty
        best_hour = 0

        for i, c in enumerate(customers):
            if c == 'Y':
                openpenalty -= 1
            else: 
                openpenalty += 1 
            
            if openpenalty < min_penalty:
                min_penalty = openpenalty
                best_hour = i + 1

        return best_hour

        