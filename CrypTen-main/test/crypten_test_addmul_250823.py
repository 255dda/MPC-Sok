import time

import crypten
import crypten.mpc as mpc
import crypten.communicator as comm
import torch
import numpy as np

from crypten.config import cfg

cfg.communicator.verbose = True


@mpc.run_multiprocess(world_size=2)
def test_time_and_comm(a, b):
    a_enc = crypten.cryptensor(a)
    b_enc = crypten.cryptensor(b)

    start = time.time()
    start_bytes = comm.get().get_communication_stats()['bytes']
    for i in range(100):
        enc_c = a_enc + b_enc
    end = time.time()
    end_bytes = comm.get().get_communication_stats()['bytes']
    crypten.print(f"[ADD]: Time {(end - start)/100:.4f}s  Comm {(end_bytes - start_bytes)/100 / 1024:.4f} KB")


    start = time.time()
    start_bytes = comm.get().get_communication_stats()['bytes']
    for i in range(100):
        enc_c = a_enc * b_enc
    end = time.time()
    end_bytes = comm.get().get_communication_stats()['bytes']
    crypten.print(f"[MUL]: Time {(end - start)/100:.4f}s  Comm {(end_bytes - start_bytes) /100 / 1024 :.4f} KB")

    start = time.time()
    start_bytes = comm.get().get_communication_stats()['bytes']
    for i in range(100):
        enc_c = a_enc.ge(b_enc)
    end = time.time()
    end_bytes = comm.get().get_communication_stats()['bytes']
    crypten.print(f"[CMP]: Time {(end - start)/100:.4f}s  Comm {(end_bytes - start_bytes)/100 / 1024:.4f} KB")

    start = time.time()
    start_bytes = comm.get().get_communication_stats()['bytes']
    for i in range(100):
        enc_c = a_enc.eq(b_enc)
    end = time.time()
    end_bytes = comm.get().get_communication_stats()['bytes']
    crypten.print(f"[EQ]: Time {(end - start)/100:.4f}s  Comm {(end_bytes - start_bytes) /100 /1024:.4f} KB")


a = np.random.randn(1024)
b = np.random.randn(1024)
test_time_and_comm(a, b)