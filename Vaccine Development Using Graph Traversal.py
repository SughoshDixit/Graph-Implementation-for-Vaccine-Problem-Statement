#This class holds the data for a node of the graph
class Node:
    _vaccineName = ""
    _strainName = ""
    _neighbors = []
    #Constructor
    def __init__(self, vaccineName, strainName):
        self._vaccineName = vaccineName
        self._strainName = strainName
        self._neighbors = []
        
#This clas is the implementation of the Graph in the memory    
class Graph:
    
    #List of nodes of the graph
    nodes = []
    
    #This will help the function which will help to find the same node in the graph
    def Find_node(self,node):
        for x in self.nodes:
            if (x._vaccineName == node._vaccineName and x._strainName == node._strainName):
                return x
            else:
                return None
    
    #This function will help to find the list of strains for the given vaccine
    def Find_strain(self,vaccineName):
        strainSet = set()
        for x in self.nodes:
            if (x._vaccineName == vaccineName):
                strainSet.add(x._strainName)
                # return x
            for neighbor in x._neighbors:
                if (neighbor._vaccineName == vaccineName):
                    
                    strainSet.add(neighbor._strainName)
                    # return x
        return list(strainSet)
    
    #This function will help to find the list of vaccines for the given strain
    def Find_vaccine(self,strainname):
        vaccineSet = set()
        for x in self.nodes:
            if (x._strainName == strainname):
                vaccineSet.add(x._vaccineName)
                # return x
            for neighbor in x._neighbors:
                if (neighbor._strainName == strainname):
                    vaccineSet.add(neighbor._vaccineName)
                    # return x
        return list(vaccineSet)
        
    
    #This function will add a node to the graph, if it is a new node otherwise it will return the existing node from the graph 
    def add_node(self,vaccine_name, strain_name):
        node = Node(vaccine_name, strain_name) 

        existing_node = self.Find_node(node)
        if existing_node != None:
            return existing_node
        else:
            isAdded = False
            for currentNode in self.nodes:
                if currentNode._strainName == node._strainName:#if its related by strain
                    isAdded = True
                    currentNode._neighbors.append(node)
                    break
                
            if isAdded == False:
               self.nodes.append(node)
    
    #To return the list of all strains from the graph
    def GetStrains(self):
        strainSet = set()
        for currentNode in self.nodes:
            strainSet.add(currentNode._strainName)
        return strainSet
    
    #To return the list of all vaccines from the graph            
    def GetVaccines(self):
        vaccineSet = set()
        for currentNode in self.nodes:
            vaccineSet.add(currentNode._vaccineName)
            for neighbor in currentNode._neighbors:
                vaccineSet.add(neighbor._vaccineName)
        return vaccineSet
    
    #The function is used to find the common strain to the given pair of vaccines
    def Find_common_strain(self,vaccineA,vaccineB):
        strainSet1 = set()
        strainsA = self.Find_strain(vaccineA)
        strainsB = self.Find_strain(vaccineB)
        
        for x in strainsA:
            if x in strainsB:
                strainSet1.add(x)
        if len(strainSet1)!=0:
            return list(strainSet1)
        return None
    
    #The function is used to connect a third vaccine to the gioven pair of vaccines
    def VaccineConnect(self, vacA, vacB):
        strainSet1 = set()
        strainsA = self.Find_strain(vacA)
        strainsB = self.Find_strain(vacB)
        F_vacA = set()
        F_vacB = set()
        for x in strainsA:
            F_vacA.update(self.Find_vaccine(x))
        for y in strainsB:
            F_vacB.update(self.Find_vaccine(y))
        
        for x in F_vacA:
            if x in F_vacB:
                strainSet1.add(x)
        if len(strainSet1)!=0:
            return [x for x in strainSet1 if x != vacA and x != vacB ]
        
        
        return None

        
    

class IMMUNIZATION:
  VaccineList=[] #list containing vaccine and strains
  Edges=[[],[]] #matrix of edges/associations
  Vaccines=[]
  Strains=[]
  myGraph = Graph()
  fo = {}
  #constructor
  def __init__(self):
      self.fo = open('outputPS16.txt','w')
      self.fo.truncate()
  #destructor    
  def __del__(self):
      if(self.fo):
          self.fo.close()
      
  #To read the input file and create the graph
  def readInputfile(self, inputfile):
    f = open(inputfile)
    a = f.read().split('\n')
    a = [x.split(' / ') for x in a]
    s= set()
    v= set()
    
    for x in a:
      s.add(x[0])
      v.update(x[1:])

    self.Strains = [*s]
    self.Vaccines = [*v]
    
    
    for line in a:
        i = 0
        strainName = ""
        for element in line:
            if i > 0:
                self.myGraph.add_node(element, strainName)
            else:
                strainName = element
            i = i + 1
    f.close()
  
  #To write the content of the graph in the output file  
  def displayAll(self):
      if(len(self.myGraph.GetStrains())!=0 and (len(self.myGraph.GetStrains()))!=0):
          self.fo.write("\n--------Function displayAll--------\n")
          self.fo.write("Total no. of strains: %d \n" %(len(self.myGraph.GetStrains())))
          self.fo.write("Total no. of vaccines: %d \n" %(len(self.myGraph.GetVaccines())))
          self.fo.write('\n List of strains:\n')
          self.fo.write('------------------\n')
          self.fo.write('\n'.join(list(self.myGraph.GetStrains())))
          self.fo.write('\n List of vaccines:\n')
          self.fo.write('\n------------------\n')
          self.fo.write('\n'.join(list(self.myGraph.GetVaccines())))
      else:
          self.fo.write('\n No Strains or vaccines found')
             
  
  #To read the content of the prompt file
  def readPromptfile(self, inputfile1):
      # fo = open(inputfile1)
      # # a = f.read().split('\n')
      # ind = fo.read().find('displayStrains: ')
      # ok=fo.read()
      # print(ok)
      fo = open(inputfile1)
      a = fo.read().split('\n')
      a = [x.split(' : ') for x in a]
      # print(a)
      fo.close()
      return a
  
  #To write the strains associated to the vaccine in the output file
  def displayStrains(self, vaccine):
      v = self.myGraph.Find_strain(vaccine)
      if (len(v)!=0):
          self.fo.write('\n------Function displayStrains---------\n')
          self.fo.write('\nVaccine Name: %s\n'%(vaccine))
          self.fo.write('\nList Of strains:\n')
          self.fo.write('\n'.join(v))
      else:
          self.fo.write('\nThere is no strain that can be neutralized with this vaccine')
  
  #To write the vaccines that can neutralize the given strain in the output file
  def displayVaccine(self, strain):
      v = self.myGraph.Find_vaccine(strain)
      if(len(v)!=0):
          self.fo.write('\n-----Function displayVaccine---------\n')
          self.fo.write('\nStrain Name:%s\n' %(strain))
          
          self.fo.write('\nList Of Vaccines:\n')
          self.fo.write('\n'.join(v))
      else:
          self.fo.write('\nThere is no vaccine that can netraize this strain')
  
  #To find a common strain to a given pair of vaccines and write the result in the output file
  def commonStrain(self, vacA, vacB):
      v = self.myGraph.Find_common_strain(vacA,vacB)
      if(len(v)!=0):
          self.fo.write('\n-----Function commonStrain---------\n')
          self.fo.write('\nVaccineA:%s'%(vacA))
          self.fo.write('\nVaccineB:%s\n'%(vacB))
          self.fo.write('\n'.join(v))
      else:
          self.fo.write('\nThere is no common strain to the given input of vaccines')    
  
  #To find a third vaccine that is common to a given pair of vaccines and write the result in the output file
  def findVaccineConnect(self, vacA, vacB):
      v = self.myGraph.VaccineConnect(vacA,vacB)
      if(len(v)!=0):
          self.fo.write('\n-----Function findVaccineConnect---------\n')
          self.fo.write('\nVaccineA:%s'%(vacA))
          self.fo.write('\nVaccineB:%s\n'%(vacB))
          self.fo.write('\n'.join(v))
      else:
          self.fo.write('\nThere is no common vaccines that connect input of vaccines')
          
#initialize the class        
x = IMMUNIZATION()

x.readInputfile('inputPS16.txt')
x.displayAll()

a = x.readPromptfile('promptsPS16.txt')
displayStrains = [x[1] for x in a if x[0] == 'displayStrains'][0]
x.displayStrains(displayStrains)

listVaccine = [x[1] for x in a if x[0] == 'listVaccine'][0]
x.displayVaccine(listVaccine)

commonStrain = [x for x in a if x[0] == 'commonStrain'][0]
x.commonStrain(commonStrain[1], commonStrain[2])

commonConnect = [x for x in a if x[0] == 'findVaccineConnect'][0]
x.findVaccineConnect(commonConnect[1], commonConnect[2])