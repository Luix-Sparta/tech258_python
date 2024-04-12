# import speedtest module
import tkinter as tk
from tkinter import ttk
import speedtest
import threading


def test_internet_speed():
    # Create Speedtest object
    st = speedtest.Speedtest()

    # Perform download speed test
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    # Perform upload speed test
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps

    # Display speed test results
    result_label.config(text=f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps")
    progress_bar.stop()
    progress_bar["value"] = 0  # Set value to 0 to make it empty after the test



def run_speed_test():
    progress_bar["value"] = 0  # Set value to 0 to make it empty after the test
    progress_bar.start()
    test_thread = threading.Thread(target=test_internet_speed)
    test_thread.start()


# Create a Tkinter window
window = tk.Tk()
window.title("Internet Speed Test")

# Add labels
instruction_label = tk.Label(window, text="Click the button below to test your internet speed:")
instruction_label.pack(pady=10)

# Add progress bar
progress_bar = ttk.Progressbar(window, mode="indeterminate", length=300)

progress_bar.pack(pady=5)


# Add button to start speed test
start_button = tk.Button(window, text="Test Speed", command=run_speed_test)
start_button.pack(pady=5)

# Add label to display speed test results
result_label = tk.Label(window, text="")
result_label.pack(pady=10)



# Run the Tkinter event loop
window.mainloop()