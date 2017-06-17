#!/usr/bin/python

# Physics 91SI
# molecule 2015
# Lab 8

# Modules you won't need
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Modules you will need
import numpy as np
import particle

class Molecule:
    def __init__(self, pos1, pos2, M1, M2, k, L0):
        self.k=k
        self.p1=particle.Particle(pos1, M1)
        self.p2=particle.Particle(pos2, M2)
        self.L0=L0
    def get_displ(self):
        p_1=np.array(self.p1.pos)
        p_2=np.array(self.p2.pos)
        return p_2-p_1
    def get_force(self):
        displ = self.get_displ()
        return -self.k*(displ-self.L0)

# TODO: Implement this function
def init_molecule():
    """Create Particles p1 and p2 inside boundaries and return a molecule
    connecting them"""
    #x0,y0 between 0 and 1
    
    return Molecule([.2,.2],[.8,.8],1,2,1,.5)
    

# TODO: Implement this function
def time_step(dt, mol):
    """Sets new positions and velocities of the particles attached to mol"""
    x1=mol.p1.pos
    x2=mol.p2.pos
    m1=mol.p1.m
    m2=mol.p2.m
    v1=mol.p1.vel
    v2=mol.p2.vel
    
    F=mol.get_force()
    vn1=v1+(F/m1)*dt
    xn1=x1+vn1*dt
    vn2=v2+(F/m2)*dt
    xn2=x2+vn2*dt
    
    mol.p1.vel=vn1
    mol.p1.pos=xn1
    mol.p2.vel=vn2
    mol.p2.pos=xn2
    
    
 
    
    
    
    
    
#############################################
# The rest of the file is already implemented
#############################################



def run_dynamics(n, dt, xlim=(0, 1), ylim=(0, 1)):
    """Calculate each successive time step and animate it"""
    mol = init_molecule()

    # Animation stuff
    fig, ax = plt.subplots()
    line, = ax.plot((mol.p1.pos[0], mol.p2.pos[0]), (mol.p1.pos[1], mol.p2.pos[1]), '-o')
    ax.clear()
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title('Dynamics simulation')
    dynamic_ani = animation.FuncAnimation(fig, update_anim, n,
            fargs=(dt, mol,line), interval=50, blit=False)
    plt.show()

def update_anim(i,dt, mol,line):
    """Update and draw the molecule. Called by FuncAnimation"""
    time_step(dt, mol)
    print(mol.p1.pos)
    print(mol.p2.pos)
    line.set_data([(mol.p1.pos[0], mol.p2.pos[0]),
                   (mol.p1.pos[1], mol.p2.pos[1])])
    return line,


if __name__ == '__main__':
    # Set the number of iterations and time step size
    n = 10
    dt = .1
    run_dynamics(n, dt)
    
print("hi")
