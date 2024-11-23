import time

def decisionTree(temperature, humidity, windSpeed, pressure):
    if temperature < 0:
        if humidity > 85:
            return "Heavy Snow"
        elif windSpeed > 30:
            return "Blustery Snow"
        else:
            return "Light Snow"
    elif 0 <= temperature <= 25:
        if pressure < 990:
            if humidity > 75:
                return "Rainy"
            elif windSpeed > 20:
                return "Windy and Cloudy"
            else:
                return "Cloudy"
        else:
            if humidity < 40:
                return "Clear"
            elif humidity > 70:
                return "Humid"
            else:
                return "Mild"
    else:
        if humidity < 30:
            if windSpeed < 15:
                return "Hot and Dry"
            else:
                return "Hot with Breeze"
        elif humidity > 60:
            return "Humid and Warm"
        else:
            return "Warm and Clear"

def testDTreeAI():
    print("\nHello! I am Rule-Based AI #2! I use a decision tree to predict the weather!\n")

    # # Normal Test cases
    # print("Testing normal data...\n")
    # testCases = [
    #     (-5, 90, 10, 970, "Heavy Snow"),
    #     (-2, 80, 35, 980, "Blustery Snow"),
    #     (-3, 70, 15, 990, "Light Snow"),
    #     (10, 80, 15, 980, "Rainy"),
    #     (15, 70, 25, 985, "Windy and Cloudy"),
    #     (20, 60, 10, 980, "Cloudy"),
    #     (20, 35, 5, 1020, "Clear"),
    #     (15, 75, 10, 1025, "Humid"),
    #     (18, 55, 5, 1030, "Mild"),
    #     (30, 20, 10, 1025, "Hot and Dry"),
    #     (35, 25, 20, 1030, "Hot with Breeze"),
    #     (28, 75, 10, 1015, "Humid and Warm"),
    #     (30, 50, 5, 1025, "Warm and Clear"),
    # ]

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

    # Extreme test cases
    testCases = [
        (-15.0, 95, 5, 960, "Heavy Snow"),
        (-10.0, 90, 40, 965, "Blustery Snow"),
        (-5.0, 85, 35, 970, "Blustery Snow"),
        (0.0, 78, 15, 980, "Light Snow"),
        (5.0, 90, 20, 990, "Rainy"),
        (35.0, 25, 5, 1025, "Hot and Dry"),
        (40.0, 20, 15, 1030, "Hot with Breeze"),
        (30.0, 85, 10, 1015, "Humid and Warm"),
        (20.0, 70, 25, 1005, "Windy and Cloudy"),
        (25.0, 65, 5, 1020, "Warm and Clear"),
    ]


        
    for temperature, humidity, windSpeed, pressure, expected in testCases:
        startTime = time.time()
        prediction = decisionTree(temperature, humidity, windSpeed, pressure)
        endTime = time.time()
        executionTime = endTime - startTime
        print(f"Test Case - Temp: {temperature}°C, Humidity: {humidity}%, Wind Speed: {windSpeed} km/h, Pressure: {pressure} hPa")
        print(f"Expected: {expected}")
        print(f"Prediction: {prediction}")
        print(f"Time Taken: {executionTime:.7f} seconds\n")

    print("Analysis complete!")

testDTreeAI()