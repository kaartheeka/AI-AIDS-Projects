# Intelligent Sleep Monitoring Agent

## Overview

This project implements an Intelligent Sleep Monitoring Agent using Python and a Sleep Health dataset. It analyzes sleep quality, sleep duration, REM sleep, deep sleep, light sleep, wake episodes, stress, and mental health conditions.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab

## Features

- Loads and checks the sleep dataset
- Calculates light sleep percentage
- Converts sleep quality from 1–10 to 0–100
- Categorizes sleep quality
- Calculates Sleep Architecture Score
- Calculates Intelligent Agent Sleep Score
- Generates sleep recommendations
- Analyzes stress and mental health
- Visualizes sleep patterns and trends
- Saves the final results as a CSV file

## Agent Score

The final Agent Sleep Score is calculated using:


Agent Score = 70% Sleep Score + 30% Architecture Score


The architecture score considers light sleep, REM sleep, deep sleep, and wake episodes.

## How to Run

1. Open the code in Google Colab.
2. Run the program.
3. Upload the Sleep Health CSV dataset.
4. Execute all cells.
5. View the analysis, visualizations, and agent recommendations.

## Output

The processed results are saved as:


intelligent_sleep_agent_results.csv


The output contains the calculated sleep scores, sleep categories, architecture scores, agent scores, and agent decisions.