all: 
	javac PACE2017-TrackA/tw/exact/*.java
	cd PACE2017-TrackA/ && jar cvf ../tamaki_solver_wrapper/jar/tamaki_solver.jar tw/exact/*.class
	python3 -m build
