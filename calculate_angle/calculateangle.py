class CalculateAngle(object):

    #class variables:

    first_selection : float = 0.0   #First Time (hh.mm)
    second_selection: float = 0.0   #Second Time (hh.mm)
    result_between : float = 0.0    #The angle value between of first and second time.

    def __init__(self,afirst_selection,asecond_selection):
        """Calculate Angle Constructor

        Args:
            afirst_selection (_float_): First Time (hh.mm)
            asecond_selection (_float_): Second Time (hh.mm)
        """
        #Instance variables:

        self.first_selection = afirst_selection  #First Time (hh.mm)
        self.second_selection = asecond_selection #Second Time (hh.mm)
        self.time_array = [] #Time Array (firsthh,firstmm,secondhh,secondmm)
        self.split_times()
        self.new_values()
        self.calculate_angle()
        
        
    def split_times(self):
        """The method is splitting times (hh.mm = hh,mm)
        """
        self.first_selection = str(self.first_selection).split(".")
        self.second_selection = str(self.second_selection).split(".")

    def new_values(self):
        """The method is setting and adding values which has been splitted. (firsthh,firstmm,secondhh,secondmm)
        """
        val1 = int(self.first_selection[0]) #first hh
        val2 = int(self.first_selection[1]) #first mm
        val3 = int(self.second_selection[0]) #second hh
        val4 = int(self.second_selection[1]) #second mm
        self.time_array.extend((val1,val2,val3,val4))
            
    def calculate_angle(self):
        """The method firstly calculates angle. After that, it writes result.
        """
        self.result_between = abs(self.time_array[0] - self.time_array[2]) * 60 + abs(self.time_array[1]-self.time_array[3])
        print(f"The result is : {self.result_between}")
        print(20 * "-")
