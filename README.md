# MPC-Sok
We evaluate both execution time and communication overhead under two network conditions: LAN and WAN. Network environments are simulated using the $\mathtt{tc}$ command, with LAN configured to 0.1 ms RTT and 1 Gbps bandwidth, and WAN to 80 ms RTT and 40 Mbps bandwidth.

We introduce how we evaluate the basic operations in frameworks one by one.
# ABY

# YACL
We test basic operations in the repository McPSI (https://github.com/liang-xiaojian/McPSI/blob/e178237c34d78015d474528fda6b33bec15c9588/mcpsi/utils/vec_op.cc#L4), which is implemented based on YACL. 

# MP-SPDZ
We test basic operations (+, *) in the malicious setting, for 128-bit input values.

# osu-crypto
We formalize basic operations based on the AND gate implemented in the repository batchDualEx (https://github.com/osu-crypto/batchDualEx).

# EMP-toolkit
