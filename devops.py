import psutil
import requests


api_url = 'http://127.0.0.1:5000/alarm'
threshold = 90

def memory_usage():
    percent = psutil.virtual_memory().percent
    if percent > threshold:
        send_alarm()

def send_alarm():
    try:
        response = requests.post(api_url)
        if response.status_code == 200:
            print(f'Alarm!')
        else:
            print(f'Failed. Status code: {response.status_code}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    memory_usage()