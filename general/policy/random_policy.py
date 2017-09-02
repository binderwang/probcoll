import numpy as np
from config import params

class RandomPolicy():

    def act(self, obs_frame=None, t=0, time_step=0, only_noise=False, only_no_noise=False, visualize=False):
        u = np.random.uniform(
            params['planning']['control_range']['lower'],
            params['planning']['control_range']['upper'])
        return u, u
