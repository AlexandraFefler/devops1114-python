# import csv
# import datetime
# import time
# import speedtest #run command "pip -m install speedtest-cli" in cmd first to acquire that library, in order to import that class

# # File name for storing results
# csv_file = "internet_speed.csv"

# # Function to test internet speed and return results
# def measure_speed():
#     try:
#         st = speedtest.Speedtest()
#         st.get_best_server()
#         download_speed = st.download() / 1_000_000  # Convert to Mbps
#         upload_speed = st.upload() / 1_000_000  # Convert to Mbps
#         return round(download_speed, 2), round(upload_speed, 2)
#     except Exception as e:
#         print(f"Error measuring internet speed: {e}")
#         return None, None

# # Function to log results into the CSV file
# def log_speed_to_csv(timestamp, download_speed, upload_speed):
#     file_exists = False
#     try:
#         # Check if the CSV file already exists
#         file_exists = open(csv_file).read() != ""
#     except FileNotFoundError:
#         pass

#     # Open the CSV file in append mode
#     with open(csv_file, mode='a', newline='') as file:
#         writer = csv.writer(file)

#         # Write the header if the file didn't exist
#         if not file_exists:
#             writer.writerow(["Timestamp", "Download Speed (Mbps)", "Upload Speed (Mbps)"])

#         # Write the new data row
#         writer.writerow([timestamp, download_speed, upload_speed])

# # Main loop to log internet speeds every 5 minutes
# try:
#     print("Starting to log internet speed data every 5 minutes. Press Ctrl+C to stop.")
#     while True:
#         # Measure internet speed
#         download_speed, upload_speed = measure_speed()
#         if download_speed is not None and upload_speed is not None:
#             # Log results if speeds were successfully measured
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             log_speed_to_csv(timestamp, download_speed, upload_speed)
#             print(f"Logged: {timestamp} | Download: {download_speed} Mbps | Upload: {upload_speed} Mbps")
#         else:
#             print("Skipping logging due to speed test error.")

#         # Wait for 5 minutes before the next measurement
#         time.sleep(300)  # 300 seconds = 5 minutes
# except KeyboardInterrupt:
#     print("\nStopped logging internet speed data.")

import datetime,speedtest, os
from time import sleep

# Function to test internet speed and return results
def measure_speed():
    try:
        st = speedtest.Speedtest()
        # st.get_servers()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # download() returns number in bytes, so convert to Mbps
        upload_speed = st.upload() / 1_000_000  # same
        return round(download_speed, 2), round(upload_speed, 2)
    except Exception as e:
        print(f"Error measuring internet speed: {e}")
        return None, None

if not("internet_speed.csv" in os.listdir(os.getcwd())): #if the file doesn't exist in current working directory
    with open("internet_speed.csv", "w") as file: # was "a" instead of "w" in fileOps 
        file.write("Timestamp,Download speed (Mbps),Upload speed (Mbps)\n") #TODO: didn't do that, need to fix

while True: # every 5 minutes for eternity
    down_speed, up_speed = measure_speed() # unpacking a returned tuple
    # down_speed = 6 #tests
    # up_speed = 7 #tests
    if down_speed is not None and up_speed is not None:
        print("Adding entry")
        with open("internet_speed.csv", "a") as file:
            file.write((datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")+","+str(down_speed)+","+str(up_speed)+"\n")
    else:
        print("Error: Measuring speed failed, didn't log this time")
    sleep(10)

#pseudo code:
# import needed speedtest cli
# create a .csv file and write (append) download and upload speeds (some funcs in speedtest cli)   -> import this speedtest-cli, also csv?
# entry syntax: timestamp (date & time), download speed (Mbps), upload speed (Mbps)  -> import datetime for timestamp, time for sleep
# cases to handle: the .csv file doesn't exist - create it with headers - timestamp, downspeed, upspeed; then add new lines according to that -> import os