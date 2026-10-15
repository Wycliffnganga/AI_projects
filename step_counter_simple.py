# AI master class foundations week 1 project
# practicing loops, conditionals and variables

steps = [5800, 4000, 3000, 7000, 10000, 2000, 5000]
target = 6000

for walk in steps:
    if walk < 5000:
        continue
    if walk >= target:
        print(f"your steps today are {walk}. keep going. you are a star.")
    else:
        print(f"you only gat {target - walk} steps to reach the goal. pull up your socks my friend.")
