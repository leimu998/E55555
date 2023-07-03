import random
import math
import matplotlib.pyplot as plt

# 定义目标函数
def objective_function(x):
    return x**2 + 3*x + 4

# 定义粒子类
class Particle:
    def __init__(self, x):
        self.x = x
        self.velocity = random.uniform(-1, 1)
        self.best_x = self.x
        self.best_fitness = objective_function(self.x)

    def update_velocity(self, global_best_x, inertia_weight, cognitive_weight, social_weight):
        self.velocity = (inertia_weight * self.velocity +
                         cognitive_weight * random.random() * (self.best_x - self.x) +
                         social_weight * random.random() * (global_best_x - self.x))

    def update_position(self):
        self.x += self.velocity

        if self.x < -10:
            self.x = -10
        elif self.x > 10:
            self.x = 10

        fitness = objective_function(self.x)
        if fitness < self.best_fitness:
            self.best_x = self.x
            self.best_fitness = fitness

# 粒子群优化算法主函数
def particle_swarm_optimization(num_particles, num_iterations, inertia_weight, cognitive_weight, social_weight):
    particles = [Particle(random.uniform(-10, 10)) for _ in range(num_particles)]

    global_best_x = particles[0].x
    global_best_fitness = objective_function(global_best_x)

    # 记录粒子群位置的变化
    particle_positions = []

    for _ in range(num_iterations):
        particle_positions.append([particle.x for particle in particles])

        for particle in particles:
            particle.update_velocity(global_best_x, inertia_weight, cognitive_weight, social_weight)
            particle.update_position()

            if particle.best_fitness < global_best_fitness:
                global_best_x = particle.best_x
                global_best_fitness = particle.best_fitness

    return global_best_x, global_best_fitness, particle_positions

# 粒子群优化算法的执行
best_solution, best_fitness, particle_positions = particle_swarm_optimization(num_particles=20, num_iterations=100,
                                                                              inertia_weight=0.8, cognitive_weight=2.0, social_weight=2.0)

print("最优解:", best_solution)
print("最优解对应的函数值:", best_fitness)

# 可视化粒子群的位置变化
num_iterations = len(particle_positions)
num_particles = len(particle_positions[0])

# 绘制粒子群位置的变化图
plt.figure(figsize=(10, 6))
for i in range(num_particles):
    plt.plot(range(num_iterations), [particle_positions[j][i] for j in range(num_iterations)], label=f'Particle {i+1}')
plt.xlabel('Iteration')
plt.ylabel('Particle Position')
plt.title('Particle Swarm Optimization')
plt.legend()
plt.grid(True)
plt.show()
