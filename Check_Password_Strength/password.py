class CheckMyPassword(object):
    
    #Class Variables
    my_password : str = ""
    lower_character_count: int = 0
    upper_character_count: int = 0
    number_character_count: int = 0
    special_character_count: int = 0
   
    """
    Cases:
    
    Character count is < 8 weak
    Character count is > 8, both smaller upper characters or including minimum one number or special character : medium
    Character Count is > 8 and its including minimum two number, special character, and both smaller/upper characters : strong
    """
    
    def __init__(self, amy_password) -> None:
        """The Class Constructor

        Args:
            amy_password (_str_): _Password which you wants to check to see how strengthly your password._
        """
        self.my_password = amy_password
        self.len_password : int = len(amy_password)

        self.testing_password()
        self.cases()
        self.print()


    def testing_password(self):
        """The method has been created for surfing in string to use in cases.
        """
        for a in self.my_password:
            if (a.isupper()) == True:
                self.upper_character_count += 1

            if (a.islower()) == True:
                self.lower_character_count += 1

            if (a.isdigit()):
                self.special_character_count += 1

            if (a.isnumeric()):
                self.number_character_count += 1
           

    def cases(self):
        #Cases for checking password strength.
        case_1 = self.len_password <= 8
        case_2 = case_1 is False and self.lower_character_count > 1 and (self.upper_character_count > 1 or self.special_character_count > 1 or self.number_character_count)
        case_3 = case_1 is False and self.lower_character_count > 2 and self.upper_character_count > 2 and self.special_character_count > 2 and self.number_character_count > 2
        print(20*"*")
        if case_1 is True :
            print("The password is weak.")
        elif case_2 is True:
            print("The password is med.")
        elif case_3 is True:
            print("The password is strong.")
        else:
            print("The password is weak.")    

    
    def print(self):
        print(f"Your pass word has:\n{self.lower_character_count} Lower Character\n{self.upper_character_count} Upper Character\n{self.special_character_count} Special/Digital Character\n{self.number_character_count} Numeric Character")
        print(20*"*")
