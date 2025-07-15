# Alzheimer-s-simulation
This is a simple Python-based simulation of a hypothetical gene regulatory network related to Alzheimer’s disease. The project uses (imaginary data) to model how certain genes might interact and influence neuron function over time.

This is (not based on real biological data) The model is exploratory and designed for learning, visualization, and testing ideas.

What It Simulates?
- Key genes involved:
  - `APP`, `BACE1`, and `PSEN1` driving amyloid production
  - `Amyloid` accumulates and affects downstream targets
  - `Tau` influenced by amyloid buildup
  - `Neuron_function` gradually inhibited as amyloid increases

The simulation shows how activity levels of these genes change over time, starting from initial values and updating based on simple activation/inhibition rules.

Output

The program generates a plot that shows how gene activity levels evolve over time steps. For example:
- Amyloid and Tau increase
- Neuron function decreases slightly due to inhibition
