import random
import math
from operator import add 

def highestTwo(a, b, c):
	if a > c:
		if b > c:
			return a + b
		else:
			return a + c
	else:
		if b > a:
			return b + c
		else:
			return a + c

def worstOf(x, l):
	l.sort()
	total = 0
	for i in range(x):
		total += l[i]
	return total

def bestOf(x, l):
	l.sort()
	total = 0
	for i in range(x):
		total += l[-1-i]
	return total

def medianOf(l):
	l.sort()
	return l[1]

validDice = [4,6,8,10,12,20]
vanillaOddsDict = {}
vanillaConOddsDict = {}
vanillaCon2OddsDict = {}
oddsDict = {}
conOddsDict = {}
con2OddsDict = {}
evenCascadeOddsDict = {}
for i in range(0, len(validDice)):
	x = validDice[i]
	vanillaOdds = []
	vanillaConOdds = [0]
	vanillaCon2Odds = [0,0]
	odds = []
	conOdds = [0]
	con2Odds = [0,0]
	evenCascadeOdds = []
	
	for y in range(0,x):
		vanillaOdds.append(1/x)
	for y in range(1,x):
		vanillaConOdds.append(1/(x-1))
	for y in range(2,x):
		vanillaCon2Odds.append(1/(x-2))
		
	for y in range(0,x-1):
		odds.append(1/x)
	if i == 0:
		odds.append(1/x)
	else:
		odds.append(0)
		for z in oddsDict[validDice[i-1]]:
			odds.append(z/x)
	for y in range(1,x-1):
		conOdds.append(1/(x-1))
	if i == 0:
		conOdds.append(1/(x-1))
	else:
		conOdds.append(0)                
		for z in conOddsDict[validDice[i-1]]:
			conOdds.append(z/(x-1))
	for y in range(2,x-1):
		con2Odds.append(1/(x-2))
	if i == 0:
		con2Odds.append(1/(x-2))
	else:
		con2Odds.append(0)               
		for z in con2OddsDict[validDice[i-1]]:
			con2Odds.append(z/(x-2))

	if i == 0:
		for y in range(0,x):
			evenCascadeOdds.append(1/x)
	else:
		for y in range(0,len(odds)):
			evenCascadeOdds.append(0)
		for y in range(0,x):
			if y % 2 == 0:
				evenCascadeOdds[y] += 1/x
			else:
				for z in range(len(evenCascadeOddsDict[validDice[i-1]])):
					evenCascadeOdds[y+z+1] += evenCascadeOddsDict[validDice[i-1]][z]/x
				
	vanillaOddsDict[x] = vanillaOdds
	vanillaConOddsDict[x] = vanillaConOdds
	vanillaCon2OddsDict[x] = vanillaCon2Odds	
	oddsDict[x] = odds
	conOddsDict[x] = conOdds
	con2OddsDict[x] = con2Odds
	evenCascadeOddsDict[x] = evenCascadeOdds

monkOddsDict = {}
monkOddsDict[4] = vanillaOddsDict[4]
for i in range(1, len(validDice)):
	x = validDice[i]
	odds = [1/x, 0]
	for y in range(2,x-1):
		odds.append(1/x)
	odds.append(0)
	for j in range(len(monkOddsDict[validDice[i-1]])):
		z = monkOddsDict[validDice[i-1]][j]
		odds.append(z/x)
		odds[j+2] += (z/x)
	monkOddsDict[x] = odds

vanillaOddsDictBest1Of2 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	odds = []
	for x in range(0, len(d1_odds)):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d1_odds)):
			odds[bestOf(1,[x,y])] += d1_odds[x] * d1_odds[y]
	vanillaOddsDictBest1Of2[(d1)] = odds

vanillaOddsDictBest1Of3 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	odds = []
	for x in range(0, len(d1_odds)):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d1_odds)):
			for z in range(0, len(d1_odds)):    
				odds[bestOf(1,[x,y,z])] += d1_odds[x] * d1_odds[y] * d1_odds[z]
	vanillaOddsDictBest1Of3[(d1)] = odds

vanillaOddsDictBest1Of4 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	odds = []
	for x in range(0, len(d1_odds)):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d1_odds)):
			for z in range(0, len(d1_odds)):    
				for w in range(0, len(d1_odds)):   
					odds[bestOf(1,[x,y,z,w])] += d1_odds[x] * d1_odds[y] * d1_odds[z] * d1_odds[w]
	vanillaOddsDictBest1Of4[(d1)] = odds

vanillaOddsDictBest2Of3 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	odds = []
	for x in range(0, len(d1_odds) * 2):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d1_odds)):
			for z in range(0, len(d1_odds)):    
				odds[bestOf(2,[x,y,z])+1] += d1_odds[x] * d1_odds[y] * d1_odds[z]
	vanillaOddsDictBest2Of3[(d1)] = odds

vanillaOddsDictBest3Of4 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	odds = []
	for x in range(0, len(d1_odds) * 3):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d1_odds)):
			for z in range(0, len(d1_odds)):    
				for w in range(0, len(d1_odds)):
					odds[bestOf(3,[x,y,z,w])+2] += d1_odds[x] * d1_odds[y] * d1_odds[z] * d1_odds[w]
	vanillaOddsDictBest3Of4[(d1)] = odds

vanillaOddsDictWorst1Of2 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	odds = []
	for x in range(0, len(d1_odds)):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d1_odds)):
			odds[worstOf(1,[x,y])] += d1_odds[x] * d1_odds[y]
	vanillaOddsDictWorst1Of2[(d1)] = odds

vanillaOddsDictWorst1Of3 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	odds = []
	for x in range(0, len(d1_odds)):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d1_odds)):
			for z in range(0, len(d1_odds)): 
				odds[worstOf(1,[x,y,z])] += d1_odds[x] * d1_odds[y] * d1_odds[z]
	vanillaOddsDictWorst1Of3[(d1)] = odds
	
vanillaOddsDictWorst2Of3 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	odds = []
	for x in range(0, len(d1_odds) * 2):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d1_odds)):
			for z in range(0, len(d1_odds)):    
				odds[worstOf(2,[x,y,z])+1] += d1_odds[x] * d1_odds[y] * d1_odds[z]
	vanillaOddsDictWorst2Of3[(d1)] = odds

vanillaOddsDictWorst3Of4 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	odds = []
	for x in range(0, len(d1_odds) * 3):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d1_odds)):
			for z in range(0, len(d1_odds)):    
				for w in range(0, len(d1_odds)):
					odds[worstOf(3,[x,y,z,w])+2] += d1_odds[x] * d1_odds[y] * d1_odds[z] * d1_odds[w]
	vanillaOddsDictWorst3Of4[(d1)] = odds

vanillaOddsDictMedianOf3 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	odds = []
	for x in range(0, len(d1_odds)):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d1_odds)):
			for z in range(0, len(d1_odds)): 
				odds[medianOf([x,y,z])] += d1_odds[x] * d1_odds[y] * d1_odds[z]
	vanillaOddsDictMedianOf3[(d1)] = odds

vanillaOddsDictPlusD6 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	d2_odds = vanillaOddsDict[6]
	odds = []
	for x in range(0, len(d1_odds)+6):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			result = x+y+1
			odds[result] += d1_odds[x] * d2_odds[y]
	vanillaOddsDictPlusD6[(d1)] = odds

vanillaOddsDictMinusD6 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	d2_odds = vanillaOddsDict[6]
	odds = []
	for x in range(0, len(d1_odds)-1):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			result = x-y-1
			if result < 0:
				result = 0
			odds[result] += d1_odds[x] * d2_odds[y]
	vanillaOddsDictMinusD6[(d1)] = odds

oddsDictFocus6 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = oddsDict[d1]
	d2_odds = vanillaOddsDict[6]
	odds = []
	for x in range(0, max(len(d1_odds), len(d2_odds))):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			odds[max(x,y)] += d1_odds[x] * d2_odds[y]
	oddsDictFocus6[d1] = odds

oddsDictFocus6Bonus = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = oddsDict[d1]
	d2_odds = vanillaOddsDict[6]
	odds = []
	for x in range(0, max(len(d1_odds), len(d2_odds), d1*6)):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			result = x+y+1 if x <= d1 else x
			odds[result] += d1_odds[x] * d2_odds[y]
	oddsDictFocus6Bonus[d1] = odds

oddsDictFocus8 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = oddsDict[d1]
	d2_odds = vanillaOddsDict[8]
	odds = []
	for x in range(0, max(len(d1_odds), len(d2_odds))):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			odds[max(x,y)] += d1_odds[x] * d2_odds[y]
	oddsDictFocus8[d1] = odds

oddsDictFocus68 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = oddsDict[d1]
	d2_odds = vanillaOddsDict[6]
	d3_odds = vanillaOddsDict[8]
	odds = []
	for x in range(0, max(len(d1_odds), len(d2_odds), len(d3_odds))):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			for z in range(0, len(d3_odds)):
				odds[max(x,y,z)] += d1_odds[x] * d2_odds[y] * d3_odds[z]
	oddsDictFocus68[d1] = odds

oddsDictFocus810 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = oddsDict[d1]
	d2_odds = vanillaOddsDict[8]
	d2_odds = vanillaOddsDict[10]
	odds = []
	for x in range(0, max(len(d1_odds), len(d2_odds), len(d3_odds))):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			for z in range(0, len(d3_odds)):
				odds[max(x,y,z)] += d1_odds[x] * d2_odds[y] * d3_odds[z]
	oddsDictFocus810[d1] = odds

conOddsDictFocus6 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = conOddsDict[d1]
	d2_odds = vanillaConOddsDict[6]
	odds = []
	for x in range(0, max(len(d1_odds), len(d2_odds))):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			odds[max(x,y)] += d1_odds[x] * d2_odds[y]
	conOddsDictFocus6[d1] = odds

conOddsDictFocus8 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = conOddsDict[d1]
	d2_odds = vanillaConOddsDict[8]
	odds = []
	for x in range(0, max(len(d1_odds), len(d2_odds))):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			odds[max(x,y)] += d1_odds[x] * d2_odds[y]
	conOddsDictFocus8[d1] = odds

con2OddsDictFocus6 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = con2OddsDict[d1]
	d2_odds = vanillaCon2OddsDict[6]
	odds = []
	for x in range(0, max(len(d1_odds), len(d2_odds))):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			odds[max(x,y)] += d1_odds[x] * d2_odds[y]
	con2OddsDictFocus6[d1] = odds

con2OddsDictFocus8 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = con2OddsDict[d1]
	d2_odds = vanillaCon2OddsDict[8]
	odds = []
	for x in range(0, max(len(d1_odds), len(d2_odds))):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			odds[max(x,y)] += d1_odds[x] * d2_odds[y]
	con2OddsDictFocus8[d1] = odds	

oddsDictFocusC6 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = oddsDict[d1]
	d2_odds = oddsDict[6]
	odds = []
	for x in range(0, max(len(d1_odds), len(d2_odds))):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			odds[max(x,y)] += d1_odds[x] * d2_odds[y]
	oddsDictFocusC6[d1] = odds

oddsDictFocusC8 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = oddsDict[d1]
	d2_odds = oddsDict[8]
	odds = []
	for x in range(0, max(len(d1_odds), len(d2_odds))):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			odds[max(x,y)] += d1_odds[x] * d2_odds[y]
	oddsDictFocusC8[d1] = odds

vanillaOddsDict2 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	for j in range(0, i+1):
		d2 = validDice[j]
		d2_odds = vanillaOddsDict[d2]
		odds = []
		for x in range(0, len(d1_odds) + len(d2_odds)):
			odds.append(0)
		for x in range(0, len(d1_odds)):
			for y in range(0, len(d2_odds)):
				odds[x + y + 1] += d1_odds[x] * d2_odds[y]
		vanillaOddsDict2[(d1, d2)] = odds

vanillaOddsDict3 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = vanillaOddsDict[d1]
	for j in range(0, i+1):
		d2 = validDice[j]
		d2_odds = vanillaOddsDict[d2]
		for k in range(0, j+1):
			d3 = validDice[k]
			d3_odds = vanillaOddsDict[d3]
			odds = []
			for x in range(0, len(d1_odds) + len(d2_odds) + len(d3_odds)):
				odds.append(0)
			for x in range(0, len(d1_odds)):
				for y in range(0, len(d2_odds)):
					for z in range(0, len(d3_odds)):
						odds[x + y + z + 2] += d1_odds[x] * d2_odds[y] * d3_odds[z]
			vanillaOddsDict3[(d1, d2, d3)] = odds

oddsDict2 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = oddsDict[d1]
	for j in range(0, i+1):
		d2 = validDice[j]
		d2_odds = oddsDict[d2]
		odds = []
		for x in range(0, len(d1_odds) + len(d2_odds)):
			odds.append(0)
		for x in range(0, len(d1_odds)):
			for y in range(0, len(d2_odds)):
				odds[x + y + 1] += d1_odds[x] * d2_odds[y]
		oddsDict2[(d1, d2)] = odds

oddsDict2Focus6 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = oddsDict[d1]
	for j in range(0, i+1):
		d2 = validDice[j]
		d2_odds = oddsDict[d2]
		d3_odds = vanillaOddsDict[6]
		odds = []
		for x in range(0, highestTwo(len(d1_odds), len(d2_odds), len(d3_odds))):
			odds.append(0)
		for x in range(0, len(d1_odds)):
			for y in range(0, len(d2_odds)):
				for z in range(0, len(d3_odds)):
					odds[highestTwo(x,y,z) + 1] += d1_odds[x] * d2_odds[y] * d3_odds[z]
		oddsDict2Focus6[(d1, d2)] = odds

oddsDictPlusFocus6 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = oddsDict[d1]
	d2_odds = vanillaOddsDict[6]
	odds = []
	for x in range(0, len(d1_odds) + len(d2_odds)):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			odds[x + y + 1] += d1_odds[x] * d2_odds[y]
	oddsDictPlusFocus6[d1] = odds

oddsDictRageCascade = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = oddsDict[d1]
	d2_odds = vanillaOddsDict[6]
	odds = []
	for x in range(0, len(d1_odds) + len(d2_odds)):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			odds[x + y + 1] += d1_odds[x] * d2_odds[y]
	oddsDictPlusFocus6[d1] = odds

explodingLimit = 10
explodingOddsDict = {}
for i in range(0, len(validDice)):
	x = validDice[i]
	explodingOdds = []
	odds = []
	depth = 1
	while True:			
		for y in range(0,x-1):
			explodingOdds.append(math.pow(1/x, depth))
			if len(explodingOdds) >= explodingLimit:
				break;
		if len(explodingOdds) >= explodingLimit:
			break;
		explodingOdds.append(0)
		depth += 1
		if len(explodingOdds) >= explodingLimit:
			break;
	explodingOddsDict[x] = explodingOdds

explodingOddsDictFocus6 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = explodingOddsDict[d1]
	d2_odds = explodingOddsDict[6]
	odds = []
	for x in range(0, max(len(d1_odds), len(d2_odds))):
		odds.append(0)
	for x in range(0, len(d1_odds)):
		for y in range(0, len(d2_odds)):
			odds[max(x,y)] += d1_odds[x] * d2_odds[y]
	explodingOddsDictFocus6[d1] = odds

explodingOddsDict2 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = explodingOddsDict[d1]
	for j in range(0, i+1):
		d2 = validDice[j]
		d2_odds = explodingOddsDict[d2]
		odds = []
		for x in range(0, len(d1_odds) + len(d2_odds)):
			odds.append(0)
		for x in range(0, len(d1_odds)):
			for y in range(0, len(d2_odds)):
				odds[x + y + 1] += d1_odds[x] * d2_odds[y]
		explodingOddsDict2[(d1, d2)] = odds

explodingOddsDict2Focus6 = {}
for i in range(0, len(validDice)):
	d1 = validDice[i]
	d1_odds = explodingOddsDict[d1]
	for j in range(0, i+1):
		d2 = validDice[j]
		d2_odds = explodingOddsDict[d2]
		d3_odds = explodingOddsDict[6]
		odds = []
		for x in range(0, highestTwo(len(d1_odds), len(d2_odds), len(d3_odds))):
			odds.append(0)
		for x in range(0, len(d1_odds)):
			for y in range(0, len(d2_odds)):
				for z in range(0, len(d3_odds)):
					odds[highestTwo(x,y,z) + 1] += d1_odds[x] * d2_odds[y] * d3_odds[z]
		explodingOddsDict2Focus6[(d1, d2)] = odds


def fullExplode(dieSize, explodeRange, depthLimit, currentTotal=0, currentDepth=0):
	totalOdds = [0] * (dieSize * (depthLimit + 1))
	for i in range(0,dieSize):
		if currentDepth < depthLimit and i > (dieSize - explodeRange - 1):
			#explode
			explodedOdds = fullExplode(dieSize, explodeRange, depthLimit, currentTotal+i+1, currentDepth+1)
			totalOdds = list(map(add, totalOdds, explodedOdds))
			
		else:
			#no explode
			totalOdds[currentTotal+i] += math.pow(1/dieSize, currentDepth+1)
	return totalOdds

	
stupid12OddsDict = {}
for i in range(0, 6):        
	stupid12OddsDict[i] = fullExplode(12, i, 2)

doubleStupid12OddsDict = {}
for i in range(0, 6):
	doubleStupid12OddsDict[i] = [0] * (2*len(stupid12OddsDict[i]) + 1)
	for x in range(len(stupid12OddsDict[i])):
		for y in range(len(stupid12OddsDict[i])):
			doubleStupid12OddsDict[i][x+y+1] += stupid12OddsDict[i][x] * stupid12OddsDict[i][y]
	
targetList = range(1,25) ##[4,6,8,10,12,16,20]
poolTargetList = range(0,21)
	
def oddsPrettyPrintHeaders(pool = False):
	s = "{:>15}{:>6}{:>4}{:>4}{:>6}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>8}"
	args = ["DIE", "AVG", "MIN", "MAX", "S-DEV", "10%", "25%", "50%", "75%", "90%", "98%", "MISS"]
	if pool:
		for x in poolTargetList:
			s += "{:>8}"
			args.append("HIT-" + str(x))
	else:
		for x in targetList:
			s += "{:>8}"
			args.append("HIT-" + str(x))
	print(s.format(*args))

def oddsPrettyPrint(label, odds, pool = False):
	average = 0
	b = 1
	myTargetList = targetList
	if pool:
		b = 0
		myTargetList = poolTargetList
	for i in range(len(odds)):
		average += (i + b) * odds[i]
		
	i = 0
	while odds[i] == 0:
		i += 1
	minimum = i + b
	
	i = len(odds) - 1
	while odds[i] == 0:
		i -= 1
	maximum = i + b

	square_mean = 0
	for i in range(len(odds)):
		square_mean += (i + b - average) * (i + b - average) * odds[i]
	std_dev = math.sqrt(square_mean)

	p_10 = -1
	p_25 = -1
	p_50 = -1
	p_75 = -1
	p_90 = -1
	p_98 = -1
	runningTotalOdds = 0
	for i in range(len(odds)):
		runningTotalOdds += odds[i]
		if p_10 < 0 and (runningTotalOdds >= 0.10 or i == len(odds) - 1):
			p_10 = i + b
		if p_25 < 0 and (runningTotalOdds >= 0.25 or i == len(odds) - 1):
			p_25 = i + b
		if p_50 < 0 and (runningTotalOdds >= 0.50 or i == len(odds) - 1):
			p_50 = i + b
		if p_75 < 0 and (runningTotalOdds >= 0.75 or i == len(odds) - 1):
			p_75 = i + b
		if p_90 < 0 and (runningTotalOdds >= 0.90 or i == len(odds) - 1):
			p_90 = i + b
		if p_98 < 0 and (runningTotalOdds >= 0.98 or i == len(odds) - 1):
			p_98 = i + b

	reverseCumulativeOdds = []
	for i in range(max(len(odds), myTargetList[-1])):
		reverseCumulativeOdds.append(0)
	if len(odds) >= len(myTargetList):
		reverseCumulativeOdds[-1] = odds[-1]
	for i in range(len(reverseCumulativeOdds)-2, -1, -1):
		reverseCumulativeOdds[i] = reverseCumulativeOdds[i+1]
		if i < len(odds):
			reverseCumulativeOdds[i] += odds[i]			
	correction = 1 - reverseCumulativeOdds[0]
	for i in range(len(reverseCumulativeOdds)):
		reverseCumulativeOdds[i] += correction
		
	miss  = odds[minimum - 1]
	
	s = "{:>15}{:>6.2f}{:>4}{:>4}{:>6.2f}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>8.2%}"
	args = [label, average, minimum, maximum, std_dev, p_10, p_25, p_50, p_75, p_90, p_98, miss]
	for x in myTargetList:
		s += "{:>8.2%}"
		args.append(reverseCumulativeOdds[x-1])
	print(s.format(*args))




def roll():
	print(random.randint(1,6))

def cascadeRoll(x):
	o = random.randint(1,x)
	if x == o and x in validDice and x != 4:
		return x + cascadeRoll(validDice[validDice.index(x)-1])
	return o;

def bestOf(inputs, bestCount, target = -1, printResult = True, printComponents = False):
	rolls = list(map(lambda x: cascadeRoll(x), inputs))
	if printComponents:
		for roll in rolls:
			print('{0:2d}'.format(roll), end=' ')
		print('', end='  ')
	rolls.sort(reverse=True)
	result = 0
	for i in range(bestCount):
		result += rolls[i]
	successCount = 0
	if target > -1:
		successCount = 1 + (result - target ) // 4
	if printResult:
		print('{0:2d}'.format(result), end=' ')
		if target != -1:
			if result >= target:
				print('Success {0:1d}'.format(successCount), end=' ')
			else:
				print('Failure    ', end=' ')
	if printComponents or printResult:
		print()
	if target > -1:
		return successCount
	else:
		return result


log = []
for i in range(10):
	log.append(bestOf([4,4,6],2,8,False,False))

	anySuccess = 0
	for e in log:
		if e > 0:
			anySuccess += 1

d6PoolOddsDict = { 1: [1-2.0/6, 2.0/6] }
for i in range(2,21):
	r = d6PoolOddsDict[1][1]
	prev = d6PoolOddsDict[i-1]
	new = [prev[0]*(1-r)]
	for j in range(1,len(prev)):
		new.append(prev[j]*(1-r) + prev[j-1]*r)
	new.append(prev[-1]*r)
	d6PoolOddsDict[i] = new

d10PoolOddsDict = { 1: [1-3.0/10, 3.0/10] }
for i in range(2,21):
	r = d10PoolOddsDict[1][1]
	prev = d10PoolOddsDict[i-1]
	new = [prev[0]*(1-r)]
	for j in range(1,len(prev)):
		new.append(prev[j]*(1-r) + prev[j-1]*r)
	new.append(prev[-1]*r)
	d10PoolOddsDict[i] = new

			
oddsPrettyPrintHeaders()

##oddsPrettyPrint("vd4", vanillaOddsDict[4])
##oddsPrettyPrint("vd6", vanillaOddsDict[6])
##oddsPrettyPrint("vd8", vanillaOddsDict[8])
##oddsPrettyPrint("vd10", vanillaOddsDict[10])
##oddsPrettyPrint("vd12", vanillaOddsDict[12])
##oddsPrettyPrint("vd20", vanillaOddsDict[20])
##
##print()
##
##oddsPrettyPrint("md4", monkOddsDict[4])
##oddsPrettyPrint("md6", monkOddsDict[6])
##oddsPrettyPrint("md8", monkOddsDict[8])
##oddsPrettyPrint("md10", monkOddsDict[10])
##oddsPrettyPrint("md12", monkOddsDict[12])
##oddsPrettyPrint("md20", monkOddsDict[20])
##
##print()
##
##oddsPrettyPrint("vd4,b1/2", vanillaOddsDictBest1Of2[4])
##oddsPrettyPrint("vd6,b1/2", vanillaOddsDictBest1Of2[6])
##oddsPrettyPrint("vd8,b1/2", vanillaOddsDictBest1Of2[8])
##oddsPrettyPrint("vd10,b1/2", vanillaOddsDictBest1Of2[10])
##oddsPrettyPrint("vd12,b1/2", vanillaOddsDictBest1Of2[12])
##oddsPrettyPrint("vd20,b1/2", vanillaOddsDictBest1Of2[20])
##
##print()
##
##oddsPrettyPrint("vd4,b1/3", vanillaOddsDictBest1Of3[4])
##oddsPrettyPrint("vd6,b1/3", vanillaOddsDictBest1Of3[6])
##oddsPrettyPrint("vd8,b1/3", vanillaOddsDictBest1Of3[8])
##oddsPrettyPrint("vd10,b1/3", vanillaOddsDictBest1Of3[10])
##oddsPrettyPrint("vd12,b1/3", vanillaOddsDictBest1Of3[12])
##oddsPrettyPrint("vd20,b1/3", vanillaOddsDictBest1Of3[20])
##
##print()
##
##oddsPrettyPrint("vd4,b1/4", vanillaOddsDictBest1Of4[4])
##oddsPrettyPrint("vd6,b1/4", vanillaOddsDictBest1Of4[6])
##oddsPrettyPrint("vd8,b1/4", vanillaOddsDictBest1Of4[8])
##oddsPrettyPrint("vd10,b1/4", vanillaOddsDictBest1Of4[10])
##oddsPrettyPrint("vd12,b1/4", vanillaOddsDictBest1Of4[12])
##oddsPrettyPrint("vd20,b1/4", vanillaOddsDictBest1Of4[20])
##
##print()
##
##oddsPrettyPrint("vd4,b2/3", vanillaOddsDictBest2Of3[4])
##oddsPrettyPrint("vd6,b2/3", vanillaOddsDictBest2Of3[6])
##oddsPrettyPrint("vd8,b2/3", vanillaOddsDictBest2Of3[8])
##oddsPrettyPrint("vd10,b2/3", vanillaOddsDictBest2Of3[10])
##oddsPrettyPrint("vd12,b2/3", vanillaOddsDictBest2Of3[12])
##oddsPrettyPrint("vd20,b2/3", vanillaOddsDictBest2Of3[20])
##
##print()
##
##oddsPrettyPrint("vd4,b3/4", vanillaOddsDictBest3Of4[4])
##oddsPrettyPrint("vd6,b3/4", vanillaOddsDictBest3Of4[6])
##oddsPrettyPrint("vd8,b3/4", vanillaOddsDictBest3Of4[8])
##oddsPrettyPrint("vd10,b3/4", vanillaOddsDictBest3Of4[10])
##oddsPrettyPrint("vd12,b3/4", vanillaOddsDictBest3Of4[12])
##oddsPrettyPrint("vd20,b3/4", vanillaOddsDictBest3Of4[20])
##
##print()
##
##oddsPrettyPrint("vd4,w1/2", vanillaOddsDictWorst1Of2[4])
##oddsPrettyPrint("vd6,w1/2", vanillaOddsDictWorst1Of2[6])
##oddsPrettyPrint("vd8,w1/2", vanillaOddsDictWorst1Of2[8])
##oddsPrettyPrint("vd10,w1/2", vanillaOddsDictWorst1Of2[10])
##oddsPrettyPrint("vd12,w1/2", vanillaOddsDictWorst1Of2[12])
##oddsPrettyPrint("vd20,w1/2", vanillaOddsDictWorst1Of2[20])
##
##print()

##oddsPrettyPrint("vd4,w1/3", vanillaOddsDictWorst1Of3[4])
##oddsPrettyPrint("vd6,w1/3", vanillaOddsDictWorst1Of3[6])
##oddsPrettyPrint("vd8,w1/3", vanillaOddsDictWorst1Of3[8])
##oddsPrettyPrint("vd10,w1/3", vanillaOddsDictWorst1Of3[10])
##oddsPrettyPrint("vd12,w1/3", vanillaOddsDictWorst1Of3[12])
##oddsPrettyPrint("vd20,w1/3", vanillaOddsDictWorst1Of3[20])
##
##print()
##
##oddsPrettyPrint("vd4,w2/3", vanillaOddsDictWorst2Of3[4])
##oddsPrettyPrint("vd6,w2/3", vanillaOddsDictWorst2Of3[6])
##oddsPrettyPrint("vd8,w2/3", vanillaOddsDictWorst2Of3[8])
##oddsPrettyPrint("vd10,w2/3", vanillaOddsDictWorst2Of3[10])
##oddsPrettyPrint("vd12,w2/3", vanillaOddsDictWorst2Of3[12])
##oddsPrettyPrint("vd20,w2/3", vanillaOddsDictWorst2Of3[20])
##
##print()
##
##oddsPrettyPrint("vd4,w3/4", vanillaOddsDictWorst3Of4[4])
##oddsPrettyPrint("vd6,w3/4", vanillaOddsDictWorst3Of4[6])
##oddsPrettyPrint("vd8,w3/4", vanillaOddsDictWorst3Of4[8])
##oddsPrettyPrint("vd10,w3/4", vanillaOddsDictWorst3Of4[10])
##oddsPrettyPrint("vd12,w3/4", vanillaOddsDictWorst3Of4[12])
##oddsPrettyPrint("vd20,w3/4", vanillaOddsDictWorst3Of4[20])
##
##print()
##
##oddsPrettyPrint("vd4,m/3", vanillaOddsDictMedianOf3[4])
##oddsPrettyPrint("vd6,m/3", vanillaOddsDictMedianOf3[6])
##oddsPrettyPrint("vd8,m/3", vanillaOddsDictMedianOf3[8])
##oddsPrettyPrint("vd10,m/3", vanillaOddsDictMedianOf3[10])
##oddsPrettyPrint("vd12,m/3", vanillaOddsDictMedianOf3[12])
##oddsPrettyPrint("vd20,m/3", vanillaOddsDictMedianOf3[20])
##
##print()

oddsPrettyPrint("vd4+vd6", vanillaOddsDictPlusD6[4])
oddsPrettyPrint("vd6+vd6", vanillaOddsDictPlusD6[6])
oddsPrettyPrint("vd8+vd6", vanillaOddsDictPlusD6[8])
oddsPrettyPrint("vd10+vd6", vanillaOddsDictPlusD6[10])
oddsPrettyPrint("vd12+vd6", vanillaOddsDictPlusD6[12])
oddsPrettyPrint("vd20+vd6", vanillaOddsDictPlusD6[20])

print()

oddsPrettyPrint("vd4-vd6", vanillaOddsDictMinusD6[4])
oddsPrettyPrint("vd6-vd6", vanillaOddsDictMinusD6[6])
oddsPrettyPrint("vd8-vd6", vanillaOddsDictMinusD6[8])
oddsPrettyPrint("vd10-vd6", vanillaOddsDictMinusD6[10])
oddsPrettyPrint("vd12-vd6", vanillaOddsDictMinusD6[12])
oddsPrettyPrint("vd20-vd6", vanillaOddsDictMinusD6[20])

print()

##oddsPrettyPrint("2vd4", vanillaOddsDict2[(4,4)])
##oddsPrettyPrint("vd4+vd6", vanillaOddsDict2[(6,4)])
##oddsPrettyPrint("vd4+vd8", vanillaOddsDict2[(8,4)])
##oddsPrettyPrint("2vd6", vanillaOddsDict2[(6,6)])
##oddsPrettyPrint("vd4+vd10", vanillaOddsDict2[(10,4)])
##oddsPrettyPrint("vd6+vd8", vanillaOddsDict2[(8,6)])
##oddsPrettyPrint("vd4+vd12", vanillaOddsDict2[(12,4)])
##oddsPrettyPrint("vd6+vd10", vanillaOddsDict2[(10,6)])
##oddsPrettyPrint("2vd8", vanillaOddsDict2[(8,8)])
##oddsPrettyPrint("vd6+vd12", vanillaOddsDict2[(12,6)])
##oddsPrettyPrint("vd8+vd10", vanillaOddsDict2[(10,8)])
##oddsPrettyPrint("vd8+vd12", vanillaOddsDict2[(12,8)])
##oddsPrettyPrint("2vd10", vanillaOddsDict2[(10,10)])
##oddsPrettyPrint("vd10+vd12", vanillaOddsDict2[(12,10)])
##oddsPrettyPrint("2vd12", vanillaOddsDict2[(12,12)])
##oddsPrettyPrint("2vd20", vanillaOddsDict2[(20,20)])
##
##print()
##
##oddsPrettyPrint("3vd4", vanillaOddsDict3[(4,4,4)])
##oddsPrettyPrint("3vd6", vanillaOddsDict3[(6,6,6)])
##oddsPrettyPrint("3vd8", vanillaOddsDict3[(8,8,8)])
##oddsPrettyPrint("3vd10", vanillaOddsDict3[(10,10,10)])
##oddsPrettyPrint("3vd12", vanillaOddsDict3[(12,12,12)])
##oddsPrettyPrint("3vd20", vanillaOddsDict3[(20,20,20)])
##
##print()
##
##oddsPrettyPrint("xd4", explodingOddsDict[4])
##oddsPrettyPrint("xd6", explodingOddsDict[6])
##oddsPrettyPrint("xd8", explodingOddsDict[8])
##oddsPrettyPrint("xd10", explodingOddsDict[10])
##oddsPrettyPrint("xd12", explodingOddsDict[12])
##
##print()
##
##oddsPrettyPrint("x4+fx6", explodingOddsDictFocus6[4])
##oddsPrettyPrint("x6+fx6", explodingOddsDictFocus6[6])
##oddsPrettyPrint("x8+fx6", explodingOddsDictFocus6[8])
##oddsPrettyPrint("x10+fx6", explodingOddsDictFocus6[10])
##oddsPrettyPrint("x12+fx6", explodingOddsDictFocus6[12])
##
##print()
##
##oddsPrettyPrint("2xd4+xf6", explodingOddsDict2Focus6[(4,4)])
##oddsPrettyPrint("xd4+xd6+xf6", explodingOddsDict2Focus6[(6,4)])
##oddsPrettyPrint("xd4+xd8+xf6", explodingOddsDict2Focus6[(8,4)])
##oddsPrettyPrint("2xd6+xf6", explodingOddsDict2Focus6[(6,6)])
##oddsPrettyPrint("xd4+xd10+xf6", explodingOddsDict2Focus6[(10,4)])
##oddsPrettyPrint("xd6+xd8+xf6", explodingOddsDict2Focus6[(8,6)])
##oddsPrettyPrint("xd4+xd12+xf6", explodingOddsDict2Focus6[(12,4)])
##oddsPrettyPrint("xd6+xd10+xf6", explodingOddsDict2Focus6[(10,6)])
##oddsPrettyPrint("2xd8+xf6", explodingOddsDict2Focus6[(8,8)])
##oddsPrettyPrint("xd6+xd12+xf6", explodingOddsDict2Focus6[(12,6)])
##oddsPrettyPrint("xd8+xd10+xf6", explodingOddsDict2Focus6[(10,8)])
##oddsPrettyPrint("xd8+xd12+xf6", explodingOddsDict2Focus6[(12,8)])
##oddsPrettyPrint("2xd10+xf6", explodingOddsDict2Focus6[(10,10)])
##oddsPrettyPrint("xd10+xd12+f6", explodingOddsDict2Focus6[(12,10)])
##oddsPrettyPrint("2xd12+f6", explodingOddsDict2Focus6[(12,12)])
##
##print()
##
##oddsPrettyPrint("d4", oddsDict[4])
##oddsPrettyPrint("d6", oddsDict[6])
##oddsPrettyPrint("d8", oddsDict[8])
##oddsPrettyPrint("d10", oddsDict[10])
##oddsPrettyPrint("d12", oddsDict[12])
##
##print()
##
##oddsPrettyPrint("d4+f6", oddsDictFocus6[4])
##oddsPrettyPrint("d6+f6", oddsDictFocus6[6])
##oddsPrettyPrint("d8+f6", oddsDictFocus6[8])
##oddsPrettyPrint("d10+f6", oddsDictFocus6[10])
##oddsPrettyPrint("d12+f6", oddsDictFocus6[12])
##
##print()
##
##oddsPrettyPrint("d4++f6", oddsDictFocus6Bonus[4])
##oddsPrettyPrint("d6++f6", oddsDictFocus6Bonus[6])
##oddsPrettyPrint("d8++f6", oddsDictFocus6Bonus[8])
##oddsPrettyPrint("d10++f6", oddsDictFocus6Bonus[10])
##oddsPrettyPrint("d12++f6", oddsDictFocus6Bonus[12])
##
##print()

##oddsPrettyPrint("d4+f8", oddsDictFocus8[4])
##oddsPrettyPrint("d6+f8", oddsDictFocus8[6])
##oddsPrettyPrint("d8+f8", oddsDictFocus8[8])
##oddsPrettyPrint("d10+f8", oddsDictFocus8[10])
##oddsPrettyPrint("d12+f8", oddsDictFocus8[12])
##
##print()
##
##oddsPrettyPrint("d4+ff6", oddsDictFocus68[4])
##oddsPrettyPrint("d6+ff6", oddsDictFocus68[6])
##oddsPrettyPrint("d8+ff6", oddsDictFocus68[8])
##oddsPrettyPrint("d10+ff6", oddsDictFocus68[10])
##oddsPrettyPrint("d12+ff6", oddsDictFocus68[12])
##
##print()
##
##oddsPrettyPrint("d4+ff8", oddsDictFocus810[4])
##oddsPrettyPrint("d6+ff8", oddsDictFocus810[6])
##oddsPrettyPrint("d8+ff8", oddsDictFocus810[8])
##oddsPrettyPrint("d10+ff8", oddsDictFocus810[10])
##oddsPrettyPrint("d12+ff8", oddsDictFocus810[12])
##
##print()
##
##oddsPrettyPrint("c4", conOddsDict[4])
##oddsPrettyPrint("c6", conOddsDict[6])
##oddsPrettyPrint("c8", conOddsDict[8])
##oddsPrettyPrint("c10", conOddsDict[10])
##oddsPrettyPrint("c12", conOddsDict[12])
##
##print()
##
##oddsPrettyPrint("c4+f6", conOddsDictFocus6[4])
##oddsPrettyPrint("c6+f6", conOddsDictFocus6[6])
##oddsPrettyPrint("c8+f6", conOddsDictFocus6[8])
##oddsPrettyPrint("c10+f6", conOddsDictFocus6[10])
##oddsPrettyPrint("c12+f6", conOddsDictFocus6[12])
##
##print()
##
##oddsPrettyPrint("c4+f8", conOddsDictFocus8[4])
##oddsPrettyPrint("c6+f8", conOddsDictFocus8[6])
##oddsPrettyPrint("c8+f8", conOddsDictFocus8[8])
##oddsPrettyPrint("c10+f8", conOddsDictFocus8[10])
##oddsPrettyPrint("c12+f8", conOddsDictFocus8[12])
##
##print()
##
##oddsPrettyPrint("cc4", con2OddsDict[4])
##oddsPrettyPrint("cc6", con2OddsDict[6])
##oddsPrettyPrint("cc8", con2OddsDict[8])
##oddsPrettyPrint("cc10", con2OddsDict[10])
##oddsPrettyPrint("cc12", con2OddsDict[12])
##
##print()
##
##oddsPrettyPrint("cc4+f6", con2OddsDictFocus6[4])
##oddsPrettyPrint("cc6+f6", con2OddsDictFocus6[6])
##oddsPrettyPrint("cc8+f6", con2OddsDictFocus6[8])
##oddsPrettyPrint("cc10+f6", con2OddsDictFocus6[10])
##oddsPrettyPrint("cc12+f6", con2OddsDictFocus6[12])
##
##print()
##
##oddsPrettyPrint("cc4+f8", con2OddsDictFocus8[4])
##oddsPrettyPrint("cc6+f8", con2OddsDictFocus8[6])
##oddsPrettyPrint("cc8+f8", con2OddsDictFocus8[8])
##oddsPrettyPrint("cc10+f8", con2OddsDictFocus8[10])
##oddsPrettyPrint("cc12+f8", con2OddsDictFocus8[12])
##
##print()
##
##oddsPrettyPrint("d4+fc6", oddsDictFocusC6[4])
##oddsPrettyPrint("d6+fc6", oddsDictFocusC6[6])
##oddsPrettyPrint("d8+fc6", oddsDictFocusC6[8])
##oddsPrettyPrint("d10+fc6", oddsDictFocusC6[10])
##oddsPrettyPrint("d12+fc6", oddsDictFocusC6[12])
##
##print()
##
##oddsPrettyPrint("d4+fc8", oddsDictFocusC8[4])
##oddsPrettyPrint("d6+fc8", oddsDictFocusC8[6])
##oddsPrettyPrint("d8+fc8", oddsDictFocusC8[8])
##oddsPrettyPrint("d10+fc8", oddsDictFocusC8[10])
##oddsPrettyPrint("d12+fc8", oddsDictFocusC8[12])
##
##print()
##
##
##oddsPrettyPrint("2d4", oddsDict2[(4,4)])
##oddsPrettyPrint("d4+d6", oddsDict2[(6,4)])
##oddsPrettyPrint("d4+d8", oddsDict2[(8,4)])
##oddsPrettyPrint("2d6", oddsDict2[(6,6)])
##oddsPrettyPrint("d4+d10", oddsDict2[(10,4)])
##oddsPrettyPrint("d6+d8", oddsDict2[(8,6)])
##oddsPrettyPrint("d4+d12", oddsDict2[(12,4)])
##oddsPrettyPrint("d6+d10", oddsDict2[(10,6)])
##oddsPrettyPrint("2d8", oddsDict2[(8,8)])
##oddsPrettyPrint("d6+d12", oddsDict2[(12,6)])
##oddsPrettyPrint("d8+d10", oddsDict2[(10,8)])
##oddsPrettyPrint("d8+d12", oddsDict2[(12,8)])
##oddsPrettyPrint("2d10", oddsDict2[(10,10)])
##oddsPrettyPrint("d10+d12", oddsDict2[(12,10)])
##oddsPrettyPrint("2d12", oddsDict2[(12,12)])
##
##print()
##
##oddsPrettyPrint("2d4+f6", oddsDict2Focus6[(4,4)])
##oddsPrettyPrint("d4+d6+f6", oddsDict2Focus6[(6,4)])
##oddsPrettyPrint("d4+d8+f6", oddsDict2Focus6[(8,4)])
##oddsPrettyPrint("2d6+f6", oddsDict2Focus6[(6,6)])
##oddsPrettyPrint("d4+d10+f6", oddsDict2Focus6[(10,4)])
##oddsPrettyPrint("d6+d8+f6", oddsDict2Focus6[(8,6)])
##oddsPrettyPrint("d4+d12+f6", oddsDict2Focus6[(12,4)])
##oddsPrettyPrint("d6+d10+f6", oddsDict2Focus6[(10,6)])
##oddsPrettyPrint("2d8+f6", oddsDict2Focus6[(8,8)])
##oddsPrettyPrint("d6+d12+f6", oddsDict2Focus6[(12,6)])
##oddsPrettyPrint("d8+d10+f6", oddsDict2Focus6[(10,8)])
##oddsPrettyPrint("d8+d12+f6", oddsDict2Focus6[(12,8)])
##oddsPrettyPrint("2d10+f6", oddsDict2Focus6[(10,10)])
##oddsPrettyPrint("d10+d12+f6", oddsDict2Focus6[(12,10)])
##oddsPrettyPrint("2d12+f6", oddsDict2Focus6[(12,12)])
##
##print()

oddsPrettyPrint("d4++f6", oddsDictPlusFocus6[4])
oddsPrettyPrint("d6++f6", oddsDictPlusFocus6[6])
oddsPrettyPrint("d8++f6", oddsDictPlusFocus6[8])
oddsPrettyPrint("d10++f6", oddsDictPlusFocus6[10])
oddsPrettyPrint("d12++f6", oddsDictPlusFocus6[12])

print()

oddsPrettyPrint("d4rage", evenCascadeOddsDict[4])
oddsPrettyPrint("d6rage", evenCascadeOddsDict[6])
oddsPrettyPrint("d8rage", evenCascadeOddsDict[8])
oddsPrettyPrint("d10rage", evenCascadeOddsDict[10])
oddsPrettyPrint("d12rage", evenCascadeOddsDict[12])

print()
##
##oddsPrettyPrint("xd12_0", stupid12OddsDict[0])
##oddsPrettyPrint("xd12_1", stupid12OddsDict[1])
##oddsPrettyPrint("xd12_2", stupid12OddsDict[2])
##oddsPrettyPrint("xd12_3", stupid12OddsDict[3])
##oddsPrettyPrint("xd12_4", stupid12OddsDict[4])
##oddsPrettyPrint("xd12_5", stupid12OddsDict[5])
##
##print()
##
##oddsPrettyPrint("2xd12_0", doubleStupid12OddsDict[0])
##oddsPrettyPrint("2xd12_1", doubleStupid12OddsDict[1])
##oddsPrettyPrint("2xd12_2", doubleStupid12OddsDict[2])
##oddsPrettyPrint("2xd12_3", doubleStupid12OddsDict[3])
##oddsPrettyPrint("2xd12_4", doubleStupid12OddsDict[4])
##oddsPrettyPrint("2xd12_5", doubleStupid12OddsDict[5])
##
##print()
##
##oddsPrettyPrintHeaders(True)
##for i in range(1,21):
##		oddsPrettyPrint(str(i) + "d6-pool", d6PoolOddsDict[i], True)
##
##print()
##
##for i in range(1,21):
##		oddsPrettyPrint(str(i) + "d10-pool", d10PoolOddsDict[i], True)
##
##print()
##
##def compete(oddsDict, a, b):
##	winRate = 0
##	for i in range(1,len(oddsDict[a])):
##		for j in range(0,min(i,len(oddsDict[b]))):
##			winRate += oddsDict[a][i] * oddsDict[b][j]
##		#if i < len(oddsDict[b]):
##		#	winRate += oddsDict[a][i] * oddsDict[b][i] * 0.5 #handle ties
##	return winRate
##
##def competeAllPrint(oddsDict, minSize, maxSize):
##	for i in range(minSize, maxSize+1):
##		s = ""
##		args = []
##		for j in range(minSize, maxSize+1):                       
##			s += "{:>8.2%}"
##			args.append(compete(oddsDict, i, j))
##		print(s.format(*args))
##
##competeAllPrint(d6PoolOddsDict,1,20)
##
##print()
##
##competeAllPrint(d10PoolOddsDict,1,20)
