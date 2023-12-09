import os, question_c as qc

exit_clause = 'EXIT'
confirmation_clause = 'YES'
stop_clause = 'STOP'

homework_number = 'Final Exam, Question C'
homework_number = homework_number.upper()
main_menu_header_text = ' \x1B[4m' + '\tWELCOME TO THE ' + homework_number + ' MENU:\x1B[0m'
selection1_text = '\tPress [1]\tto search stock symbol.'
selection2_text = '\tPress [2]\tto search company name.'
exit_choice_text = '\tType  [exit]\tto exit the program'
input_prompt = '\033[1m' + '\033[96m' + '\n\t >>> ' + '\033[0m'
unknown_entry = '\033[91m' + '\033[1m' + '\t>>>INVALID ENTRY<<<' + '\033[0m'
exit_confirmation_text = '\033[93m' + '\n\tDo you want to exit?\n\tEnter [YES]\tto exit\n\tEnter [NO]\tto return to the menu.' + '\033[0m'
exit_text = '\x1B[3m' + '\033[1m' + '\033[91m' + '\tEXITING THE ' + homework_number + ' MENU' + '\x1B[0m'

"""
    >>> START FUNCTIONS FOR MENU NAVIGATION 
"""

def is_confirmed_clause(str):
    str = str.upper()
    global confirmation_clause
    return str == confirmation_clause or str == confirmation_clause[0:1:1] or str == confirmation_clause[0:2:1]

def exit_confirmation(user_confirmation):
    global exit_clause, confirmation_clause, exit_confirmation_text

    print(exit_confirmation_text)

    user_confirmation = input(input_prompt).upper()

    if is_confirmed_clause(user_confirmation) == True:
        result = exit_clause
        print(exit_text)
    else: result = 0    
    return result

def is_exit_clause(str):
    str = str.upper()
    global exit_clause
    return str == exit_clause or str == exit_clause[0:1:1] or str == exit_clause[0:2:1] or str == exit_clause[0:3:1] 

def main_menu():

    global exit_clause, confirmation_clause, main_menu_header_text, selection1_text, input_prompt, unknown_entry
    user_selection = '0'
    count = 0
    
    while user_selection != exit_clause:
        if count < 1:
            os.system('clear')
            count += 1

        print(main_menu_header_text)
        print(selection1_text)
        print(selection2_text)
        print(exit_choice_text)

        user_selection = input(input_prompt)
        
        if user_selection == '1':
            os.system('clear')
            stock_path = qc.Stock()
            print('\tEnter Company Name')
            print('\tStock symbol is:   ' + stock_path.get_symbol(input(input_prompt)) + '\n')

        if user_selection == '2':
            os.system('clear')
            stock_path = qc.Stock()
            print('\tEnter Stock Symbol')
            print('\tCompany name is:   ' + str(stock_path.get_company_name(input(input_prompt))) + '\n')
                     
        elif is_exit_clause(user_selection) == True:
            user_selection = exit_confirmation(user_selection)
            
        elif user_selection not in ['1','2',True]:
            print(unknown_entry)