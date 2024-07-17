import psycopg2  # This imports the binary version since it's installed as psycopg2-binary
import requests
import logging

# Function to get IP information (ISP and country)
def get_ip_info(ip,cursor):
    cursor.execute("SELECT ip_address FROM ip_info WHERE ip_address = %s;", (ip,))
    result = cursor.fetchone()
    if result:
        return
        
    else:
        try:
            response = requests.get(f'http://ip-api.com/json/{ip}')
            data = response.json()
            ip_info = {
                'ip_address': ip,
                'isp': data.get('isp', 'Unknown'),
                'country': data.get('country', 'Unknown')
            }
            cursor.execute("""
                INSERT INTO ip_info (ip_address, isp, country)
                VALUES (%s, %s, %s)
                ON CONFLICT (ip_address) DO NOTHING;
            """, (ip_info['ip_address'], ip_info['isp'], ip_info['country']))
            print(ip_info)
            conn.commit()
            print("data inserted")
            return 
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data for IP {ip}: {e}")
            return 


# PostgreSQL connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost'
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()


# Fetch distinct IP addresses
cur.execute("SELECT DISTINCT ip_address FROM parsed_data ORDER BY ip_address;")
ip_addresses = cur.fetchall()

# Insert IP information into ip_info table
for ip_tuple in ip_addresses:
    ip = ip_tuple[0]
    ip_info = get_ip_info(ip, cur)

# Close the connection
cur.close()
conn.close()