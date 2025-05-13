import matplotlib.pyplot as plt
import copy
import numpy as np
import matplotlib

from grades import grades as grades
#print(grades)

midTerm1 = []
midTerm2 = []
midTerm3 = []
final    = []
homework = []

class studentGrades:

    def __init__(self, m1=None, m2=None, m3=None, f=None, hw=None):
        self.m1 = float(m1) if m1 is not None else None
        self.m2 = float(m2) if m2 is not None else None
        self.m3 = float(m3) if m3 is not None else None
        self.f  = float(f)  if f  is not None else None
        self.hw = float(hw) if hw is not None else None


doMidterm2 = True
doMidterm3 = True
doFinal    = True
doHomework = True





def plot1D(name, grades, ave, rms, bins = np.linspace(0,100,40), xMin = 20, xlim=(0,100)):

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



def unpackGrades(inputList):
    if  len(inputList) == 1:
        return studentGrades(m1 = inputList[0])
    if  len(inputList) == 2:
        return studentGrades(m1 = inputList[0],
                             m2 = inputList[1],
                             )

    if  len(inputList) == 3:
        return studentGrades(m1 = inputList[0],
                             m2 = inputList[1],
                             m3 = inputList[2],
                             )


    else:
        return studentGrades(m1 = inputList[0],
                             m2 = inputList[1],
                             m3 = inputList[2],
                             f  = inputList[3],
                             hw = inputList[4])

for n in grades:
    thisStudent = unpackGrades(grades[n])

    if thisStudent.m2 is None:
        doMidterm2 = False

    if thisStudent.m3 is None:
        doMidterm3 = False

    if thisStudent.f is None:
        doFinal    = False

    if thisStudent.hw is None:
        doHomework = False

    midTerm1.append(thisStudent.m1)
    if doMidterm2:
        midTerm2.append(thisStudent.m2)

    if doMidterm3:
        midTerm3.append(thisStudent.m3)

    if doFinal:
        final   .append(thisStudent.f)

    if doHomework:
        homework.append(thisStudent.hw)

midTerm1 = np.array(midTerm1)
midTerm2 = np.array(midTerm2)
midTerm3 = np.array(midTerm3)
final    = np.array(final)
homework = np.array(homework)

#breakpoint()

def convertToPercent(scores, totalPoints):
    return np.array(scores)/totalPoints*100

def getAveRMS(grades):
    return np.average(grades), np.std(grades)

#print(np.array(midTerm1))
#print(len(midTerm1))



combinedMidTerms = copy.copy(midTerm1)
if doMidterm2:
    combinedMidTerms += midTerm2
if doMidterm3:
    combinedMidTerms += midTerm3



midTerm1Total = 90
midTerm2Total = 90
midTerm3Total = 80
finalTotal    = 200
midTerm1Percent = convertToPercent(midTerm1, midTerm1Total)
midterm1_ave_raw, midterm1_rms_raw = getAveRMS(midTerm1)
midterm1_ave, midterm1_rms = getAveRMS(midTerm1Percent)

print("MidTerm 1")
print(f"\t{midterm1_ave:.2f} +/- {midterm1_rms:.2f} %")
print(f"\t\t{midterm1_ave_raw:.2f} +/- {midterm1_rms_raw:.2f} (raw)")
plot1D("MidTerm1", midTerm1Percent, midterm1_ave, midterm1_rms)

if doMidterm2:
    midTerm2Percent = convertToPercent(midTerm2, midTerm2Total)
    midterm2_ave_raw, midterm2_rms_raw = getAveRMS(midTerm2)
    midterm2_ave, midterm2_rms = getAveRMS(midTerm2Percent)

    print("MidTerm 2")
    print(f"\t{midterm2_ave:.2f} +/- {midterm2_rms:.2f} %")
    print(f"\t\t{midterm2_ave_raw:.2f} +/- {midterm2_rms_raw:.2f} (raw)")

    plot1D("MidTerm2", midTerm2Percent, midterm2_ave, midterm2_rms)
    plotScatter('midTerm1_vs_midTerm2',midTerm1Percent, "Midterm 1", midTerm2Percent, "Midterm 2")

if doMidterm3:
    midTerm3Percent = convertToPercent(midTerm3, midTerm3Total)
    midterm3_ave_raw, midterm3_rms_raw = getAveRMS(midTerm3)
    midterm3_ave, midterm3_rms = getAveRMS(midTerm3Percent)


    print("MidTerm 3")
    print(f"\t{midterm3_ave:.2f}+/- {midterm3_rms:.2f}")
    print(f"\t\t{midterm3_ave_raw:.2f} +/- {midterm3_rms_raw:.2f} (raw)")

    plot1D("MidTerm3", midTerm3Percent, midterm3_ave, midterm3_rms, xlim=(20,100))

    plotScatter('midTerm1_vs_midTerm3',midTerm1Percent, "Midterm 1", midTerm3Percent, "Midterm 3")
    plotScatter('midTerm2_vs_midTerm3',midTerm2Percent, "Midterm 2", midTerm3Percent, "Midterm 3")

    aveMid1and2Percent = 0.5*(midTerm1Percent + midTerm2Percent)
    plotScatter('midTerm1and2_vs_midTerm3',aveMid1and2Percent, "Average of Midterm 1 and 2", midTerm3Percent, "Midterm 3")


combinedMidTermPercent = convertToPercent(combinedMidTerms, midTerm1Total + midTerm2Total + midTerm3Total)
combinedMidTerm_ave, combinedMidTerm_rms = getAveRMS(combinedMidTermPercent)


if doFinal:
    finalPercent    = convertToPercent(final,    finalTotal   )
    final_ave_raw,    final_rms_raw    = getAveRMS(final)
    final_ave,    final_rms    = getAveRMS(finalPercent)

    print("Final")
    print(f"\t{final_ave:.2f}+/- {final_rms:.2f} %")
    print(f"\t\t{final_ave_raw:.2f} +/- {final_rms_raw:.2f} (raw)")

    plot1D("Final",    finalPercent,    final_ave,    final_rms, xlim=(20,100))


if doHomework:
    homeworkPercent = homework
    homework_ave, homework_rms = getAveRMS(homeworkPercent)

    print("Homework")
    print(f"\t{homework_ave:.2f}+/- {homework_rms:.2f} %")



if True:
    combinedGradePercent = 0.1* homeworkPercent  + 0.45 * combinedMidTermPercent + 0.45 * finalPercent
    #combinedGradePercent = combinedMidTermPercent
    combinedGrade_ave, combinedGrade_rms = getAveRMS(combinedGradePercent)

    combinedGradeZScore = (combinedGradePercent - combinedGrade_ave)/combinedGrade_rms

    print(grades.keys())
    for n, g, z in zip(grades.keys(),combinedGradePercent, combinedGradeZScore):
        print(f"\t\t{n:10}\t{g:.2f}\t{z:.2f}")
        if g > 85:   print("\t\t\tA")
        elif g > 70: print("\t\t\tB")
        elif g > 60: print("\t\t\tC")
        elif g > 50: print("\t\t\tD")
        else       : print("\t\t\tF")

    print("Combined Grade")
    print(f"\t{combinedGrade_ave:.2f} +/- {combinedGrade_rms:.2f} %")

    plot1D("CombinedMidTerm", combinedMidTermPercent, combinedMidTerm_ave, combinedMidTerm_rms, bins=np.linspace(0,100,50))
    plot1D("CombinedGrade",  combinedGradePercent, combinedGrade_ave, combinedGrade_rms, bins=np.linspace(0,100,50), xlim=(40,100))
    plot1D("CombinedGradeZScore",  combinedGradeZScore, 0, 1, bins=np.linspace(-3,3,25), xlim=(-3,3))

if doFinal:
    plotScatter('combinedMidterm_vs_final',combinedMidTermPercent, "Average of Midterms", finalPercent, "Final")









#plt.hist(grades, bins=bins,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
