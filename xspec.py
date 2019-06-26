#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-

# Generic/Built-in
import sys, subprocess

__author__ = 'Yohan Alexander'
__copyright__ = 'Copyright 2019, Xspec Script' 
__credits__ = ['Yohan Alexander']
__license__ = 'MPL 2.0'
__version__ = '0.1.0'
__maintainer__ = 'Yohan Alexander'
__email__ = 'yohanfranca@gmail.com'
__status__ = 'Dev'

class Parameters():
        def __init__(self, folder, expo):
            self.program = ["xspec"]
            self.dir = "cd %s\n" %folder
            self.model = "model apec*phabs\n"
            self.kT = "12\n"
            self.abundancy = "0.3\n"
            self.redshift = "0\n"
            self.norm = "0.1617486\n"
            self.nH = "0.1\n"
            self.energies = "energies 0.3 12.0 1000\n"
            self.flux = "flux 0.3 12.0\n"
            self.reset = "energies reset\n"
            self.fakeit = "fakeit none\n"
            self.pnrmf = "pn-thin-5-ao18.rmf\n"
            self.pnarf = "pn-thin-5-ao18.arf\n"
            self.y = "\n"
            self.exposition = "%s\n" %expo
            self.cstat = "statistic cstat\n"
            self.pchi = "statistic test pchi\n"
            self.ignore = "ignore **-0.15 12.0-**\n"
            self.freeze = "freeze 5\n"
            self.fit = "fit\n"
            self.parallel = "parallel error 3\n"
            self.err = "err 1 4\n"
            self.setplot = "setplot energy\n"
            self.iplot = "iplot data\n"
            self.quit = "quit\n"
            self.cpd = "cpd %s.ps/cps\n" %expo
            self.data = "plot data\n"
            self.ldata = "plot ldata\n"
            self.none = "cpd none\n"
            self.exit = "exit\n"

def main(args):

    folder = args[1]
    expo = args[2]

    i = Parameters(folder, expo)

    xspec = subprocess.Popen(i.program, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, universal_newlines=True, bufsize=0)

    xspec.stdin.write(i.dir)
    xspec.stdin.write(i.model)
    xspec.stdin.write(i.kT)
    xspec.stdin.write(i.abundancy)
    xspec.stdin.write(i.redshift)
    xspec.stdin.write(i.norm)
    xspec.stdin.write(i.nH)
    xspec.stdin.write(i.energies)
    xspec.stdin.write(i.flux)
    xspec.stdin.write(i.reset)
    xspec.stdin.write(i.fakeit)
    xspec.stdin.write(i.pnrmf)
    xspec.stdin.write(i.pnarf)
    xspec.stdin.write(i.y)
    xspec.stdin.write(i.y)
    xspec.stdin.write(i.y)
    xspec.stdin.write(i.y)
    xspec.stdin.write(i.exposition)
    xspec.stdin.write(i.cstat)
    xspec.stdin.write(i.pchi)
    xspec.stdin.write(i.ignore)
    xspec.stdin.write(i.freeze)
    xspec.stdin.write(i.fit)
    xspec.stdin.write(i.parallel)
    xspec.stdin.write(i.err)
    xspec.stdin.write(i.setplot)
    xspec.stdin.write(i.iplot)
    xspec.stdin.write(i.quit)
    xspec.stdin.write(i.cpd)
    xspec.stdin.write(i.data)
    xspec.stdin.write(i.ldata)
    xspec.stdin.write(i.none)
    xspec.stdin.write(i.exit)
    
    xspec.stdin.close()

    for line in xspec.stdout:
        print(line)
        
if __name__ == "__main__":
    main(sys.argv)