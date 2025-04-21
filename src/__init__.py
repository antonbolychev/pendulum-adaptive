import gymnasium as gym


gym.register(
    id="PendulumQuanser-v0",
    entry_point="src.pendulum:PendulumQuanserEnv",
    max_episode_steps=1000,
)
