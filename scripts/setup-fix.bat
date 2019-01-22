if ! [ -x "$(command -v python)" ];
then 
	echo "Python environment notfound.."
else 
	echo "Python environment found.."
fi
python --version
cp -R ../kubernetes/base/* ../kubernetes/
cd ../ && python setup.py install


