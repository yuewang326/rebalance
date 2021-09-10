import pandas as pd
import numpy as np
def rebalance(holdings, target_weigts, band):
    """
    Args: 
        holdings(array): The portfolios with current weights.
        target_weights(array): The portfolios with target weights.
        band(float): The tolerance around the target weights.
    return:
        The ticker and shares(positive shares to buy, negative to sell).
    """
    portfolio= pd.DataFrame(holdings, columns = ['ticker', 'price', 'shares'])
    tar_port = pd.DataFrame(target_weigts, columns = ['ticker', 'weights'])
    port_sum = (portfolio['price'] * portfolio['shares']).sum()
    portfolio['weights'] = portfolio['price'] * portfolio['shares']/port_sum
    portfolio['tar_weights'] = tar_port['weights']
    portfolio['band'] = portfolio['tar_weights'] - portfolio['weights']
    df = portfolio[portfolio['band'].abs() > band]
    df['buy_sell'] = round(((df['tar_weights']* port_sum) - (df['price'] * df['shares']))/df['price'], 0)
    result = np.array(df[['ticker','buy_sell']])
    return result

if __name__ == "__main__":
    Holdings = (["AAA", 125, 100], ["BBBB", 100, 200], ["CC", 50, 500], ["DDD", 200, 50], ["EE", 25, 750], ["FFFF", 150, 65], ["G", 100, 150], ["HHH", 310, 25], ["II", 15, 500], ["JJJJ", 205, 75])
    tar_Weights= (["HHH", 0.087], ["BBBB", 0.113], ["II", 0.05], ["EE", 0.15], ["CC", 0.05], ["G", .05], ["FFFF", 0.15], ["AAA", 0.15], ["JJJJ", 0.092], ["DDD", 0.108]) 
    bands = 0.002
    print(rebalance(Holdings, tar_Weights, bands))
