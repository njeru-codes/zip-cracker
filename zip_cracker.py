'''
    A Python script that attempts to crack password-protected ZIP files 
    using a list of common passwords.

    Usage:
        python3 zip_cracker.py --threads=10 --file "path_to file" -w "path_to_wordlist"
        python3 zip_cracker.py -f "file_path" -w "worldlist_file"  -t=20

'''
import zipfile
import concurrent.futures

# Constants
zip_file_path = ""
password_file_path = ""
max_threads = 40

def print_banner():
    banner = r"""
      _                                  _                
     (_)                                | |               
 ____ _  _ __     ___  _ __  __ _   ___ | | __ ___  _ __  
|_  /| || '_ \   / __|| '__|/ _` | / __|| |/ // _ \| '__| 
 / / | || |_) | | (__ | |  | (_| || (__ |   <|  __/| |    
/___||_|| .__/   \___||_|   \__,_| \___||_|\_\\___||_|    
        | |                                               
        |_|             @njeru-codes
    """
    print(f"{banner} \n\n")

def crack_password(zip_file_path, password):
    try:
        with zipfile.ZipFile(zip_file_path) as zip_file:
            zip_file.extractall(pwd=password.encode('utf-8'))
            return password  
    except :
        return None  

def main():
    print_banner()
    with open(password_file_path, 'r') as password_file:
        passwords = [line.strip() for line in password_file]

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        
        future_to_password = {executor.submit(crack_password, zip_file_path, passkey): passkey for passkey in passwords}

        for future in concurrent.futures.as_completed(future_to_password):
            result = future.result()
            if result is not None:
                print(f"Password of the file is: {result}")
                break  
            
if __name__ == "__main__":
    main()
