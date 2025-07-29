
import numpy as np
import matplotlib.pyplot as plt

# Simulated conversion rates for 3 variants
true_rates = [0.05, 0.07, 0.04]  # B is best

# Simulate user interaction
def simulate_ab(n=10000):
    counts = [0, 0, 0]
    rewards = [0, 0, 0]
    choices = []
    for _ in range(n):
        variant = np.random.choice([0, 1, 2])  # Randomly select A/B/C
        reward = np.random.rand() < true_rates[variant]
        counts[variant] += 1
        rewards[variant] += reward
        choices.append(variant)
    return counts, rewards, choices

def simulate_bandit(n=10000):
    counts = [0, 0, 0]
    rewards = [0, 0, 0]
    choices = []
    for t in range(n):
        avg = [rewards[i] / counts[i] if counts[i] > 0 else 1.0 for i in range(3)]
        epsilon = 0.1
        if np.random.rand() < epsilon:
            variant = np.random.choice([0, 1, 2])  # Explore
        else:
            variant = np.argmax(avg)  # Exploit
        reward = np.random.rand() < true_rates[variant]
        counts[variant] += 1
        rewards[variant] += reward
        choices.append(variant)
    return counts, rewards, choices

ab_counts, ab_rewards, ab_choices = simulate_ab()
bandit_counts, bandit_rewards, bandit_choices = simulate_bandit()

# Plot results
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].bar(["A", "B", "C"], ab_rewards, color="skyblue")
ax[0].set_title("A/B Testing Total Rewards")
ax[0].set_ylabel("Conversions")

ax[1].bar(["A", "B", "C"], bandit_rewards, color="lightgreen")
ax[1].set_title("Multi-Armed Bandit Total Rewards")

plt.suptitle("A/B Testing vs Multi-Armed Bandit")
plt.tight_layout()
plt.savefig("/mnt/data/ab_vs_bandit_result.png")
plt.show()
