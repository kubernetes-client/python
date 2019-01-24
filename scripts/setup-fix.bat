( 	python --version>nul 2>&1 && (
		echo Python environment found..
	) || (
	    echo Python environment not found..
	)
	python --version
	copy ..\kubernetes\base\* ..\kubernetes\ 
	cd ../ && python setup.py install )
