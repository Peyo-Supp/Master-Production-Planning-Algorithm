import numpy as np
import math as m



demand_forecast = (120,151,103,114,180,117,115,102)
total_demand = sum(demand_forecast)
aggregate_order_cost = 91.57
unit_cost = 12.15
holding_rate = 0.34
q = m.sqrt((2 * total_demand * aggregate_order_cost) / (unit_cost* holding_rate))

print(demand_forecast)


def subs(demand_forecast, q):
    sum = 0
    for i, e in enumerate(demand_forecast):
        sum += e
        if sum > q:
            if abs(sum - q) > abs(sum - e - q):
                r = sum - e
                sum = e
                n = i - 1
            else:
                r = sum
                sum = 0
                n = i
            yield n, r
    yield i, sum

print(list(subs(demand_forecast, q)))

