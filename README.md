# AI-AIDS-Projects
A Simple Reflex Agent for Air Quality Index (AQI) analysis and classification using Indian air quality data.
# AI-AIDS Projects

## AQI Simple Reflex Agent

A Simple Reflex Agent for Air Quality Index (AQI) analysis and classification using Indian air quality data.

---

## 1. Problem Statement

The objective of this project is to develop a Simple Reflex Agent that analyzes the Air Quality Index (AQI) of a particular location and determines the corresponding air-quality category.

The agent takes the current AQI value as its input and uses predefined condition-action rules to classify the air quality as Good, Satisfactory, Moderate, Poor, Very Poor, or Severe.

---

## 2. Objective

The main objectives of this project are:

- To understand the concept of a Simple Reflex Agent.
- To use real-world air-quality data from Indian cities.
- To process AQI data using Python.
- To apply condition-action rules for AQI classification.
- To provide an understandable output indicating the quality of air.

---

## 3. Dataset

The project uses the **Air Quality Data in India** dataset.

The dataset contains air-quality measurements from different Indian cities over different dates.

Important attributes include:

- City
- Date
- PM2.5
- PM10
- NO
- NO2
- NOx
- NH3
- CO
- SO2
- O3
- AQI
- AQI_Bucket

The main file used in this project is:

`city_day.csv`

---

## 4. What is a Simple Reflex Agent?

A Simple Reflex Agent is an intelligent agent that selects an action based only on the current percept.

It does not use past experiences, memory, or learning.

The agent follows predefined **condition-action rules**.

The basic structure is:

Current Percept → Condition → Action

For this project:

AQI Value → AQI Rule → AQI Category

---

## 5. Agent Architecture

```text
              Environment
                   |
                   v
             AQI Dataset
                   |
                   v
             Current AQI
                   |
                   v
        +---------------------+
        | Simple Reflex Agent |
        +---------------------+
                   |
                   v
          Condition-Action
               Rules
                   |
                   v
            AQI Category
                   |
                   v
               Output
****Sample Output
----- AQI SIMPLE REFLEX AGENT -----

Cities available in the dataset:
Ahmedabad
Amritsar
Bengaluru
Chandigarh
Delhi
Hyderabad
Mumbai
Patna
...

Enter city name: Patna

----- CURRENT AQI -----
City: Patna
Date: 2020-07-01
AQI: 120.0

----- AGENT RESULT -----
Category: Moderate
Action: Sensitive people should be careful

----- LAST 5 AQI VALUES -----
2020-06-27 : 110.0
2020-06-28 : 125.0
2020-06-29 : 130.0
2020-06-30 : 115.0
2020-07-01 : 120.0

----- NEXT DAY ESTIMATE -----
Estimated AQI: 120.0
Category: Moderate
Action: Sensitive people should be careful



















