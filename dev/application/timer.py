import time
import threading

class CountUpTimer(object):
    def __init__(self):
        self.__stop_signal = threading.Event()
        self.__is_running = False
        self.__time = ""

    def start_timer(self):
        self.__is_running = True
        timer_thread = threading.Thread(target=self.count_up_timer, args=(self.__stop_signal,))
        timer_thread.start()
        
    def count_up_timer(self, stop_signal):
        start_time = time.time()  # Get the current time

        while not self.__stop_signal.is_set():
            current_time = time.time() - start_time  # Calculate the elapsed time
            minutes = int(current_time // 60)
            seconds = int(current_time % 60)
            milliseconds = int((current_time % 1) * 1000)

            # Format the time
            time_str = "{:02d}:{:02d}.{:03d}".format(minutes, seconds, milliseconds)

            # Print the formatted time
            print("\r", time_str, end="", flush=True)
            self.__time = time_str
            # Wait for a short while before updating the timer
            time.sleep(0.001)

        self.__is_running = False   
        print("\nTimer stopped.")


    def stop_timer(self):
        self.__stop_signal.set()
        self.__is_running = False
        return self.__time

    def is_running(self):
        return self.__is_running