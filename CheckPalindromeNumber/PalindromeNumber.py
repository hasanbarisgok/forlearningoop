class Palindrome(object): 

    def __init__(self,num):
        """Palindrome Class Constructor

        Args:
            num (_int or float_): _Any number to check is it palindrome or not._
        """
        self.const_num = num #The original num. We're saving the value in this variable.
        self.num = num #Num (int or float), Instance Varible
        self.numsinarray = [] #The list which includes $num digits as seperatly. : Example: num = 100, numsinarray = [1,0,0]
        self.shredNum() 
        self.printResult()

    
    def shredNum(self):
        """The function seperates num digits to list of numsinarray. 

        Returns:
            The function returns list of numsinarray.
        """
        
        while self.num > 0:
            self.numsinarray.insert(0, self.num % 10)
            self.num = self.num // 10
        return self.numsinarray

    
    def checkPalindrome(self):
        """The function compares numsinarray & newArr. 
        Program returns True or False as using the compare's result (same list or not).

        Returns:
            True meaning : The num is Palindrome.
            False meaning: The num is not Palindrome.
        """

        newArr = self.reverseArray(self.numsinarray)
        if self.numsinarray == newArr and self.num >= 0:
            return True
        else:
            return False


    def printResult(self):
        print(20*"*")
        print(f"Is {self.const_num} Palindrome? : {self.checkPalindrome()}")   
        


    @staticmethod
    def reverseArray(_numsinarr):
        """The method reverses numsinarray list.
    
        Returns:
            _numsinarr: The new list of reversed numsinarray list. 
        """
        return _numsinarr[::-1]
