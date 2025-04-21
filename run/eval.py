import gymnasium as gym
from gymnasium.wrappers import RecordVideo
from src.controller import ControllerAdaptive


def make_env(env_id: str):
    def init():
        env = gym.make(env_id, render_mode="rgb_array")
        env = RecordVideo(env, "videos")
        return env

    return init


env = make_env("PendulumQuanser-v0")()
controller = ControllerAdaptive()

observation, info = env.reset()
truncated = False
while not truncated:
    action = controller.get_action(observation)
    observation, reward, terminated, truncated, info = env.step(action)
