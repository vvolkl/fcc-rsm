
all: module-sandwich-render CA-cartoon

.PHONY: module-sandwich-render
module-sandwich-render:
	blender -b -P tgeo-blender-plugin/blender-module-sandwich.py
	mv blender-module-sandwich.png tgeo-blender-plugin
	cp tgeo-blender-plugin/blender-module-sandwich.png /afs/cern.ch/work/v/vavolkl/plot/0.9pre/detector-geometry

.PHONY: CA-cartoon
CA-cartoon:
	python CA-cartoon/plot.py
	mv CA-cartoon.png CA-cartoon
	cp CA-cartoon/CA-cartoon.png /afs/cern.ch/work/v/vavolkl/plot/0.9pre/seeding

