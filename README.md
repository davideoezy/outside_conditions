outside_conditions

Python 3 script to read observations of local station. Values inserted into a InfluxDB database
running on another network node

Instructions - weather polling
1. sudo apt-get install python-pip
# replace with influxdb # 2. Install myslq-connector - sudo apt-get -y install python3-mysql.connector
#3. Create SQL table 'outside_conditions' in host db, with columns:
air_temp float,
apparent_t float,
cloud varchar(40),
cloud_oktas int,
dewpt float,
gust_kmh int,
press float,
rain_trace float,
rel_hum int,
vis_km int,
wind_dir varchar(10),
wind_spd_kmh int,
reader_ts datetime,
ts timestamp
4. cp outside_conditions.service /etc/systemd/system/
5. enable outside_conditions.service

All things working, a record will be inserted every 10 minutes
