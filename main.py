#!/usr/bin/env python3
from client.Application import Application
from client.Client import Client

if __name__ == '__main__':
    client = Client()
    client.mainloop()
    client.exit()
