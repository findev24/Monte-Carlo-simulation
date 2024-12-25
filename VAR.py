import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical data for a stock
data = yf.download("MSFT", start="2020-01-01", end="2025-01-01")
returns = data['Adj Close'].pct_change().dropna()

# Simulate future returns using Monte Carlo
num_simulations = 10000
simulation_horizon = 252  # trading days in a year
simulated_returns = np.random.normal(np.mean(returns), np.std(returns), (simulation_horizon, num_simulations))

# Calculate the simulated portfolio values
initial_investment = 1000000  # $1,000,000
portfolio_values = initial_investment * np.exp(np.cumsum(simulated_returns, axis=0))

# Calculate the portfolio returns
portfolio_returns = portfolio_values[-1] / portfolio_values[0] - 1

# Calculate the VaR at 99% confidence level
confidence_level = 0.99
VaR_monte_carlo = np.percentile(portfolio_returns, (1 - confidence_level) * 100)

print(f"Monte Carlo VaR (99% confidence level): {VaR_monte_carlo:.2%}")

# Plot the distribution of simulated portfolio returns and VaR threshold
plt.figure(figsize=(10, 6))
plt.hist(portfolio_returns, bins=50, alpha=0.75, color='blue', edgecolor='black')
plt.axvline(VaR_monte_carlo, color='red', linestyle='--', label=f'VaR (99%): {VaR_monte_carlo:.2%}')
plt.title('Simulated Portfolio Returns Distribution')
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.legend()
plt.show()
