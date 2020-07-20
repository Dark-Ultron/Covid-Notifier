
import time
from plyer import notification
import requests
from bs4 import BeautifulSoup


def notify_me(title, msg):
    notification.notify(
        title=title,
        message=msg,
        app_icon='virus.ico',
        timeout=10,
        ticker='just testing'
    )

def get_data(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    states = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam',
    'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa', 'Gujarat',
    'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Madhya Pradesh',
    'Maharashtra','Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab'
    , 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal']
    print('select the state:')
    for i in range(len(states)):
        print(f"{i+1}. {states[i]}")
    selected = int(input())
    while True:
        html_data = get_data("https://www.mohfw.gov.in/")
        soup = BeautifulSoup(html_data, 'html.parser')
        data_str = str()
        for tr in soup.find('tbody').find_all("tr"):
            data_str += tr.get_text()
        data_list = data_str.strip().split('\n\n')
        final = [r.split('\n') for r in data_list]
        # states = [state[1] for state in final[:35]]


        for state in final:
            if states[int(selected)-1] == state[1]:
                ntitle = "Cases of Covid 19"
                ntext = f"State: {state[1]}\nConfirmed: {state[-1]}\nActive: {state[2]}\nRecovered: {state[3]} & Death: {state[-2]}"
                notify_me(ntitle,ntext)
                break

        time.sleep(20)
