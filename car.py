# Project           In class demo - Demo 2
# Description       Demonstrate if, elif, match statements
# Developed by      Apiwan Thumsamisorn
# Date              9/23/2025

# initializer = initialize newly initialized attributes 



class Car4:

    #Region Initializer
    def __init__(self,make,model,volume, type):
        self.__car_make = make      # Make it private attribute
        self.__car_model = model    # Make it private attribute
        self.__car_volume = volume  # Make it private attribute
        self.__car_type = type      # Make it private attribute

        #self.__car_size = self.__set_car_size()
        #self.__car_size = self.__find_car_size()
        #self.__car_size = self.__determine_car_size() #Make it private
        #self.__car_size = self.__identify_car_size()
        #self.__car_size = self.__assign_car_size()
        self.__car_size = self.__define_car_size()



    #Endregion

    #Region getters

    @property
    def car_make(self):
        return self.__car_make
    
    @property
    def car_model(self):
        return self.__car_model
    
    @property
    def car_volume(self):
        return self.__car_volume
    
    @property
    def car_type(self):
        return self.__car_type
    
    @property
    def car_size(self):
        return self.__car_size
    
    #EndRegion
    
    #Region instance methods

# Vehicle size classes by U.S. Fuel Economy Guide for sedans[5]
# Class	Interior combined passenger and cargo volume index
# Minicompact	< 85 cubic feet (2,405 L)
# Subcompact	85–99.9 cubic feet (2,405–2,830 L)
# Compact	100–109.9 cubic feet (2,830–3,110 L)
# Mid-size	110–119.9 cubic feet (3,115–3,395 L)
# Large	≥ 120 cubic feet (3,400 L)
    def __set_car_size(self):
        size = ""
        if self.car_volume < 85: # relational operator
            size = "Minicompact"
        elif self.car_volume < 100:
            size = "Subcompact"
        elif self.car_volume < 110:
            size = "Compact"
        elif self.car_volume <120:
            size = "Mid-size"
        else: 
            size = "Large"
        return size
    
    def __find_car_size(self):
        size = ""
        # example of nested if
        if self.car_type == "Sedan": # check equality >> using the 2 equals
            if self.car_volume < 85: # relational operator
                size = "Minicompact"
            elif self.car_volume < 100:
                size = "Subcompact"
            elif self.car_volume < 110:
                size = "Compact"
            elif self.car_volume <120:
                size = "Mid-size"
            else: 
                size = "Large"
        elif self.car_type == "Station Wagon":
            if self.car_volume < 130:
                size = "Small"
            elif self.car_volume < 160: 
                size = "Mid-size"
            else: 
                size = "Large"
        return size            
# Vehicle size classes by U.S. Fuel Economy Guide for sedans[5]
# Class	Interior combined passenger and cargo volume index
# Minicompact	< 85 cubic feet (2,405 L)
# Subcompact	85–99.9 cubic feet (2,405–2,830 L)
# Compact	100–109.9 cubic feet (2,830–3,110 L)
# Mid-size	110–119.9 cubic feet (3,115–3,395 L)
# Large	≥ 120 cubic feet (3,400 L)
# Vehicle size classes by U.S. Fuel Economy Guide for station wagons[5]
# Class	Interior volume index
# Small	< 130 cubic feet (3,680 L)
# Midsize	130–159 cubic feet (3,680–4,500 L)
# Large	≥ 160 cubic feet (4,530 L)

    #Endregion 

    # Region determine car size
    # multiple condition

    def __determine_car_size(self):

        size = "" # String variable
        if self.car_type == "sedan" and self.car_volume < 85: #both expressions are true
            size = "Mini Compact"
        elif self.car_type == "sedan" and self.car_volume < 100: 
            size = "Sub Compact"
        elif self.car_type == "sedan" and self.car_volume < 110:
            size = "Compact"
        elif self.car_type == "sedan" and self.car_volume < 120:
            size = "Mid-size"
        elif self.car_type == "sedan" and self.car_volume >= 120:
            size = "Large"
        elif self.car_type == "Station Wagon" and self.car_volume < 120:
            size = "Small"
        elif self.car_type == "Station Wagon" and self.car_volume < 160:
            size = "Mid-size"           
        elif self.car_type == "Station Wagon" and self.car_volume >= 160:
            size = "Large" 
        return size          


    # End Region

    # Region Match function 

    def __identify_car_size(self):
        size = ""
        match (self.car_type, self.car_volume):
            case (x,y) if x == "Sedan" and y < 85:
                size = "Mini Compact"
            case (x,y) if x == "Sedan" and y < 100:
                size = "Sub Compact"
            case (x,y) if x == "Sedan" and y < 110:
                size = "Compact"
            case (x,y) if x == "Sedan" and y < 120:
                size = "Mid-Size"  
            case (x,y) if x == "Sedan" and y >= 120:
                size = "Large"     
            case (x,y) if x == "Station Wagon" and y < 120:
                size = "Small"
            case (x,y) if x == "Station Wagon" and y < 160:
                size = "Mid-Size"  
            case (x,y) if x == "Station Wagon" and y >= 160:
                size = "Large"        
        return size
    # End Region

    # Region 

    def __assign_car_size(self):
        size = ""
        match self.car_type:
            case "sedan" if self.car_volume < 85:
                size = "Mini compact"
            case "sedan" if self.car_volume < 100:
                size = "Sub compact"
            case "sedan" if self.car_volume < 110:
                size = "Compact"
            case "sedan" if self.car_volume < 120:
                size = "Mid-size"
            case "sedan" if self.car_volume >= 120:
                size = "Large"
            case "Station Wagon" if self.car_volume < 130:
                size = "Small"
            case "Station Wagon" if self.car_volume < 160:
                size = "Mid-size"
            case "Station Wagon" if self.car_volume >= 160:
                size = "Large"

    def __define_car_size(self):
        size = "Standard" if self.car_type == "Sedan" else "Large"
        return size

    def __str__(self):
        return f"Make: {self.car_make}\nModel: {self.car_model}\nVolume: {self.car_volume}\nType: {self.car_type}\nSize: {self.car_size}"  
    
my_car = Car4("Toyota","Rav4","Red",50000)
print(my_car)
