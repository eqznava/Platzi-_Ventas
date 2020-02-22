

clients = 'Pablo, Ricardo'


def create_client(client_name):
    global clients

    if client_name not in clients:
        _add_comma()
        clients += client_name
    else:
        print('Client already is in the client\'s list')

def list_clients():
    global clients
    print(clients)

def _update_clients(client_name,updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name, updated_client_name)
    else:
        print('Client is not in clients list')

def _add_comma():
    global clients

    clients += ', '


def _print_welcome():
    print('*' * 30)
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 30)
    print('What would you like to do today')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')

def _get_client_name():
    list_clients()
    return input('What is the client name?\n')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name?\n')
        _update_clients(client_name, updated_client_name)
        list_clients()
    else:
        print('Invalid command')
