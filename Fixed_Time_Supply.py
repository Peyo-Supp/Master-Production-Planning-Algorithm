import math as m

def st(demand_forecast, t, setup_cost, holding_cost, acquisition_cost):


    for i in range(0, len(demand_forecast), int(round(t))):

        yield demand_forecast[i:int(i + t)]




#very simple algorithm

# demand_forecast = []
# avg_demand = sum(demand_forecast)
# setup_cost =
# holding_cost =
# acquisition_cost =
#t = m.sqrt((2*setup_cost)/(avg_demand*holding_cost*acquisition_cost))*len(demand_forecast)





