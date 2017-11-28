import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/charlotte/class_perso-ScalarField/class_perso-ScalarField/output/CJ_SF15_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['CJ_SF15_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'H[1/Mpc]', u'rho_scf']
tex_names = ['H [1/Mpc]', u'(8\\pi G/3)rho_scf']
x_axis = 'z'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 3]))
ax.loglog(curve[:, 0], abs(curve[:, 14]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('z', fontsize=16)
plt.show()