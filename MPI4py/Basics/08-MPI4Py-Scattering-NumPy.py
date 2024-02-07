from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

sendbuf = None
if rank == 0:
    sendbuf = np.empty([size, 100], dtype='i') # note the order of the dimensions, the first dimension is the number of processes
    sendbuf.T[:,:] = range(size)
recvbuf = np.empty(100, dtype='i')

comm.Scatter(sendbuf, recvbuf, root=0) # sendbuf and recvbuf must be different, unlike broadcast, scatter sends different data to different processes

assert np.allclose(recvbuf, rank)

print("Rank", rank, "received", recvbuf) # even the master rank 0 receives a piece of the data

