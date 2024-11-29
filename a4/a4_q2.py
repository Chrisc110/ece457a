import numpy as np
import matplotlib.pyplot as plt

# Define the six-hump camelback function
def camelback(x, y):
    return (4 - 2.1 * x**2 + x**4 / 3) * x**2 + x * y + (-4 + 4 * y**2) * y**2

# PSO implementation
def pso(
    objective_function, bounds, num_particles=30, max_iter=100, w=0.0, c1=1.5, c2=1.5
):
    # Initialize particle positions and velocities
    dim = len(bounds)
    particles = np.random.uniform(
        [b[0] for b in bounds], [b[1] for b in bounds], (num_particles, dim)
    )
    velocities = np.random.uniform(-1, 1, (num_particles, dim))
    
    # Initialize personal best positions and global best position
    personal_best_positions = np.copy(particles)
    personal_best_scores = np.array(
        [objective_function(*p) for p in particles]
    )
    global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
    global_best_score = min(personal_best_scores)
    
    # Store progress for plotting
    best_scores = []
    avg_scores = []
    
    for iteration in range(max_iter):
        # Evaluate fitness
        scores = np.array([objective_function(*p) for p in particles])
        
        # Update personal best
        better_scores_idx = scores < personal_best_scores
        personal_best_scores[better_scores_idx] = scores[better_scores_idx]
        personal_best_positions[better_scores_idx] = particles[better_scores_idx]
        
        # Update global best
        if min(scores) < global_best_score:
            global_best_score = min(scores)
            global_best_position = particles[np.argmin(scores)]
        
        # Update particle velocities and positions
        r1 = np.random.random((num_particles, dim))
        r2 = np.random.random((num_particles, dim))
        velocities = (
            w * velocities
            + c1 * r1 * (personal_best_positions - particles)
            + c2 * r2 * (global_best_position - particles)
        )
        particles += velocities
        
        # Apply bounds
        for i in range(dim):
            particles[:, i] = np.clip(particles[:, i], bounds[i][0], bounds[i][1])
        
        # Record progress
        best_scores.append(global_best_score)
        avg_scores.append(np.mean(scores))
    
    return global_best_position, global_best_score, best_scores, avg_scores

# Define bounds for x and y
bounds = [(-5, 5), (-5, 5)]

# Run PSO
best_position, best_score, best_scores, avg_scores = pso(camelback, bounds)

# Print the results
print("Best Position:", best_position)
print("Best Score:", best_score)

# Plot the progress
plt.figure(figsize=(10, 5))
plt.plot(best_scores, label="Best Score")
plt.plot(avg_scores, label="Average Score")
plt.xlabel("Iteration")
plt.ylabel("Score")
plt.legend()
plt.title("PSO Progress")
plt.show()