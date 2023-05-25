import json
filename="F:\\Python\\Project\\computer_lab.txt"
jsfilename="F:\\Python\\Project\\computer_lab.json"  

def show_menu():
    """Displaying menu containing all the available options."""
    prompt= '\n###################################################'
    prompt+='\n\tComputer Lab Management Application'
    prompt+='\n###################################################\n'
    prompt+='\n[1] Add a new PC'
    prompt+='\n[2] Update an existing PC'
    prompt+='\n[3] Delete an existing PC'
    prompt+='\n[4] Display all the PCs'
    prompt+='\n[5] Display a specific PC'
    prompt+='\n[6] Quit\n'
    prompt+='\nEnter the option number from the above menu : '

    option_number = ''
    while option_number != '6':
        option_number=input(prompt)

        if option_number == '1':
            adding_pc()
        elif option_number == '2':
            update_pc()
        elif option_number == '3':
            remove_pc()
        elif option_number == '4':
            display_all_pcs()
        elif option_number == '5':
            display_individual_pc()
        elif option_number == '6':
            print("")
            print("---------------------------------------------------")
            print("\t    Exiting from the application")
            print("---------------------------------------------------")
            break
        else:
            print("\n--------Please enter a valid option number--------")


def adding_pc():
    """To add a new PC"""
    print("")
    print("------------------------------------------------")
    print("|           Adding a new PC in the lab         |")
    print("------------------------------------------------")

    try:
        with open(jsfilename) as file_object:
            pcs = json.load(file_object)       
    except FileNotFoundError:
        print("\n-----------Sorry the file does not exist-----------")
        
    pc_number = input('\t    PC number : ')

    exist=0 
    for name in pcs.keys():
        if pc_number == name:
            exist=1 
            print("\n-----------PC number is already exists-----------")
            prompt='\n   [1] Modify information of this existing PC'
            prompt+='\n   [2] Remove the PC from the lab'
            prompt+='\n   [3] Go back to the main menu\n'
            prompt+='\nEnter the option number from the above menu : '

            option=''
            while option != '1' or '2' or '3':
                option=input(prompt)
                if(option == '1'):
                    update_pc()
                    break
                elif(option == '2'):
                    remove_pc()
                    break
                elif(option == '3'):
                    show_menu()
                    break
                else:
                    print("\n--------Please enter a valid option number--------")

        elif pc_number != name:
            pass
    
    if exist == 1:
        pass
    elif exist !=1: 
        operating_system = input('\t    Operating system : ')
        sample_code = input('\t    Status : ')

        pcs[pc_number]={}
        pcs[pc_number]['PC number']=pc_number
        pcs[pc_number]['Operating system']=operating_system
        pcs[pc_number]['Status']=sample_code

        try:
            with open(filename,'w') as file:
                for keys,values in pcs.items():
                    file.write(f"\n\nPC number : {keys}")
                    file.write(f"\n\tOperating system : {values['Operating system']}")
                    file.write(f"\n\tStatus : {values['Status']}")
        except FileNotFoundError:
            print("\n-----------Sorry the file does not exist-----------")

        try:
            with open(jsfilename,'w') as file:
                json.dump(pcs,file)
        except FileNotFoundError:
            print("\n-----------Sorry the file does not exist-----------")
        
        anything = input("\n\tEnter anything to continue.")


def update_pc():
    """To update information of an existing PC."""
    print("")
    print("------------------------------------------------")
    print("|           Updating the PC in the lab         |")
    print("------------------------------------------------")
       
    try:
        with open(jsfilename) as file_object:
            pcs = json.load(file_object)   
    except FileNotFoundError:
        print("\n---------Sorry the file does not exist----------") 
        
    exist=0 
    num = input('   Enter the PC number you want to update : ')
    for name in pcs.keys():
        if num == name:
            ask=''
            while ask != 'Y' or 'N':
                ask = input('   Update Operating system? [Y/N] : ')
                if(ask == 'Y'):
                    new_operating_system = input('   Enter new Operating system : ')
                    pcs[num]['Operating system']=new_operating_system
                    exist=1 
                    break
                elif(ask == 'N'):
                    exist=1
                    break
                else:
                    print("\n--------Please choose a valid option--------")

            ask_again=''
            while ask_again != 'Y' or 'N':
                ask_again = input('   Update Status? [Y/N] : ')
                if(ask_again == 'Y'):
                        new_status = input('   Enter new status : ')
                        pcs[num]['Status']=new_status
                        exist=1 
                        break
                elif(ask_again == 'N'):
                        exist=1
                        break
                else:
                    print("\n--------Please choose a valid option--------")

        elif num != name:
            pass
    
    if exist == 1:
        pass
        print("")
        print('\t     PC Updated successfully')
    elif exist != 1:
        print("")
        print('\t     PC does not exist')
        prompt='\n\tDo you want to search again'
        prompt+='\n\t\t[1] Yes'
        prompt+='\n\t\t[2] No'
        prompt+='\n\tEnter the option number : '

        option=''
        while option != '1' or '2':
            option=input(prompt)
            if(option == '1'):
                update_pc()
                break
            elif(option == '2'):
                show_menu()
                break
            else:
                print("\n--------Please choose a valid option--------")
    
    try:
        with open(jsfilename,'w') as file:
            json.dump(pcs,file)
    except FileNotFoundError:
        print("\n---------Sorry the file does not exist----------")

    try:
        with open(filename,'w') as file:
            for keys,values in pcs.items():
                file.write(f"\n\nPC number: {keys}")
                file.write(f"\n\tOperating system: {values['Operating system']}")
                file.write(f"\n\tStatus: {values['Status']}")
    except FileNotFoundError:
        print("\n---------Sorry the file does not exist----------")

    anything = input("\n\tEnter anything to continue.")


def remove_pc():
    """To remove an existing PC from the lab. """
    print("")
    print("-------------------------------------------")
    print("|         Removing PC from the lab         |")
    print("-------------------------------------------")

    num = input('\t  Enter the PC number : ')
    print("-------------------------------------------")

    try:
        with open(jsfilename) as file_object:
            pcs = json.load(file_object)       
    except FileNotFoundError:
        print("\n---------Sorry the file does not exist----------")    

    exist = 0
    for name in pcs.keys():
        if num == name:
            del pcs[num]  
            exist = 1
            print("")
            print('\t  PC deleted successfully')
            break

        elif num != name:
            pass

    if exist == 1:
        pass

    elif exist != 1:
        print("")
        print('\t     PC does not exist')
        prompt='\n\tDo you want to search again'
        prompt+='\n\t\t[1] Yes'
        prompt+='\n\t\t[2] No'
        prompt+='\n\tEnter the option number : '

        option=''
        while option != '1' or '2':
            option=input(prompt)
            if(option == '1'):
                remove_pc()
            elif(option == '2'):
                show_menu()
            else:
                print("\n--------Please choose a valid option--------")

    try:
        with open(jsfilename,'w') as file:
            json.dump(pcs,file)
    except FileNotFoundError:
        print("\n---------Sorry the file does not exist----------")

    try:
        with open(filename,'w') as file:
            for keys,values in pcs.items():
                file.write(f"\n\nPC number : {keys}")
                file.write(f"\n\tOperating system : {values['Operating system']}")
                file.write(f"\n\tStatus : {values['Status']}")
    except FileNotFoundError:
        print("\n---------Sorry the file does not exist----------")

    anything = input("\n\tEnter anything to continue.")


def display_all_pcs():
    """To display information about all the PCs."""
    print("")
    print("-------------------------------------------")
    print("|      Displaying the PCs in the lab      |")
    print("-------------------------------------------")

    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("\n--------Sorry the file does not exist--------")
    else:
        print(contents)

    anything = input("\n     Enter anything to continue.")

def display_individual_pc():
    """To display all the information of a specific PC in the lab."""
    print("")
    print("-------------------------------------------")
    print("|      Displaying the PC information      |")
    print("-------------------------------------------")

    num = input('\t  Enter the PC number : ')
    print("-------------------------------------------")

    try:
        with open(jsfilename) as file_object:
            pcs = json.load(file_object)
    except FileNotFoundError:
        print("\n--------Sorry the file does not exist--------")

    exist=0  
    for name in pcs.keys():
        if num == name:
            print(f"\n\t  PC number : {pcs[num]['PC number']}")
            print(f"\t  Operating system : {pcs[num]['Operating system']}")
            print(f"\t  Status : {pcs[num]['Status']}")
            exist=1
        elif num != name:
            pass

    if exist == 1:
        pass
    elif exist != 1:
        print("") 
        print("-------Sorry the PC doesnot exist!!!-------")
        prompt='\n\tDo you want to add the PC'
        prompt+='\n\t\t[1] Yes'
        prompt+='\n\t\t[2] No'
        prompt+='\n\tEnter the option number : '

        option=''
        while option != '1' or '2':
            option=input(prompt)
            if(option == '1'):
                adding_pc()
                break
            elif(option == '2'):
                show_menu()
                break
            else:
                print("\n--------Please choose a valid option--------")
    
    anything = input("\n\tEnter anything to continue.")

show_menu()