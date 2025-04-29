import random

# Define the puzzle box environment
actions = ["press_lever", "scratch_box", "meow"]
reward_action = "press_lever"

def puzzle_box(action):
    if action == reward_action:
        return 1  # Reward for the correct action
    return 0  # No reward for other actions

# Trial-and-error simulation
for trial in range(10):
    action = random.choice(actions)
    reward = puzzle_box(action)
    print(f"Trial {trial+1}: Action = {action}, Reward = {reward}")
