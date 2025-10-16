import socket
"""
Networking in python
"""
# host and port to connect to
HOST = 'localhost'
PORT = 9999

BUFFER_SIZE = 1024

# modes
CREATE_NEW = "CREATE"
LOGIN_EXISTING = "ENTER"
QUIT = "QUIT"

def main():
    # create socket object
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to socket
    client_sock.connect((HOST, PORT))

    
    quit = False
    while not quit:
        # choose mode
        answer = input("Create new login or enter login?: ").upper()
        while answer != CREATE_NEW and answer != LOGIN_EXISTING and answer != QUIT:
            print(f"Invalid input. Please enter '{CREATE_NEW}' to create a new login or '{LOGIN_EXISTING}' to enter an existing login.")
            answer = input("Create new login or enter login?: ").upper()
        
        if answer == QUIT:
            quit = True
            client_sock.send(answer.encode())
            break
        else:
            client_sock.send(answer.encode())

            # enter credentials
            username = input("Enter username: ").strip()
            if (username.upper() == QUIT):
                quit = True
                break
            password = input("Enter password: ")
            if (password.upper() == QUIT):
                quit = True
                break

            client_sock.send(username.encode())
            client_sock.send(password.encode())
            print("Server:", client_sock.recv(BUFFER_SIZE).decode())
            print()


    # get data from server and decode it
    print("Server:", client_sock.recv(BUFFER_SIZE).decode())

    # close socket
    client_sock.close()

if __name__ == "__main__":
    main()