# What is Time Complexity 🤔
- The code we write it is judged on Time Complexity and Space Complexity.
- A code runs on a machine takes 2s,3s,4s . So time taken will it be the time complexity. No,  it won't.
- ***TC != Time Taken***.

- Suppose we have a cold macbook and a new macbook , newer macbook has lastest configurations and runs the particular code in 1s and the older runs the code on its machine in 2s. Thats the reason TC is not dependent on the time taken.

- ***The rate at which the time taken increases with the respect to input size is called Time Complexity.***

- So hence, we dont use 2s , 3s, 4s to express the time complexity.
- We use **Big O notation** to express the time complexity. Big O notation is used to express the Time Complexity Expression : `O( )` here inside the brackets we can mention the time taken.

- Big O of a particular syntax :
             ```javascript
  #1 for(let x = 0; x < 5; x++ ){
  #2              console.log(x)
  #3 }