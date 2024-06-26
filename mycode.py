import csv
import math

#function for linear interpolation, getting the cooresponding y coordinate for the given x coordinate
#the function will be used for different gmbyId vs IdbyW plots, gmbyId vs gmro plots, gmbyId vs ft plots, etc...
def linear_interpolation(x, x_data, y_data): 
    for i in range(len(x_data) - 1):
        if x >= x_data[i]:
            x0, x1 = x_data[i], x_data[i + 1]
            y0, y1 = y_data[i], y_data[i + 1]
            # Perform linear interpolation
            y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
            return y
    # If x is outside the range of x_data, return None
    return None

#this function will help us to calculate the distance between given input curve and the input point
#this is very basic distance between 2 points formula based function
def distance_to_curve(x, y, x_curve, y_curve):
    min_distance = float('inf')
    for i in range(len(x_curve)):
        distance = math.sqrt((x_curve[i] - x)**2 + (y_curve[i] - y)**2)
        if distance < min_distance:
            min_distance = distance
    #returns the distance between a point and a curve
    return min_distance

def main():
    
    # prompt the user for 9 input values
    # please look at the units specified carefully!
    # These are the input specifications
    Vin = float(input("Enter Vin in volts: "))
    Vout = float(input("Enter Vout in volts: "))
    Iloadmax = float(input("Enter Iloadmax in mili amperes: "))
    Iloadmin = float(input("Enter Iloadmin in mili amperes: "))
    Cload = float(input("Enter Cload in micro Farads: "))
    Iq = float(input("Enter Iq (equal to Ibias in micro amperes): "))
    loopgain = float(input("Enter loopgain: "))
    gmbyId = float(input("Enter gmbyId: "))
    minLength = float(input("Enter minLength in nano meters: "))
    
    print("\nLet's do some calculations.")
    
    # getting gm of M1 using the simple formula, M1 is the passFET
    gmofM1 = gmbyId*(Iloadmax*0.001)
    print(f"\nThe value of gmofM1 is : {gmofM1}")
    
    # In this method, the assumption is that the minimum length is 180nm of any transistor
    # Hardcoded path to the CSV file for Width of M1 for L=180nm, plot of gmbyID vs gmro
    filename = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsgmroL\\test180.csv"

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data, y_data = [], []
        for row in reader:
            x_data.append(float(row[0]))  # Assuming x values are in the first column
            y_data.append(float(row[1]))  # Assuming y values are in the second column
            
    # This is one of the given input specification term        
    x_input = gmbyId

    # Perform linear interpolation to get the corresponding gain AM1
    y_output = linear_interpolation(x_input, x_data, y_data)
    
    # gmroM1 or the AM1
    AM1 = y_output
    print(f"\nThe value of AM1 is : {AM1}")
    
    # getting the roM1 using gain and gmM1
    roM1 = y_output/gmofM1
    print(f"\nThe value of roM1 is : {roM1}")
    
    # finding the first pole frequency, here, Cload is also a part of the input specification
    Wp1 = 1000000/(roM1*Cload)
    print(f"\nThe value of Wp1 is : {Wp1}")
    
    fp1 = 1000000/(2*3.14*roM1*Cload)
    print(f"\nThe value of fp1 is : {fp1}")
    
    print("\nFirstly we will get the Width of M1.")
    # Hardcoded path to the CSV file for Width of M1 for L=180nm, plot of gmbyId vs IdbyW
    filename = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsIdbyWL\\M1L180nm.csv"

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data, y_data = [], []
        for row in reader:
            x_data.append(float(row[0]))  # Assuming x values are in the first column
            y_data.append(float(row[1]))  # Assuming y values are in the second column
    
    # This is one of the given input specification term  
    x_input = gmbyId

    # Perform linear interpolation
    y_output = linear_interpolation(x_input, x_data, y_data)
    
    # if y_output is not None:
    #     print(f"The corresponding Id by W value for gm by Id ={x_input} is {y_output}")
    # else:
    #     print("The provided x value is outside the range of the data.")

    # using a factor of 0.001 to get in SI units, the I_load_max value is input specification
    # Here, we use the mathematical expression Iload / (Id/W) to get the W. y_output is IdbyW 
    print(f"The corresponding Width value for M1 is : {(Iloadmax*0.001)/y_output} meters.")
    
    # Hardcoded path to the CSV file for Width of M1 for L=180nm, plot of ft vs gmbyId
    filenameforft = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\frequencyTvsgmId\\ftvsgmId.csv"

    with open(filenameforft, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data, y_data = [], []
        for row in reader:
            x_data.append(float(row[0]))  # Assuming x values are in the first column
            y_data.append(float(row[1]))  # Assuming y values are in the second column
            
    # This is one of the given input specification term 
    x_input = gmbyId

    # Perform linear interpolation
    y_output = linear_interpolation(x_input, x_data, y_data)
    
    # getting the transition frequency using the ft vs gmbyId plot of M1 for 180nm length
    ft = y_output
    print(f"\nThe value of ft is : {ft}")
    
    # getting the value of Cgg using the formula below, pi value is approximated to 3.14
    Cgg = gmofM1/(2*3.14*ft)
    print(f"\nThe value of Cgg is {Cgg}")
    
    # Here, the 0.000001 factor is being used for getting outputs in SI units
    rodiffAmp = (0.000001*Cload*roM1)/(loopgain*Cgg)
    
    # all the formulae and there justification will be available in the methodology based pdf attached along with the code, which gives
    # the step by step process in detail
    
    roM3 = 2*rodiffAmp
    
    gmofM3 = (2*loopgain)/(AM1*roM3)
    
    # Here, the 0.000001 factor is being used for getting outputs in SI units
    gmbyIdforM3 = (2*gmofM3)/(Iq*0.000001) 
    
    gmdiffro3 = (2*loopgain)/AM1
        
    print(f"\nThe value of gmbyIdforM3 is : {gmbyIdforM3}")
    print(f"\nThe value of gmdiffrodiff is : {gmdiffro3}")
    
    print("\nNow we will get the Widths of M2 and M3.")
    
    # Now we will save the plots of gmbyId vs gmro for different lengths 180nm, 360nm, 540nm, and so on.
    # We have the point (gmbyIdforM3, gmdiffro3). We will try to find the curve on which this point lies among all the length-based-curves.
    # using the distance_to_curve function, the curve which is the closest to the point tells us the length of M3, and hence, M2 also. 
    
    # Hardcoded path to the CSV file for 180nm, plot of gmbyId vs gmro
    filename180 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsgmroL\\test180.csv"

    with open(filename180, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data180, y_data180 = [], []
        for row in reader:
            x_data180.append(float(row[0]))  # Assuming x values are in the first column
            y_data180.append(float(row[1]))  # Assuming y values are in the second column
            
    # Hardcoded path to the CSV file for 360nm, plot of gmbyId vs gmro
    filename360 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsgmroL\\test360.csv"

    with open(filename360, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data360, y_data360 = [], []
        for row in reader:
            x_data360.append(float(row[0]))  # Assuming x values are in the first column
            y_data360.append(float(row[1]))  # Assuming y values are in the second column
            
    # Hardcoded path to the CSV file for 540nm, plot of gmbyId vs gmro
    filename540 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsgmroL\\test540.csv"

    with open(filename540, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data540, y_data540 = [], []
        for row in reader:
            x_data540.append(float(row[0]))  # Assuming x values are in the first column
            y_data540.append(float(row[1]))  # Assuming y values are in the second column
            
    # Hardcoded path to the CSV file for 720nm, plot of gmbyId vs gmro
    filename720 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsgmroL\\test720.csv"

    with open(filename720, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data720, y_data720 = [], []
        for row in reader:
            x_data720.append(float(row[0]))  # Assuming x values are in the first column
            y_data720.append(float(row[1]))  # Assuming y values are in the second column
                    
    # x_coordinate = float(input("Enter the x coordinate: "))
    # y_coordinate = float(input("Enter the y coordinate: "))
    
    x_coordinate = gmbyIdforM3
    y_coordinate = gmdiffro3
    
    
    # here, we are checking the distance between the input point and curves representing different lengths
    distance180 = distance_to_curve(x_coordinate, y_coordinate, x_data180, y_data180)
    distance360 = distance_to_curve(x_coordinate, y_coordinate, x_data360, y_data360)
    distance540 = distance_to_curve(x_coordinate, y_coordinate, x_data540, y_data540)
    distance720 = distance_to_curve(x_coordinate, y_coordinate, x_data720, y_data720)
    
    print(f"The corresponding distance for the 180nm case is {distance180}")
    print(f"The corresponding distance for the 360nm case is {distance360}")
    print(f"The corresponding distance for the 540nm case is {distance540}")
    print(f"The corresponding distance for the 720nm case is {distance720}")
    
    # Right now, it is hardcoded but it will be changed in future into if else conditions
    # Hardcoded path to the CSV file for the curve matching the optimal length of transistor M2 and M3, plot of gmbyId vs IdbyW
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
    # x_input = float(input("Enter the x value for IdbyW value : "))
    x_input = gmbyIdforM3

    # Perform linear interpolation
    y_output = linear_interpolation(x_input, x_dataM2M3, y_dataM2M3)
    if y_output is not None:
        print(f"The corresponding y value for x={x_input} is {y_output}")
    else:
        print("The provided x value is outside the range of the data.")
        
    # Again, look into the methodology pdf for the justification of the formula used below
    # Note the units mentioned at every point
    print(f"The corresponding Width value for M2M2 NMOS are : {Iq/(2*y_output)} um.")
    
    # Repeat the steps done for M2 and M3 to get the 'L' and 'W' of M4 and M5 now.
    
    # Hardcoded path to the CSV file for 180nm for M4M5, plot of gmbyId vs gmro
    filename180 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\M4M5plots\\test180.csv"

    with open(filename180, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data180, y_data180 = [], []
        for row in reader:
            x_data180.append(float(row[0]))  # Assuming x values are in the first column
            y_data180.append(float(row[1]))  # Assuming y values are in the second column
            
    # Hardcoded path to the CSV file for 360nm for M4M5, plot of gmbyId vs gmro
    filename360 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\M4M5plots\\test360.csv"

    with open(filename360, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data360, y_data360 = [], []
        for row in reader:
            x_data360.append(float(row[0]))  # Assuming x values are in the first column
            y_data360.append(float(row[1]))  # Assuming y values are in the second column
    
    # Hardcoded path to the CSV file for 540nm for M4M5, plot of gmbyId vs gmro
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
    
    print(f"\ngmbyId is considered to be {gmbyId}")
    
    # the factor 0.000001 is to maintain the units
    gmofM5 = gmbyId*((Iq*0.000001)/2)
    roM5 = roM3
    
    gmroM5 = gmofM5*roM5
    
    print(f"The value of gmroM5 is {gmroM5}")
            
    # x_coordinate = float(input("Enter the x coordinate: "))
    # y_coordinate = float(input("Enter the y coordinate: "))
    
    x_coordinate = gmbyId
    y_coordinate = gmroM5
    
    # here, we are doing the same thing we did to find out length of M2 and M3. Mentioned in comments above in detail for M2 and M3, 
    # same goes for M4 and M5.
    
    distance180 = distance_to_curve(x_coordinate, y_coordinate, x_data180, y_data180)
    distance360 = distance_to_curve(x_coordinate, y_coordinate, x_data360, y_data360)
    distance540 = distance_to_curve(x_coordinate, y_coordinate, x_data540, y_data540)
    
    print(f"The corresponding distance for the 180nm case is {distance180}")
    print(f"The corresponding distance for the 360nm case is {distance360}")
    print(f"The corresponding distance for the 540nm case is {distance540}")
    
    print("\nNow we will get the widths of M4 and M5.")
    
    # Right now, it is hardcoded but it will be changed in future into if else conditions
    # Hardcoded path to the CSV file for 540nm for M4M5 Widths, plot of gmbyId vs IdbyW
    filenameM4M5 = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\M4M5plots\\gmbyIdvsIdbyW360.csv"

    with open(filenameM4M5, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_dataM4M5, y_dataM4M5 = [], []
        for row in reader:
            x_dataM4M5.append(float(row[0]))  # Assuming x values are in the first column
            y_dataM4M5.append(float(row[1]))  # Assuming y values are in the second column
            
    # gmbyId is an input specification
    x_input = gmbyId

    # Perform linear interpolation
    y_output = linear_interpolation(x_input, x_dataM4M5, y_dataM4M5)
    if y_output is not None:
        print(f"The corresponding y value for x={x_input} is {y_output}")
    else:
        print("The provided x value is outside the range of the data.")
        
    # Note the units mentioned here and in every print statement. If unit is not shown, assume the SI unit.
    print(f"The corresponding Width value for M2M2 NMOS are : {Iq/(2*y_output)} um.")
    
    # Now, we will find the 'W' for M6 and M7, for which we have assumed 'L' to be 180nm
    
    print("\nWe will get the Width of Bias Ms.")
    # Hardcoded path to the CSV file for Width of M1 for L=180nm, plot of gmbyId vs IdbyW
    filename = "C:\\4th_Year\\8th_semester\\courses\\APIC\\Course-Project\\scripts\\gmbyIdvsIdbyWMBias\\MBiasL180nm.csv"

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # Skip header row if present
        next(reader, None)
        x_data, y_data = [], []
        for row in reader:
            x_data.append(float(row[0]))  # Assuming x values are in the first column
            y_data.append(float(row[1]))  # Assuming y values are in the second column
            
    # gmbyId is an input specification
    x_input = gmbyId
    # Perform linear interpolation
    y_output = linear_interpolation(x_input, x_data, y_data)
    
    if y_output is not None:
        print(f"The corresponding Id by W value for gm by Id ={x_input} is {y_output}")
    else:
        print("The provided x value is outside the range of the data.")
        
    print(f"The corresponding Width value for M bias is : {Iq/y_output} um.")
    
if __name__ == "__main__":
    main()
