import random
import math

class Compound():
        def __init__(self, name):
                self.isSoluble = False
                self.name = name
                self.alkali = {'Na':['Sodium', '+1'], 'K':['Potassium', '+1'], 'Li':['Lithium', '+1'], 'Rb':['Rubidium', '+1'], 'Fr':['Francium', '+1'], 'Cs':['Cesium', '+1']}
                self.over = {'NO3':['Nitrate', '-1'], 'NH4': ['Ammonium', '+1']}
                self.carphos = {'CO3': ['Carbonate', '-2'], 'PO4': ['Phosphate', '-3']}
                self.halo = {'Cl': ['Chlorine', '-1'], 'Br': ['Bromine', '-1'], 'I': ['Iodine', '-1']}
                self.sulfate = {'SO4': ['Sulfate', '-2']}
                self.hydroxide = {'OH':['Hydroxide', '-1']}
                self.sulfide = {'S':['Sulfide', '-2']}
                self.hydro = {'H':['Hydrogen', '+1']}
                self.tempDictionary = {'E':['Eeeeeeee', '+1']} #stores the dictionary being used
                self.tempIon = ""
                self.numberz =1
                self.chargies = [1,0,1,0]
                self.commonElements = ['H', 'N', 'O', 'F', 'Si', 'P', 'S', 'Cl', 'Ge', 'As', 'Se', 'Br', 'Sn', 'Sb', 'Te', 'I']
                self.uncommonElements = ['B', 'Na', 'Al', 'K', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Rb', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Ag', 'Cd', 'In', 'Cs', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Ti', 'Pb', 'Bi']     
                self.letters = {"0":"⁰","1":"¹","2":"²","3":"³","4":"⁴","5":"⁵","6":"⁶","7":"⁷","8":"⁸","9":"⁹","+":"⁺","-":"⁻"}	
                self.letters2 = {"0":"₀","1":"₁","2":"₂","3":"₃","4":"₄","5":"₅","6":"₆","7":"₇","8":"₈","9":"₉"}
                #self.allthethings = {'over': self.over, 'alkali': self.alkali, 'carphos': self.carphos, 'halo': self.halo, 'sulfate':self.sulfate, 'hydroxide':self.hydroxide, 'sulfide': self.sulfide}
        def getName(self):
                return self.name
        def haloCheck(self,compound):
                exceptions = {'Ag':['Silver','+1'],'Pb':['Lead(I)','+1'],'Hg2':['Mercury(I)','+2']}
                for key in exceptions:
                        if compound.find(key) != -1:
                              return False
                return True
        def sulfateCheck(self,compound):
                exceptions2 = {'Ba':['Barium','+2'],'Pb':['Lead(II)','+2'],'Ca':['Calcium','+2'], 'Ag': ['Silver', '+1'], 'Sr':['Strontium','+2']}
                for key in exceptions2:
                        if compound.find(key) != -1:
                              return False
                return True
        def hydroxideCheck(self,compound):
                exceptions3 = {'Ba':['Barium','+2'], 'Sr':['Strontium','+2']}
                for key in exceptions3:
                        if compound.find(key) != -1:
                              return True
                return False
        def sulfideCheck(self,compound):
                exceptions4 = {'Mg':['Magnesium', '+2'], 'Ba':['Barium','+2'], 'Ca':['Calcium','+2'], 'Sr':['Strontium','+2']}
                for key in exceptions4:
                        if compound.find(key) != -1:
                              return True
                return False
        def searchFinal(self,compound):
                for key in self.over:
                        if compound.find(key) != -1:
                                self.isSoluble = True
                                self.tempDictionary = self.over
                                self.tempIon = key
                                return self.isSoluble
                for key in self.alkali:
                        if compound.find(key) != -1:
                                self.isSoluble = True
                                self.tempDictionary = self.alkali
                                self.tempIon = key
                                return self.isSoluble
                for key in self.carphos:
                        if compound.find(key) != -1:
                                self.isSoluble = False
                                self.tempDictionary = self.carphos
                                self.tempIon = key
                                return self.isSoluble
                for key in self.halo:
                        if compound.find(key) != -1:
                                self.isSoluble = self.haloCheck(compound)
                                self.tempDictionary = self.halo
                                self.tempIon = key
                                return self.isSoluble
                for key in self.sulfate:
                        if compound.find(key) != -1:
                                self.isSoluble = self.sulfateCheck(compound)
                                self.tempDictionary = self.sulfate
                                self.tempIon = key
                                return self.isSoluble
                for key in self.hydroxide:
                        if compound.find(key) != -1:
                                self.isSoluble = self.hydroxideCheck(compound)
                                self.tempDictionary = self.hydroxide
                                self.tempIon = key
                                return self.isSoluble
                for key in self.sulfide:
                        if compound.find(key) != -1 and (compound.index(key)==len(compound)-1 or compound[compound.index(key)+1] != 'i'):                                    
                                self.isSoluble = self.sulfideCheck(compound)
                                self.tempDictionary = self.sulfide
                                self.tempIon = key
                                return self.isSoluble
                if self.firstIsNum(compound)[0] == 'H' and (self.firstIsNum(compound)[1].isdigit() or self.firstIsNum(compound)[1].isupper()):
                        self.tempDictionary = self.hydro
                        self.tempIon = 'H'
                        return self.hydrogen(compound)

class Breaking(Compound):
        def __init__(self, name):
                Compound.__init__(self,name)
                self.primes = [2, 3, 5, 7, 11, 13, 17]
        def firstIsNum(self, compound):
                num =""
                comp = ""
                if compound[0].isdigit():
                        if compound[1].isdigit():
                                num = compound[0:2]
                                comp = compound[2:]
                        else:
                                num = compound[0]
                                comp = compound[1:]
                        self.numberz = int(float(num))
                else:
                        comp = compound
                return comp
        def removeParentheses(self, ion, nummy, isIon1):
                tempString = ""
                tempArray = []
                if ion[0]=="(":
                        tempString = ion[1:]
                        tempArray = tempString.split(")")
                        newNum = nummy*int(float(tempArray[1]))
                        if isIon1:
                                self.chargies[0] = nummy*int(float(tempArray[1]))
                        else:
                                self.chargies[2] = nummy*int(float(tempArray[1]))
                        tempString = str(newNum)+tempArray[0]
                        return tempString
                else:
                    if ion[len(ion)-1].isdigit() and isIon1 and ion!="NH4":
                        self.chargies[0]=nummy*int(float(ion[len(ion)-1]))
                        return str(nummy*int(float(ion[len(ion)-1])))+ion[0:len(ion)-1]
                    elif ion[len(ion)-1].isdigit() and ion!="NH4":
                        if ion[:len(ion)-1] in self.commonElements:
                            self.chargies[2]=nummy*int(float(ion[len(ion)-1]))
                            return str(nummy*int(float(ion[len(ion)-1])))+ion[0:len(ion)-1]
                        elif ion[:len(ion)-1] in self.uncommonElements:
                            self.chargies[2]=nummy*int(float(ion[len(ion)-1]))
                            return str(nummy*int(float(ion[len(ion)-1])))+ion[0:len(ion)-1]
                        elif nummy!=1:
                            self.chargies[2]=nummy
                            return str(nummy) + ion
                        else:
                            return ion
                    elif nummy!=1:
                        if isIon1:
                                self.chargies[0] = nummy
                        else:
                                self.chargies[2]=nummy
                        return str(nummy) + ion
                    else:
                        return ion
        def breakUp(self, paramComp):
                broken = []
                ion1 =""
                ion2 = ""
                compound = self.firstIsNum(paramComp)
                charge = self.tempDictionary[self.tempIon][1]
                if(self.tempIon == 'NH4' or self.tempDictionary == self.alkali or self.tempIon == 'H'):
                        if compound[0]=="(":
                                self.chargies[1] = int(float(charge))
                                ion1 = self.removeParentheses(compound[0:compound.index(self.tempIon)+len(self.tempIon)+2],self.numberz, True)+self.superScript(charge)
                                ion2 = self.removeParentheses(compound[compound.index(self.tempIon)+len(self.tempIon)+2:],self.numberz, False)+self.findminiCharge()
                        else:
                                self.chargies[1] = int(float(charge))
                                ion1 = self.removeParentheses(compound[0:compound.index(self.tempIon)+len(self.tempIon)],self.numberz, True)+self.superScript(charge)
                                if compound.index(self.tempIon)+len(self.tempIon)>=len(compound):
                                        broken.append(self.removeParentheses(compound,self.numberz,True))
                                        return broken
                                if  compound[compound.index(self.tempIon)+len(self.tempIon)].isdigit():
                                    ion1 = self.removeParentheses(compound[0:compound.index(self.tempIon)+len(self.tempIon)+1],self.numberz, True)+self.superScript(charge)
                                    ion2 = self.removeParentheses(compound[compound.index(self.tempIon)+len(self.tempIon)+1:],self.numberz, False)+self.findminiCharge()
                                else:
                                    ion2 = self.removeParentheses(compound[compound.index(self.tempIon)+len(self.tempIon):],self.numberz, False)+self.findminiCharge()         
                else:
                        if compound.index(self.tempIon)==0:
                                if self.numberz != 1:
                                        broken.append(str(self.numberz) + compound)
                                else:
                                        broken.append(compound)
                                return broken
                        self.chargies[3] = int(float(charge))
                        if compound[compound.index(self.tempIon)-1] == "(":
                                ion2= self.removeParentheses(compound[compound.index(self.tempIon)-1:],self.numberz, False)+self.superScript(charge) 
                                ion1= self.removeParentheses(compound[:compound.index(self.tempIon)-1],self.numberz, True)+ self.findminiCharge()
                        else:
                                #COME BACK FIXIN A THING
                                ion2= self.removeParentheses(compound[compound.index(self.tempIon):],self.numberz, False)+self.superScript(charge)
                                ion1= self.removeParentheses(compound[:compound.index(self.tempIon)],self.numberz, True)+ self.findminiCharge()
                #print(ion2)
                broken.append(ion1)
                broken.append(ion2)
                return broken
        def findminiCharge(self):
                fullCharge=0
                coefL=self.chargies[0]
                coefR=self.chargies[2]
                miniL=self.chargies[1]
                miniR=self.chargies[3]
                chargeL = miniL * coefL
                chargeR= miniR*coefR
                #print("Lc: " + str(chargeL) + " Rc: " + str(chargeR))
                if chargeL==0:
                        miniL= int((fullCharge-chargeR)/coefL)
                        miniL=self.superScript(str(miniL))
                        return "⁺" + miniL
                elif chargeR==0:
                        miniR = int((fullCharge - chargeL)/coefR)
                        miniR=self.superScript(str(miniR))
                        return miniR
        def superScript(self,mini):
                i = 0
                for key in self.letters:
                    mini=mini.replace(key, self.letters[key])
                return mini
        def subScript(self, mini): #SKYLAR WAS HERE: Okay, I wrote a method that takes a compound a returns it where all
                #the numbers are in subscript (except for the coefficient obviously lol:P But the question is, do we use
                #this and if so where do we do it????? idk, get Malyn's opinion on this.
                i = 0
                mini2 = mini
                numb = ""
                if mini[0].isdigit():
                        if mini[1].isdigit():
                                numb = str(mini[:2])
                                mini2 = mini[2:]
                        else:
                                numb = str(mini[0])
                                mini2 = mini[1:]
                for key in self.letters2:
                    mini2 = mini2.replace(key, self.letters2[key])
                mini = numb + mini2
                return mini
        def hydrogen(self, compound):
                if ('C' in compound) and (len==compound.index('C')+1 or compound[compound.index('C')+1].isdigit() or compound[compound.index('C')+1].isupper()):
                        return False
                oxy = 0
                hydro = 0
                num = 0
                while num<len(compound):
                        if compound[num] == 'O':
                                if num+1==len(compound) or (compound[num+1].isdigit()==False):
                                        oxy+=1
                                else:
                                        oxy+= int(float(compound[num+1]))
                        elif compound[num] == 'H':
                                if compound[num+1].isdigit():
                                        hydro+= int(float(compound[num+1]))
                                else:
                                        hydro+=1
                        num+=1
                if oxy >= hydro + 2:
                        return True
                else:
                        return False
        def reduce(self, reacts, prods):
                tempList = reacts + prods
                coefficients = []
                for thing in tempList:
                        if thing[0].isdigit():
                                if thing[1].isdigit():
                                        coefficients.append(int(float(thing[0:2])))
                                        #print("1 time")
                                else:
                                        coefficients.append(int(float(thing[0])))
                                        #print("2 time")
                        else:
                                return [reacts, prods]
                i = 0
                while i<len(self.primes):
                        booly = True
                        for thing in coefficients:
                                if thing%self.primes[i]!=0:
                                        booly = False
                        if booly:
                                b = 0
                                while b<len(coefficients):
                                        coefficients[b] = int(coefficients[b]/self.primes[i])
                                        b = b + 1
                        else:
                                i = i + 1
                i = 0
                while i<len(reacts):
                        if reacts[i][0].isdigit():
                                if reacts[i][1].isdigit():
                                        if coefficients[i] == 1:
                                                reacts[i] = reacts[i][2:]
                                        else:
                                                reacts[i] = str(coefficients[i]) + reacts[i][2:]
                                else:
                                        if coefficients[i] == 1:
                                                reacts[i] = reacts[i][1:]
                                        else:
                                                reacts[i] = str(coefficients[i]) + reacts[i][1:]
                        else:
                                return [reacts, prods]
                        i += 1
                i = 0
                while i<len(prods):
                        if prods[i][0].isdigit():
                                if prods[i][1].isdigit():
                                        if coefficients[i+len(reacts)] == 1:
                                                prods[i] = prods[i][2:]
                                        else:
                                                prods[i] = str(coefficients[i+len(reacts)]) + prods[i][2:]
                                else:
                                        if coefficients[i+len(reacts)] == 1:
                                                prods[i] = prods[i][1:]
                                        else:
                                                prods[i] = str(coefficients[i+len(reacts)]) + prods[i][1:]
                        else:
                                return [reacts, prods]
                        i += 1
                return [reacts, prods]
                                                        
class Equation():
    def __init__(self, reacts, prods):
        self.reactants = reacts
        self.products = prods
    def getIon(self, ion):
        iontemp = ""
        if ion[0].isdigit():
                if ion[1].isdigit():
                        iontemp = ion[2:]
                else:
                        iontemp = ion[1:]
        else:
                iontemp = ion
        return iontemp
    def getNum(self, ion):
        num = 1
        if ion[0].isdigit():
                if ion[1].isdigit():
                        num = ion[:2]
                else:
                        num = ion[0]
        return int(float(num))
    def areSame(self, ion1, array):
        index = 0
        while index<len(array):
                if (self.getIon(ion1) == self.getIon(array[index])) and index != array.index(ion1):
                        ion2 = array[index]
                        num1 = self.getNum(ion1)
                        num2 = self.getNum(ion2)
                        ionA = self.getIon(ion1)
                        num3 = num1 + num2
                        ionC = str(num3) + ionA
                        array[array.index(ion1)] = ionC
                        array.remove(ion2)
                        return True
                index += 1
        index=0
        return False
    def cancelOut(self):
        r = 0
        p = 0
        co1 = 1
        co2 = 1
        coFinal = 0
        while r<len(self.reactants):
                while p<len(self.products) and r<len(self.reactants):
                        if self.getIon(self.reactants[r])==self.getIon(self.products[p]):
                                co1 = self.getNum(self.reactants[r])
                                co2 = self.getNum(self.products[p])
                                coFinal = str(abs(co1 - co2))
                                if coFinal=="1":
                                        coFinal = ""
                                if co2 > co1:
                                        self.reactants.remove(self.reactants[r])
                                        self.products[p] = coFinal + self.getIon(self.products[p])
                                        p=0

                                elif co1 == co2:
                                        self.reactants.remove(self.reactants[r])
                                        self.products.remove(self.products[p])
                                        p=0
                                else:
                                        self.products.remove(self.products[p])
                                        self.reactants[r] = coFinal + self.getIon(self.reactants[r])
                        else:
                                p+=1
                r+=1
                p=0
    def toString(self):
        for component in self.reactants[:-1]:
                print(component + " + ", end = "")
        if len(self.reactants) > 0:
                print(self.reactants[len(self.reactants)-1], end="")
        if len(self.products)>0:
                print(" -> ", end="")
        for component in self.products[:-1]:
                print(component + " + ", end = "")
        if len(self.products) > 0:
                print(self.products[len(self.products)-1])
class Balance(Breaking):
        def __init__(self, reactants, products, name):
                Breaking.__init__(self, name)
                self.reactCOListODict = []
                self.prodCOListODict = []
                self.reactMg = {}
                self.prodMg = {}
                self.reactants = reactants
                self.products = products
                self.failureIsSad = False
                self.failureIsSUPERSad = False
                self.failureIsSour = True
                i = 0
                while i<len(self.reactants): 
                        self.reactants[i] = self.firstIsNum(self.reactants[i])
                        #print("Thing 1: " + self.reactants[i])
                        self.makeDictionary([self.reactants[i], self.formatCompound(self.reactants[i])], True)
                        i+=1
                i = 0
                while i<len(self.products):
                        self.products[i] = self.firstIsNum(self.products[i])
                        #print("Thing 2: " + self.products[i])
                        self.makeDictionary([self.products[i], self.formatCompound(self.products[i])], False)
                        i+=1
                #print("Reacts: " + str(self.reactants))
                #print("Prods: " + str(self.products))
                self.makeSuperDictionary(self.reactants, True)
                self.makeSuperDictionary(self.products, False)
                self.finalReacts = []
                self.finalProds = []
                self.thingy = ""
        def formatCompound(self, compound):
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
        def setKeyVals(self, compound):
            i = 0
            dictionary = {}
            key = ""
            value = 1
            while i<len(compound):
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
        def makeDictionary(self, compound, isReact):
            dictionary = self.setKeyVals(compound[1])
            dictionary["*" + compound[0]] = 1 #adds the name of a compound as a key and the coefficient (1 by default) as the value
            if isReact:
                self.reactCOListODict.append(dictionary)
            else:
                self.prodCOListODict.append(dictionary)
            return dictionary
        def makeSuperDictionary(self, unformattedList, isReact):
                i = 0
                superString = ""
                superDict = {}
                while i < len(unformattedList):
                        superString = superString + self.formatCompound(unformattedList[i])
                        i = i + 1
                superDict = self.setKeyVals(superString)
                if isReact:
                        self.reactMg = superDict
                else:
                        self.prodMg = superDict
                #print("reacts: " + str(self.reactMg) + ", prods: " + str(self.prodMg))
                return superDict
        def shorterMethod(self, thing):
                #print("THE THING: " + thing)
                reactVal = 0
                prodVal = 0
                listy = []
                found= 0
                coef = {}
                left= True
                failSafeR = self.reactMg
                failSafeP = self.prodMg
                if thing[0]=="*":
                        return#????
                compsWithElement = []
                reactVal = self.reactMg[thing] #current values for this element aka how many are on the react
                prodVal = self.prodMg[thing] #or product side 
                if reactVal > prodVal:
                        #product coef needs adjustment
                        #print("Products bein' looked at")
                        listy = self.prodCOListODict
                        left = False
                elif reactVal < prodVal:
                        #print("Reacts bein' looked at")
                        #reactant coef needs adjustment
                        listy = self.reactCOListODict
                        left = True
                else:
                        return #nothing happens
                change = abs(prodVal-reactVal)
                for compound in listy: #for each compound in its respective List
                        if thing in compound: # if the key (element ex:c) is in this compound we need to use this compound
                                compsWithElement.append(compound)
                                  #must mess with this compound
                for dictionary in compsWithElement:
                        coefff = 1
                        for i in dictionary:
                                if i[0]=="*":
                                        coefff = dictionary[i]
                                        #print("COEFFF: " + str(coefff))
                        if change%(dictionary[thing])==0:
                                found=int(change/(dictionary[thing]))
                                # SHOULD FOUND take into acount coefff????????????? - Apparently Not SKYLAR WAS HERE
                                for i in dictionary:
                                        if i[0]=="*":
                                                coef[i[1:]]=found + dictionary[i]
                                                coeffff = coef[i[1:]]
                                                b = 0
                                                oldCoef = 1
                                                while b < len(listy):
                                                        if i in listy[b]:
                                                                oldCoef = listy[b][i]
                                                                listy[b][i] = found + dictionary[i]
                                                                break
                                                        b = b + 1
                                                if left:
                                                        self.reactCOListODict = listy
                                                        for i in self.reactCOListODict[b]:
                                                                if i[0]!="*":
                                                                        self.reactMg[i] = self.reactMg[i] - (oldCoef * self.reactCOListODict[b][i]) + (coeffff * self.reactCOListODict[b][i])
                                                else:
                                                        self.prodCOListODict = listy
                                                        for i in self.prodCOListODict[b]:
                                                                if i[0]!="*":
                                                                        self.prodMg[i] = self.prodMg[i] - (oldCoef * self.prodCOListODict[b][i]) + (coeffff * self.prodCOListODict[b][i])
                        if self.thingy==thing:
                                for key in dictionary:
                                        if key[0]!="*" and key!=thing:
                                                self.shorterMethod(key)
                #print("Reactant Dict: " + str(self.reactMg) + ", Product Dict: " + str(self.prodMg))
                #ADD A RESET FAILSAFE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!               
                        
        def longMethod(self):
                reactVal = 0
                prodVal = 0
                listy = []
                found= 0
                coef = {}
                left= True
                balanced = False
                while balanced!=True:
                        failSafeR = self.reactMg
                        failSafeP = self.prodMg
                        for thing in self.reactMg:
                                self.thingy = thing
                                self.shorterMethod(thing)
                        if self.reactMg== self.prodMg:
                                balanced = True
#if we ever get caught in an infinite loop, this will come in handy:
                        if failSafeR == self.reactMg and failSafeP == self.prodMg and balanced==False and self.failureIsSUPERSad == True:
                               balanced = True
                               #print("YOU CAN CRY NOW")
                        if failSafeR == self.reactMg and failSafeP == self.prodMg and balanced == False and self.failureIsSad == True:
                                if self.failureIsSour:
                                        self.failureIsSour = False
                                        #print("YOU ARE NOT A QUITTER!")
                                else:
                                        #print("LEASITJI COMMON MULTIPEL")
                                        self.failureIsSUPERSad = True
                                        count = 0
                                        officialKey = ""
                                        for key in self.reactMg:
                                                if self.reactMg[key] != self.prodMg[key]:
                                                        count = count + 1
                                                        if count!=1:
                                                                print("CRY NOW")
                                                        else:
                                                                officialKey = key
                                        if count==1:
                                                count2 = 0
                                                i = 0
                                                reactNum = 1
                                                prodNum = 1
                                                while i<len(self.reactCOListODict):
                                                        for key in self.reactCOListODict[i]:
                                                                if key==officialKey:
                                                                        count2 += 1
                                                                        if count2==1:
                                                                                reactNum = self.reactCOListODict[i][key]
                                                        i = i + 1
                                                count2 = 0
                                                i = 0
                                                while i<len(self.prodCOListODict):
                                                        for key in self.prodCOListODict[i]:
                                                                if key==officialKey:
                                                                        count2 += 1
                                                                        if count2==1:
                                                                                prodNum = self.prodCOListODict[i][key]
                                                        i = i + 1
                                                oldCoef = 1
                                                
                                                for dictionary in self.reactCOListODict:
                                                        if officialKey in dictionary:
                                                                for key in dictionary:
                                                                        if key[0]=="*":  
                                                                                #print("Before: " + str(dictionary))
                                                                                oldCoef = dictionary[key]
                                                                                dictionary[key] = prodNum
                                                                                #print("AFter: " + str(dictionary))
                                                                for key in dictionary:
                                                                        if key[0]!="*":
                                                                                self.reactMg[key] = self.reactMg[key] - (oldCoef * dictionary[key]) + (prodNum * dictionary[key])
                                                oldCoef = 1
                                                for dictionary in self.prodCOListODict:
                                                        if officialKey in dictionary:
                                                                for key in dictionary:
                                                                        if key[0]=="*":
                                                                                #print("Before: " + str(dictionary))
                                                                                oldCoef = dictionary[key]
                                                                                dictionary[key] = reactNum
                                                                                #print("AFter: " + str(dictionary))
                                                                for key in dictionary:
                                                                        if key[0]!="*":
                                                                                self.prodMg[key] = self.prodMg[key] - (oldCoef * dictionary[key]) + (reactNum * dictionary[key])
                                
                        if failSafeR == self.reactMg and failSafeP == self.prodMg and balanced==False and self.failureIsSad == False:
                                #print("DOUBlign EVERthiNG")
                                self.failureIsSad = True
                                k = 0
                                while k<len(self.reactCOListODict):
                                        for ast in self.reactCOListODict[k]:
                                                if ast[0]=="*":
                                                        self.reactCOListODict[k][ast]= self.reactCOListODict[k][ast]*2
                                        k = k + 1
                                k = 0
                                while k<len(self.prodCOListODict): 
                                        for ast in self.prodCOListODict[k]:
                                                if ast[0]=="*":
                                                        self.prodCOListODict[k][ast] = self.prodCOListODict[k][ast]*2
                                        k = k + 1
                                for keyy in self.reactMg:
                                        self.reactMg[keyy] = self.reactMg[keyy]*2
                                        self.prodMg[keyy] = self.prodMg[keyy]*2
                                #print("FAILSAFE")
#------------------------------------This Code is gonna take the results and stick them in a convenient list-------------------------
#and by that I mean so later, if we want to, we can use the results from this part of the program to make net ionics???????
#this just seems like it should be stored in a more convenient way than in the clunky dictionary situation we've got:)
                numz = ""
                for dictionary in self.reactCOListODict:
                        for i in dictionary:
                                if i[0]=="*":
                                        if dictionary[i]==1:
                                                numz = ""
                                        else:
                                                numz = str(dictionary[i])
                                        self.finalReacts.append(numz + i[1:])
                for dictionary in self.prodCOListODict:
                        for i in dictionary:
                                if i[0]=="*":
                                        if dictionary[i]==1:
                                                numz = ""
                                        else:
                                                numz = str(dictionary[i])
                                        self.finalProds.append(numz + i[1:])
                #print("REACTS: " + str(self.finalReacts) + ", PRODS: " + str(self.finalProds))
                #print(self.toString())
                reducedList = self.reduce(self.finalReacts, self.finalProds)
                self.finalReacts = reducedList[0]
                self.finalProds = reducedList[1]
                i = 0
                """while i<len(self.finalReacts):
                        self.finalReacts[i] = self.subScript(self.finalReacts[i])
                        i += 1
                        print("Reacts: the thing: " + thing)
                i = 0
                while i<len(self.finalProds):
                        self.finalProds[i] = self.subScript(self.finalProds[i])
                        print("Prods: the thing: " + thing)
                        i += 1"""
        def toString(self):
                numz = ""
                for item in self.finalReacts:
                        if self.finalReacts.index(item)!=len(self.finalReacts)-1:
                                print(item + " + ", end ="")
                        else:
                                print(item, end = "")
                print(" -> ", end="")
                for item in self.finalProds:
                        if self.finalProds.index(item)!=len(self.finalProds)-1:
                                print(item + " + ", end ="")
                        else:
                                print(item)
                
def runner():
        repeat = True
        while repeat:
                option = input("Would you like to balance an equation (B) or find a net ionic (N)? ")
                option = option.upper()
                comp = Compound("")
                shmeep = ""
                if option == "B":
                        shmeep = input("Enter the skeleton equation: ")
                elif option == "N":
                        shmeep = input("Enter the complete balanced equation: ")
                elif option == "*":
                        repeat = False
                else:
                        print("wrong form!")
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
                if option == "N":
                        print("This is the expanded form:")
                        if shmeep.find("->")!=-1:
                                for thing in react:
                                        comp = Breaking(thing)
                                        willitbreak = comp.searchFinal(thing)
                                        if willitbreak:
                                                broken = comp.breakUp(thing, True)
                                                for ion in broken:
                                                        reactants.append(ion)
                                        else:
                                                reactants.append(thing)
                                for thing in prod:
                                        comp = Breaking(thing)
                                        willitbreak = comp.searchFinal(thing)
                                        if willitbreak:
                                                broken = comp.breakUp(thing, True)
                                                for ion in broken:
                                                        products.append(ion)
                                        else:
                                                products.append(thing)
                                for component in reactants[:-1]:
                                        print(component + " + ", end = "")
                                print(reactants[len(reactants)-1], end="")
                                print(" -> ", end="")
                                for component in products[:-1]:
                                        print(component + " + ", end = "")
                                print(products[len(products)-1])
                        else:
                                compounds = shmeep.split("+")
                                for thing in compounds:
                                        comp = Breaking(thing)
                                        willitbreak = comp.searchFinal(thing)
                                        if willitbreak:
                                                broken = comp.breakUp(thing, True)
                                                for ion in broken:
                                                        reactants.append(ion)
                                        else:
                                                reactants.append(thing)
                                for component in reactants[:-1]:
                                        print(component + " + ", end = "")
                                print(reactants[len(reactants)-1])
                        equation = Equation(reactants, products)
                        item = 0
                        while item<len(equation.reactants):
                                booly = equation.areSame(equation.reactants[item], equation.reactants)
                                if booly == False:
                                        item += 1
                        item = 0
                        while item<len(equation.products):
                                booly = equation.areSame(equation.products[item], equation.products)
                                if booly == False:
                                        item += 1
                        equation.cancelOut()
                        print("")
                        print("This is your net ionic: ")
                        equation.toString()
                elif option == "B":
                        balance = Balance(react, prod, "balancer")
                        balance.longMethod()
                        print("This is your balanced equation: ")
                        balance.toString()
                        
                print("")
                print("")
#So we should probably add something that will the reduce the equations --- for example, if all components have a coefficient of 2, we can remove that. 
#ClO4? Is that a problem? Is it soluble? Or insoluble? Ask Mrs. Rosier.
#Mg3(PO4)2 + H2O + CO2 -> O2 + C6H12O6 + Mg3(PO4)2
