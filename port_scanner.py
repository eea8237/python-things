import socket
import time

REMOTE_HOST = "scanme.nmap.org"
LOCALHOST = "localhost"
DEFAULT_START = 1
DEFAULT_END = 500

MIN_PORT = 1
MAX_PORT = 65535

# port types
OPEN = "open"
CLOSED = "closed"
FILTERED = "filtered"

# commands
LOCAL = {"local", "l"}
REMOTE = {"remote", "r"}
QUIT = {"quit", "q"}

OPEN_CMDS = {"open", "o"}
CLOSED_CMDS = {"closed", "c"}
FILTERED_CMDS = {"filtered", "f"}
ALL_CMDS = {"all", "a"}

YES = {"yes", "y"}
NO = {"no", "n"}


def scan_ports(start=DEFAULT_START, end=DEFAULT_END, host=REMOTE_HOST, no_text=False):
    """
    Scan port numbers between start (inclusive) and end (inclusive) on the specified host. 
    no_text parameter hides print statements if True.
    Returns number of each type of port scanned and the total number of ports scanned
    """
    total_count = 0
    open_count = 0
    closed_count = 0
    filtered_count = 0
    for i in range(start, end+1):
        try:
            client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_sock.settimeout(4)
            client_sock.connect((host, i))
            # open port
            if not no_text: print(f"port {i} is open.")
            total_count += 1
            open_count += 1
        except ConnectionRefusedError:
            # closed port
            if not no_text: print(f"port {i} is closed.")
            total_count += 1
            closed_count += 1

        except TimeoutError:
            # filtered port
            if not no_text: print(f"port {i} is filtered.")
            total_count += 1
            filtered_count += 1

    return open_count, closed_count, filtered_count, total_count

def cli():
    """
    CLI for scanning ports
    """
    host = ""
    start = -1
    end = -1
    no_text = None

    go_ahead = False
    
    # configure port scan
    while not go_ahead:
        # set host
        while host == "":
            cmd = input("Scan local or remote host?: ").lower()

            if cmd in LOCAL or cmd == "": # default is localhost
                host = LOCALHOST
            elif cmd in REMOTE:
                host = REMOTE_HOST
            else:
                print(f"Invalid input. Enter 'remote'/'r' for the remote host {REMOTE_HOST} or 'local'/'l' for localhost.")
                continue
        
        # set start port number
        while start == -1:
            cmd = input("Starting port number: ")
            try:
                if cmd == "":
                    # if the user doesn't enter anything, go with the default
                    start = DEFAULT_START
                elif int(cmd) > MAX_PORT or int(cmd) < MIN_PORT:
                    raise ValueError
                else:
                    start = int(cmd)
            except ValueError:
                print(f"Invalid input. Enter an integer between {MIN_PORT} and {MAX_PORT}.")

        # set end port number
        while end == -1:
            cmd = input("End port number: ")
            try:
                if cmd == "":
                    # if the user doesn't enter anything, go with the default
                    end = DEFAULT_END
                    if end < start: end = start
                elif int(cmd) > MAX_PORT or int(cmd) < MIN_PORT or int(cmd) < start:
                    raise ValueError
                else:
                    end = int(cmd)
            except ValueError:
                print(f"Invalid input. End must be greater than or equal to start and an integer between {MIN_PORT} and {MAX_PORT}.")
        
        # choose to show text or not
        while no_text == None:
            cmd = input("Show ports being scanned? (Y/N): ").lower()
            while cmd not in YES and cmd not in NO and cmd != "":
                print("Please enter (y)es or (n)o.")
                cmd = input("Show ports being scanned? (Y/N): ").lower()

            if cmd in YES:
                no_text = False
            else: # default is no
                no_text = True


        print(f"Host: {host}, Start: {start}, End: {end}, Show Text: {not no_text}")
        cmd = input("Scan ports with these configurations? (Y/N): ").lower()
        while cmd not in YES and cmd not in NO:
            print("Please enter (y)es or (n)o.")
            cmd = input("Scan ports with these configurations? (Y/N): ").lower()
        
        if cmd in NO:
            print("Restarting configuration...")
            start = -1
            end = -1
            host = ""
            no_text = None
        else:
            print("Starting scan...")
            go_ahead = True

    start_time = time.perf_counter()
    open_count, closed_count, filtered_count, total_count = scan_ports(start, end, host, no_text)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Scanning complete!")
    print(f"Number of open ports: {open_count}")
    print(f"Number of closed ports: {closed_count}")
    print(f"Number of filtered ports: {filtered_count}")
    print(f"Total number of ports scanned: {total_count}")
    print(f"Time to scan: {elapsed_time} s")


def main():
    cli()

if __name__ == "__main__":
    main()