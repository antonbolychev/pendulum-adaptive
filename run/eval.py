import gymnasium as gym
from gymnasium.wrappers import RecordVideo
from src.controller import ControllerAdaptive, ControllerNotAdaptive
import tyro
from typing import Literal
from dataclasses import dataclass
import os


@dataclass
class Args:
    env_id: str = "PendulumQuanser-v0"
    eval_type: Literal["adaptive", "energy_based"] = "adaptive"
    friction_coeff: float = 0.08
    video_dir: str = "videos"

    def __post_init__(self):
        if self.eval_type == "adaptive":
            self.video_dir = os.path.join(self.video_dir, "adaptive")
        else:
            self.video_dir = os.path.join(
                self.video_dir, f"energy_based_friction_coef_{self.friction_coeff}"
            )


def make_env(env_id: str, video_dir: str):
    def init():
        env = gym.make(env_id, render_mode="rgb_array")
        env = RecordVideo(env, video_dir)
        return env

    return init


if __name__ == "__main__":
    args = tyro.cli(Args)

    env = make_env(args.env_id, args.video_dir)()
    if args.eval_type == "adaptive":
        controller = ControllerAdaptive()
    else:
        controller = ControllerNotAdaptive(friction_coeff=args.friction_coeff)

    observation, info = env.reset()
    truncated = False
    while not truncated:
        action = controller.get_action(observation)
        observation, reward, terminated, truncated, info = env.step(action)
