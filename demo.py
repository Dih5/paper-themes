#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

from os.path import join

with plt.style.context('paper'):
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
    legend=plt.legend()

    plt.gcf().tight_layout()
    
    for ext in ["eps", "png", "pdf"]:
        plt.savefig(join('img', 'demo.' + ext))

        
with plt.style.context(['paper','larger-fonts', 'size22']):
    fig=plt.figure()

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
    
    plt.gcf().tight_layout()
    
    for ext in ["eps", "png", "pdf"]:
        plt.savefig(join('img', 'demo4.' + ext))
