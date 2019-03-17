import argparse
import sys
# def check_args1():
#     parser = argparse.ArgumentParser()
#     parser.parse_args()

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Script to learn basic argparse')
    parser.add_argument('-H', '--host',
                        help='host ip',
                        required='True')
    parser.add_argument('-p', '--port',
                        help='port of the web server',
                        default='8080')
    parser.add_argument('-u', '--user',
                        help='user name',
                        default='root')

    results = parser.parse_args(args)
    return (results.host,
            results.port,
            results.user)

if __name__ == '__main__':
    h, p, u = check_arg(sys.argv[1:])
    print ('h =',h)
    print ('p =',p)
    print ('u =',u)