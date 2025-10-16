import socket
import threading

import bcrypt

from password_client import *

#__LOGINS_FILE = "C:\\Users\\r0wl3t\\Desktop\\csec projects\\python\\passwords\\logins.txt"
__LOGINS_FILE = ".\\passwords\\logins.txt"

"""
the most secure password server of all time
"""
def handle(client_sock):
    quit = False
    while not quit:
        # first see if new login is being created or existing login
        mode = client_sock.recv(BUFFER_SIZE).decode()
        print(f"Selected mode: {mode}")

        if mode == QUIT:
            quit = True
            client_sock.send("Closing connection. Goodbye!".encode())
            print("Quitting...")
            break

        # recieve username and password
        username = client_sock.recv(BUFFER_SIZE).decode()
        password = client_sock.recv(BUFFER_SIZE).decode()
            
        if username.upper() == QUIT or password.upper() == QUIT:
            quit = True
            client_sock.send("Closing connection. Goodbye!".encode())
            break

        msg = "" # message to be sent
        found = False
        # store username and password if this is a new login
        if mode == CREATE_NEW:
            print("opening file...")
            with open(__LOGINS_FILE, "a+") as file:
                print("file opened")
                # first, check if this username is already in the file
                exists = False
                for line in file:
                    line = line.strip().split(",") # format is usrname,psw
                    if line[0] == username:
                        # for now, repeat usernames aren't saved
                        # maybe add a mode for replacing username and password?
                        msg = f"{username} already in logins. New username was not saved."
                        exists = True
                if not exists:
                    # file.write(f"{username},")
                    # password = password.encode()
                    # salt = bcrypt.gensalt()
                    # hash = bcrypt.hashpw(password, salt)
                    # file.write(f"{hash}\n")
                    file.write(f"{username},{password}\n")
                    msg = "Password and username stored."
        
        # if the login exists, search through the file for the login and compare the entered password
        elif mode == LOGIN_EXISTING:
            with open(__LOGINS_FILE, "r") as file:
                for line in file:
                    line = line.strip().split(",") # format is usrname,psw
                    if line[0] == username:
                        if len(line) < 2: print("what")
                        else:
                            if (password == line[1]):
                            # if bcrypt.checkpw(password.encode(), line[1]):
                                msg = f"Login successful. Welcome, {username}."
                            else:
                                msg = f"Login unsuccessful..."
                            found = True
                            break
                
                # if we get through the file without finding the username, it hasn't been stored
                if not found: msg = f"Username {username} not found."
                
        print(msg)
        client_sock.send(msg.encode())
        
    # close socket
    client_sock.send(b'Thank you for connecting')
    client_sock.close()


def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((HOST, PORT))

    server_sock.listen(5)

    print("Waiting...")
    while True:
        client_sock, addr = server_sock.accept()
        print("Got connection from", addr)
        
        thread = threading.Thread(target=handle, args=(client_sock,))
        thread.start()
        print("Waiting...")

if __name__ == "__main__":
    main()

    
