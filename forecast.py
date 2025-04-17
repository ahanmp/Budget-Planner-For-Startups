import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset from a CSV string (you can replace this part with reading from a file if you have one)
from io import StringIO

data = """
data,ds,marketing,salaries,operations
1990-01-01,2099,7521,3234
1990-02-01,1977,7830,2873
1990-03-01,2139,8021,3029
1990-04-01,2319,8044,2891
1990-05-01,1973,7905,2901
1990-06-01,1978,8236,2935
1990-07-01,2345,7739,3070
1990-08-01,2188,8027,2897
1990-09-01,1946,8116,3333
1990-10-01,2153,8244,2798
1990-11-01,1957,8313,2978
1990-12-01,1961,7772,2917
1991-01-01,2108,7660,3391
1991-02-01,1682,8513,3081
1991-03-01,1725,8240,3293
1991-04-01,1962,7925,2666
1991-05-01,1877,8625,3106
1991-06-01,2148,8205,3265
1991-07-01,1908,8534,3065
1991-08-01,1812,8210,3313
1991-09-01,2393,8818,2920
1991-10-01,2060,8737,3404
1991-11-01,2123,8145,3629
1991-12-01,1830,8522,2966
1992-01-01,2011,8434,2948
1992-02-01,2147,8661,3426
1992-03-01,1900,7971,3460
1992-04-01,2210,8476,2936
1992-05-01,2020,8598,2965
1992-06-01,2087,7763,3002
1992-07-01,2030,7945,2739
1992-08-01,2525,7699,2848
1992-09-01,2157,8239,2829
1992-10-01,1953,8546,2890
1992-11-01,2334,8791,3076
1992-12-01,1931,8373,3146
"""  # Add more data as needed

# Load data into pandas DataFrame
df = pd.read_csv(StringIO(data), parse_dates=['data'])

# Plotting the data
plt.figure(figsize=(10, 6))

# Plot each department data over time
plt.plot(df['data'], df['ds'], label='Data Science (DS)', marker='o')
plt.plot(df['data'], df['marketing'], label='Marketing', marker='o')
plt.plot(df['data'], df['salaries'], label='Salaries', marker='o')
plt.plot(df['data'], df['operations'], label='Operations', marker='o')

# Customizing the plot
plt.title('Departmental Salaries and Expenses Over Time')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.legend(loc='upper left')
plt.grid(True)

# Show the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
