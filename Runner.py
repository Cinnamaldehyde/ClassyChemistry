import CompoundClassyNew
import LinearIsHard
import ReactPredictions

class Runner():
    def run(self):
        repeat = True
        while repeat:
                option = input("Would you like to balance an equation (B), find a net ionic (N), or predict a decomposition reaction (R)? ")
                option = option.upper()
                comp = CompoundClassyNew.Compound("")
                shmeep = ""
                if option == "B":
                        shmeep = input("Enter the skeleton equation: ")
                elif option == "N":
                        shmeep = input("Enter the complete balanced equation: ")
                elif option == "R":
                        shmeep = input("Enter the reactant for the decomposition reaction: ")
                elif option == "*":
                        repeat = False
                else:
                        print("wrong form!")
                        print("")
                        continue
                if shmeep == '*':
                        repeat = False
                print("")
                shmeep = shmeep.replace(" ", "")
                reactants = []
                products = []
                listOThings = []
                if shmeep.find("->")!=-1:
                        listOThings = shmeep.split("->")
                        react = listOThings[0].split('+')
                        prod = listOThings[1].split('+')
                elif shmeep.find("+")!=-1:
                        react = shmeep.split('+') #WE ARE HERE
                elif shmeep.find("+")==-1:
                        react = [shmeep]
                if option == "N":
                        print("This is the expanded form:")
                        if shmeep.find("->")!=-1:
                                for thing in react:
                                        comp = CompoundClassyNew.Breaking(thing)
                                        willitbreak = comp.searchFinal(thing)
                                        if willitbreak:
                                                broken = comp.breakUp(thing)
                                                for ion in broken:
                                                        reactants.append(ion)
                                        else:
                                                reactants.append(thing)
                                for thing in prod:
                                        comp = CompoundClassyNew.Breaking(thing)
                                        willitbreak = comp.searchFinal(thing)
                                        if willitbreak:
                                                broken = comp.breakUp(thing)
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
                                        comp = CompoundClassyNew.Breaking(thing)
                                        willitbreak = comp.searchFinal(thing)
                                        if willitbreak:
                                                broken = comp.breakUp(thing)
                                                for ion in broken:
                                                        reactants.append(ion)
                                        else:
                                                reactants.append(thing)
                                for component in reactants[:-1]:
                                        print(component + " + ", end = "")
                                print(reactants[len(reactants)-1])
                        equation = CompoundClassyNew.Equation(reactants, products)
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
                        shmoop = LinearIsHard.Linear(react, prod,"")
                        shmoop.reducer(shmoop.matrix)
                        shmoop.upper(shmoop.matrix)
                        #shmoop.printMatrix(shmoop.matrix)
                        #print("shmoop.2")
                        shmep = shmoop.finalSolveandReturn()
                        #print("shmeep")
                        print("Your balanced equation is: " + shmep)
                        print("")
                elif option == "R":
                        shmoop = ReactPredictions.Runner()
                        shmoop.run(react[0])
                        
                print("")
                print("")

shmelp = Runner()
shmelp.run()
