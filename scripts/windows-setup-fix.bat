(	python --version>nul 2>&1 && ( & :: checks for the availability of python environment
	echo Python environment found.	& :: prints if python environment is found
	)
	python --version	& :: prints python environment version
	copy ..\kubernetes\base\* ..\kubernetes\ 	& :: copies every file & folder that's inside \kubernetes\base\ to \kubernetes\	
	cd .. && python setup.py install )	& :: runs setup.py file
