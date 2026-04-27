import math
import random

def random_trig_value():
    
    angle_deg = random.randint(0, 360)

    angle_rad = math.radians(angle_deg)
    
    sine = math.sin(angle_rad)
    cosine = math.cos(angle_rad)
    tangent = math.tan(angle_rad)
    

    print("Angle (degrees):", angle_deg)
    print("Sin:", sine)
    print("Cos:", cosine)
    print("Tan:", tangent)


random_trig_value()
