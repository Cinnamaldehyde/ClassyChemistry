import CompoundClassyNew

class Fraction():
    def __init__(self, numerator, denominator):
        self.primes = [2,3,5,7,11,13,17]
        self.numerator = int(numerator)
        self.denominator = int(denominator)
    def multiplyByWhole(self, num):
        self.numerator = self.numerator * num
        self.reduceFrac()
    def looping(self, listy):
        coefList = listy
        largestDenom=0
        isOne=False
        while isOne==False:
            for thing in coefList:
                if abs(thing.denominator) > largestDenom:
                    largestDenom = abs(thing.denominator)
            
            i = 0
            while i<len(coefList):
                coefList[i].numerator = coefList[i].numerator * largestDenom
                if coefList[i].numerator%coefList[i].denominator == 0:
                    coefList[i].numerator = coefList[i].numerator/coefList[i].denominator
                    coefList[i].denominator = 1
                i+=1
            if largestDenom == 1:
                isOne = True
        return coefList
    def reduceFrac(self): # reduces Fractions, example: 10/5--> 2/1
        i = 0
        while i<len(self.primes):
            booly = True
            if self.numerator%self.primes[i]!=0 or self.denominator%self.primes[i]!=0:
                booly = False
            if booly:
                self.numerator = self.numerator/self.primes[i]
                self.denominator = self.denominator/self.primes[i]
            else:
                i = i + 1
        self.negatives()
    def addition(self,tackon): #This adds tackon (a Fraction object) to the original item (also a Fraction object) and returns that new item.
        orignumtor=self.numerator
        origdenom=self.denominator
        tacnumtor=tackon.numerator
        tacdenom=tackon.denominator
        self.numerator=(orignumtor*tacdenom)+(tacnumtor*origdenom)
        self.denominator=origdenom*tacdenom
        self.reduceFrac()
        return True
    def negatives(self):
        if self.numerator<0 and self.denominator < 0:
            self.numerator = abs(self.numerator)
            self.denominator = abs(self.denominator)
        return True
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
        

class Linear(CompoundClassyNew.Breaking): #USING LINEAR ALGEBRA TO BALANCE REACTIONS. TRY TO BALANCE THINGS NUMBER TWO!!! :O
    def __init__(self, reactants, products, name):
        CompoundClassyNew.Breaking.__init__(self, name)
        self.reactCOListODict = []
        self.prodCOListODict = []
        self.reactMg = {}
        self.prodMg = {}
        self.reactants = reactants
        self.products = products
        i = 0
        while i<len(self.reactants):
            #print("a")
            self.reactants[i] = self.firstIsNum(self.reactants[i])
            #print("Thing 1: " + self.reactants[i])
            self.makeDictionary([self.reactants[i], self.formatCompound(self.reactants[i])], True)
            i+=1
        i = 0
        while i<len(self.products):
            #print("b")
            self.products[i] = self.firstIsNum(self.products[i])
            #printr("Thing 2: " + self.products[i])
            self.makeDictionary([self.products[i], self.formatCompound(self.products[i])], False)
            i+=1
        #print("Reacts: " + str(self.reactants))
        #print("Prods: " + str(self.products))
        self.makeSuperDictionary(self.reactants, True)
        self.makeSuperDictionary(self.products, False)
        self.finalReacts = []
        self.finalProds = []
        self.thingy = ""
        self.compoundOrder = self.reactants + self.products
        self.matrix = []
        isFound = False
        for element in self.reactMg:
            tempList = []
            i = 0
            while i<len(self.reactCOListODict):
                #print("c")
                for key in self.reactCOListODict[i]:
                    if key==element: # we are looking for a specific element to fill the rows, example: C for Carbon
                        isFound = True
                        tempList.append(self.reactCOListODict[i][key])#puts the number of element in question found in the compound into the matrix
                if isFound == False:
                    tempList.append(0) # in case a compound doesnt contain this element
                isFound = False
                i+=1
            i = 0
            while i<len(self.prodCOListODict):
                #print("d")
                for key in self.prodCOListODict[i]:
                    if key==element: # we are looking for a specific element to fill the rows, example: C for Carbon
                        isFound = True
                        tempList.append(-1*self.prodCOListODict[i][key]) #puts the number of element in question found in the compound into the matrix
                        #The above is negative because we need to compare the systems of equations for reactants versus products. Products are negative.
                if isFound == False: 
                    tempList.append(0) # in case a compound doesnt contain this element
                isFound = False
                i+=1
            # obsolete : tempList.append(0) #This is to form an augmented matrix of all of our elements plus the extra zero before we find reduced form
            self.matrix.append(tempList)
                
    def formatCompound(self, compound): # Takes compounds and rewrites them. Mg3(PO4)2 becomes Mg3P2O8. Makes easier to parse.
        tempString = ""
        tempArray = []
        openParen = -1
        closeParen = -1
        originalIon = ""
        ion1 = ""
        ion = ""
        num = 1
        number = 1
        newCompound = ""
        if "(" in compound:
            openParen = compound.index("(")
            closeParen = compound.index(")")
            originalIon = compound[openParen:closeParen+2]
            ion1 = compound[openParen+1:closeParen]
            number = int(float(compound[closeParen+1]))
            for spot in ion1:
                if spot.isupper():
                    if ion1.index(spot)+1 < len(ion1):
                        if ion1[ion1.index(spot) + 1].islower():
                            if ion1.index(spot) + 2 < len(ion1):
                                if ion1[ion1.index(spot) + 2].isdigit():
                                    num = int(float(ion1[ion1.index(spot) + 2]))
                            ion = ion + ion1[ion1.index(spot):ion1.index(spot)+2] + str(num*number)
                        elif ion1[ion1.index(spot) + 1].isdigit():
                            num = int(float(ion1[ion1.index(spot) + 1]))
                            ion = ion + ion1[ion1.index(spot):ion1.index(spot)+1] + str(num*number)
                        else:
                            ion = ion + ion1[ion1.index(spot):ion1.index(spot)+1] + str(num*number)
                    else:
                        ion = ion + ion1[ion1.index(spot):ion1.index(spot)+2] + str(num*number)
            newCompound = compound.replace(originalIon, ion)
            return newCompound
        else:
            return compound
    def setKeyVals(self, compound): # Probably making dictionaries. :S *shrugs* We need it though. Important somehow.
        i = 0
        dictionary = {}
        key = ""
        value = 1
        while i<len(compound):
            #print("e")
            if compound[i].isupper():
                if i + 1 <len(compound):
                    if compound[i + 1].islower():
                        key = compound[i:i+2]
                    else:
                        key = compound[i]
                else:
                    key = compound[i]
            if key in dictionary:
                if len(key)==2:
                    if i+2 < len(compound):
                        if compound[i+2].isdigit():
                            if i+3<len(compound) and compound[i+3].isdigit():
                                value = dictionary[key] + int(float(compound[i+2:i+4]))
                            else:
                                value = dictionary[key] + int(float(compound[i+2]))
                        else:
                            value = dictionary[key] + 1
                    else:
                        value = dictionary[key] + 1
                else:
                    if i+1 < len(compound):
                        if compound[i+1].isdigit():
                            if i+2<len(compound) and compound[i+2].isdigit():
                                value = dictionary[key] + int(float(compound[i+1:i+3]))
                            else:
                                value = dictionary[key] + int(float(compound[i+1]))
                        else:
                            value = dictionary[key] + 1
                    else:
                        value = dictionary[key] + 1
            else:
                if len(key)==2:
                    if i+2<len(compound):
                        if compound[i+2].isdigit():
                            if i+3 < len(compound) and compound[i+3].isdigit():
                                value = int(float(compound[i+2:i+4]))
                            else:
                                value = int(float(compound[i+2]))
                else:
                    if i+1<len(compound):
                        if compound[i+1].isdigit():
                            if i+2<len(compound) and compound[i+2].isdigit():
                                value = int(float(compound[i+1:i+3]))
                            else:
                                value = int(float(compound[i+1]))
            if len(key)>0:
                dictionary[key] = value
            key = ""
            value = 1
            i = i + 1
        return dictionary
    def makeDictionary(self, compound, isReact): # Makes a dictionary of a specific compounds (including the individual element counts) and adds them to reactCOListODict or ProdCOListODict
        dictionary = self.setKeyVals(compound[1])
        dictionary["*" + compound[0]] = 1 #adds the name of a compound as a key and the coefficient (1 by default) as the value
        if isReact:
            self.reactCOListODict.append(dictionary)
        else:
            self.prodCOListODict.append(dictionary)
        return dictionary
    def makeSuperDictionary(self, unformattedList, isReact): # Makes the list of the total count of all the occurances of an element on either the prod or react side
            i = 0
            superString = ""
            superDict = {}
            while i < len(unformattedList):
                #print("f")
                superString = superString + self.formatCompound(unformattedList[i])
                i = i + 1
            superDict = self.setKeyVals(superString)
            if isReact:
                self.reactMg = superDict
            else:
                self.prodMg = superDict
            return superDict
    def addLists(self, list1, list2): #even though python thinks that subtracting individual list values from eachother is super dumb. We do what we want.
        # We are strong independent young coders and we dont need your imports!!
        i = 0
        newList = []
        if len(list1)==len(list2):
            while i<len(list1):
                #print("g")
                newList.append(list1[i]+list2[i])
                i+=1
        return newList
    def subtractLists(self, list1, list2): #even though python thinks that subtracting individual list values from eachother is super dumb. We do what we want.
        # We are strong independent young coders and we dont need your imports!!
        i = 0
        newList = []
        if len(list1)==len(list2):
            while i<len(list1):
                #print("h")
                newList.append(list1[i]-list2[i])
                i+=1
        return newList
    def reduceLists(self, reacts):
        coefficients = reacts
        i = 0
        while i<len(self.primes):
            #print("i")
            booly = True
            for thing in coefficients:
                if thing%self.primes[i]!=0:
                    booly = False
            if booly:
                b = 0
                while b<len(coefficients):
                    #print("j")
                    coefficients[b] = int(coefficients[b]/self.primes[i])
                    b = b + 1
            else:
                i = i + 1
        return coefficients
    def reduce(self, tempList): # reduces a list by all the common factors
        coefficients = tempList
        i = 0
        while i<len(self.primes):
            #print("k")
            booly = True
            count = 0
            for thing in coefficients:
                if thing == 0:
                    count+=1
                if thing%self.primes[i]!=0:
                    booly = False
            if count==len(coefficients):
                return coefficients
            if booly:
                b = 0
                while b<len(coefficients):
                    #print("l")
                    coefficients[b] = int(coefficients[b]/self.primes[i])
                    b = b + 1
            else:
                i = i + 1
        return coefficients  
    def adjust(self, tempMatrix, row1, row2, col): # multiplies row by the coeffs of the other row and does subtract. to make the second row =0 in spot 
        fSpotRow1 = tempMatrix[row1][col]
        fSpotRow2 = tempMatrix[row2][col]
        tempMatrix[row1] = [x * fSpotRow2 for x in tempMatrix[row1]] 
        tempMatrix[row2] = [x * fSpotRow1 for x in tempMatrix[row2]] 
        tempMatrix[row2] = self.subtractLists(tempMatrix[row2], tempMatrix[row1])
    def reducer(self, fakeMatrix): # makes the row echelon form from a matrix
        tempMatrix = fakeMatrix
        row = 0
        col = 0
        while row<len(tempMatrix) and col<len(tempMatrix[row]):
            #print("m")
            i = row + 1
            if tempMatrix[row][col]==0:
                while i<len(tempMatrix):
                    if tempMatrix[i][col]!=0:
                        tempMatrix[row] = self.addLists(tempMatrix[row], tempMatrix[i])
                        break
                    i+=1
            i = row + 1
            while i<len(tempMatrix):
                if tempMatrix[i][col]!=0:
                    self.adjust(tempMatrix,row,i,col)
                i+=1
            row+=1
            col+=1
            for thing in tempMatrix:
                thing = self.reduce(thing)
            #self.printMatrix(tempMatrix)
        self.matrix = tempMatrix
        return tempMatrix
    def leadingZeros(self, tempList):
        count = 0
        for thing in tempList:
            if thing==0:
                count+=1
            else:
                break
        return count
    def upper(self, matrixy):
        #print("UPPER")
        tempMatrix = matrixy
        leadingZerosPerRow = []
        for thing in tempMatrix:
            leadingZerosPerRow.append(self.leadingZeros(thing))
        row = len(tempMatrix)-1
        col = len(tempMatrix[row])-1
        while row>=0 and col>=0:
            #print("u1")
            i = row - 1
            if tempMatrix[row][col]==0:
                while i>=0:
                    #print("u2")
                    if tempMatrix[i][col]!=0:
                        row = i
                        break
                    i-=1
                #print("u5")
            i = row - 1
            while i>=0:
                #print("u3")
                if (tempMatrix[i][col]!=0 and leadingZerosPerRow[row]>leadingZerosPerRow[i]):                    
                    self.adjust(tempMatrix,row,i,col)
                i-=1
            #print("u4")
            row-=1
            col-=1
            for thing in tempMatrix:
               # print("upper reduced tempMatrix: " + str(tempMatrix))
                thing = self.reduce(thing)
            #self.printMatrix(tempMatrix)
        #print("TempMatrix: " + str(tempMatrix))
        self.matrix = tempMatrix
        return tempMatrix   
    def solveEquations(self, matrix): #method for solving reduced echelon system of equations for coefficient matrix
        coeffs = []
        tempMatrix = matrix
        for thing in self.compoundOrder:
            coeffs.append(0)
        i = len(tempMatrix)-1 #start from the bottom (now the whole team's here)
        booly = True
        while i>=0:
            #print("C")
            count = 0
            for thing in tempMatrix[i]:
                if thing != 0:
                    count+=1
            if count==2:
                booly = False
                break
            i-=1
        if booly:
            self.upper(tempMatrix)
            while i>=0:
                #print("D")
                count = 0
                for thing in tempMatrix[i]:
                    if thing != 0:
                        count+=1
                if count==2:
                    break
                i-=1
        k = 0
        valColList = [] #format: [value of coeff, index of column, value of coeff 2, index of column 2, etcetera]
        while k<len(matrix[i]):
            #print("E")
            if matrix[i][k]!=0:
                valColList.append(matrix[i][k])
                valColList.append(k)
            k+=1
        k = 0
        coeffs[valColList[1]] = Fraction(1,1)
        coeffs[valColList[3]] = Fraction(-valColList[0],valColList[2])
        if valColList[2]>valColList[0]:
            coeffs[valColList[3]] = Fraction(1,1)
            coeffs[valColList[1]] = Fraction(-valColList[2],valColList[0])
        coeffs[valColList[1]].negatives()
        coeffs[valColList[3]].negatives()
        tempMatrix.remove(tempMatrix[i])
        county = 0
        booly = False
        while len(tempMatrix)>0: #<-----
            #print("F")
            j = 0
            funLength = len(tempMatrix)
            while j<len(tempMatrix):
                #print("G")
                t = 0
                index = 0 # This is the column that the single unknown is found in
                count = 0 # counting number of column spots that are != to 0 and have not been solved already
                while t<len(tempMatrix[j]):
                    #print("H")
                    if tempMatrix[j][t] != 0 and coeffs[t] == 0:
                        index = t
                        count+=1
                    t+=1
                if count == 1:
                    county+=1
                    summy = Fraction(0,1) # this is the total amount of the number found in the row corresponding with a known multiplied by its coef value.
                    b = 0
                    while b<len(tempMatrix[j]):
                        #print("I")
                        summy.addition(Fraction(tempMatrix[j][b]*coeffs[b].numerator, coeffs[b].denominator))
                        #print("shmup")
                        b+=1
                    coeffs[index] = Fraction(-summy.numerator,summy.denominator*tempMatrix[j][index])
                    tempMatrix.remove(tempMatrix[j])
                elif count == 0:
                    tempMatrix.remove(tempMatrix[j])
                else:
                    j+=1
                if j==len(tempMatrix):
                    if county==0:
                        tempMatrix = self.reducer(tempMatrix)
                        #self.printMatrix(tempMatrix)
            if booly and funLength == len(tempMatrix):
                #print("ValColList: " + str(valColList))
                #print("Coeffs: " + str(coeffs))
                h = 0
                while h<len(coeffs):
                    if coeffs[h] == 0:
                        coeffs[h] = Fraction(0,1)
                    h+=1
                break
            if funLength == len(tempMatrix):
                tempMatrix = self.upper(tempMatrix)
                booly = True
        coeffs = self.noFractions(coeffs)
        coeffsFinal = []
        for thing in coeffs:
            coeffsFinal.append(int(thing.numerator))
        coeffsFinal = self.reduceLists(coeffsFinal)
        return coeffsFinal
    def noFractions(self, coeffs):
        biggestDenom = 1
        for thing in coeffs:
            if thing.denominator > biggestDenom:
                biggestDenom = thing.denominator
        while biggestDenom>1:
            s = 0
            while s<len(coeffs):
                coeffs[s].multiplyByWhole(biggestDenom)
                s+=1
            biggestDenom = 1
            for thing in coeffs:
                if thing.denominator > biggestDenom:
                    biggestDenom = thing.denominator
        return coeffs
    def finalSolveandReturn(self):
        #print("shmep")
        finalCoeffs = self.solveEquations(self.matrix)
        #print("shmip")
        #finalCoeffs = ["a", "b", "c", "d"]
        i = 0
        finalString = ""
        while i<len(self.reactants):
            #print("A")
            if finalCoeffs[i]==1:
                finalString = finalString + self.reactants[i]
            else:
                finalString = finalString + str(finalCoeffs[i]) + self.reactants[i]
            if i!=len(self.reactants)-1:
                finalString = finalString + " + "
            i+=1
        finalString = finalString + " -> "
        i = 0
        while i<len(self.products):
            #print("B")
            if finalCoeffs[i+len(self.reactants)]==1: 
                finalString = finalString + self.products[i]
            else:
                finalString = finalString + str(finalCoeffs[i+len(self.reactants)]) + self.products[i]
            if i!=len(self.products)-1:
                finalString = finalString + " + "
            i+=1
        return str(finalString)
    def printMatrix(self, matrix): #prints each line with a break in between
        for thing in matrix:
            print(thing)
def runner(self):
    run = True
    while run:
        shmeep = input("Enter the skeleton equation: ")
        if shmeep == '*':
            repeat = False
        print("")
        shmeep = shmeep.replace(" ", "")
        reactants = []
        products = []
        if shmeep.find("->")!=-1:
            listOThings = shmeep.split("->")
        react = listOThings[0].split('+')
        prod = listOThings[1].split('+')
        shmoop = Linear(react, prod, "")
        #print("shmoop")
        #shmoop.printMatrix(shmoop.matrix)
        shmoop.reducer(shmoop.matrix)
        shmoop.upper(shmoop.matrix)
        #shmoop.printMatrix(shmoop.matrix)
        #print("shmoop.2")
        shmep = shmoop.finalSolveandReturn()
        #print("shmeep")
        print("Your balanced equation is: " + shmep)
        print("")

    #Br2 + N2+ Cl2+ I2+H2+O2+F2-> HBr + HCl + NH4 + HI + H2O + HF
