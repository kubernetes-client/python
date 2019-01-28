(	python --version>nul 2>&1 && (
	echo Python environment found.
	)
	python --version
	copy ..\kubernetes\base\* ..\kubernetes\ 
	cd .. && python setup.py install )
