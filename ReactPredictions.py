import CompoundClassyNew

#CompoundClassyNew.runner()

class Predictor(CompoundClassyNew.Balance):
    def __init__(self, compounds):
        CompoundClassyNew.Balance.__init__(self, [],[],"")
        self.compounds = compounds
        self.products = []
        self.diatomics = ['Br', 'I', 'N', 'Cl', 'H', 'O', 'F']
        #self.tempDictionary = {'E':['Eeeeeeee', '+1']}
        #self.tempIon = ""
        #print(len(self.compounds))
    def isCompound(self, compound):
        count = 0
        for letter in compound:
            if letter.isupper():
                count+=1
        if count>1:
            return True # is a compound (possibly polyatomic!!)
        return False #is an element 
    def breakUp(self, compound):
        ion1 = ""
        ion2 =""
        if compound[0] == "(": #in case formatting is like (SOMETHING)BLAH
            if compound[compound.index(")")+1].isdigit():
                if compound[compound.index(")")+2].isdigit():
                    ion1 = compound[:compound.index(")")+3]
                    ion2 = compound[compound.index(")")+3:]
                else:
                    ion1 = compound[:compound.index(")")+2]
                    ion2 = compound[compound.index(")")+2:]
            else:
                ion1 = compound[:compound.index(")")+1]
                ion2 = compound[compound.index(")")+1:]
        else: #For when compound starts with a letter
            hitDigit = False
            if compound.find("NH4")>-1:
                #print("HEYYYYYY" + str(compound.find("NH4")))
                ion1 = compound[:3]
                ion2 = compound[3:]
                return [ion1, ion2]
            i = 1
            while i<len(compound):
                if compound[i].isupper():
                    if compound[i-1] == "(": #makes sure second half isnt a parenthesis
                        ion1 = compound[:i-1]
                        ion2 = compound[i-1:]
                    else: #finding where to split if normal NaCl or something
                        ion1 = compound[:i]
                        ion2 = compound[i:]
                    break
                i+=1
        #SKLYAR WAS HERE she added these two lines of code on 1/3 when malyn was at band
        #this is set up to remove the parentheses of the ions after they are broken up
        #ion1 = self.removeParentheses(ion1, 1, True)
        #ion2 = self.removeParentheses(ion2, 1, False)
        #-----------------------------------------------
        return [ion1, ion2]
    def diatomic(self, ionList):
        #print("diatomic called")
        i = 0
        while i<len(ionList):
            #print("1")
            k = 0
            count=0
            while k<len(ionList[i]):
                #print("2")
                if ionList[i][k].isalpha():
                    #print("3")
                    count+=1
                k+=1
            #print("count: " + str(count))
            for element in self.diatomics:
                #print("ion: " + ionList[i] + ", element: " +element)
                #print(ionList[i].find(element)>-1)
                #print(count==1)
                if ionList[i].find(element)>-1 and count==1:
                    #print("5")
                    ionList[i] = element+'2'
                elif ionList[i].find("Cl")>-1 and count==2:
                    ionList[i] = "Cl2"
                elif ionList[i].find("Br")>-1 and count==2:
                    ionList[i] = "Br2" 
            i+=1
        return ionList  
    def predictReaction(self):
        i = 0
        while i<len(self.compounds):
            self.compounds[i] = self.firstIsNum(self.compounds[i])
            i+=1
        if len(self.compounds) == 1 and self.isCompound(self.compounds[0]):
            self.products = self.decomposition()
        else:
            print("you messed up!")
    def decomposition(self):
        #print("Hey")
        compound = CompoundClassyNew.Compound(self.compounds[0])
        element = ""
        ionList = []
        if self.compounds[0].find("H2O")>-1:
            ionList = ["H2", "O2"]
        elif (self.compounds[0][0] == 'H' and not(self.compounds[0][1].islower()) and (self.compounds[0].find('O')>-1 and (self.compounds[0].find('Os')==-1))) or (self.compounds[0].find('OH')>-1):
            #print("ACID/BASE")
            i = 0
            while i<len(self.compounds[0]):
                if self.compounds[0][i] != 'H' and self.compounds[0][i] != 'O' and self.compounds[0][i].isupper():
                    if i+1!=len(self.compounds[0]) and self.compounds[0][i+1].islower():
                        element = self.compounds[0][i:i+2]
                    else:
                        element = self.compounds[0][i]
                i+=1
            tempComp = self.formatCompound(self.compounds[0])
            #print("TempComp: " + str(tempComp))
            #this code bit is going to figure out the charge of the non-hydrogen or oxygen element
            numH = 1
            numO = 1
            numMetal = 1
            metalCharge = 0
            oxide = ""
            i = 0
            while i<len(tempComp):
                if tempComp[i] == "H" and (i+1<len(tempComp) and not tempComp[i+1].islower()) and tempComp[i+1].isdigit():
                    if i+2<len(tempComp) and tempComp[i+2].isdigit():
                        numH = int(float(tempComp[i+1:i+3]))
                    else:
                        numH = int(float(tempComp[i+1]))
                elif tempComp[i] == "O" and (i+1<len(tempComp) and tempComp[i+1].isdigit()):
                    if i+2<len(tempComp) and tempComp[i+2].isdigit():
                        numO = int(float(tempComp[i+1:i+3]))
                    else:
                        numO = int(float(tempComp[i+1]))   
                i+=1
            if tempComp[tempComp.find(element)+len(element)].isdigit():
                numMetal = int(float(tempComp[tempComp.find(element)+len(element)]))
                if tempComp[tempComp.find(element)+len(element)+1].isdigit():
                    numMetal = int(float(tempComp[tempComp.find(element)+len(element):tempComp.find(element)+len(element)+2]))
            metalCharge = -(numH - 2*numO)/numMetal
            #print("metalcharge: " + str(metalCharge))
            oxide = element + "O"
            if metalCharge%2==0 and metalCharge>2:
                 oxide+= str(int(metalCharge/2))
            elif metalCharge%2==1:
                oxide= element + "2O"
                if metalCharge>1:
                    oxide+= str(int(metalCharge))
            ionList = [oxide, "H2O"]
            #working here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #there is more code to be added here: find out charges, etc etc to create oxide + water
        elif self.compounds[0].find('CO3')>-1:
            #print("CARBONATE")
            element = self.compounds[0][0:self.compounds[0].find('CO3')]
            element = element.replace('(','')
            num = ""
            if self.compounds[0].find(")")>-1:
                num = self.compounds[0][len(self.compounds[0])-1]
            ionList = [element+"O"+num, "CO2"]
        elif self.compounds[0].find('ClO3')>-1:
            #print("CHLORATE")
            element = self.compounds[0][0:self.compounds[0].find('ClO3')]
            element = element.replace('(',"")
            num =""
            if self.compounds[0].find(")")>-1:
                num = self.compounds[0][len(self.compounds[0])-1]
            ionList = [element+"Cl"+num, 'O2']
        else:
            #print("BINARY")
            ionList = self.breakUp(self.compounds[0])
            ionList = self.diatomic(ionList)
        #print("Heyy: " + str(ionList))
        return ionList
    def toString(self):
        string = ""
        for item in self.compounds:
            if self.compounds.index(item)!=len(self.compounds)-1:
                string = string + item + " + "
            else:
                string = string + item
            string = string + " -> "
        for item in self.products:
            if self.products.index(item)!=len(self.products)-1:
                string = string + item + " + "
            else:
                string = string + item
        return string
        

class Runner:
    def __init__(self):
        self.compounds = []
        self.runAgain = True
    def makeList(self, shmeep):
        if shmeep == "*":
            self.runAgain = False
        shmeep = shmeep.replace(" ", "")
        self.compounds = shmeep.split('+')
    def run(self, shmeep):
        self.makeList(shmeep)
        predictor = Predictor(self.compounds)
        predictor.predictReaction()
        print(predictor.toString())


        
