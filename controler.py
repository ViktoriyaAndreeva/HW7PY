import menu
import function


def button_click():
    menu = menu.menu()
    choice = menu.control_menu()
    if choice == True:
        go_to ={
            '1' : function.add,
            '2' : function.delete,
            '3' : function.upload_format1,
            '4' : function.upload_format2,
            '5' : function.create_format1,
            '6' : function.create_format2,
            '7' : function.view_contakt,
            '8' : function.find_contakt,
            '9' : function.about_work,
            '10' : function.exit
        }
        go_to[menu]()
    
button_click()   