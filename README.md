# Self-Optimized-Agent-for-Load-Balancing-and-Energy-Efficiency
 We consider the problem of optimization of mobile networks. We aim to enhance the
network throughput, minimize energy consumption, and improve network coverage. The problem is cast
as a reinforcement learning (RL) problem. The reward function accounts for the joint optimization of
throughput, energy consumption, and coverage; our formulation allows the network operator to assign
weights to each of these cost functions based on the operator’s preferences. Moreover, the state is defined
by key performance indicators (KPIs) that are readily available on the network operator side. Finally, the
action space for the RL agent comprises a hybrid action space, where we have two continuous action
elements, namely, cell individual offsets (CIOs) and transmission powers, and one discrete action element,
which is switching MIMO ON and OFF. To that end, we propose a new layered RL agent structure to
account for the agent hybrid space. We test our proposed RL agent over two scenarios: a simple (proof
of concept) scenario and a realistic network scenario. Our results show significant performance gains of
our proposed RL agent compared to some baseline approaches, e.g., a system where no optimization is
carried out or RL agents that optimize only one or two parameters.
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

1- Copy New_agent,TD3 folders to Path_to_NS3_Directory/scratch/. Try not to use nested folders i.e. avoid: scratch/folder1/folder2/file.cc, instead use scratch/folder1/file.cc. 

2- Replace the diectory Path_to_NS3_Directory/scr/lte with the directory inside the archived file in lte(1).zip (Rememebr to backup the original)

3- Copy cell-individual-offset.h and cell-individual-offset.cc to Path_to_NS3_Directoy/src/lte/model/.

4- Copy LTE_Attributes.txt, Real_model-attributes.txt, script_LTE_POCS.sh, script_LTE_RealSce.sh and Power_CIO.sh to Path_to_NS3_Directoy/.

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
  
10- You can configure your own attributes from the (LTE_Attributes.txt, Real_model-attributes.txt)

11- Place the mobility model files in Path_to_NS3_Directory/scratch.

12- To run the Proof of concept scenario. In the directory Path_to_NS3_Directoy:

- right-click to open the terminal and run the command:
     
```
$ ./New_agent.sh
```
For the first run, you may need to run
```
$ chmod +x ./New_agent.sh
```

-To run one episode only run the following command instead:

```
$ ./waf --run "scratch/New_agent/New_agent --RunNum=$(($i))"
```
-Same applies for the TD3 agent by changing New_agent to TD3 when using aformentioned commands
