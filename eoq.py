import math as m
import matplotlib.pyplot as plt

def EOQ(demand,cost_per_unit,holding_rate,aggregate_placement_cost):

    Economic_order_quantity = m.sqrt((2*demand*aggregate_placement_cost)/cost_per_unit*holding_rate)
    return Economic_order_quantity

d = 64800
v = 0.34
r = 0.01
a = 295

print(EOQ(d,v,r,a))

