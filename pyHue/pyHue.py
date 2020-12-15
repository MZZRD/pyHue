
import requests
import time


def get_bridge_info():
    """get dict object containing id and internal ip address
    of the bridge connected to the current network"""

    r = requests.get("https://discovery.meethue.com")
    response = r.json()[0]

    return response


def create_new_user(bridge_ip, user):
    """Create a new user"""

    wait_time = 10
    url = "http://%s/api" % bridge_ip
    body = '{"devicetype": "pyHue#%s"}' % user

    print("Waiting for link button to be pressed")
    for i in range(wait_time):
        r = requests.post(url, body)
        response = r.json()[0]

        if response.get("error") is not None:
            print(".", end="")
        elif response.get("success") is not None:
            user_name = response.get("success").get("username")
            print("\nSUCCESS : New user with username %s created" % user_name)
            return 1

        time.sleep(1)

    print("\nERROR : Link button not pressed in time")

    return 0


def main():
    # get bridge information
    bridge_info = get_bridge_info()

    # create a new user
    bridge_ip = bridge_info.get('internalipaddress')
    create_new_user(bridge_ip, "mjmtv")


if __name__ == '__main__':
    main()