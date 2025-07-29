
# A/B Testing vs Multi-Armed Bandit Simulation

This Python script simulates and compares traditional A/B testing versus a basic epsilon-greedy multi-armed bandit algorithm using random user responses and conversion probabilities.

## Key Concepts

- **A/B Testing:** Even traffic split, longer test duration, slower adaptation
- **Bandits:** Dynamic exploration and exploitation, faster convergence to best option

## How to Run

1. Install requirements:
```bash
pip install matplotlib numpy
```

2. Run the script:
```bash
python ab_vs_bandit_simulation.py
```

3. View the comparison chart in your default image viewer.

## Use Case

This is useful to demonstrate the efficiency of bandits in dynamic environments, such as fraud rule optimization or user risk threshold testing in real time.

