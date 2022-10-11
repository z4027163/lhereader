import numpy as np
from lhereader import LHEReader
import math
import ROOT
from ROOT import TCanvas, TPad, TFile, TPaveLabel, TPaveText, TLegend
from array import array
h = ROOT.TH1F("h",";mass ;Events;;",90,1,10)

reader = LHEReader('lhefile/dy1to8_to2j_xqcut5.lhe')

# Mediator mass in each event
mmed = []
counter = 0
for iev, event in enumerate(reader):
    # Find muon particles
    mu = filter(lambda x: abs(x.pdgid)== 13, event.particles)

    # Sum over all muon four-momenta in the event
    combined_p4 = None
    for p4 in map(lambda x: x.p4(), mu):
        if combined_p4:
            combined_p4 += p4
        else:
            combined_p4 = p4 
    mmed.append(combined_p4.mass)
    h.Fill(combined_p4.mass)

myfile = TFile( 'dy2j.root', 'RECREATE' )
h.Write()
myfile.Close()
