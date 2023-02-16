import matplotlib.pyplot as plt

import numpy as np
import matplotlib

from grades import grades as grades
print(grades)

scores = []

for n in grades:
    print(n,grades[n])
    scores.append(float(grades[n]))


print(np.array(scores))
print(len(scores))
scoresPercent = np.array(scores)/90*100
print(scoresPercent)
midterm1_ave = round(np.average(scoresPercent),1)
midterm1_rms = round(np.std(scoresPercent),1)

print(midterm1_ave, midterm1_rms)

bins = np.linspace(0,100,25)
#print( bins)
xMin = 20


plt.hist(scoresPercent, bins=bins,color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
plt.plot([midterm1_ave,midterm1_ave],[0,3],'r--')
plt.annotate("Mean = "+str(midterm1_ave), xy=(xMin+2, 2.5), xytext=(xMin+2,4),
             color="red", weight="light", fontsize=14,
             #arrowprops={"facecolor": "red"}
             )
plt.annotate("RMS ="+str(midterm1_rms), xy=(xMin+2, 2.5), xytext=(xMin+2,3),
             color="red", weight="light", fontsize=14,
             #arrowprops={"facecolor": "red"}
             )
plt.xlim(0, 100)
plt.ylim(0, 8)
plt.xlabel("Midterm 1 Grades (%)")
plt.savefig("MidTerm1.pdf")
plt.savefig("MidTerm1.png")
plt.close()
