REM Install python client in Windows.
REM Windows doesn't have symbolic link that this repo uses.
REM This batch script provides a workaround for symbolic link by copying the folders over.

 (	python --version>nul 2>&1 && (
	echo "Python environment found."
	)
	python --version
	copy ..\kubernetes\base\* ..\kubernetes\
	cd .. && python setup.py install )