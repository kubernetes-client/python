( 	where python >null
	echo Python environment found..
	python --version
	copy ..\kubernetes\base\* ..\kubernetes\ 
	cd ../ && python setup.py install )
