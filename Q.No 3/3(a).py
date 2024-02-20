
# Question 3
# (a).
# You are developing a student score tracking system that keeps track of scores from different assignments. 
# The ScoreTracker class will be used to calculate the median score from the stream of assignment scores. 
# The class should have the following methods: • ScoreTracker() initializes a new ScoreTracker object. • void addScore(double score) adds a new assignment score to the data stream. • double getMedianScore() returns the median of all the assignment scores in the data stream. If the number of scores is even, the median should be the average of the two middle scores. Input: ScoreTracker scoreTracker = new ScoreTracker(); scoreTracker.addScore(85.5); // Stream: [85.5] scoreTracker.addScore(92.3); // Stream: [85.5, 92.3] scoreTracker.addScore(77.8); // Stream: [85.5, 92.3, 77.8] scoreTracker.addScore(90.1); // Stream: [85.5, 92.3, 77.8, 90.1] double median1 = scoreTracker.getMedianScore(); // Output: 88.9 (average of 90.1 and 85.5) scoreTracker.addScore(81.2); // Stream: [85.5, 92.3, 77.8, 90.1, 81.2] scoreTracker.addScore(88.7); // Stream: [85.5, 92.3, 77.8, 90.1, 81.2, 88.7] double median2 = scoreTracker.getMedianScore(); // Output: 86.95 (average of 88.7 and 85.5)


class Score_Tracker:
    def __init__(self):
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_middle_value(self):
        self.scores.sort()
        mid_index = len(self.scores) // 2

        if len(self.scores) % 2 == 1:
            # Odd number of elements
            return self.scores[mid_index]
        else:
            # Even number of elements
            return self.scores[mid_index - 1], self.scores[mid_index]

score_tracker = Score_Tracker()
score_tracker.add_score(85.5)
score_tracker.add_score(92.3)
score_tracker.add_score(77.8)
score_tracker.add_score(90.1)
print(score_tracker.scores)
median1 = score_tracker.get_middle_value()
print(sum(median1)/2)
score_tracker.add_score(81.2)
score_tracker.add_score(88.7)
print(score_tracker.scores)
median2 = score_tracker.get_middle_value()
print(sum(median2)/2)