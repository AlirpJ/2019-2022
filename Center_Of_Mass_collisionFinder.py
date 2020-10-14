# Joshua Prila
print("Hello! This program can solve for velocities after an elastic collision (1D problems only)")
# Momentum is mass multiplied by velocity
mass1=input("Enter the mass of object 1 (kg) ")
vel1=input("Enter the velocity of object 1 (m/s) ")

mass2=input("Enter the mass of object 2 (kg) ")
vel2=input("Enter the velocity of object 2 (m/s) ")

# Makes sure that these are numerical values and not strings or such
# Missing: try except to catch invalid user inputs
mass1 = float(mass1)
vel1 = float(vel1)
mass2 = float(mass2)
vel2 = float(vel2)

vel_centerOfMass = ((mass1*vel1) + (mass2*vel2)) / (mass1+mass2)
print("The velocity of the center of mass is: ", vel_centerOfMass)
vel1a=vel1-vel_centerOfMass
vel2a=vel2-vel_centerOfMass

print("Initial Velocity of object 1 in CM frame of reference:",vel1a)
print("Initial Velocity of object 2 in CM frame of reference:",vel2a)

vel1a = vel1a * (-1)
vel2a = vel2a * (-1)

vel1_output = vel1a + vel_centerOfMass
vel2_output = vel2a + vel_centerOfMass
print("\nFinal velocities:")
print("Object 1 will have mass", mass1, "Velocity:", vel1_output)
print("Object 2 will have mass", mass2, "Velocity:", vel2_output)
