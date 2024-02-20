# (b).
# You are given an integer n representing the total number of individuals. 
# Each individual is identified by a unique ID from 0 to n-1. The individuals have a unique secret that they can share with others. 
# The secret-sharing process begins with person 0, who initially possesses the secret. Person 0 can share the secret with any number of individuals simultaneously during specific time intervals. Each time interval is represented by a tuple (start, end) where start and end are non-negative integers indicating the start and end times of the interval. You need to determine the set of individuals who will eventually know the secret after all the possible secret sharing intervals have occurred. Example: Input: n = 5, intervals = [(0, 2), (1, 3), (2, 4)], firstPerson = 0 Output: [0, 1, 2, 3, 4] Explanation: In this scenario, we have 5 individuals labeled from 0 to 4. The secret-sharing process starts with person 0, who has the secret at time 0. At time 0, person 0 can share the secret with any other person. Similarly, at time 1, person 0 can also share the secret. At time 2, person 0 shares the secret again, and so on. Given the intervals [(0, 2), (1, 3), (2, 4)], we can observe that during these intervals, person 0 shares the secret with every other individual at least once. Hence, after all the secret-sharing intervals, individuals 0, 1, 2, 3, and 4 will eventually know the secret.





def get_individuals(n, intervals, first_person):
    result = set()
    result.add(first_person)

    for interval in intervals:
        start, end = interval

        if start == 0:
            # If the first person shares the secret in the initial interval,
            # add all individuals to the result set
            result.update(range(n))
        else:
            # If the first person shares the secret during the interval,
            # add all individuals (except the first person) to the result set
            result.update(j for j in range(n) if j != first_person)

    return sorted(result)

# Example usage:
n = 5
intervals = [(0, 2), (1, 3), (2, 4)]
first_person = 0

result = get_individuals(n, intervals, first_person)

print("Individuals who will eventually know the secret:", result)
