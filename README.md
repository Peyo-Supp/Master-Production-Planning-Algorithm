# Algorithms-for-Master-Production-Planning

This project provides tools that help with planning production and raw materials purchase activities. All the algorithms aim to optimize the planning process by minimizing costs.
The first part of this project includes several heuristics for raw material replenishment. The second part of this project includes two simulation algorithms that are modeling the behavior of the raw materials based on specified parameters.

Requirements:
this project was done from scractch using Python 3.7. 

# Table of content:
- EOQ (Economic Order Quantity)
- Fixed EOQ
- Fixed Time Supply
- Discount Bracket Replenishment 
- Least Unit Cost

- Inventory Policy Simulation 
- Simulation Order Placement

# EOQ:
This algorithm optimize the order quantity that should be purchased to minimize the order cost and holding cost. It is a robust algorithm that can easily be adjusted to account for storage constraints, etc... it is also the basis for many more complicated replenishment algorithm

# Fixed EOQ:
The fixed EOQ algorithm works like the EOQ, however it accounts for time varying demand. 

# Fixed Time Supply:
Build up from the EOQ and the Fixed EOQ. This algorithm calculates quantity for a fixed time interval.

# Discount Bracket Replenishment
This algorithm calculates the cost minimizing bracket range quantity amongs a supplier bracket. 

# Least Cost Unit
This is a complex algorithm that gives an solution that is very close to the optimal. 


# Inventory Policy and Order Placement Simulations

They simulates the evolution of the inventory for a given period given different replenishment strategies. They give really good insights as the replenishment method versus demand for the raw materials. 









