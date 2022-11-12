class LetterCombinations():
    phone_keys = {'1': [],
             '2': ["a","b","c"],
             '3': ["d","e","f"],
             '4': ["g","h","i"],
             '5': ["j","k","l"],
             '6': ["m","n","o"],
             '7': ["p","q","r","s"],
             '8': ["t","u","v"],
             '9': ["w","x","y","z"],
             '0': [" "]}
    

    def __init__(self,firstTouch:int,secondTouch:int) -> None:
        """The keys which will touch from person.
        Given a string containing digits from 2-9 inclusive. Return the answer in any order.

        Args:
            firstTouch (str): _a number between of 2 - 9_
            secondTouch (str): _a number between of 2 - 9_
        """
        self.firstTouch = firstTouch
        self.secondTouch = secondTouch
        self.combinate()
        self.print()
        
          
    def combinate(self):
        """The Combinate Function.
        The function creates 2D Array(combinated_array), and returns combinated_array.
        The function returns all possible letter combinations that the number could represent.
        
        Returns:
            _combinated_array_: _letter combinations_
        """
        
        combinated_array = []
        for i in range(self.from_dictionary(self.firstTouch)):
            for j in range(self.from_dictionary(self.secondTouch)):
                combinated_array.append(LetterCombinations.phone_keys[f'{self.firstTouch}'][i] + LetterCombinations.phone_keys[f'{self.secondTouch}'][j])
        return combinated_array
        
    def print(self):
        """The function prints letter combinations.
        """
        print(f"These are all combinates for these keys: Key First Touched : {self.firstTouch}, Key Second Touched: {self.secondTouch}")
        print(self.combinate())
        print(100*"*")    
                 
    @staticmethod
    def from_dictionary(_calculatelen):
        """The staticmethod returns length of key's values.
        Args:
            _calculatelen (_instanceVariable_): _firstTouch or secondTouch_

        Returns:
            _length of key's values._: _description_
        """
        return len(LetterCombinations.phone_keys[f'{_calculatelen}'])     
      
    
            
