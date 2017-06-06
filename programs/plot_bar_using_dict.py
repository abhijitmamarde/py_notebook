import matplotlib.pyplot as plt

D = dict(
    jan=120,
    feb=130,
    mar=160,
    apr=130,
    may=140,
    jun=170,
    jul=190,
    aug=150,
    sep=120,
    oct=190,
    nov=180,
    dec=210,
)

plt.bar(range(len(D)), D.values(), align='center')
plt.xticks(range(len(D)), D.keys())
plt.show()