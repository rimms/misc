#!/usr/bin/env python

from jubatus.bandit.client import Bandit


client = Bandit('127.0.0.1', 9199, 'test')


# Register arm
client.register_arm('arm-1')

# Select arm
print client.select_arm('player-1')  # Return `arm-1`

# Register reward
client.register_reward('player-1', 'arm-1', 1.0)

# Select arm
print client.select_arm('player-1')  # Return `arm-1`

# Get arm info
print client.get_arm_info('player-1')  # Return {'arm-1': arm_info{trial_count: 1, weight: 1.0}}
