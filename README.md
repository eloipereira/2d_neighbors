# 2D Neighbors algorithm

Given a list of 2D integer points in a Manhattan grid, return the list of points that are at a given distance of at least one other point.

The script `generate_points.py` generates random 2D points saved in `data/` with the format `data_<Np>_<N>x<M>.txt` where `Np` is the number of points, `N` is the size of the x dimention and `M` is the size of the y dimention. 

The script `2d_neighbors.py` takes as arguments the input file and the distance `dist` and generates an output file with the name `data_<Np>_<N>x<M>_d<dist>_result.txt`

## Example

```
$ python 2d_neighbors.py data/data_12_1000x1000.txt 1
Total number of points: 12
Total number of neighbors: 4
```

The result is saved at `data/data_12_1000x1000_d1_result.txt`.

## Algorithm

The algorithm for finding neighbors takes advantage of the Priority Queue (PQ) data structure. 

First, the data is first pushed into a PQ taking the `x` component as the metric. Next, all the elements are popped forming bands of elements within `dist` in the x dimention. The bands are also PQs but now taking `y` as the metric. At last each band is popped and elements within `dist` in the y dimention are stored in the result file. 