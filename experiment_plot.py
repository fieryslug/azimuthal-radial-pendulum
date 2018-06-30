import xlrd
import matplotlib.pyplot as plt

file = 'D:\Document\\fisicaF\\azimuthal_radial_pendulum\\vids\\60g\\60g_2.12.xlsx'
data = xlrd.open_workbook(file)
sh = data.sheet_by_index(0)

xplotr = sh.col_values(11)
yplotr = sh.col_values(12)

xplot = []
yplot = []

for i in range(len(xplotr)):
    if type(xplotr[i]) is float and type(yplotr[i]) is float:
        xplot.append(xplotr[i])
        yplot.append(yplotr[i])



plt.plot(xplot, yplot)
plt.show()