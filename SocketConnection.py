import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Changing below "host" value to a target IP will give you information about that target.
    host = 'localhost'
    # If you are looking for a port, change the below value.
    port = 5000
    result = s.connect_ex((host, port))
    print('Result is {}'.format(result))
    s.close()


if __name__ == '__main__':
    main()
