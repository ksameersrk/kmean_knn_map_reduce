 BDS Assignment 2
---

## Solutions

#### Solution to Question1:

- `driver.py` - The hadoop job starter file. This will keep count of iterations and check for centroids convergence.
- `mapper.py` - mapper file
- `reducer.py` - reducer file
- `utils.py` - utility functions
- `preprocess.py` - The preprocessing script for the mall customers. The output of this script is `input1.txt`.
- `input1.txt` - The output from the preprocessing script.
- `output1.txt` - The output which contains the centroids id, count, objects and value.

#### Solution to Question2:
- `output2.txt` - This contains the labelling for the `output1.txt`.

#### Solution to Question3:
- `preprocess3.py` - The preprocessing script to preprae the input for the problem 3. Combining the `input1.txt`
and the labels.
- `input3.txt` - The input to knn algorithm.