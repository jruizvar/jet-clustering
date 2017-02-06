# Jet clustering with [scikit-learn](http://scikit-learn.org)

-   Instruction to setup working area and produce the csvFiles

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cmsrel CMSSW_8_0_26_patch1
cd CMSSW_8_0_26_patch1/src
cmsenv
mkdir csvFiles; python jetConstituents.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Exploring csv files
===================

Each csv file contains the list of jet constituents with kinematic information necessary to seed the clusterization algorithm later on. Example: 

-   [1_1_1.csv](csvFiles/1_1_1.csv)

The momentum coordinates are normalized such that Px * Px + Py * Py + Pz * Pz = 1.

Analysis of csv files
=====================

Each csv file is analysed with the code

-   [analyze_csvFiles.py](analyze_csvFiles.py)

The requirements to execute the code are

-   Pandas Data Analysis Library (http://pandas.pydata.org)
-   Machine Learning in Python (http://scikit-learn.org)
-   Python 3.X (https://www.python.org/downloads/)

Example of output:

![](outPlots/1_1_1.png)
