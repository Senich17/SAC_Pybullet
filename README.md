# SAC_Pybullet

This project involves experimenting with hyperparameters for training agents in continuous action spaces using SAC (Soft Actor-Critic) and PPO (Proximal Policy Optimization) algorithms within the PyBullet environment.

## Experiment Procedure

1. **Baseline Training**: Train the algorithm with default hyperparameters (using CleanRL).
2. **Hyperparameter Tuning**: Select and test various hyperparameters such as entropy coefficient, learning rate, and gradient steps. These parameters significantly influence the training process and model performance.
3. **Experiment Execution**: Run experiments using a matrix of chosen hyperparameters.
4. **Visualization**: Review the visual results of the experiments [here](https://wandb.ai/senich17/SAC_Pybullet?nw=nwusersenich17).

## Hyperparameter Variations and Model Behavior

- **Run 0**: Default hyperparameters, effective for most tasks, demonstrating general efficiency.
- **Run 1**: `learning_rate=0.001`, `ent_coef=0.1`, `gradient_steps=2`
  - Shows improved average reward but slower training. Significant reward fluctuations may indicate instability.
- **Run 2**: `learning_rate=0.0001`, `ent_coef=0.1`, `gradient_steps=3`
  - Shows better average reward per episode, though the training time is longer. The model remains stable.
- **Run 3**: `ent_coef=0.5`
  - The model demonstrates a significant departure from previous runs, with a tendency to explore more and less reward acquisition. High entropy coefficient requires sufficient model updates to stabilize learning and avoid strategy degradation.

## Conclusion

Based on the visualizations available in the [Colab notebook](https://colab.research.google.com/drive/1dLI0-pR5mbzEsuXZp3u0CEUAx57vpDJi?usp=sharing), you can assess the reward distribution at each stage of the experiment. It is crucial to consider both the stability of the learning process and the resource consumption when tuning hyperparameters.
