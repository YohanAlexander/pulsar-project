#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-

# Generic/Built-in
import sys, subprocess

# Other libs
import click, xspec

__author__ = 'Yohan Alexander'
__copyright__ = 'Copyright 2019, Xspec Script' 
__credits__ = ['Yohan Alexander']
__license__ = 'MPL 2.0'
__version__ = '0.1.0'
__maintainer__ = 'Yohan Alexander'
__email__ = 'yohanfranca@gmail.com'
__status__ = 'Dev'

class Parameters():
        def __init__(self, expo, folder=""):
            self.program = ["xspec"]
            self.dir = "cd %s\n" %folder
            self.cpd = "cpd /xs\n"
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
            self.ldata = "plot ldata chi\n"
            self.iplot = "iplot\n"
            self.timeoff = "time off\n"
            self.labeltop = "label top Simulated Spectrum with exposition time of %s seconds\n" %expo
            self.labelfile = "label file Gamma Cassiopeiae\n"
            self.labely = "label y counts s\\u-1\\d keV\\u-1\\d\n"
            self.csize = "csize 0.8\n"
            self.plot = "plot\n"
            self.hard = "hard %s.ps/cps\n" %expo
            self.logy = "log y\n"
            self.rescale = "rescale y 0.1 100\n"
            self.plot2 = "plot\n"
            self.hard2 = "hard l%s.ps/cps\n" %expo
            self.quit = "quit.ps/cps\n"
            self.exit = "exit\n"


@click.command()
@click.argument('exposition')
@click.option('--folder', '-f', help='full or relative path to your pn file')
def main(exposition, folder):
    """
    Python script to automate the xspec spectral fitting
    """

    i = Parameters(exposition, folder)

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
    xspec.stdin.write(i.ldata)
    xspec.stdin.write(i.iplot)
    xspec.stdin.write(i.timeoff)
    xspec.stdin.write(i.labeltop)
    xspec.stdin.write(i.labelfile)
    xspec.stdin.write(i.labely)
    xspec.stdin.write(i.csize)
    xspec.stdin.write(i.plot)
    xspec.stdin.write(i.hard)
    xspec.stdin.write(i.logy)
    xspec.stdin.write(i.rescale)
    xspec.stdin.write(i.plot2)
    xspec.stdin.write(i.hard2)
    xspec.stdin.write(i.quit)

    xspec.stdin.write(i.exit)
    
    xspec.stdin.close()

    for line in xspec.stdout:
        print(line)
        
if __name__ == "__main__":
    main()