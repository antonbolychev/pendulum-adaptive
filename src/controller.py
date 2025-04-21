import numpy as np
import gymnasium as gym


class ControllerNotAdaptive:
    def __init__(
        self,
        gain: float = 0.03,
        action_min: float = -0.1,
        action_max: float = 0.1,
        pd_coeffs: np.ndarray = np.array([0.6, 0.2]),
        switch_loc: float = np.cos(np.pi / 10),
        env_id: str = "PendulumQuanser-v0",
    ):
        super().__init__()
        self.gain = gain
        self.action_min = action_min
        self.action_max = action_max
        self.switch_loc = switch_loc
        self.pd_coeffs = pd_coeffs
        self.env = gym.make(env_id)

    def get_action(self, observation: np.ndarray) -> np.ndarray:
        mass, grav_const, length, friction_coeff = (
            self.env.m,
            self.env.g,
            self.env.l,
            self.env.friction_coeff,
        )

        cos_angle = observation[0]
        sin_angle = observation[1]
        angle = np.arctan2(sin_angle, cos_angle)
        angle_vel = observation[2]
        energy_total = (
            mass * grav_const * length * (np.cos(angle) - 1) / 2
            + 1 / 2 * self.env.pendulum_moment_inertia() * angle_vel**2
        )
        energy_control_action = -self.gain * np.sign(
            angle_vel * energy_total
        ) + friction_coeff * self.env.pendulum_moment_inertia() * angle_vel * np.abs(
            angle_vel
        )

        if np.cos(angle) <= self.switch_loc:
            action = energy_control_action
        else:
            action = -self.pd_coeffs[0] * np.sin(angle) - self.pd_coeffs[1] * angle_vel

        return np.array(
            [
                np.clip(
                    action,
                    self.action_min,
                    self.action_max,
                )
            ]
        )


class ControllerAdaptive:
    def __init__(
        self,
        gain: float = 0.03,
        action_min: float = -0.1,
        action_max: float = 0.1,
        sampling_time: float = 0.01,
        gain_adaptive: float = 0.02,
        switch_loc: float = np.cos(np.pi / 10),
        pd_coeffs: list = [0.6, 0.2],
        env_id: str = "PendulumQuanser-v0",
        friction_coeff_est_init: float = 0,
    ):
        super().__init__()
        self.gain = gain
        self.action_min = action_min
        self.action_max = action_max
        self.friction_coeff_est = friction_coeff_est_init
        self.sampling_time = sampling_time
        self.gain_adaptive = gain_adaptive
        self.switch_loc = switch_loc
        self.pd_coeffs = pd_coeffs
        self.env = gym.make(env_id)

    def get_action(self, observation: np.ndarray) -> np.ndarray:
        mass, grav_const, length = (
            self.env.m,
            self.env.g,
            self.env.l,
        )

        cos_angle = observation[0]
        sin_angle = observation[1]
        angle = np.arctan2(sin_angle, cos_angle)
        angle_vel = observation[2]

        energy_total = (
            mass * grav_const * length * (np.cos(angle) - 1) / 2
            + 1 / 2 * self.env.pendulum_moment_inertia() * angle_vel**2
        )
        energy_control_action = -self.gain * np.sign(
            angle_vel * energy_total
        ) + self.friction_coeff_est * self.env.pendulum_moment_inertia() * angle_vel * np.abs(
            angle_vel
        )

        # Parameter adaptation using Euler scheme
        self.friction_coeff_est += (
            -self.gain_adaptive
            * energy_total
            * mass
            * length**2
            * np.abs(angle_vel) ** 3
            * self.sampling_time
        )

        action = (
            energy_control_action
            if np.cos(angle) <= self.switch_loc
            else -self.pd_coeffs[0] * np.sin(angle) - self.pd_coeffs[1] * angle_vel
        )
        return np.array(
            [
                np.clip(
                    action,
                    self.action_min,
                    self.action_max,
                )
            ]
        )
