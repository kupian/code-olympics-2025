import math

coordinates = [math.radians(int(a.strip(" {}:latlong"))) for a in input().split(",")]

lambda_1 = coordinates[1]
lambda_2 = coordinates[3]
phi_1 = coordinates[0]
phi_2 = coordinates[2]

delta_lambda = abs(lambda_1-lambda_2)
delta_phi = abs(phi_1-phi_2)

delta_sigma = math.acos(
    (math.sin(phi_1)*math.sin(phi_2)) + (math.cos(phi_1)*math.cos(phi_2)*math.cos(delta_lambda))
)

R = 6371000

print(round((delta_sigma*R)/300000))
