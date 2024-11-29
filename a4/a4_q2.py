import numpy as np
import matplotlib.pyplot as plt

# six-hump camelback function
def camelback(x, y):
    return (4 - 2.1 * x**2 + x**4 / 3) * x**2 + x * y + (-4 + 4 * y**2) * y**2

# PSO implementation with constriction factor
def pso(
    objective_function, bounds, num_particles=30, max_iter=100, vel_update="guaranteed_convergence"
):

    if vel_update == "simple":
        w = 0.0 # no consideration for old velocity value
        chi = 1.0 # ignore
        c1 = 1.5
        c2 = 1.5
    elif vel_update == "inertia_weight":
        w = 0.5
        chi = 1.0 # ignore
        c1 = 1.5
        c2 = 1.5
    elif vel_update == "constriction_factor":
        w = 1.0 # setting w = 1 does not scale old velocity
        c1 = 2.5
        c2 = 2.5
        # calculate constriction factor
        phi = c1 + c2
        if phi <= 4:
            raise ValueError("The sum of c1 and c2 must be greater than 4 to use constriction factor.")
        chi = 2 / abs(2 - phi - np.sqrt(phi**2 - 4 * phi))

    elif vel_update == "guaranteed_convergence":
        w = 0.5
        rho = 1.0
        s_c = 20
        f_c = 20
        consecutive_success = 0
        consecutive_fail = 0

    else:
        raise ValueError("Invalid choice of velocity update profile")

    # initialize particle positions and velocities
    dim = len(bounds)
    particles = np.random.uniform(
        [b[0] for b in bounds], [b[1] for b in bounds], (num_particles, dim)
    )
    velocities = np.random.uniform(-1, 1, (num_particles, dim))
    
    # initialize personal best positions and global best position
    personal_best_positions = np.copy(particles)
    personal_best_scores = np.array(
        [objective_function(*p) for p in particles]
    )
    global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
    global_best_score = min(personal_best_scores)
    
    # store progress for plotting
    best_scores = []
    avg_scores = []
    
    for iteration in range(max_iter):
        # evaluate fitness
        scores = np.array([objective_function(*p) for p in particles])
        
        # update personal best
        better_scores_idx = scores < personal_best_scores
        personal_best_scores[better_scores_idx] = scores[better_scores_idx]
        personal_best_positions[better_scores_idx] = particles[better_scores_idx]
        
        # update global best
        if min(scores) < global_best_score:
            global_best_score = min(scores)
            global_best_position = particles[np.argmin(scores)]

            if vel_update == "guaranteed_convergence":
                consecutive_success += 1
                consecutive_fail = 0
        else:
            if vel_update == "guaranteed_convergence":
                consecutive_fail += 1
                consecutive_success = 0

        # update particle velocities and positions
        if vel_update == "guaranteed_convergence":
            if consecutive_success > s_c:
                rho = 2 * rho
            elif consecutive_fail > f_c:
                rho = 0.5 * rho
            else:
                rho = rho

            r = np.random.random((num_particles, 1)) * 2 - 1
            velocities = (w * velocities
                        - particles
                        + rho * r)

        else:
            r1 = np.random.random((num_particles, dim))
            r2 = np.random.random((num_particles, dim))
            velocities = chi * (
                w * velocities
                + c1 * r1 * (personal_best_positions - particles)
                + c2 * r2 * (global_best_position - particles)
            )

        particles += velocities
        
        # apply bounds
        for i in range(dim):
            particles[:, i] = np.clip(particles[:, i], bounds[i][0], bounds[i][1])
        
        # record progress
        best_scores.append(global_best_score)
        avg_scores.append(np.mean(scores))

    return global_best_position, global_best_score, best_scores, avg_scores

# define bounds for x and y
bounds = [(-5, 5), (-5, 5)]

# run PSO
best_position, best_score, best_scores, avg_scores = pso(camelback, bounds)

# print the results
print("Best Position:", best_position)
print("Best Score:", best_score)

# plot the progress
plt.figure(figsize=(10, 5))
plt.plot(best_scores, label="Best Score")
plt.plot(avg_scores, label="Average Score")
plt.xlabel("Iteration")
plt.ylabel("Score")
plt.legend()
plt.title("PSO Progress with Constriction Factor")
plt.show()