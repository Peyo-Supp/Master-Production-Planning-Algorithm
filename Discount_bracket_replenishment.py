import pandas as pd
import math as m
import numpy as np

"""
algorithm that calculate the best alternative from supplier order bracket based on data provided.

"""

#input data here!
# demand_in_cases =
# order_cost =
# cost_per_case =
# bracket_cost = []
# bracket_minimum = []
# holding_rate =

EOQ0 = np.sqrt((2*demand_in_cases*order_cost)/(cost_per_case*holding_rate))
ATCEOQ = demand_in_cases/EOQ0*order_cost + EOQ0/2*holding_rate*cost_per_case + demand_in_cases*cost_per_case

#create a dataframe for the bracket_minimum)
BM = np.array(bracket_minimum)


dfBM = pd.DataFrame({'1':[BM[0]],'2':[BM[1]],'3':[BM[2]],'4':[BM[3]],'5':[BM[4]],'6':[BM[5]],'7':[BM[6]]}, index = [1])

#compute EOQ for each bracket and put into its own dataframe

BC = np.array(bracket_cost)
BM = np.array(bracket_minimum)

EOQ = np.sqrt((2*demand_in_cases*order_cost)/(BC*holding_rate))

DfEOQ = pd.DataFrame({'1':[EOQ[0]],'2': [EOQ[1]],'3':[EOQ[2]],'4':[EOQ[3]],'5':[EOQ[4]],'6':[EOQ[5]],'6':[EOQ[6]]}, index =[1])


#substrack the BM data frame with eoq dataframe to find which data is greater than 0

check = (dfBM.sub(DfEOQ))

c = np.array(check)
print(c)

def calc_atc(c,val):

    for i in c:
        if i<= val:
            print( 'a' )

        else:
            print('b')
val = 0
calc_atc(c,val)





