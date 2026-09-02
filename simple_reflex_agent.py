import pandas as pd

# reading the csv file
data = pd.read_csv("city_day.csv")

# converting date into date format
data["Date"] = pd.to_datetime(data["Date"])

# removing rows where AQI is empty
data = data.dropna(subset=["AQI"])


# simple reflex agent
def aqi_agent(aqi):

    if aqi <= 100:
        return "Good", "Normal outdoor activities are okay"

    elif aqi <= 200:
        return "Moderate", "Sensitive people should be careful"

    elif aqi <= 300:
        return "Poor", "Reduce outdoor activities"

    elif aqi <= 400:
        return "Very Poor", "Avoid unnecessary outdoor activities"

    else:
        return "Severe", "Stay indoors and take precautions"


print("----- AQI SIMPLE REFLEX AGENT -----")

# showing all cities
print("\nCities available in the dataset:")

cities = sorted(data["City"].dropna().unique())

for city_name in cities:
    print(city_name)


city = input("\nEnter city name: ")

# selecting the city
city_data = data[data["City"] == city]

if len(city_data) == 0:
    print("City not found")

else:
    city_data = city_data.sort_values("Date")

    # taking latest AQI
    latest = city_data.iloc[-1]

    aqi = latest["AQI"]

    category, action = aqi_agent(aqi)

    print("\n----- CURRENT AQI -----")
    print("City:", city)
    print("Date:", latest["Date"].date())
    print("AQI:", round(aqi, 2))

    print("\n----- AGENT RESULT -----")
    print("Category:", category)
    print("Action:", action)

    # storing last 5 AQI values
    last_five = city_data.tail(5)

    print("\n----- LAST 5 AQI VALUES -----")

    for i, row in last_five.iterrows():
        print(row["Date"].date(), ":", round(row["AQI"], 2))

    # simple prediction
    values = last_five["AQI"].tolist()

    predicted_aqi = sum(values) / len(values)

    predicted_category, predicted_action = aqi_agent(predicted_aqi)

    print("\n----- NEXT DAY ESTIMATE -----")
    print("Estimated AQI:", round(predicted_aqi, 2))
    print("Category:", predicted_category)
    print("Action:", predicted_action)