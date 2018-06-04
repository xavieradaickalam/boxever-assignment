# boxever-assignment

Prerequisites: 

  1. Install Python 2.7.13 
  2. set path to python interpretor (i.e c:\software\python27\python.exe)
  3. Optional(for editing) : Install PyCharm Python IDE Community Edition from https://www.jetbrains.com/pycharm
  
Running the script(Windows 10 OS):

  1. Running with default input 

      python seats-allocation.py
	  
  2. Running with input file 

      python seats-allocation.py -i input-data.txt

  Input File content : input-data.txt
  
	    4 4
		1W 2 3
		4 5 6 7
		8
		9 10 11W
		12W
		13 14
		15 16
	  
   Example output :
  
		1W 2 3 8
		4 5 6 7
		11W 9 10 12W
		13 14 15 16
		100%
	  
Improvements :

    1. Algorithm can be improved to work different data
	2. Optimize algorithm to run efficiently (avoid some loops)
    3. Unit Tests	