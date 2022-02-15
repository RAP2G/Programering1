# Soma Szabo
# INF20
# 07-09-2021
# Boll Släpps

import math

height = int(input("How high is the ball? Is it high as ...BALLS?????? "))
print(height)
while height > 0.01:
    height = height*0.7

    if height > 0.9:
        print(f"{round(height,1)}m")
    elif height > 0.09:
        print(f"{round((height*10),1)}dm")
