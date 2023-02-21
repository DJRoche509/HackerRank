Suppose there is a circle. There are **N** petrol pumps on that circle. Petrol pumps are numbered **0** to **(N-1)**
(both inclusive). You have two pieces of information corresponding to each of the petrol pump: 
(1) the amount of petrol that particular petrol pump will give, and (2) the distance from that petrol pump to the next petrol pump.

Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol
pumps. Calculate the first point from where the truck will be able to complete the circle. Consider that the
truck will stop at each of the petrol pumps. The truck will move one kilometer for each litre of the petrol.
Input Format
The first line will contain the value of **N**.
The next **N** lines will contain a pair of integers each, i.e. the amount of petrol that petrol pump will give and
the distance between that petrol pump and the next petrol pump.

Constraints:

- **1 < N < 10<sup>5</sup>** 

- **1 < amount of petrol, distance < 10 <sup>9</sup>** 
<br>

Output Format: <br>
An integer which will be the smallest index of the petrol pump from which we can start the tour.

<br> <br>
In this program, the steps below are implemented as a solution:

  - The first possible petrol pump where the amount of petrol is greater than the distance to the next petrol pump is found.
  - Traverse from i = start to N:
    - If the amount of petrol becomes inefficient (i.e., negative) we need to update the new start point.
      - Traverse from i+1 to N and find the point where petrol is greater than the distance to the next petrol pump.
    - Start from the new start point and continue the above procedure.
  - Start from 0 to the found start point. If the sum of the petrol is non-negative then the start point is feasible otherwise not.
<br>

![Screenshot 2023-02-20 10 58 35 PM](https://user-images.githubusercontent.com/100164051/220252953-a2283f24-3e72-49ca-94e9-d2bd66665556.png)
