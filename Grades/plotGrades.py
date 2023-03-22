import matplotlib.pyplot as plt

import numpy as np
import matplotlib

from grades import grades as grades
print(grades)

midTerm1 = []
midTerm2 = []

for n in grades:
    print(n,grades[n])
    _midTerm1, _midTerm2 = grades[n]
    midTerm1.append(float(_midTerm1))
    midTerm2.append(float(_midTerm2))

midTerm1 = np.array(midTerm1)
midTerm2 = np.array(midTerm2)
    
def convertToPercent(scores, totalPoints):
    return np.array(scores)/totalPoints*100    

def getAveRMS(grades):
    return np.average(grades), np.std(grades)

#print(np.array(midTerm1))
#print(len(midTerm1))
combinedMidTerms = midTerm1 + midTerm2

midTerm1Percent = convertToPercent(midTerm1, 90)
midTerm2Percent = convertToPercent(midTerm2, 90)
combinedPercent = convertToPercent(combinedMidTerms, 90+90)

print(grades.keys())
for n, g in zip(grades.keys(),combinedPercent):
    print(n,"\t",round(g,1))

midterm1_ave, midterm1_rms = getAveRMS(midTerm1Percent)
midterm2_ave, midterm2_rms = getAveRMS(midTerm2Percent)
combined_ave, combined_rms = getAveRMS(combinedPercent)


print("MidTerm 1")
print(f"\t{midterm1_ave}, {midterm1_rms}")

print("MidTerm 2")
print(f"\t{midterm2_ave}, {midterm2_rms}")



def plot1D(name, grades, ave, rms, bins = np.linspace(0,100,25), xMin = 20):

    plt.hist(grades, bins=bins,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
    plt.plot([ave,ave],[0,3],'r--')
    plt.annotate("Mean = "+str(round(ave,1)), xy=(xMin+2, 2.5), xytext=(xMin+2,4),
                 color="red", weight="light", fontsize=14,
                 )
    plt.annotate("RMS ="+str(round(rms,1)), xy=(xMin+2, 2.5), xytext=(xMin+2,3),
                 color="red", weight="light", fontsize=14,
                 )
    plt.xlim(50, 100)
    plt.ylim(0, 8)
    plt.xlabel(name+" Grades (%)")
    plt.savefig(name+".pdf")
    plt.savefig(name+".png")
    plt.close()

plot1D("MidTerm1", midTerm1Percent, midterm1_ave, midterm1_rms)
plot1D("MidTerm2", midTerm2Percent, midterm2_ave, midterm2_rms)
plot1D("CombinedGrade", combinedPercent, combined_ave, combined_rms, bins=np.linspace(0,100,50))




plt.scatter(midTerm1Percent, midTerm2Percent, color='b') #, label='') 
plt.xlim(0, 100) 
plt.ylim(0, 100) 
plt.xlabel('Midterm 1') 
plt.ylabel('Midterm 2') 
#plt.legend() 
plt.savefig('midTerm1_vs_midTerm2.pdf')
plt.savefig('midTerm1_vs_midTerm2.png') 

#plt.hist(grades, bins=bins,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
