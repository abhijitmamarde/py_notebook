import matplotlib.pyplot as plt

D = dict(
    Q1=210,
    Q2=260,
    Q3=250,
    Q4=230,
)

explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice

fig1, ax1 = plt.subplots()
ax1.pie(list(D.values()), explode=explode, labels=list(D.keys()),
        autopct='%1.1f%%', shadow=True, startangle=90
)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
