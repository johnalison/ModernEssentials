import matplotlib.pyplot as plt

import numpy as np
import matplotlib

from grades import grades as grades
print(grades)

midTerm1 = []
midTerm2 = []
midTerm3 = []

for n in grades:
    print(n,grades[n])
    _midTerm1, _midTerm2, _midTerm3 = grades[n]
    midTerm1.append(float(_midTerm1))
    midTerm2.append(float(_midTerm2))
    midTerm3.append(float(_midTerm3))

midTerm1 = np.array(midTerm1)
midTerm2 = np.array(midTerm2)
midTerm3 = np.array(midTerm3)
    
def convertToPercent(scores, totalPoints):
    return np.array(scores)/totalPoints*100    

def getAveRMS(grades):
    return np.average(grades), np.std(grades)

#print(np.array(midTerm1))
#print(len(midTerm1))
combinedMidTerms = midTerm1 + midTerm2 + midTerm3

midTerm1Total = 90
midTerm2Total = 90
midTerm3Total = 80
midTerm1Percent = convertToPercent(midTerm1, midTerm1Total)
midTerm2Percent = convertToPercent(midTerm2, midTerm2Total)
midTerm3Percent = convertToPercent(midTerm3, midTerm3Total)
combinedPercent = convertToPercent(combinedMidTerms, midTerm1Total+midTerm2Total+midTerm3Total)

print(grades.keys())
for n, g in zip(grades.keys(),combinedPercent):
    print(n,"\t",round(g,1))

midterm1_ave_raw, midterm1_rms_raw = getAveRMS(midTerm1)
midterm2_ave_raw, midterm2_rms_raw = getAveRMS(midTerm2)
midterm3_ave_raw, midterm3_rms_raw = getAveRMS(midTerm3)

midterm1_ave, midterm1_rms = getAveRMS(midTerm1Percent)
midterm2_ave, midterm2_rms = getAveRMS(midTerm2Percent)
midterm3_ave, midterm3_rms = getAveRMS(midTerm3Percent)

combined_ave, combined_rms = getAveRMS(combinedPercent)


print("MidTerm 1")
print(f"\t{midterm1_ave}, {midterm1_rms}")
print(f"\t\t{midterm1_ave_raw}, {midterm1_rms_raw}")

print("MidTerm 2")
print(f"\t{midterm2_ave}, {midterm2_rms}")
print(f"\t\t{midterm2_ave_raw}, {midterm2_rms_raw}")

print("MidTerm 3")
print(f"\t{midterm3_ave}, {midterm3_rms}")
print(f"\t\t{midterm3_ave_raw}, {midterm3_rms_raw}")


def plot1D(name, grades, ave, rms, bins = np.linspace(0,100,25), xMin = 20, xlim=(50,100)):

    plt.hist(grades, bins=bins,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
    plt.plot([ave,ave],[0,3],'r--')
    plt.annotate("Mean = "+str(round(ave,1)), xy=(xMin+2, 2.5), xytext=(xMin+2,4),
                 color="red", weight="light", fontsize=14,
                 )
    plt.annotate("RMS ="+str(round(rms,1)), xy=(xMin+2, 2.5), xytext=(xMin+2,3),
                 color="red", weight="light", fontsize=14,
                 )
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(0, 8)
    plt.xlabel(name+" Grades (%)")
    plt.savefig(name+".pdf")
    plt.savefig(name+".png")
    plt.close()



    
    
plot1D("MidTerm1", midTerm1Percent, midterm1_ave, midterm1_rms)
plot1D("MidTerm2", midTerm2Percent, midterm2_ave, midterm2_rms)
plot1D("MidTerm3", midTerm3Percent, midterm3_ave, midterm3_rms, xlim=(20,100))
plot1D("CombinedGrade", combinedPercent, combined_ave, combined_rms, bins=np.linspace(0,100,50))


def plotScatter(name, data1, name1, data2, name2):
    plt.scatter(data1, data2, color='b') #, label='') 
    plt.xlim(0, 100) 
    plt.ylim(0, 100) 
    plt.xlabel(name1)
    plt.ylabel(name2)
    #plt.legend() 
    plt.savefig(name+'.pdf')
    plt.savefig(name+'.png') 
    plt.close()
    
plotScatter('midTerm1_vs_midTerm2',midTerm1Percent, "Midterm 1", midTerm2Percent, "Midterm 2")
plotScatter('midTerm1_vs_midTerm3',midTerm1Percent, "Midterm 1", midTerm3Percent, "Midterm 3")
plotScatter('midTerm2_vs_midTerm3',midTerm2Percent, "Midterm 2", midTerm3Percent, "Midterm 3")

aveMid1and2Percent = 0.5*(midTerm1Percent + midTerm2Percent)
plotScatter('midTerm1and2_vs_midTerm3',aveMid1and2Percent, "Average of Midterm 1 and 2", midTerm3Percent, "Midterm 3")

#plt.hist(grades, bins=bins,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
