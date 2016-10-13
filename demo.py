#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12, 6)
from matplotlib.backends.backend_pdf import PdfPages

import numpy as np

with plt.style.context('paper'):
    with PdfPages('demo.pdf') as pdf:

        t = np.arange(0.0, 2.0, 0.01)
        s = 1 - np.cos(2*np.pi*t)
        s2 = 1 - np.sin(2*np.pi*t)
        s3 = (1- np.cos(2*np.pi*t))/2
        plt.plot(t, s, label="Versine")
        plt.plot(t, s2,label="Coversine")
        plt.plot(t, s3,label="Haversine")

        plt.xlabel('$x$')
        plt.ylabel('$f(x)$')
        plt.title('Ye olde trigonometric funtions')
        legend=plt.legend();

        plt.gcf().set_size_inches([6*np.sqrt(2),6])
        plt.gcf().tight_layout()

        pdf.savefig()
        plt.savefig('demo.eps', format='eps', dpi=300)
        plt.savefig('demo.png', format='png', dpi=300)
        

fig=plt.figure()
with plt.style.context(['paper','larger-fonts']):
    with PdfPages('demo4.pdf') as pdf:

        t = np.arange(0.0, 2.0, 0.01)
        s = 1 - np.cos(2*np.pi*t)
        s2 = 1 - np.sin(2*np.pi*t)
        s3 = (1- np.cos(2*np.pi*t))/2
        
        fig.add_subplot(2,2,1,aspect='auto')
        plt.plot(t, s)
        plt.xlabel('$x$')
        plt.ylabel('$f(x)$')
        plt.title('Versine')
        fig.add_subplot(2,2,2,aspect='auto')
        plt.plot(t, s2)
        plt.xlabel('$x$')
        plt.ylabel('$f(x)$')
        plt.title('Coversine')
        fig.add_subplot(2,2,3,aspect='auto')
        plt.plot(t, s3)
        plt.xlabel('$x$')
        plt.ylabel('$f(x)$')
        plt.title('Haversine')
        fig.add_subplot(2,2,4,aspect='auto')
        plt.plot(t, t)
        plt.xlabel('$x$')
        plt.ylabel('$f(x)$')
        plt.title('Linear')


        plt.gcf().set_size_inches([2*6*np.sqrt(2),2*6])
        plt.gcf().tight_layout()

        pdf.savefig()
        plt.savefig('demo4.eps', format='eps', dpi=300)
        plt.savefig('demo4.png', format='png', dpi=300)
