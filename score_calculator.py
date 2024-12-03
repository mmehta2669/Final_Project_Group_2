
class ScoreCalculator:
    def __init__(self):
        self.score = 0
        self.base = 10
        self.multiplier = 1

    def increse_score(self):
        # Increment the score by the base x the mutiplier
        self.score += self.base * self.multiplier
        
    #getters for the class
    def get_score(self):
        return self.score
    def get_multiplier(self):
        return self.multiplier

    #setters for the multiplier
    def increase_multiplier(self):
        self.multiplier += 1
    def reset_multiplier(self):
        self.multiplier = 1
    
    