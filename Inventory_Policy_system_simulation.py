import simpy
import numpy as np
import matplotlib.pyplot as plt


"""
this code creates a simulation for a inventory management policy

parameters can be adjusted to see how the inventory would behave based on different input


"""
def inventory_cycle(env, order_cutoff, order_target):
    global inventory, balance, num_ordered

    inventory = order_target
    balance = 0.0
    num_ordered = 0


    #customer arrival
    while True:
        interarrival = generate_interarrival()
        yield env.timeout(interarrival)
        balance = inventory * 2 * interarrival
        demand = generate_demand()

        if demand < inventory:
            #100 is the example selling price. in our case it would be viibit selling price point
            balance += 100*demand
            inventory -= demand
            print('sold {}'.format(demand))

        else:
            balance += 100*inventory
            inventory = 0
            print('sold {} (out of stock)'.format(inventory))

        if inventory < order_cutoff and num_ordered ==0:
            env.process(handle_order(env, order_target))

def handle_order(env, order_target):
    global inventory, balance, num_ordered

    num_ordered = order_target - inventory
    print('place order for {}'.format(env.now, num_ordered))
    #50 is just the example price to order each thing
    balance -= 50*num_ordered
    yield env.timeout(2.0)
    inventory += num_ordered
    num_ordered = 0
    print('receive order for {}'.format(env.now, inventory))



#generate random customer number bought
def generate_interarrival():
    return np.random.exponential(1./5)

def generate_demand():
    return np.random.randint(1, 5)


obs_time = []
inventory_level = []

def observe(env):
    global inventory

    while True:
        obs_time.append(env.now)
        inventory_level.append(inventory)
        yield env.timeout(0.1)


#simulation
np.random.seed(0)

env = simpy.Environment()

#10 is the re order point, and 30 is re order quantity
env.process(warehouse_run(env, 10, 30))
env.process(observe(env))

env.run(until=5)


plt.figure()
plt.step(obs_time, inventory_level, where= 'post')
plt.xlabel('simulation time (days')
plt.ylabel('inventory level')

plt.show()



