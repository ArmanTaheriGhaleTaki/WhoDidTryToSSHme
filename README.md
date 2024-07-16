# SSH Auth Log Parser and Visualizer

## Overview
This project provides a comprehensive pipeline for parsing `auth.log` files on Linux systems to extract data on IP addresses attempting to SSH into the server. The extracted information includes the user they tried to reach, the country their IP belongs to, and their ISP. The data is then visualized to provide insights into the SSH login attempts.

## Features
- **Log Parsing:** Extracts relevant information from `auth.log` files.
- **Geolocation:** Determines the geographical location of the IP addresses.
- **ISP Lookup:** Identifies the ISP of the IP addresses.
- **Data Visualization:** Visualizes the data to show patterns and insights.

## Installation
1. **Clone the Repository:**
    ```sh
    git clone https://github.com/yourusername/ssh-auth-log-parser.git
    cd WhoDidTryToSSHme
    ```

2. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up Geolocation and ISP Services:**
    - **Geolocation:** Sign up for a free API key from a geolocation service like [ipstack](https://ipstack.com/) or [GeoIP2](https://www.maxmind.com/en/geoip2-services-and-databases).
    - **ISP Lookup:** Ensure the service you choose also provides ISP data.


## Usage
1. **Parsing Logs:**
    - Place your `auth.log` file in the `logs` directory.
    - Run the parser:
      ```sh
      python parse_logs.py
      ```

2. **Visualizing Data:**
    - After parsing, run the visualization script:
      ```sh
      python visualize_data.py
      ```

## Project Structure
```
WhoDidTryToSSHme/
│
├── logs/
│ └── auth.log # Directory for auth.log files
│
├── parse_logs.py # Script to parse auth.log files
│
├── visualize_data.py # Script to visualize the parsed data
│
├── requirements.txt # Python dependencies
│
└── README.md # Project README
```
## Data Visualization
The visualizations include:
- **User Attempt Analysis:** Shows which users were targeted the most.
- **Geographical Distribution:** Maps the origin countries of the SSH attempts.
- **ISP Distribution:** Highlights which ISPs the attacking IPs belong to.

## Contribution
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Thanks to [ipstack](https://ipstack.com/) and [GeoIP2](https://www.maxmind.com/en/geoip2-services-and-databases) for their geolocation APIs.
- Inspired by the need to secure and monitor SSH access attempts.
## Blue print
![blueprint](https://github.com/user-attachments/assets/689461ad-3312-4c9f-9111-bddb2b463ce1)
