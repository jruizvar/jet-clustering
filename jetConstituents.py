"""
Description: The program picks the first 10 events from the dataset BulkGravToZZToZhadZhad_M-1800 

             For each event creates a csv file with the list of jet constituents

             The name of the csv file follows the syntax run_lumi_event.csv


Usage:       mkdir csvFiles; python jetConstituents.py

"""

import ROOT
ROOT.gROOT.SetBatch(True)

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable()

# load FWlite python libraries
from DataFormats.FWLite import Events, Handle

jets, jetLabel = Handle("std::vector<pat::Jet>"), "slimmedJetsAK8"

events = Events(
"root://eoscms.cern.ch//eos/cms/store/mc/RunIISummer16MiniAODv2/BulkGravToZZToZhadZhad_narrow_M-1800_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/48313E83-C4BD-E611-9A1C-001C23BED459.root")

# Loop over events
for e,event in enumerate(events):
    print "\nEvent", e
    if e >= 10: break
    event.getByLabel(jetLabel, jets)

    # output file
    aux = event.eventAuxiliary()
    file = open('csvFiles/%d_%d_%d.csv'%(aux.run(),aux.luminosityBlock(),aux.event()),'w')
    file.write("Jet,Constituent,Eta,Phi,Px,Py,Pz,P\n")
    # Loop over jets 
    for i,j in enumerate(jets.product()):
        print "jet %3d, pt %5.1f, eta %5.1f, phi %5.1f, mass %5.1f" % (i, j.pt(), j.eta(), j.phi(), j.userFloat('ak8PFJetsCHSSoftDropMass'))

        # Jet constituents
        constituents = []
        for ida in xrange( j.numberOfDaughters() ) :
            cand = j.daughter(ida)
            if cand.numberOfDaughters() == 0 :
                constituents.append( cand )
            else :
                for jda in xrange( cand.numberOfDaughters() ) :
                    cand2 = cand.daughter(jda)
                    constituents.append( cand2 )
        constituents.sort(key = lambda c:c.pt(), reverse=True)
        for k, cand in enumerate(constituents):
            p = cand.p()
            file.write("%d,%d,%f,%f,%f,%f,%f,%f\n" % (i, k, cand.eta(), cand.phi(), cand.px()/p, cand.py()/p, cand.pz()/p, p))

    file.close()
