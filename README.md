# Hierarchical-Multi-Agent-Reinforcement-Learning-Framework-for-Cellular-Mobility-Load-Management

The increasing complexity and density of modern networks necessitate advanced, AI-driven solutions to manage traffic efficiently and maintain high-quality service. In this paper, we present a novel reinforcement learning (RL) framework designed to optimize handover parameters for load balancing in cellular networks. Our framework adopts a \emph{hierarchical multi-agent} RL approach. Closely adjacent cells (a.k.a., cluster) are controlled by cluster-level agents, whereas inter-cluster parameters are controlled by a network-level agent. By intricate design of state spaces and agent communication, both cluster-level and network-level agents work collaboratively to enhance network performance in terms of throughput and coverage. This method reduces the action and state spaces for each agent, facilitating faster learning, scalable network-wide control, and more efficient decision-making. Our simulation results demonstrate significant improvements in downlink throughput with respect to fully decentralized agents. Our approach incurs negligible throughput loss when compared to a fully centralized agent with full knowledge of the entire network. Our approach not only achieves scalable load balancing with minimal overhead but also allows for customizable reward functions tailored to different network needs.

# Installation
## Installing Prerequisites

1- Install Python 3.8.10 (Do Not use the virtual environment)

2- Install [ns-3.30](https://www.nsnam.org/wiki/Installation) (Follow prerequisites steps and then manual installation (Do not use bake)).
 Notice that:  1- some of the packages to be installed are deprecated with higher Ubuntu versions
			         2-(./build.py) is not applicable for versions less than 3.36. skip it and use (Configuration with Waf) commands. 
			         3- Make sure you run (./waf -enable-tests --enable-examples configure) and (./waf build) before running the test (./test.py)

3- Download [ns3gym](https://apps.nsnam.org/app/ns3-gym/). For versions less than 3.36 download the package in this [link](https://github.com/tkn-tub/ns3-gym/tree/app)


4- Follow installation steps: [ns3gym installation](https://github.com/tkn-tub/ns3-gym). For versions less than 3.36 use the instructions in this [link](https://github.com/tkn-tub/ns3-gym/tree/app)


5- Install tensorflow 2.8.0 and keras 2.8.0. (Do Not use the virtual environment, use pip3). 

6- Install [Stablebasline3](https://github.com/DLR-RM/stable-baselines3).

7- Install mobility models from [here](https://drive.google.com/file/d/1fyL4PGqiqbIlOouuoAEH4TrHVXOqhQWG/view?usp=sharing) and [here](https://drive.google.com/file/d/11UdEeDm5oidBuLs9Ud9w5zmWwloGh8Z3/view?usp=sharing) in /Scratch directory
## Installing the code

Note: that ns-3 installtion directory is called Path_to_NS3_Directory.

1- Copy Fully_Decentralized,RealScee,SB_TD3_double folders to Path_to_NS3_Directory/scratch/. Try not to use nested folders i.e. avoid: scratch/folder1/folder2/file.cc, instead use scratch/folder1/file.cc. 

2- Replace the diectory Path_to_NS3_Directory/scr/lte with the directory inside the archived file in lte(1).zip (Rememebr to backup the original)

3- Copy cell-individual-offset.h and cell-individual-offset.cc to Path_to_NS3_Directoy/src/lte/model/.

4- Copy LTE_Attributes.txt, Real_model-attributes.txt, RealSce_1.sh, sb_td3_double.sh and Fully_Decentralized.sh to Path_to_NS3_Directoy/.

5- Copy and replace lte-ue-rrc.cc with Path_to_NS3_Directoy/src/lte/model/lte-ue-rrc.cc (Rememebr to backup the original).

6- Copy and replace lte-enb-phy.cc with Path_to_NS3_Directoy/src/lte/model/lte-enb-phy.cc (Rememebr to backup the original).

7- Copy and replace wscript with Path_to_NS3_Directoy/src/lte/wscript (Remember to backup the original).

8- Rename ns3gym folder to "opengym" and place it in Path_to_NS3_Directory/src.

9- Build ns-3 again by navigating to Path_to_NS3_Directoy and running the commands:
```
$ ./waf configure -d debug --enable-examples --enable-tests
$ ./waf
```
Notice that: If the ./waf command resulted in an error, remove the directory Path_to_NS3_Directory/contrib/opengym from this path
  
10- You can configure your own attributes from the Real_model-attributes.txt

11- Place the mobility model files in Path_to_NS3_Directory/scratch.

12- To run the Fully_Decentralized_Scenario. In the directory Path_to_NS3_Directoy:

- right-click to open the terminal and run the command:
     
```
$ ./Fully_Decentralized.sh
```
For the first run, you may need to run
```
$ chmod +x ./Fully_Decentralized.sh
```

-To run one episode only run the following command instead:

```
$ ./waf --run "scratch//Fully_Decentralized.sh/Fully_Decentralized.sh --RunNum=$(($i))"
```
-Same applies for other agents agent by changing Fully Decentralized to (sb_td3_double or RealSce_1) when using aformentioned commands

-After Running the simulator run agent/s in thier respective folders using following command:
	python3 "agent python file"
 
Fully_Decentralized : agent1-6.py
sb_td3_double : agent1-3.py
RealSce_1 : Agent_TD3.py

