from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = [(i+1)**2 for i in range(size)]
else:
    data = None
data = comm.scatter(data, root=0) # Scatter data from rank 0 to all processes, unlike broadcast, scatter sends different data to different processes

print("Rank", rank, "received", data) # even the master rank 0 receives a piece of the data

assert data == (rank+1)**2