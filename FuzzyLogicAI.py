import numpy
import skfuzzy
from skfuzzy import control
import time

def createFuzzyWeatherAI():
    # Define fuzzy variables
    temperature = control.Antecedent(numpy.arange(-20, 41, 1), 'temperature')
    humidity = control.Antecedent(numpy.arange(0, 101, 1), 'humidity')
    windSpeed = control.Antecedent(numpy.arange(0, 51, 1), 'windSpeed')
    pressure = control.Antecedent(numpy.arange(900, 1101, 1), 'pressure')
    weather = control.Consequent(numpy.arange(0, 10, 1), 'weather')

    # Memberships for temp, humidity, wind speed and pressure
    temperature['cold'] = skfuzzy.trapmf(temperature.universe, [-20, -20, -5, 0])
    temperature['cool'] = skfuzzy.trapmf(temperature.universe, [-5, 0, 10, 15])
    temperature['mild'] = skfuzzy.trapmf(temperature.universe, [10, 15, 20, 25])
    temperature['warm'] = skfuzzy.trapmf(temperature.universe, [20, 25, 30, 35])
    temperature['hot'] = skfuzzy.trapmf(temperature.universe, [30, 35, 40, 40])

    humidity['low'] = skfuzzy.trapmf(humidity.universe, [0, 0, 30, 40])
    humidity['medium'] = skfuzzy.trapmf(humidity.universe, [30, 40, 60, 70])
    humidity['high'] = skfuzzy.trapmf(humidity.universe, [60, 70, 100, 100])

    windSpeed['calm'] = skfuzzy.trapmf(windSpeed.universe, [0, 0, 10, 15])
    windSpeed['breezy'] = skfuzzy.trapmf(windSpeed.universe, [10, 15, 25, 30])
    windSpeed['windy'] = skfuzzy.trapmf(windSpeed.universe, [25, 30, 50, 50])

    pressure['low'] = skfuzzy.trapmf(pressure.universe, [900, 900, 970, 990])
    pressure['medium'] = skfuzzy.trapmf(pressure.universe, [970, 990, 1020, 1030])
    pressure['high'] = skfuzzy.trapmf(pressure.universe, [1020, 1030, 1100, 1100])

    weather['heavySnow'] = skfuzzy.trimf(weather.universe, [0, 0, 1])
    weather['rainy'] = skfuzzy.trimf(weather.universe, [1, 1, 2])
    weather['windyAndCloudy'] = skfuzzy.trimf(weather.universe, [2, 2, 3])
    weather['clear'] = skfuzzy.trimf(weather.universe, [3, 3, 4])
    weather['humid'] = skfuzzy.trimf(weather.universe, [4, 4, 5])
    weather['mild'] = skfuzzy.trimf(weather.universe, [5, 5, 6])
    weather['hotAndDry'] = skfuzzy.trimf(weather.universe, [6, 6, 7])
    weather['hotWithBreeze'] = skfuzzy.trimf(weather.universe, [7, 7, 8])
    weather['humidAndWarm'] = skfuzzy.trimf(weather.universe, [8, 8, 9])
    weather['warmAndClear'] = skfuzzy.trimf(weather.universe, [9, 9, 10])

    # Fuzzy rules
    rules = [
        control.Rule(temperature['cold'] & humidity['high'] & windSpeed['calm'], weather['heavySnow']),
        control.Rule(temperature['cool'] & humidity['medium'] & windSpeed['breezy'], weather['rainy']),
        control.Rule(temperature['mild'] & humidity['medium'] & windSpeed['breezy'], weather['windyAndCloudy']),
        control.Rule(temperature['warm'] & humidity['low'] & pressure['high'], weather['clear']),
        control.Rule(temperature['mild'] & humidity['high'] & pressure['medium'], weather['humid']),
        control.Rule(temperature['mild'] & humidity['medium'] & pressure['medium'], weather['mild']),
        control.Rule(temperature['hot'] & humidity['low'] & pressure['high'], weather['hotAndDry']),
        control.Rule(temperature['hot'] & humidity['low'] & windSpeed['breezy'], weather['hotWithBreeze']),
        control.Rule(temperature['warm'] & humidity['high'] & pressure['high'], weather['humidAndWarm']),
        control.Rule(temperature['warm'] & humidity['medium'] & pressure['high'], weather['warmAndClear']),
    ]

    # Default rule (so that the program doesnt crash)
    rules.append(control.Rule(
        temperature['cold'] | temperature['cool'] | temperature['mild'] | temperature['warm'] | temperature['hot'],
        weather['clear'] 
    ))

    # Control system
    weatherControl = control.ControlSystem(rules)
    return control.ControlSystemSimulation(weatherControl)


def predictWeather(weatherPrediction, temperature, humidity, windSpeed, pressure):
    weatherPrediction.input['temperature'] = temperature
    weatherPrediction.input['humidity'] = humidity
    weatherPrediction.input['windSpeed'] = windSpeed
    weatherPrediction.input['pressure'] = pressure
    weatherPrediction.compute()
    weatherScore = weatherPrediction.output['weather']
    weatherConditions = [
        "Heavy Snow", "Rainy", "Windy and Cloudy", "Clear",
        "Humid", "Mild", "Hot and Dry", "Hot with Breeze",
        "Humid and Warm", "Warm and Clear"
    ]
    return weatherConditions[int(round(weatherScore))]

def testFuzzyAI():
    print("\nHello! I am Rule-Based AI #2! I use fuzzy logic to predict the weather!")

    weatherPrediction = createFuzzyWeatherAI()

    # Normal Test cases
    print("Testing normal data...\n")
    testCases = [
        (-5, 90, 10, 970, "Heavy Snow"),
        (-2, 80, 35, 980, "Blustery Snow"),
        (-3, 70, 15, 990, "Light Snow"),
        (10, 80, 15, 980, "Rainy"),
        (15, 70, 25, 985, "Windy and Cloudy"),
        (20, 60, 10, 980, "Cloudy"),
        (20, 35, 5, 1020, "Clear"),
        (15, 75, 10, 1025, "Humid"),
        (18, 55, 5, 1030, "Mild"),
        (30, 20, 10, 1025, "Hot and Dry"),
        (35, 25, 20, 1030, "Hot with Breeze"),
        (28, 75, 10, 1015, "Humid and Warm"),
        (30, 50, 5, 1025, "Warm and Clear"),
    ]


    # # Noisy test cases
    # print("Testing noisy data...\n")
    # testCases = [
    #     (-4.8, 89.7, 10.3, 971, "Heavy Snow"),
    #     (-1.9, 81.2, 34.6, 982, "Blustery Snow"),
    #     (-2.7, 69.8, 14.7, 991, "Light Snow"),
    #     (10.3, 79.5, 15.1, 981, "Rainy"),
    #     (14.7, 69.9, 24.8, 986, "Windy and Cloudy"),
    #     (20.2, 59.6, 9.8, 979, "Cloudy"),
    #     (19.5, 36.2, 4.7, 1021, "Clear"),
    #     (15.1, 74.8, 9.7, 1026, "Humid"),
    #     (18.3, 54.9, 5.2, 1029, "Mild"),
    #     (29.7, 19.6, 10.4, 1024, "Hot and Dry"),
    #     (35.4, 24.7, 19.8, 1031, "Hot with Breeze"),
    #     (27.6, 74.5, 10.2, 1014, "Humid and Warm"),
    #     (30.3, 50.4, 5.3, 1026, "Warm and Clear"),
    # ]

    # # Extreme test cases
    # testCases = [
    #     (-15.0, 95, 5, 960, "Heavy Snow"),
    #     (-10.0, 90, 40, 965, "Blustery Snow"),
    #     (-5.0, 85, 35, 970, "Blustery Snow"),
    #     (0.0, 78, 15, 980, "Light Snow"),
    #     (5.0, 90, 20, 990, "Rainy"),
    #     (35.0, 25, 5, 1025, "Hot and Dry"),
    #     (40.0, 20, 15, 1030, "Hot with Breeze"),
    #     (30.0, 85, 10, 1015, "Humid and Warm"),
    #     (20.0, 70, 25, 1005, "Windy and Cloudy"),
    #     (25.0, 65, 5, 1020, "Warm and Clear"),
    # ]


    for temperature, humidity, windSpeed, pressure, expected in testCases:
        startTime = time.time()
        prediction = predictWeather(weatherPrediction, temperature, humidity, windSpeed, pressure)
        endTime = time.time()
        executionTime = endTime - startTime
        print(f"Test Case - Temp: {temperature}°C, Humidity: {humidity}%, Wind Speed: {windSpeed} km/h, Pressure: {pressure} hPa")
        print(f"Expected: {expected}")
        print(f"Prediction: {prediction}")
        print(f"Time Taken: {executionTime:.7f} seconds\n")

    print("Analysis Complete! BEEP BOOP BLOOPITY BOP")

testFuzzyAI()
