
from time import sleep
from threading import Thread
from logging_program import log_to_window, start_log_window

def print_something():
    for i in range(50):
        log_to_window(f"Line {i}")
        sleep(0.5)

Thread(target = start_log_window).start() 
Thread(target = print_something).start() 
