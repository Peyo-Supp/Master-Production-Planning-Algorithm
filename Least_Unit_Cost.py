import numpy as np


def mps_luc(demand_forecast,setup_cost,holding_cost,init_inventory):
    '''
    argument:
    demand_forecast (list): demand for each time period
    setup_cost (float): fixed cost of setting up manufacturing
    holding_cost (float): fixed cost of init_inventory
    init_inventory(float): initial inventory
    output:
    inventory (list): inventory for each time period
    quantity (list): quantity of product manufactured for each time period
    total_cost (float): total cost of manufacturing and inventory
    '''


    prod_schedule = []
    inventory = []
    #First check how many time period the current inventory can hold
    init_prod = 0
    while init_prod in range(len(demand_forecast)):
        if np.sum(demand_forecast[:init_prod + 1]) <= init_inventory:
            init_prod += 1
        else: break


    #Add 0 as the production during this period of using current inventory
    for idx in range(init_prod):
        if idx == 0:
            prod_schedule.append(0)
            inventory.append(init_inventory - demand_forecast[idx])
        else:
            prod_schedule.append(0)
            inventory.append(inventory[idx-1] - demand_forecast[idx])

    ix = init_prod

    while ix in range(init_prod,len(demand_forecast)):
        cost = setup_cost

        if ix+1 == len(demand_forecast):
            prod_schedule.append(demand_forecast[ix])
            inventory.append(0)
            break
        next_cost = (setup_cost + demand_forecast[ix+1]*holding_cost)/((demand_forecast[1+ix]))
        inventory_factor = [1*holding_cost]
        ix2 = 1
        while next_cost <= cost and ix+ix2 < len(demand_forecast):
            cost = next_cost
            ix2 += 1
            inventory_factor.append(ix2*holding_cost)
            next_cost = ((setup_cost + sum(i[0] * i[1]
                         for i in zip(demand_forecast[ix+1:ix+ix2+1],inventory_factor)))/((demand_forecast[ix2+1])))

        ix += ix2
        if not inventory:
            production = sum(demand_forecast[ix-ix2:ix])
            inventory.append(production-demand_forecast[ix-ix2])
        else:
            production = sum(demand_forecast[ix-ix2:ix])-inventory[-1]
            inventory.append(inventory[-1]+production-demand_forecast[ix-ix2])

        prod_schedule.append(production)

        for i in range(ix2-1):
            prod_schedule.append(0)
            inventory.append(inventory[-1]-demand_forecast[ix-ix2+i+1])

    total_setup_cost = 0
    for i in prod_schedule:
        if i > 0: total_setup_cost += setup_cost

    total_holding_cost = 0
    for i in inventory:
        if i > 0: total_holding_cost += i*holding_cost

    total_cost = total_setup_cost + total_holding_cost

    return inventory,prod_schedule,total_cost



#just fill in the data that is necessary to run the model!
# demand_forecast = []
# set_up cost =
# holding_cost =
# init_inv =










