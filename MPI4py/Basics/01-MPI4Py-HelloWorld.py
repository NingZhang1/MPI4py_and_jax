from mpi4py import MPI

# MPI point-to-point communication

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11) # return nothing! 
    print('Rank 0 sent:', data)
elif rank == 1:
    data = comm.recv(source=0, tag=11) # return the data, you can pass a buffer This buffer must be sufficiently large to accommodate the transmitted messages
    print('Rank 1 received:', data)
    
# note: 

# Communication of generic Python objects

# there is inner memory copy of the data

