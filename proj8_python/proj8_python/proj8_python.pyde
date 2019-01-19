import random
import copy
from math import sqrt

lmbda = 30
mu = 10
lsComp = []
fitness = []
Generation = 0
maxFitness = 0

def setup():
  global lmbda, mu, lsComp, fitness, Generation, maxFitness, graphics, water, forest, farm, mountain, school, playground, cemetery, hospital, shrine_left, shrine_right, shrine_up, shrine_down, government
  size(1600,900)
  graphics = createGraphics(1600, 900)
  water = loadImage("water.jpg")
  forest = loadImage("forest.jpg")
  farm = loadImage("farm.jpg")
  mountain = loadImage("mountain.jpg")
  school = loadImage("school.png")
  playground = loadImage("play.png")
  cemetery = loadImage("skull.jpeg")
  hospital = loadImage("redcross.png")
  shrine_left = loadImage("temple_left.png")
  shrine_right = loadImage("temple_right.png")
  shrine_up = loadImage("temple_up.png")
  shrine_down = loadImage("temple_down.png")
  government = loadImage("govt.png")
  
  #initializing with random population
  while len(lsComp) < lmbda+mu:
    clear()
    background(222,184,135)
    lsComp.append(randomVillage())
    fitness.append(evaluateVillage(lsComp[-1]))

def drawMountain(x,y):
  smooth(8)
  image(mountain, x, y, 20, 20)
  
def drawForest(x,y):
  smooth(2)
  image(forest, x, y, 20, 20)
  
def drawWaterbody(x,y):
  smooth(4)
  image(water, x, y, 20, 20)
  
def drawFarmland(x,y):
  image(farm, x, y, 20, 20)

def drawHouse(x,y):
  fill(222,184,135) 
  noStroke()
  rect(x,y,20,20)
  fill(220,20,60)
  stroke(0,0,0)
  strokeWeight(4)
  triangle(x+10,y,x,y+10,x+20,y+10)
  fill(220,20,60)
  stroke(0,0,0)
  strokeWeight(4)
  rect(x+3,y+10,14,10)

def drawSchool(x,y):
  x1 = x - 10
  x2 = x + 30
  y1 = y - 10
  y2 = y + 30
  for i in range(11): 
    a = lerp(x1, x2, i/10.0)
    b = lerp(y1, y2, i/10.0)
    point(a, y1)
    point(x1, b)
    point(a, y2)
    point(x2, b)
  image(school, x, y, 20, 20)

def drawPlayground(x,y):
  image(playground, x, y, 20, 20)

def drawShrine(x,y, Dir, walled):
  if walled == True:
    x1 = x - 10
    x2 = x + 30
    y1 = y - 10
    y2 = y + 30
    for i in range(11): 
        a = lerp(x1, x2, i/10.0)
        b = lerp(y1, y2, i/10.0)
        point(a, y1)
        point(x1, b)
        point(a, y2)
        point(x2, b)

  if Dir == 0: #right
    image(shrine_right, x, y, 20, 20)
  if Dir == 1: #left
    image(shrine_left, x, y, 20, 20)
  if Dir == 2: #down
    image(shrine_down, x, y, 20, 20)
  if Dir == 3: #up
    image(shrine_up, x, y, 20, 20)

def drawCemetery(x,y):
  x1 = x - 30
  x2 = x + 50
  y1 = y - 30
  y2 = y + 50
  for i in range(11): 
    a = lerp(x1, x2, i/10.0)
    b = lerp(y1, y2, i/10.0)
    point(a, y1)
    point(x1, b)
    point(a, y2)
    point(x2, b)
  image(cemetery, x, y, 20, 20)

def drawHospital(x,y):
  x1 = x - 10
  x2 = x + 30
  y1 = y - 10
  y2 = y + 30
  for i in range(11): 
    a = lerp(x1, x2, i/10.0)
    b = lerp(y1, y2, i/10.0)
    point(a, y1)
    point(x1, b)
    point(a, y2)
    point(x2, b)
  image(hospital, x, y, 20, 20)

def drawGovernment(x,y):
  x1 = x - 10
  x2 = x + 30
  y1 = y - 10
  y2 = y + 30
  for i in range(11): 
    a = lerp(x1, x2, i/10.0)
    b = lerp(y1, y2, i/10.0)
    point(a, y1)
    point(x1, b)
    point(a, y2)
    point(x2, b)
  image(government, x, y, 20, 20)

def generateCoordinate():
  x_cord = random.randint(0,79)
  y_cord = random.randint(0,44)
  return [x_cord,y_cord]

def generateAdjacentCoordinate(list):
  pivot = random.choice(list)
  left = [pivot[0] - 1, pivot[1]]
  right = [pivot[0] + 1, pivot[1]]
  up = [pivot[0], pivot[1] + 1]
  down = [pivot[0], pivot[1] - 1]
  adjPoints = [left, right, up, down]
  cord = random.choice(adjPoints)
  return cord

def randomVillage():
  noComponent = []
  noComponent.append(random.randint(200,300)) #Mountain
  noComponent.append(random.randint(300,500)) #Forest
  noComponent.append(random.randint(150,250)) #Waterbody
  noComponent.append(random.randint(1,3)) #Cemetery
  noComponent.append(random.randint(4,6)) #Shrine
  noComponent.append(random.randint(2,4)) #Hospital
  noComponent.append(2) #Government
  noComponent.append(random.randint(2,3)) #School
  noComponent.append(random.randint(3,8)) #Playground
  noComponent.append(random.randint(350,600)) #Farmland
  noComponent.append(random.randint(150,220)) #House
  
  listAll = []
  listComponents = []
  listTerrain = []
  listPublicBuildings = []
  
  #Generating coordinates for terrains
  for i in range(0,3):
    listComponents.append([])
    count = random.randint(2,4)
    listCount = random.sample(range(noComponent[i]/(2*count),noComponent[i]/count), count - 1)
    listCount.append(noComponent[i] - sum(listCount))
    for j in range(len(listCount)):
        lsTemp = []
        while (len(lsTemp) != 1):
            rootComponent = generateCoordinate()
            nearestPoint = float('Inf')
            for k in listAll:
                nearestPoint = min(sqrt((rootComponent[0] - k[0])**2 + (rootComponent[1] - k[1])**2), nearestPoint)
            if nearestPoint > 8:
               listAll.append(rootComponent)
               listComponents[i].append(rootComponent)
               listTerrain.append(rootComponent)
               lsTemp.append(rootComponent)
        while (len(lsTemp) != listCount[j]):
            newComponent = generateAdjacentCoordinate(lsTemp)
            if newComponent not in listAll:
                listAll.append(newComponent)
                listComponents[i].append(newComponent)
                listTerrain.append(newComponent)
                lsTemp.append(newComponent)
  
  #Generating coordinates for cemetery
  i = 3
  listComponents.append([])
  while (len(listComponents[i]) != noComponent[i]):
    newComponent = generateCoordinate()
        
    #Implementing Constraint 2 in initial random population
    nearestComponent = float('Inf')
    for k in listAll:
        nearestComponent = min(sqrt((newComponent[0] - k[0])**2 + (newComponent[1] - k[1])**2), nearestComponent)

    if nearestComponent > sqrt(8):
        listAll.append(newComponent)
        listComponents[i].append(newComponent)
  
  #Ensuring every cemetery has a nearby shrine      
  cemShrine = []
  for k in listComponents[3]:
    newComponent = [80,45]
    while not (0 <= newComponent[0] < 80 and 0 <= newComponent[1] < 45):
        a = 0
        b = 0
        while a == b == 0:
            a = random.randint(-2, 2)
            b = random.randint(-2, 2)
        newComponent = [k[0]+a, k[1]+b]
    cemShrine.append(newComponent)

  #Generating coordinates for public buildings
  for i in range(4,8):
    listComponents.append([])
    if i == 4:
        listAll = listAll + cemShrine
        listComponents[i] = listComponents[i] + cemShrine
        listPublicBuildings = listPublicBuildings + cemShrine
    while (len(listComponents[i]) != noComponent[i]):
        newComponent = generateCoordinate()
        
        #Implementing Constraint 3 in initial random population
        nearestComponent = float('Inf')
        for k in listAll:
            nearestComponent = min(sqrt((newComponent[0] - k[0])**2 + (newComponent[1] - k[1])**2), nearestComponent)
        
        #Implementing Constraint 2 in initial random population
        nearestCemetery = float('Inf')
        for k in listComponents[3]:
            nearestCemetery = min(sqrt((newComponent[0] - k[0])**2 + (newComponent[1] - k[1])**2), nearestCemetery)

        if nearestComponent > sqrt(2) and nearestCemetery > sqrt(8):
            listAll.append(newComponent)
            listComponents[i].append(newComponent)
            listPublicBuildings.append(newComponent)
  
  #Generating coordinates for other buildings
  for i in range(8,11):
    listComponents.append([])
    while (len(listComponents[i]) != noComponent[i]):
        newComponent = generateCoordinate()
        
        #Implementing Constraint 1 in initial random population
        nearestTerrain = float('Inf')
        for k in listTerrain:
            nearestTerrain = min(sqrt((newComponent[0] - k[0])**2 + (newComponent[1] - k[1])**2), nearestTerrain)
        
        #Implementing Constraint 2 in initial random population
        nearestCemetery = float('Inf')
        for k in listComponents[3]:
            nearestCemetery = min(sqrt((newComponent[0] - k[0])**2 + (newComponent[1] - k[1])**2), nearestCemetery)
            
        #Implementing Constraint 3 in initial random population
        nearestPublicBuilding = float('Inf')
        for k in listPublicBuildings:
            nearestPublicBuilding = min(sqrt((newComponent[0] - k[0])**2 + (newComponent[1] - k[1])**2), nearestPublicBuilding)

        if newComponent not in listAll and nearestTerrain > sqrt(2) and nearestCemetery > sqrt(8) and nearestPublicBuilding > sqrt(2):
            listAll.append(newComponent)
            listComponents[i].append(newComponent)
  
  del listAll
  del listTerrain
  del listPublicBuildings
  del lsTemp
  return listComponents

def mutateVillage(parentVillage):
  listAll = parentVillage[0] + parentVillage[1] + parentVillage[2] + parentVillage[3]
  listTerrain = parentVillage[0] + parentVillage[1] + parentVillage[2]
  listPublicBuildings = parentVillage[4] + parentVillage[5] + parentVillage[6] + parentVillage[7]
  mutationChance = 1
  
  #Applying Gaussian Mutation by probability = 'mutationChance'
  
  #Ensuring every cemetery has a nearby shrine      
  cemShrine = []
  for k in range(len(parentVillage[3])):
    newComponent = [80,45]
    while not (0 <= newComponent[0] < 80 and 0 <= newComponent[1] < 45):
        a = 0
        b = 0
        while a == b == 0:
            a = random.randint(-2, 2)
            b = random.randint(-2, 2)
        newComponent = [parentVillage[3][k][0]+a, parentVillage[3][k][1]+b]
    parentVillage[4][k] = newComponent
    listAll.append(newComponent)
  
  #Mutating public buildings
  for i in range(4,9):
    for j in range(len(parentVillage[i])):
        listPublicBuildings = parentVillage[4] + parentVillage[5] + parentVillage[6] + parentVillage[7]
        if random.random() < mutationChance:
            mutated = False
            if (i == 4) and (j in range(len(parentVillage[3]))):
                mutated = True
                
            while mutated == False:
                newX = (parentVillage[i][j][0] + int(random.gauss(40, 8))) % 80 #mean = 40; std = 8
                newY = (parentVillage[i][j][1] + int(random.gauss(22.5, 4.5))) % 45 #mean = 22.5; std = 4.5
                newComponent = [newX,newY]
                
                #Implementing Constraint 3 in mutated population
                nearestComponent = float('Inf')
                for k in listAll:
                    nearestComponent = min(sqrt((newComponent[0] - k[0])**2 + (newComponent[1] - k[1])**2), nearestComponent)
                
                #Implementing Constraint 2 in mutated population
                nearestCemetery = float('Inf')
                for k in parentVillage[3]:
                    nearestCemetery = min(sqrt((newComponent[0] - k[0])**2 + (newComponent[1] - k[1])**2), nearestCemetery)
                
                if nearestComponent > sqrt(2) and nearestCemetery > sqrt(8):
                    listAll.append(newComponent)
                    parentVillage[i][j] = newComponent
                    mutated = True

  #Mutating other buildings              
  for i in range(9,11):
    for j in range(len(parentVillage[i])):
        if random.random() < mutationChance:
            mutated = False
            while mutated == False:
                newX = (parentVillage[i][j][0] + int(random.gauss(40, 8))) % 80 #mean = 40; std = 8
                newY = (parentVillage[i][j][1] + int(random.gauss(22.5, 4.5))) % 45 #mean = 22.5; std = 4.5
                newComponent = [newX,newY]
                
                #Implementing Constraint 1 in mutated population
                nearestTerrain = float('Inf')
                for k in listTerrain:
                    nearestTerrain = min(sqrt((newComponent[0] - k[0])**2 + (newComponent[1] - k[1])**2), nearestTerrain)
                
                #Implementing Constraint 2 in mutated population
                nearestCemetery = float('Inf')
                for k in parentVillage[3]:
                    nearestCemetery = min(sqrt((newComponent[0] - k[0])**2 + (newComponent[1] - k[1])**2), nearestCemetery)
                    
                #Implementing Constraint 3 in mutated population
                nearestPublicBuilding = float('Inf')
                for k in listPublicBuildings:
                    nearestPublicBuilding = min(sqrt((newComponent[0] - k[0])**2 + (newComponent[1] - k[1])**2), nearestPublicBuilding)
        
                if newComponent not in listAll and nearestTerrain > sqrt(2) and nearestCemetery > sqrt(8) and nearestPublicBuilding > sqrt(2):
                    listAll.append(newComponent)
                    parentVillage[i][j] = newComponent
                    mutated = True
  
  return parentVillage

def drawVillage(listComponents):
  
  for i in range(len(listComponents[0])):
    drawMountain(20*listComponents[0][i][0],20*listComponents[0][i][1])
    
  for i in range(len(listComponents[1])):
    drawForest(20*listComponents[1][i][0],20*listComponents[1][i][1])
    
  for i in range(len(listComponents[2])):
    drawWaterbody(20*listComponents[2][i][0],20*listComponents[2][i][1])
    
  for i in range(len(listComponents[3])):
    drawCemetery(20*listComponents[3][i][0],20*listComponents[3][i][1])
    
  for i in range(len(listComponents[4])):
    water_dist = []
    for k in range(len(listComponents[2])):
        water_dist.append(sqrt((listComponents[2][k][0] - listComponents[4][i][0])**2 + (listComponents[2][k][1] - listComponents[4][i][1])**2))
        least_dist_index = water_dist.index(min(water_dist))
        nearestWater = listComponents[2][least_dist_index]
        listDir = [listComponents[4][i][0] - nearestWater[0], nearestWater[0] - listComponents[4][i][0], listComponents[4][i][1] - nearestWater[1], nearestWater[1] - listComponents[4][i][1]]
        Dir = listDir.index(min(listDir))
    if i >= len(listComponents[3]):
        walled = True
    else:
        walled = False
    drawShrine(20*listComponents[4][i][0],20*listComponents[4][i][1], Dir, walled)
    
  for i in range(len(listComponents[5])):
    drawHospital(20*listComponents[5][i][0],20*listComponents[5][i][1])
    
  for i in range(len(listComponents[6])):
    drawGovernment(20*listComponents[6][i][0],20*listComponents[6][i][1])
    
  for i in range(len(listComponents[7])):
    drawSchool(20*listComponents[7][i][0],20*listComponents[7][i][1])
    
  for i in range(len(listComponents[8])):
    drawPlayground(20*listComponents[8][i][0],20*listComponents[8][i][1])
    
  for i in range(len(listComponents[9])):
    drawFarmland(20*listComponents[9][i][0],20*listComponents[9][i][1])
    
  for i in range(len(listComponents[10])):
    drawHouse(20*listComponents[10][i][0],20*listComponents[10][i][1])

def roulette_Wheel_Selection(lsComp, fitness):
  total_fitness = sum(fitness)
  flag = random.uniform(0, total_fitness)
  for i, ind_fitness in enumerate(fitness):
    total_fitness -= ind_fitness
    if total_fitness < flag:
        return lsComp[i]

#Houses near closest waterbody
def evaluationFunction1(listHouse,listWaterbody):
  dist = []
  for i in listHouse:
    temp = float('Inf')
    for j in listWaterbody:
        temp = min(sqrt((j[0] - i[0])**2 + (j[1] - i[1])**2),temp)
    dist.append(temp)
  avgDist = sum(dist)/len(dist)
  fitness = min(100,max(0,100 - (avgDist - 10)*7.5)) #min/max: so that fitness is always between 0% and 100%
  return fitness

#Houses near closest forest
def evaluationFunction2(listHouse,listForest):
  dist = []
  for i in listHouse:
    temp = float('Inf')
    for j in listForest:
        temp = min(sqrt((j[0] - i[0])**2 + (j[1] - i[1])**2),temp)
    dist.append(temp)
  avgDist = sum(dist)/len(dist)
  fitness = min(100,max(0,100 - (avgDist - 10)*7.5)) #min/max: so that fitness is always between 0% and 100%
  return fitness
    
#Farmlands near water
def evaluationFunction3(listFarmland, listWaterbody):
  dist = []
  for i in listFarmland:
    temp = float('Inf')
    for j in listWaterbody:
        temp = min(sqrt((j[0] - i[0])**2 + (j[1] - i[1])**2),temp)
    dist.append(temp)
  avgDist = sum(dist)/len(dist)
  fitness = min(100,max(0,100 - (avgDist - 10)*7.5)) #min/max: so that fitness is always between 0% and 100%
  return fitness

#Schools distant from each other
def evaluationFunction4(listSchool):
  dist = []
  for i in listSchool:
    for j in listSchool:
        dist.append(sqrt((j[0] - i[0])**2 + (j[1] - i[1])**2))
  avgDist = sum(dist)/len(dist)
  fitness = min(100,avgDist/32*100) #min: so that fitness is always below 100%
  return fitness

#Hospitals distant from each other
def evaluationFunction5(listHospital):
  dist = []
  for i in listHospital:
    for j in listHospital:
        dist.append(sqrt((j[0] - i[0])**2 + (j[1] - i[1])**2))
  avgDist = sum(dist)/len(dist)
  fitness = min(100,avgDist/32*100) #min: so that fitness is always below 100%
  return fitness
    
#The nearest playground to a school should be in reachable distance
def evaluationFunction6(listSchool, listPlayground):
  dist = []
  for i in listSchool:
    temp = float('Inf')
    for j in listPlayground:
        temp = min(sqrt((j[0] - i[0])**2 + (j[1] - i[1])**2),temp)
    dist.append(temp)
  avgDist = sum(dist)/len(dist)
  fitness =  min(100,max(0,100 - (avgDist - 8)*2.5)) #min/max: so that fitness is always between 0% and 100%
  return fitness

#Government buildings distant from each other
def evaluationFunction7(listGovernment):
  dist = []
  for i in listGovernment:
    for j in listGovernment:
        dist.append(sqrt((j[0] - i[0])**2 + (j[1] - i[1])**2))
  avgDist = sum(dist)/len(dist)
  fitness = min(100,avgDist/32*100) #min: so that fitness is always below 100%
  return fitness

#Government buildings close to nearest 50 houses
def evaluationFunction8(listGovernment, listHouse):
  dist = []
  dist_avg50 = []
  for i in range(len(listGovernment)):
      dist.append([])
      for j in listHouse:
          dist[i].append(sqrt((j[0] - listGovernment[i][0])**2 + (j[1] - listGovernment[i][1])**2))
      dist[i].sort()
      dist_avg50.append(sum(dist[i][:50])/50)
  avgDist = sum(dist_avg50)/len(dist_avg50)
  fitness = min(100,max(0,100 - (avgDist - 12)*10)) #min/max: so that fitness is always between 0% and 100%
  return fitness

#Maximize water bodies available per farmland
def evaluationFunction9(listFarmland, listWaterbody):
  fitness = min(100,(len(listWaterbody)/float(250))/(len(listFarmland)/float(600))*100)
  print fitness
  return fitness

#Maximize forests available per house
def evaluationFunction10(listHouse,listForest):
  fitness = min(100,(len(listForest)/float(500))/(len(listHouse)/float(220))*100)
  print fitness
  return fitness

def evaluateVillage(lsComp):
  useFitnessFunction = [1,2,3,4,5,6,7,8,9,10]
  lsFitness = []
  if 1 in useFitnessFunction:
    lsFitness.append(evaluationFunction1(lsComp[10],lsComp[2]))
  if 2 in useFitnessFunction:
    lsFitness.append(evaluationFunction2(lsComp[10],lsComp[1]))
  if 3 in useFitnessFunction:
    lsFitness.append(evaluationFunction3(lsComp[9],lsComp[2]))
  if 4 in useFitnessFunction:
    lsFitness.append(evaluationFunction4(lsComp[7]))
  if 5 in useFitnessFunction:
    lsFitness.append(evaluationFunction5(lsComp[5]))
  if 6 in useFitnessFunction:
    lsFitness.append(evaluationFunction6(lsComp[7],lsComp[8]))
  if 7 in useFitnessFunction:
    lsFitness.append(evaluationFunction7(lsComp[6]))
  if 8 in useFitnessFunction:
    lsFitness.append(evaluationFunction8(lsComp[6],lsComp[10]))
  if 9 in useFitnessFunction:
    lsFitness.append(evaluationFunction9(lsComp[9],lsComp[2]))
  if 10 in useFitnessFunction:
    lsFitness.append(evaluationFunction10(lsComp[10],lsComp[1]))
  
  convergance_rate = 0.95 #Toggle in neighborhood of 1 to control how slow or fast the algortihm converges to 90% fitness
  avg_fitness = convergance_rate*sum(lsFitness)/len(lsFitness)
  return avg_fitness

def draw():
  global lmbda, mu, lsComp, fitness, Generation, maxFitness
  Generation += 1
        
  while len(lsComp) < lmbda+mu:
    clear()
    background(222,184,135)
    parentVillage = copy.deepcopy(roulette_Wheel_Selection(lsComp, fitness)) #call by value
    lsComp.append(mutateVillage(parentVillage)) #randomly select a village from lmbda to mutate
    fitness.append(evaluateVillage(lsComp[-1]))
  
  combinedCompFitness = zip(fitness, lsComp)
  combinedCompFitness.sort(reverse = True)
  fitness,lsComp = zip(*combinedCompFitness)
  fitness = list(fitness[0:lmbda])
  lsComp = list(lsComp[0:lmbda])
  
  drawVillage(lsComp[0])

  maxFitness = fitness[0]
    
  font = createFont("Arial",32)
  textFont(font,32)
  textAlign(RIGHT)
  fill(255,255,255)
  text("Highest fitness in Generation " + str(Generation) + ": " + str(maxFitness) + "%",1600,900)
  
  if maxFitness > 90:
    noLoop()
