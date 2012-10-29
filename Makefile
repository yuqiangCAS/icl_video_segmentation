TOP=$(shell pwd)
export PYTHONPATH:=$(TOP)/src:$(TOP)/tests:$(PYTHONPATH)

shell:
	rm -f .pystart
	echo "from cv2 import *; from VideoWrapper import *" > .pystart
	PYTHONSTARTUP="./.pystart" python 
	rm -f .pystart

cluster:
	python src/FaceClustering.py res/skyfall.mp4

test:
	python -m unittest discover -s 'tests/' -p '*Test.py'
