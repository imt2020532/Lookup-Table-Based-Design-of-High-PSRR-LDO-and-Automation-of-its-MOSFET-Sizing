import csv
import math

def linear_interpolation(x, x_data, y_data):
    # Find the two data points surrounding the x value
    #print("I am testing...")
    for i in range(len(x_data) - 1):
        if x >= x_data[i]:
            #print("I am testing if condition")
            x0, x1 = x_data[i], x_data[i + 1]
            y0, y1 = y_data[i], y_data[i + 1]
            # Perform linear interpolation
            y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
            return y
    # If x is outside the range of x_data, return None
    return None

def linear_interpolation_from_lower_side(x, x_data, y_data):
    # Find the two data points surrounding the x value
    #print("I am testing...")
    for i in range(len(x_data) - 1):
        if x > x_data[i]:
            #print("I am testing if condition")
            x0, x1 = x_data[i], x_data[i + 1]
            y0, y1 = y_data[i], y_data[i + 1]
            # Perform linear interpolation
            y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
            return y_data[i-1]
        
        elif x == x_data[i]:
            return y_data[i]
    # If x is outside the range of x_data, return None
    return None

def distance_to_curve(x, y, x_curve, y_curve):
    min_distance = float('inf')
    for i in range(len(x_curve)):
        distance = math.sqrt((x_curve[i] - x)**2 + (y_curve[i] - y)**2)
        if distance < min_distance:
            min_distance = distance
    return min_distance

def distance_to_curve_modified(x, y, x_curve, y_curve, num_points=10):
    min_distance = float('inf')
    for i in range(len(x_curve) - 1):
        # Interpolate additional points between consecutive curve points
        interpolated_x = [x_curve[i] + (x_curve[i+1] - x_curve[i]) * j / num_points for j in range(num_points)]
        interpolated_y = [y_curve[i] + (y_curve[i+1] - y_curve[i]) * j / num_points for j in range(num_points)]
        
        # Include the last point of the segment
        interpolated_x.append(x_curve[i+1])
        interpolated_y.append(y_curve[i+1])
        
        # Calculate distances to the interpolated points
        for j in range(len(interpolated_x)):
            distance = math.sqrt((interpolated_x[j] - x)**2 + (interpolated_y[j] - y)**2)
            if distance < min_distance:
                min_distance = distance
    return min_distance

def main():
    
    print("\nFirstly we will get the Width of M1.")
    # Hardcoded path to the CSV file for Width of M1 for L=180nm
    filename = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsIdbyWL\\M1L180nm.csv"

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data, y_data = [], []
        for row in reader:
            x_data.append(float(row[0]))  # Assuming x values are in the first column
            y_data.append(float(row[1]))  # Assuming y values are in the second column
            
    # Prompt the user for an x value
    x_input = float(input("Enter the gm by Id value for getting Id by W value : "))

    # Perform linear interpolation
    y_output = linear_interpolation(x_input, x_data, y_data)
    if y_output is not None:
        print(f"The corresponding Id by W value for gm by Id ={x_input} is {y_output}")
    else:
        print("The provided x value is outside the range of the data.")

    print(f"The corresponding Width value for M1 is : {0.1/y_output}")
    
    print("\nNow we will get the Widths of M2 and M3.")
    
    # Hardcoded path to the CSV file for 180nm
    filename180 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsgmroL\\test180.csv"

    with open(filename180, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data180, y_data180 = [], []
        for row in reader:
            x_data180.append(float(row[0]))  # Assuming x values are in the first column
            y_data180.append(float(row[1]))  # Assuming y values are in the second column
            
    # Hardcoded path to the CSV file for 360nm
    filename360 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsgmroL\\test360.csv"

    with open(filename360, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data360, y_data360 = [], []
        for row in reader:
            x_data360.append(float(row[0]))  # Assuming x values are in the first column
            y_data360.append(float(row[1]))  # Assuming y values are in the second column
            
    # Hardcoded path to the CSV file for 540nm
    filename540 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsgmroL\\test540.csv"

    with open(filename540, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data540, y_data540 = [], []
        for row in reader:
            x_data540.append(float(row[0]))  # Assuming x values are in the first column
            y_data540.append(float(row[1]))  # Assuming y values are in the second column
            
    # Hardcoded path to the CSV file for 720nm
    filename720 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsgmroL\\test720.csv"

    with open(filename720, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data720, y_data720 = [], []
        for row in reader:
            x_data720.append(float(row[0]))  # Assuming x values are in the first column
            y_data720.append(float(row[1]))  # Assuming y values are in the second column
            
    # print(x_data[0])
    # print(x_data[len(x_data) - 1])
    # print(y_data[0])
    # print(y_data[len(y_data) - 1])
    # print(len(x_data))

    # Prompt the user for an x value
    # x_input = float(input("Enter the x value: "))

    # # Perform linear interpolation
    # y_output = linear_interpolation(x_input, x_data180, y_data180)
    # if y_output is not None:
    #     print(f"The corresponding y value for x={x_input} is {y_output}")
    # else:
    #     print("The provided x value is outside the range of the data.")
        
    x_coordinate = float(input("Enter the x coordinate: "))
    y_coordinate = float(input("Enter the y coordinate: "))
    
    distance180 = distance_to_curve(x_coordinate, y_coordinate, x_data180, y_data180)
    distance360 = distance_to_curve(x_coordinate, y_coordinate, x_data360, y_data360)
    distance540 = distance_to_curve(x_coordinate, y_coordinate, x_data540, y_data540)
    distance720 = distance_to_curve(x_coordinate, y_coordinate, x_data720, y_data720)
    
    print(f"The corresponding distance for the 180nm case is {distance180}")
    print(f"The corresponding distance for the 360nm case is {distance360}")
    print(f"The corresponding distance for the 540nm case is {distance540}")
    print(f"The corresponding distance for the 720nm case is {distance720}")
    
    # Hardcoded path to the CSV file for 180nm
    filenameM2M3 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsIdbyWL\\M2M3IdbyWgmbyId.csv"

    with open(filenameM2M3, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_dataM2M3, y_dataM2M3 = [], []
        for row in reader:
            x_dataM2M3.append(float(row[0]))  # Assuming x values are in the first column
            y_dataM2M3.append(float(row[1]))  # Assuming y values are in the second column
            
    # Prompt the user for an x value
    x_input = float(input("Enter the x value for IdbyW value : "))

    # Perform linear interpolation
    y_output = linear_interpolation(x_input, x_dataM2M3, y_dataM2M3)
    if y_output is not None:
        print(f"The corresponding y value for x={x_input} is {y_output}")
    else:
        print("The provided x value is outside the range of the data.")

    print(f"The corresponding Width value for M2M2 NMOS are : {250/y_output} um.")
    
    # Hardcoded path to the CSV file for 180nm for M4M5
    filename180 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\M4M5plots\\test180.csv"

    with open(filename180, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data180, y_data180 = [], []
        for row in reader:
            x_data180.append(float(row[0]))  # Assuming x values are in the first column
            y_data180.append(float(row[1]))  # Assuming y values are in the second column
            
    # Hardcoded path to the CSV file for 360nm for M4M5
    filename360 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\M4M5plots\\test360.csv"

    with open(filename360, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data360, y_data360 = [], []
        for row in reader:
            x_data360.append(float(row[0]))  # Assuming x values are in the first column
            y_data360.append(float(row[1]))  # Assuming y values are in the second column
    
    # Hardcoded path to the CSV file for 540nm for M4M5
    filename540 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\M4M5plots\\test540.csv"

    with open(filename540, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data540, y_data540 = [], []
        for row in reader:
            x_data540.append(float(row[0]))  # Assuming x values are in the first column
            y_data540.append(float(row[1]))  # Assuming y values are in the second column
            
    print("\nNow we will get the length of the M4M5 transistors.\n")
            
    x_coordinate = float(input("Enter the x coordinate: "))
    y_coordinate = float(input("Enter the y coordinate: "))
    
    distance180 = distance_to_curve(x_coordinate, y_coordinate, x_data180, y_data180)
    distance360 = distance_to_curve(x_coordinate, y_coordinate, x_data360, y_data360)
    distance540 = distance_to_curve(x_coordinate, y_coordinate, x_data540, y_data540)
    
    print(f"The corresponding distance for the 180nm case is {distance180}")
    print(f"The corresponding distance for the 360nm case is {distance360}")
    print(f"The corresponding distance for the 540nm case is {distance540}")
    
    print("\nNow we will get the widths of M4 and M5.")
    
    # Hardcoded path to the CSV file for 540nm for M4M5 Widths.
    filenameM4M5 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\M4M5plots\\gmbyIdvsIdbyW360.csv"

    with open(filenameM4M5, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_dataM4M5, y_dataM4M5 = [], []
        for row in reader:
            x_dataM4M5.append(float(row[0]))  # Assuming x values are in the first column
            y_dataM4M5.append(float(row[1]))  # Assuming y values are in the second column
            
    # Prompt the user for an x value
    x_input = float(input("Enter the x value for IdbyW value : "))

    # Perform linear interpolation
    y_output = linear_interpolation(x_input, x_dataM4M5, y_dataM4M5)
    if y_output is not None:
        print(f"The corresponding y value for x={x_input} is {y_output}")
    else:
        print("The provided x value is outside the range of the data.")

    print(f"The corresponding Width value for M2M2 NMOS are : {250/y_output} um.")
    
    print("\nWe will get the Width of Bias Ms.")
    # Hardcoded path to the CSV file for Width of M1 for L=180nm
    filename = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsIdbyWMBias\\MBiasL180nm.csv"

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data, y_data = [], []
        for row in reader:
            x_data.append(float(row[0]))  # Assuming x values are in the first column
            y_data.append(float(row[1]))  # Assuming y values are in the second column
            
    # Prompt the user for an x value
    x_input = float(input("Enter the gm by Id value for getting Id by W value : "))

    # Perform linear interpolation
    y_output = linear_interpolation(x_input, x_data, y_data)
    if y_output is not None:
        print(f"The corresponding Id by W value for gm by Id ={x_input} is {y_output}")
    else:
        print("The provided x value is outside the range of the data.")

    print(f"The corresponding Width value for M bias is : {500/y_output} um.")
    
if __name__ == "__main__":
    main()
