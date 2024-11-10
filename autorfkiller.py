#!/usr/bin/env python3
#!/bin/bash

from gnupython import main as bruteforce_chip #brute force for chip
from gnupythonnb import main as bruteforce_nbits
from gnupython_jamming import main as bruteforce2
from replayattack import main3 as replayattack
from generatesignallock1 import main as generatesignal
from termcolor import colored

def main_menu():

    intro = """
                    ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░       ░▒▓███████▓▒░░▒▓████████▓▒░ 
                    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                    ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓██████▓▒░   
                    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                    ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓██████▓▒░       ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                                                                       
                                                                                                        
                        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓███████▓▒░         
                        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░        
                        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░        
                        ░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓███████▓▒░         
                        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░        
                        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░        
                        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░        
                                                                                                        
                                            [Author: Danilo Erazo -> revers3 everything]
                                                            Version: 3.0
                                                              November 2024
                                                        [Car Key Fob Hacking]
    """

    print(f"\033[91m{intro}\033[0m")

    description = """                      
[Description]: AUTORFKILLER IS A TOOL THAT ALLOWS YOU TO UNLOCK CARS.
          
          A brute force attack can be carried out on learning codes/fixed codes since it contains a
          complete database with the coding and modulation carried out by the all IC chips that emit
          learning codes/fixed codes. Also, you can test if your car is vulnerable to relay attacks
          (learning/fixed codes). You can create and send jamming signals to execute RollJam attacks.
          Finally, you can create an RF signal with the parameters you want, this can be used to
          inject a backdoor into KES.
        """
    
    print(colored(description, 'green'))
    warning = """
[Warning]: This tool was created to verify the safety of cars and help in the world of automotive cybersecurity.
          Any unethical use is the responsibility of the user. This tool can cause DoS.
    """

    print(f"\033[91m{warning}\033[0m")

    print("[1] Brute force to a learning/fixed codes")
    print("[2] Set a backdoor in the KES/Send a learning code")
    print("[3] Record and Replay an RF Signal (Discover if your car use learning/fixed codes | execute RollJam attack)")
    print("[4] Send a Jamming Signal (execute RollJam attack)")
    print("[0] Exit")

def brute_force_menu():
    print("\n--> Brute force to a learning/fixed code")
    print("[1] Enter the learning/fixed code chip")
    print("[2] Another chip? Set custom arguments")
    print("[0] Back to main menu")

def main1():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                brute_force_menu()
                sub_choice = input("Enter your choice: ")

                if sub_choice == '1':#BRUTE FORCE CODE!!!!!!!!!!!!!!!!
                    bruteforce_chip()
                    
                elif sub_choice == '2':
                    bruteforce_nbits()
                elif sub_choice == '0':
                    break
                else:
                    print("Invalid choice, please try again.")
        
        elif choice == '2':
            print("\nSet a backdoor in the KES")
            # Implement functionality for option 2
            generatesignal()

        elif choice == '3':#REPLAY ATACK!!!!!!!!!!!!
            print("\n--> Record and Replay an RF Signal")
            # Implement REPLAY ATTACK FUNCTION
            replayattack()

        elif choice == '4':
            print("\n--> Send a jamming signal")
            # Implement functionality for option 4
            bruteforce2()#Enter the frequency

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main1()
