from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Not sure how to initiate this map...
        # probably create each label (key) in it when it appears in the
        # queries.
        labels_to_counts = defaultdict(int)
        # Every ball starts off unlabelled.
        balls_to_labels = defaultdict(lambda: None)
        n = len(queries)
        results = [0] * n
        for i in range(n):
            ball, new_label = queries[i]
            current_label = balls_to_labels[ball]
            # If this is the first time labeling the ball, we only have
            # to increment labels_to_counts[new_label]
            # and update balls_to_labels.
            if current_label is None:
                labels_to_counts[new_label] += 1
            # Otherwise, we need to decrement labels_to_counts for
            # current_label, increment it for new_label, and update
            # balls_to_labels.
            else:
                labels_to_counts[current_label] -= 1
                # To save on memory, we can delete unused labels from the
                # dict
                if labels_to_counts[current_label] == 0:
                    labels_to_counts.pop(current_label)
                labels_to_counts[new_label] += 1
            # Updating balls_to_labels is the same whether or not this
            # is the first time the ball is being labeled.
            balls_to_labels[ball] = new_label

            # Since we delete every (k, v) pair in labels_to_counts if
            # the label appears 0x, the result after the current round
            # is how many labels are in the dict.
            results[i] = len(labels_to_counts)
        return results
