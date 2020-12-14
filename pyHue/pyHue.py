
import requests


def get_bridge_info():
    # get dict object containing id and internal ip address
    # of the bridge connected to the current network
    r = requests.get("https://discovery.meethue.com")
    response = r.json()[0]

    return response


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()