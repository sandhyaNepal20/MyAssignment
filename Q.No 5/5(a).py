# Task 5
# a) Implement ant colony algorithm solving travelling a salesman problem


import random

class AntColonyTSP:
    def __init__(self, distances, num_ants, num_iterations, decay_factor, alpha, beta):
        self.distances = distances
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay_factor = decay_factor
        self.alpha = alpha
        self.beta = beta
        self.num_cities = len(distances)
        self.pheromone_levels = [[1.0 / self.num_cities] * self.num_cities for _ in range(self.num_cities)]
        self.best_path = []
        self.best_distance = float('inf')
        self.initialize_pheromones()

    def initialize_pheromones(self):
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                if i != j:
                    self.pheromone_levels[i][j] = 1.0 / (self.num_cities * self.num_cities)

    def solve(self):
        for iteration in range(self.num_iterations):
            ant_paths = []
            ant_distances = [0] * self.num_ants
            for ant_index in range(self.num_ants):
                path = self.construct_solution(random.randint(0, self.num_cities - 1))
                ant_paths.append(path)
                ant_distances[ant_index] = self.calculate_distance(path)
                if ant_distances[ant_index] < self.best_distance:
                    self.best_distance = ant_distances[ant_index]
                    self.best_path = path.copy()
            self.update_pheromones(ant_paths)
            self.decay_pheromones()

    def construct_solution(self, starting_city):
        path = [starting_city]
        available_cities = set(range(self.num_cities))
        available_cities.remove(starting_city)

        while available_cities:
            next_city = self.select_next_city(path[-1], available_cities)
            path.append(next_city)
            available_cities.remove(next_city)

        return path

    def select_next_city(self, current_city, available_cities):
        probabilities = [0] * self.num_cities
        total_probability = 0

        for city in available_cities:
            probabilities[city] = pow(self.pheromone_levels[current_city][city], self.alpha) * pow(1.0 / self.distances[current_city][city], self.beta)
            total_probability += probabilities[city]

        random_value = random.random() * total_probability
        cumulative_probability = 0

        for city in available_cities:
            cumulative_probability += probabilities[city]
            if cumulative_probability >= random_value:
                return city

    def calculate_distance(self, path):
        distance = 0
        for i in range(len(path) - 1):
            distance += self.distances[path[i]][path[i + 1]]
        return distance

    def update_pheromones(self, ant_paths):
        evaporation = 1.0 - self.decay_factor

        for i in range(self.num_cities):
            for j in range(self.num_cities):
                if i != j:
                    pheromone_delta = 0
                    for path in ant_paths:
                        if j in path and i in path:
                            pheromone_delta += 1 / self.calculate_distance(path)
                    self.pheromone_levels[i][j] = (evaporation * self.pheromone_levels[i][j]) + pheromone_delta

    def decay_pheromones(self):
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                self.pheromone_levels[i][j] *= self.decay_factor

    def get_best_path(self):
        return self.best_path

    def get_best_distance(self):
        return self.best_distance

# Example usage:
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
num_ants = 10
num_iterations = 100
decay_factor = 0.5
alpha = 1
beta = 2
ant_colony = AntColonyTSP(distances, num_ants, num_iterations, decay_factor, alpha, beta)
ant_colony.solve()
best_path = ant_colony.get_best_path()
best_distance = ant_colony.get_best_distance()
print("Best path:", best_path)
print("Best distance:", best_distance)
