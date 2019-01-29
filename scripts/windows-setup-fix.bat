(	python --version>nul 2>&1 && ( REM checks the availability of python environment
	echo Python environment found. REM prints if python environment is found
	)
	python --version REM prints python environment version
	copy ..\kubernetes\base\* ..\kubernetes\ REM copies every file and folder that's inside \kubernetes\base\ to \kubernetes\	
	cd .. && python setup.py install ) REM runs setup.py file
