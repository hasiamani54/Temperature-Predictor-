import glob
import pandas as pd
# Ask the user for an approximate airbubble size
airbubble_size = int(input("Enter approximate airbubble size (mL): "))

data_files = glob.glob('*{}*'.format(airbubble_size))
if not data_files:
    print("Error: Data files for airbubble size {} not found.".format(airbubble_size))
    exit()
data_file = data_files[0]
data = pd.read_excel(data_file)

# Extract temperature and time columns
temperatures = data['temperature']
times = data['time']
coefficients = np.polyfit(times, temperatures, deg=3
def approximate_temperature(time):
    return np.polyval(coefficients, time)
#Test Case
print(approximate_temperature(10))


#Previous code that I did not work 
#import glob
#airbubble_size= int(input("Enter the airbubble size in mL. If it is a large airbubble that is of unknown size then enter"))
#if airbubble_size=0:
#data_files=glob.glob('*{}*'.format(0))
#else if airbubble_size<=90:
#data_files = glob.glob('*{}*'.format(90))
#else if airbubble_size>90:
#data_files = glob.glob('*{}*'.format(200))
#data_files=glob.glob('*{}*'.format(airbubble_size))
#if not data_files:
#print("Error")
#data_file= data_files[airbubble_size]
#data= pd.read_excel(data_file)
#Product_Temp_4= data['Product Temp 4 Scaled; AVE']
#Time= data['Relative Time']
#Values= np.polyfit(Time, Product_Temp_4, deg=3) #not too sure what deg to fit the function to
#def approximate_temp(time):
#return np.polyval(values, time)