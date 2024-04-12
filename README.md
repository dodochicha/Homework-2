# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
> 
tokenB->tokenA->tokenE->tokenD->tokenC->tokenB

swap, tokenB -> tokenA, AmountIn = 5.000000000000000000, AmountOut =  5.666666666666666  

swap, tokenA -> tokenE, AmountIn = 5.666666666666666, AmountOut =  1.0624999999999996

swap, tokenE -> tokenD, AmountIn = 1.0624999999999996, AmountOut =  2.4460431654676285

swap, tokenD -> tokenC, AmountIn = 2.4460431654676285, AmountOut = 5.079681274900402

swap, tokenC -> tokenB, AmountIn = 5.079681274900402, AmountOut = 20.140412461605976 

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

 When you make a trade on a platform like Uniswap V2, the price you expect to get may not match the price you actually get. This difference is called slippage. It happens because when you trade, you're affecting the balance of assets in the pool. So, even though you might start with a certain ratio of assets, your trade changes that ratio, causing the price to shift slightly. Uniswap V2 tries to minimize this slippage using a formula that keeps the product of the amounts of each asset constant in the pool.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

The reason for deducting a minimum liquidity amount during the initial liquidity creation process in the mint function of the UniswapV2Pair contract is to avoid the formation of excessively small liquidity positions. This precautionary measure helps to ensure that the liquidity pool is utilized more effectively and reduces the likelihood of liquidity providers facing significant impermanent loss risks.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

the formula used when adding tokens to the UniswapV2Pair contract ensures that the new tokens being added are in harmony with the existing reserves in the liquidity pool, keeping the product of the reserves constant. This prevents any attempts to manipulate the pool and keeps trading conditions fair and efficient for all users.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

A sandwich attack in decentralized exchanges involves frontrunners who watch for pending transactions, swiftly place their own trades to influence prices, and profit by executing trades before and after a targeted transaction. This activity can affect your swaps by causing slippage, leading to less advantageous prices for you.

