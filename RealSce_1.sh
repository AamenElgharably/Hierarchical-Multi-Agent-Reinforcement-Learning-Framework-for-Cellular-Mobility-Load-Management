#! /bin/bash
for i in {1..600}
do
	./waf --run "scratch/RealSce_1/RealSce_1 --RunNum=$(($i))"
done
