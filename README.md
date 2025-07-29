# Monte-Carlo-simulation
This repository provides an implementation of a Monte Carlo Simulation. Monte Carlo methods are widely used for solving problems in various fields, such as finance, physics, engineering, and more. The simulation uses random sampling to estimate numerical results and is particularly useful for modeling systems with inherent uncertainty.

📌 Key Features
Pulls real historical price data using the yfinance library.

Simulates 10,000 potential return paths over a 1-year horizon (252 trading days).

Estimates portfolio value paths using log-normal return accumulation.

Calculates Monte Carlo-based Value at Risk (VaR) at a 99% confidence level.

Visualizes the distribution of simulated returns and the VaR threshold.

📈 Financial Concept: Value at Risk (VaR)
VaR estimates the maximum potential loss in portfolio value over a defined period for a given confidence level.
In this project:

A 1-year holding period

A 99% confidence level

Monte Carlo simulation with normally distributed daily returns

# Use Cases 
- Risk assessment in financial portfolios
- Estimation of probabilities in complex systems
- Simulation of physical phenomena
- Decision-making under uncertainty

# Contributing 
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

# Contact 
For questions or suggestions, feel free to open an issue or reach out at manasa.savnur@gmail.com
