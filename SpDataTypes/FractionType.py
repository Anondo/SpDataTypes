# Written by Ahmad Anondo <aanondos@gmail.com>
# This module is currently compatible with python 2.7 and still currently under development




class Fraction(object):

    """
     This class works with two integer values and represents them in
     the numerator/denominator format.For example, Fraction(1 , 2)
     becomes (1/2).
     Contains Methods which accepts float numbers and turns them into
     the fractional format.
     Any basic programming operations can be performed.
     Keep in mind:
     1. Maximum of 5 digits after the decimal point will be
     counted when working with float numbers.
     2.This class only works with integers as numerators and
     denominators so far.

    """



    def __init__(self , numerator = 1 , denominator = 1):
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        self.result = "(" + str(self.numerator) + "/" + str(self.denominator) + ")"
    #setting data methods
    def setArgument(self , numerator , denominator):
        """ sets the numerator and the denominator of the fractional data"""
        self.numerator =int(numerator)
        self.denominator = int(denominator)
        self.result = "(" + str(self.numerator) + "/" + str(self.denominator) + ")"
    def setNumerator(self , numerator):
        """ sets the numerator of the fractional data """
        self.numerator = int(numerator)
        self.result = "(" + str(self.numerator) + "/" + str(self.denominator) + ")"
    def setDenominator(self , denominator):
        """ sets the denominator of the fractional data """
        self.denominator = int(denominator)
        self.result = "(" + str(self.numerator) + "/" + str(self.denominator) + ")"
    def getNumerator(self):
        """ Returns the numerator """
        return self.numerator
    def getDenominator(self):
        """ Returns the denominator """
        return self.denominator
    def getFloatingResult(self):
        """ Returns the result of the division of the numerator and the denominator """
        return float(self.numerator)/self.denominator

    #overloading methods
    def __str__(self):
        return self.result
    def __add__(self , fr):
        val1 = float(self.numerator)/ self.denominator
        if(fr.__class__.__name__ == "Fraction"): #if the second parameter of the + operator is a Fraction object
            val2 = float(fr.numerator) / fr.denominator
        else: # else a digit
            fr = float(fr)
            temp = Fraction()
            temp.setValue(fr)
            val2 = float(temp.numerator) / temp.denominator
        total = val1 + val2
        total = self.reducePrecision(total)
        temp = Fraction()
        temp.setValue(total)
        return temp
    def __radd__(self , val):
        val = float(val)
        temp = Fraction()
        temp.setValue(val)
        val1 = float(temp.numerator) / temp.denominator
        val2 = float(self.numerator)/ self.denominator
        total = val1 + val2
        temp.setValue(total)
        return temp
    def __sub__(self , fr):
        val1 = float(self.numerator)/ self.denominator
        if(fr.__class__.__name__ == "Fraction"):
            val2 = float(fr.numerator) / fr.denominator
        else:
            fr = float(fr)
            temp = Fraction()
            temp.setValue(fr)
            val2 = float(temp.numerator) / temp.denominator
        diff = val1 - val2
        diff = self.reducePrecision(diff)
        temp = Fraction()
        temp.setValue(diff)
        return temp
    def __rsub__(self , val):
        val = float(val)
        temp = Fraction()
        temp.setValue(val)
        val1 = float(temp.numerator) / temp.denominator
        val2 = float(self.numerator)/ self.denominator
        diff = val1 - val2
        temp.setValue(diff)
        return temp
    def __mul__(self , fr):
        val1 = float(self.numerator)/ self.denominator
        if(fr.__class__.__name__ == "Fraction"):
            val2 = float(fr.numerator) / fr.denominator
        else:
            fr = float(fr)
            temp = Fraction()
            temp.setValue(fr)
            val2 = float(temp.numerator) / temp.denominator
        product = val1 * val2
        product = self.reducePrecision(product)
        temp = Fraction()
        temp.setValue(product)
        return temp
    def __rmul__(self , val):
        val = float(val)
        temp = Fraction()
        temp.setValue(val)
        val1 = float(temp.numerator) / temp.denominator
        val2 = float(self.numerator)/ self.denominator
        product = val1 * val2
        temp.setValue(product)
        return temp
    def __div__(self , fr):
        val1 = float(self.numerator)/ self.denominator
        if(fr.__class__.__name__ == "Fraction"):
            val2 = float(fr.numerator) / fr.denominator
        else:
            fr = float(fr)
            temp = Fraction()
            temp.setValue(fr)
            val2 = float(temp.numerator) / temp.denominator
        answer = val1 / val2
        answer = self.reducePrecision(answer)
        temp = Fraction()
        temp.setValue(answer)
        return temp
    def __rdiv__(self , val):
        val = float(val)
        temp = Fraction()
        temp.setValue(val)
        val1 = float(temp.numerator) / temp.denominator
        val2 = float(self.numerator)/ self.denominator
        answer = val1 / val2
        temp.setValue(answer)
        return temp
    def __lt__(self , fr):
        if(fr.__class__.__name__ == "Fraction"):
            return self.getFloatingResult() < fr.getFloatingResult()
        else:
            return self.getFloatingResult() < fr
    def __gt__(self , fr):
        if(fr.__class__.__name__ == "Fraction"):
            return self.getFloatingResult() > fr.getFloatingResult()
        else:
            return self.getFloatingResult() > fr
    def __eq__(self , fr):
        if(fr.__class__.__name__ == "Fraction"):
            return self.getFloatingResult() == fr.getFloatingResult()
        else:
            return self.getFloatingResult() == fr
    def __ne__(self , fr):
        if(fr.__class__.__name__ == "Fraction"):
            return self.getFloatingResult() != fr.getFloatingResult()
        else:
            return self.getFloatingResult() != fr
    def __le__(self , fr):
        if(fr.__class__.__name__ == "Fraction"):
            return self.getFloatingResult() <= fr.getFloatingResult()
        else:
            return self.getFloatingResult() <= fr
    def __ge__(self , fr):
        if(fr.__class__.__name__ == "Fraction"):
            return self.getFloatingResult() >= fr.getFloatingResult()
        else:
            return self.getFloatingResult() >= fr

    #data manipulation methods
    def setValue(self , value):
        """ sets the data in a fractional format """
        value = float(value)
        value = self.reducePrecision(value) #limits the number of digits after decimal point to avoid  overflow error
        self.convert(value) #converts the floating number into fractional format
    def convert(self , value):
        """ converts a float number to a fractional number """
        self.numerator = int(str(value).split(".")[0] + str(value).split(".")[1]) #extracting the numerator part i.e, for an input of 1.5 the numerator becomes 15
        afterDec = str(value).split(".")[1] #extracting the digits after decimal point
        self.denominator = int("1" + len(afterDec) * "0") #seting denominator depending on the length of the digits after point.
        self.result = "(" + str(self.numerator) + "/" + str(self.denominator) + ")"
        self.applyCancellation() #starts looking for common divisors and starts cancelling
    def applyCancellation(self):
        """ The data is reduced to the lowest terms using cancellation """
        if(self.numerator > self.denominator): #depending on which of the data is bigger,the matching of common divisor will beign
            for num in [self.denominator] + range(abs(int(self.denominator))/2, 1 , -1): #the range of data to check will be from the numerator/denominator itself then from the half of its value to 2
                self.divideToCancel(num)
                if(self.denominator == 1):
                    break
        else:
            for num in [self.denominator] + range(abs(int(self.numerator))/2, 1 , -1): #the range of data to check will be from the numerator/denominator itself then from the half of its value to 2
                self.divideToCancel(num)
                if(self.numerator == 1):
                    break
    def divideToCancel(self , num):
        """ Checks for the common divisor and applies cancellation """
        if(self.numerator % num == 0 and self.denominator % num == 0): # if there is a common divisor
            self.numerator /= num #apply division
            self.denominator /= num
            self.result = "(" + str(self.numerator) + "/" + str(self.denominator) + ")" #compute result
    def reducePrecision(self , val):
        """ Reduces the number of digits after decimal to a maximum of 5 """
        beforeDec = str(val).split(".")[0] #the number before decimal point
        afterDec = str(val).split(".")[1] # the nmber after decimal point
        afterDec = afterDec[0:5] #limiting the number of digits after the decimal point
        return float(beforeDec + "." + afterDec) #returning the new value with limited digits after decimal point
