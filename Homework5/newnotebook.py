notes= {1:'Wake up',2:'brush teath',3:'go to the moon',4:'eat something'}
def show_menu():
    print('CHOOSE OPTIONS\n' '   1: SHOW THEM ALL\n''   2: SHOW NOTE DETAILS\n''   3: CREATE NOTES\n''   4: UPDATE NOTE\n''   5: DELETE NOTE\n''   Q: QUIT THE APPLICATION\n''   M:SHOW MENU')
def option1():
        for key, value in notes.items():
            print(f"{key}: {value}")
def option2():
    action=int(input('Which note u wish to see: '))
    print('--------------------------------------------------------')
    print(f'NOTE {action} DETAILS')
    print(f'NOTE id: {notes[action]}')
    print(f'NOTE details: {notes[action]}')
def option3():
        lennotes=len(notes)
        notes[lennotes+1]=input('ADD A NEW NOTE: ')
def option4():
        upd=int(input('Which note you want to change: '))
        notes[upd]=input('Enter edited note: ')
        print('note updated')
def option5():
        deldict=int(input('Which note u want to delete: '))
        del(notes[deldict])

show_menu()
while True:
    choice=input('Choice: ')
    if choice == str(1):
        option1()
    elif choice ==str(2):
        option2()
    elif choice == str(3):
         option3()
    elif choice== str(4):
         option4()
    elif choice== str(5):
         option5()
    elif choice.upper() == 'Q':
        print("Goodbye!")
        break
    elif choice.upper() == 'M':
         show_menu()
    else:
        print("Invalid choice, please try again.")