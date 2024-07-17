import psycopg2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# PostgreSQL connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost'
}
# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)

# Fetch data from parsed_data table
parsed_data_query = "SELECT * FROM parsed_data;"
parsed_data_df = pd.read_sql(parsed_data_query, conn)

# Fetch data from ip_info table
ip_info_query = "SELECT * FROM ip_info;"
ip_info_df = pd.read_sql(ip_info_query, conn)

# Close the connection
conn.close()

# Display the first few rows of the dataframes
print(parsed_data_df.head())
print(ip_info_df.head())

# Merge the dataframes on ip_address to get the country information in the parsed_data dataframe
merged_df = pd.merge(parsed_data_df, ip_info_df, on='ip_address')

# Failed login attempts by country
plt.figure(figsize=(12, 6))
country_counts = merged_df['country'].value_counts()
sns.barplot(x=country_counts.index, y=country_counts.values)
plt.title('Failed Login Attempts by Country')
plt.xlabel('Country')
plt.ylabel('Number of Attempts')
plt.xticks(rotation=45)
# Save the plot as an image file
plt.savefig('failed_login_attempts_by_country.png')

# Failed login attempts by time (hourly)
merged_df['time'] = pd.to_datetime(merged_df['time'], format='%H:%M:%S').dt.time
merged_df['hour'] = merged_df['time'].apply(lambda x: x.hour)

plt.figure(figsize=(12, 6))
hour_counts = merged_df['hour'].value_counts().sort_index()
sns.lineplot(x=hour_counts.index, y=hour_counts.values, marker='o')
plt.title('Failed Login Attempts by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Attempts')
plt.xticks(range(0, 24))
# Save the plot as an image file
plt.savefig('failed_login_attempts_by_hour.png')

# Print message indicating where the plots are saved
print("Plots saved as 'failed_login_attempts_by_country.png' and 'failed_login_attempts_by_hour.png'")