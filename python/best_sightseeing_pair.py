class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        score_i = values[0]
        max_score = -1_000_000
        for ind in range(1, len(values)):
            candidate_score_j = values[ind] - ind
            max_score = max(max_score, score_i + candidate_score_j)
            score_i = max(score_i, values[ind] + ind)
        return max_score
