# Create a Python script that tests your internet speed (upload and download).

# import speedtest module
import speedtest

def test_internet_speed():

    speed_test = speedtest.Speedtest()

    print("Testing download speed...")
    # Mbps
    download_speed = speed_test.download() / 1_000_000
    print(f"Your Download speed is {download_speed:.2f}Mbps")

    print("Testing upload speed...")
    # Mbps
    upload_speed = speed_test.upload() / 1_000_000
    print(f"Your Upload speed is {upload_speed:.2f}Mbps")

if __name__ == "__main__":
    test_internet_speed()