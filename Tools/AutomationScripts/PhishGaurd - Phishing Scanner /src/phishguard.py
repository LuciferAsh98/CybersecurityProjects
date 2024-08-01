import sys
from phishing_check import is_phishing_url
from colorama import init, Fore, Style
import pyfiglet

init(autoreset=True)

def main():
    # ASCII Art for the tool name
    ascii_art = pyfiglet.figlet_format("PhishGuard", font="slant")
    print(f"{Fore.BLUE}{Style.BRIGHT}{ascii_art}")
    
    print(f"{Fore.GREEN}PhishGuard v1.0 - Your personal phishing protection tool.\n")
    
    while True:
        url = input(Fore.GREEN + "🔍 Enter a URL to check (or type 'q' to quit): " + Style.RESET_ALL)
        
        if url.lower() == 'q':
            print(Fore.CYAN + "Goodbye! Stay safe online. 👋")
            sys.exit()
        
        is_phishing = is_phishing_url(url)
        if is_phishing:
            print(f"{Fore.RED}🚩 Warning: The URL appears to be a phishing site!")
        else:
            print(f"{Fore.GREEN}✅ The URL is safe.")
        print()  # Add space between checks

if __name__ == "__main__":
    main()
