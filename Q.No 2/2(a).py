
# Question 2
# (a).
# You are the manager of a clothing manufacturing factory with a production line of super sewing machines. 
# The production line consists of n super sewing machines placed in a line. Initially, each sewing machine has a certain number of dresses or is empty. For each move, you can select any m (1 <= m <= n) consecutive sewing machines on the production line and pass one dress from each selected sewing machine to its adjacent sewing machine simultaneously. Your goal is to equalize the number of dresses in all the sewing machines on the production line. You need to determine the minimum number of moves required to achieve this goal. If it is not possible to equalize the number of dresses, return -1. Input: [2, 1, 3, 0, 2] Output: 5 Example 1: Imagine you have a production line with the following number of dresses in each sewing machine: [2, 1, 3, 0, 2]. The production line has 5 sewing machines. Here's how the process works: 1. Initial state: [2, 1, 3, 0, 2] 2. Move 1: Pass one dress from the second sewing machine to the first sewing machine, resulting in [2, 2, 2, 0, 2] 3. Move 2: Pass one dress from the second sewing machine to the first sewing machine, resulting in [3, 1, 2, 0, 2] 4. Move 3: Pass one dress from the third sewing machine to the second sewing machine, resulting in [3, 2, 1, 0, 2] 5. Move 4: Pass one dress from the third sewing machine to the second sewing machine, resulting in [3, 3, 0, 0, 2] 6. Move 5: Pass one dress from the fourth sewing machine to the third sewing machine, resulting in [3, 3, 1, 0, 1] After these 5 moves, the number of dresses in each sewing machine is equalized to 1. Therefore, the minimum number of moves required to equalize the number of dresses is 5.



def min_moves_to_equalize(sewing_machines):
    total_dresses = sum(sewing_machines)
    machines_count = len(sewing_machines)

    # Calculate the target number of dresses for each machine
    if total_dresses % machines_count != 0:
        return -1
    target_dresses = total_dresses // machines_count
    moves = 0

    # Iterate until all machines have the target dress count
    for dresses in sewing_machines:
        # Calculate the difference between current dresses and the target
        diff = dresses - target_dresses
        # Accumulate moves needed to equalize dresses
        if diff > 0:
            moves += diff

    return moves

# Example usage:
sewing_machines = [1, 0, 5]
print(min_moves_to_equalize(sewing_machines))  # Output: 2