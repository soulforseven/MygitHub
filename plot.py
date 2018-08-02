# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
x = np.linspace(-np.pi, np.pi, 1000)
cos_y = np.cos(x) / 2
sin_y = np.sin(x)
xo = np.pi * 3 / 4
yo_cos = np.cos(xo) / 2
yo_sin = np.sin(xo)
mp.yticks([-1, -0.5, 0, 0.5, 1])
mp.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
          [r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$'])
ax = mp.gca()
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_position(('data', 0))
ax.spines['top'].set_position(('data', 0))


mp.plot(x, cos_y, label=r'$y=\frac{1}{2}cos(x)$')
mp.plot(x, sin_y, label=r'$y=sin(x)$')
mp.scatter([xo, xo], [yo_cos, yo_sin])
mp.annotate(r'$\frac{1}{2}cos(\frac{3\pi}{4})=-\frac{\sqrt{2}}{4}$',
            xy=(xo, yo_cos), xycoords='data', xytext=(-90, -40), textcoords='offset points', fontsize=14, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
mp.legend(loc='upper left')
mp.show()
