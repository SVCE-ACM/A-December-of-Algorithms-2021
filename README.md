<div align="left">
<h1>
    <img alt="header" src="/src/assets/header.png" width="1200"></img>
</h1>
Welcome to A December of Algorithms (2021). After overwhelming responses from previous years, we present you with a new collection of algorithms to implement this December. Each Day, Each Algorithm ;) Finish them all to get a certificate :)

**Send a pull request only after completing all 31 algorithms.**

**Please submit all PRs on or before January 10th 11:59 PM IST.**

## What Do I Do?
We have a small collection of algorithms, one for every day of the month. Scroll down to take a look at them. All you need to do is fork this repository, implement all 31  algorithms and send a pull request over to us. Check out our FAQ for more information.

## Index
  - [**December 1 - Elegant facelift**](#december-1---elegant-facelift)
  - [**December 2 - Bingo!**](#december-2---bingo)
  - [**December 3 - Lotto!**](#december-3---lotto)   
  - [**December 4 - Sandhya and her Tic-Tac-Toe love**](#december-4---sandhya-and-her-tic-tac-toe-love)
  - [**December 5 - Biscuit Bonanza**](#december-5---biscuit-bonanza)
  - [**December 6 - Save The Templars**](#december-6---save-the-templars)
  - [**December 7 - Amy helps Pawnee**](#december-7---amy-helps-pawnee)
  - [**December 8 - Anomalous Counter**](#december-8---anomalous-counter)
  - [**December 9 - Dream 11**](#december-9---dream-11)
  - [**December 10 - Juicy Orange Field**](#december-10---juicy-orange-field)  
  - [**December 11 - Maze Festival**](#december-11---maze-festival)
  - [**December 12 - Ford vs Ferrari**](#december-12---ford-vs-ferrari)
  - [**December 13 - Desert Shopping**](#december-13---desert-shopping)
  - [**December 14 - The Math Test**](#december-14---the-math-test)
  - [**December 15 - Twinkling Bracelets**](#december-15---twinkling-bracelets)  
  - [**December 16 - Catch Me If You Can**](#december-16---catch-me-if-you-can)
  - [**December 17 - The Bossy Manager**](#december-17---The-Bossy-Manager)
  - [**December 18 - Connections**](#december-18---Connections)
  - [**December 19 - Winter is coming**](#december-19---winter-is-coming)
  - [**December 20 - High Traffic Server(s)**](#december-20---high-traffic-servers)
  - [**December 21 - Transform to Checkerboard**](#december-21---transform-to-checkerboard)
  - [**December 22 - Richie Rich**](#december-22---richie-rich)
  - [**December 23 - Ant Got Track**](#december-23---ant-got-track)
  - [**December 24 - Mayday Mayday!!**](#december-24---mayday-mayday)
  - [**December 25 - Ranthambore Diaries**](#december-25---ranthambore-diaries)
  - [**December 26 - Bellisima Florencia**](#december-26---bellisima-florencia)
  - [**Maintainers**](#maintainers)
  - [**FAQ**](#faq)


## Algorithms

 ### December 1 - Elegant facelift
 
   #### Problem Statement
   - There is a collection of necklaces where each necklace has various stones embedded in it. Each type of stone is designated by a lowercase letter in the range ascii `[a-z]`.
   - There may be multiple occurrences of a stone in a necklace. A stone is called a `facelift` if it occurs at least once in each of the necklaces in the collection.
   - Given a list of stones embedded in each of the necklaces, display the number of types of `facelift`'s in the collection.

   <p align="center"><img src="https://media3.giphy.com/media/nxgSkZNaOFMoo/giphy.gif?cid=ecf05e47lvyzgys0csclvx3lnblvzgr2q32yk6vr1euioe7n&rid=giphy.gif&ct=g"></p>
   
   #### Sample Input/Output
   ```
      Input: arr = ['abcdde', 'baccd', 'eeabg']             
      Output: 2           
   ```
   ```
      Input: arr = ['abc', 'def', 'ghi', ‘jkl’]                    
      Output: 0
   ```  
   #### Explanation   
   - In sample input 1, only `a` and `b` occur in every necklace. Therefore, the output is `2`.
   - In sample input 2, there are no characters repeating in the list. Therefore, the output is `0`.  
   
----
  
 ### December 2 - Bingo!
  
  #### Problem Statement
   - Your local community conducts a game night every Saturday and they want you to lead a game of Bingo this weekend. You must come up with numbers to be read out during the     game. The numbers can be chosen on the basis of certain criteria.  
   - Begins with a positive integer, sum of squares of digits must replace the number. Continue until the number is 1 or loops interminably without including 1. 
   - The numbers which end in 1 are to be selected. Return ‘YES’ if the number is selected, and ‘NO’ if not.

     <p align="center"><img src="https://i.makeagif.com/media/8-14-2017/ZtZuZT.gif" /></p>    
  
  #### Sample Input/Output
  ```
  Input: n = 2
  Output: NO
  ```
  ```
  Input: n = 19
  Output: YES
  ```

  #### Explanation
  ```
   1^2 + 9^2 = 82
   8^2 + 2^2 = 68
   6^2 + 8^2 = 100
   1^2 + 0^2 + 0^2 = 1
   ```   
   
   #### Resources
  - [Detecting loops](https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/)
  - [Unordered Hash sets in C++](https://www.geeksforgeeks.org/unordered_set-in-cpp-stl/)
  - [Sets in python](https://www.geeksforgeeks.org/sets-in-python/)
----

### December 3 - Lotto!
  
  #### Problem Statement
  - In a lottery game , each participant can choose a lucky board which is in the form of a 2D `(x x y)` grid. He/she can win the lottery if they are able to find their name on    the lucky board. Find whether a particular participant can win the game or not. Assume that there can be more than one winner who wins the lottery. 
  - Return true if the participant wins else return false
 
  ### Rules:
  - The name of the participant has to be arranged in a sequentially adjacent manner.
  - The  neighbouring alphabets can be horizontal as well as vertical
  - Same alphabet cell cannot be used more than once while forming the name.
        
  <p align="center"><img src="/src/assets/input1.png" /></p>
  
  #### Sample Input/Output
  ```
  Input: [["D","J","O","G"],["W","B","H","S"],["T","Z","N","E"]], name = "JOHN"
  Output: true
  ```
   <p align="center"><img src="/src/assets/input2.png" /></p>
     
  ```
  Input: [["L","N","A","C"],["W","B","A","D"],["T","Z","F","E"]], name = "DEV"
  Output: false
  ```

  #### Resources
  - [Backtracking](https://www.geeksforgeeks.org/backtracking-algorithms/)

---
### December 4 - Sandhya and her Tic-Tac-Toe love
  
  #### Problem Statement
  - Sandhya likes to play tic-tac-toe (using `2x2` matrix), and uses the elements `0`and `1`. She is wondering how many matrices with `X` rows and `Y` columns there are. Everyone obviously knows that - it is just `2X⋅Y`. But what no one knows is that, she considers two identical matrices if and only if by permuting the `X` no.of rows and then permuting the `Y` no.of columns, and the resulting matrix is transverse of itself. 
  - Help Sandhya by finding the number of `X×Y` matrices which are distinct according to her definition (even though she doesn't know how to solve them). Since the answer can/may be quite large, compute it modulo 10^9+7.
       
   <p align="center"><img src="https://media.giphy.com/media/3oriNKQe0D6uQVjcIM/giphy.gif" /></p>
  
  #### Sample Input/Output
  ```
  Input: 1 5
  Output: 6
  ```
  ```
   Input: 10 10
   Output: 508361223
  ``` 
  
   #### Explaination
   ```
   According to Sandhya's definition, there are 6 different binary matrices. 
   This is because the number of 1-s uniquely identifies a 1×5 matrix and 
   the number of 1-s can take any value between 0 and 5 inclusive.
   ```            
---

### December 5 - Biscuit Bonanza
 
   #### Problem Statement
   - A local biscuit store sells only `2` types of biscuits: circular and rectangular biscuits. They are referred to by the numbers `0` and `1` respectively. The customers stand in a queue and they either purchase circular or rectangular biscuits. 
   - The number of biscuits is equal to the number of customers. They are placed in a stack. 
   - At each step: If the customer at the front of the queue prefers the biscuit on the top of the stack, they will take it and leave the queue.
   - Otherwise, they will directly go to the queue's end.
   -  Consider two integer arrays `customers` and `biscuits` where `biscuits[i]` is the type of the `i`th biscuit in the stack (i = 0 is the top of the stack) and `customers[j]` is the preference of the `j`th customer in the initial queue (j = 0 is the front of the queue). This continues until none want to take the top biscuit and are thus unable to eat.
   -  Return the number of customers that are unable to eat.

   <p align="center"><img src ="https://media.giphy.com/media/nAErqE3k2C3fy/giphy.gif" /></p>                  
   
   ### Sample Input and output
   ```
   customers = [1,1,1,0,1]
   biscuits = [1,0,0,0,1,1]
   
   Customers that are unable to eat = 3
   ```
   ```
   customers = [1,1,0,0]
   biscuits = [0,1,0,1]
   
   Customers that are unable to eat = 0
   ```   
   ```
   customers = [1,1,0,0,1,0]
   biscuits = [0,1,0,1,1,1]
   
   Customers that are unable to eat = 1
   ```   
   ### Explanation
   ```
   Input: customers = [1,1,0,0], biscuits = [0,1,0,1]
   Output: 0 
   - Front customer leaves the top biscuit and returns to the end of the line making customers = [1,0,0,1].
   - Front customer leaves the top biscuit and returns to the end of the line making customers = [0,0,1,1].
   - Front customer takes the top biscuit and leaves the line making customers = [0,1,1] and biscuits = [1,0,1].
   - Front customer leaves the top biscuit and returns to the end of the line making customers = [1,1,0].
   - Front customer takes the top biscuit and leaves the line making customers = [1,0] and biscuits = [0,1].
   - Front customer leaves the top biscuit and returns to the end of the line making customers = [0,1].
   - Front customer takes the top biscuit and leaves the line making customers = [1] and biscuits = [1].
   - Front customer takes the top biscuit and leaves the line making customers = [] and biscuits = [].
   Hence all customers are able to eat.
   ```   
   #### Resources
   - [Queues using Arrays](https://www.geeksforgeeks.org/queue-set-1introduction-and-array-implementation/)
   - [Queues using Linked List](https://www.geeksforgeeks.org/queue-linked-list-implementation/?ref=rp)
---
### December 6 - Save The Templars

### Problem Statement
  - The conflict continues. The Templar Assasins `T` and the Undying `U` are fighting to the death, but the bad is prevailing over the good. The Templars must band together in order to combat the Undying.
- At the top of the Undying Resource tower, everyone is initially arranged in a circular path.
- The Templar Assassin at index 1 is in front of the Templar Assassin at index 2 and stands close to the Templar Assassin at index `n`.
- The Templars must band together in order to win the battle.
- The Templars have a particular ability that allows them to switch bodies with anyone.
- Assist the Templars in determining the least number of swaps required so that they can all stand together.
- Given the sequence of Templar Assasins `T` and the Undying `U`, return the minimal number of swaps required. 

<p align="center"><img src ="/src/assets/templars.gif" /></p>

#### Sample Input and Output
 ```
 Input: UUTUTUT
 Output: 1
 ```
 ```
 Input: UTUTTU
 Output: 1  
 ```
 ### Explanation
 ```
 To get all U and T together in the sample test case, first replace the T at index 3 with U at index 6.
 Second, we can combine all U and T by swapping U at index 3 with T at index 2.
 ```
---

### December 7 - Amy helps Pawnee!

 #### Problem Statement
 - Amy Santiago is a pilot and she went to Pawnee for official work. She noticed that the city had a food shortage due to the devastating impact of COVID-19. So, she decided to help the people who are in desperate need of food by supplying them on their building with the help of her private jet-plane. 
 - All the buildings are represented by three pairs of points: `(a1, b1), (a2,b2) and (a3,b3).`
 - The jet can fly in a direction either parallel to the `x` axis or the `y` axis. It drops the food packets on every building Amy flies over in her flight. 
 - The food packet will be wasted if it is dropped on the boundary of the building as it will fall down. No two buildings touch each other. Figure out the number of buildings that receive the food packets on each flight. 
 -  A single line integer i.e the number of buildings that received the food packets on their roofs on each flight.  
 
<p align="center"><img src ="https://media.giphy.com/media/8PKXkHuRl5ht8BvXrO/giphy.gif" /></p> 

#### Sample Input and Output
 ``` 
 Number of Buildings: 3
 Coordinates of the buildings:
 1 0 0 2 2 2
 1 3 3 5 4 0 
 5 4 4 5 4 4
 Number of jet-planes: 3
 x = 1
 x = 2
 y = 1
 
 Buildings that received food:
 1
 1
 2
 ```
 ```
 Number of Buildings: 4
 Coordinates of the buildings:
 1 1 2 3 4 1
 2 5 3 3 0 0
 3 2 2 1 1 3
 4 5 5 0 1 0
 Number of jet-planes: 2
 x=1
 y=3

 Buildings that received food:
 1
 2
 ```
---
### December 8 - Anomalous Counter

   #### Problem Statement
   - You found a rather bizarre counter around your area. You see that there are two dials, one is the cycle dial and another is the counter value dial. 
   - When you start the counter, you see in the counter dial that it starts with the initial value 3 and then you see the counter value decreases by 1 each second until the value becomes 1.
   - In the next second you see that the cycle dialer is incremented to 1 and the counter value becomes twice the initial value of the counter in the previous cycle.
   - You decided to invite your friends to play a guessing game, i.e to find the value displayed by the counter at a particular time(in seconds). 


   <p align="center"><img src ="/src/assets/counter.png" /></p>                  

   ### Sample Input and output
   ```
   Input: time = 22   
   Output: counter value = 24
   ```
   ```
   Input: time = 0
   Output: counter value = 0
   ```

   ### Explanation
   ```
   Input: time = 22
   Output: 24
   
   time=22 marks the beginning of the fourth cycle. 
   So the counter value is double the number displayed at the beginning of the third cycle(when time=10): 12X2 = 24.
   This is shown in the diagram in the problem statement.
   ```   

---
### December 9 - Dream 11

   #### Problem Statement
    - As a Cricket coach, you have to pick `P` understudies to address your school. There are `N` understudies. 
    - The aptitude rating of `N` understudies has been given as input, which is a positive number indicating how gifted they are. Right away, it likely will not be possible to pick a sensible gathering, so you will give a piece of the understudies one-on-one educating. 
    - It requires one hour of preparing to extend the ability rating of any understudy by 1. The resistance season is starting very soon, so you'd like to notice the base number of extensive stretches of guidance you need to give before you can pick a sensible gathering.
    - Output the base number of long periods of instruction required, before you can pick a reasonable group of `P` understudies.

   <p align="center"><img src ="https://media.giphy.com/media/kBf6l8fkDWiWfDhdNu/giphy.gif" height = "300"/></p> 
 
   ### Sample Input and output

   ```
   N = 4, P =3   
   N = [3, 1, 9, 100]
   
   Base number of periods required = 14
   ```
   ```
   N = 6, P = 2
   N = [5, 5, 1, 2, 3, 4]
   
   Base number of periods required = 0
   ```
   ```
   N = 5, P = 5
   N = [7, 7, 1, 7, 7]
   
   Base number of periods required = 6
   ```     
---
### December 10 - Juicy Orange Field

   #### Problem Statement
   - You are in a field of juicy oranges that is like a grid of size `n x n`. You plan to collect most of the oranges in the field before the storm comes. Each cell can be any one of the following:
        - A cell can be empty (represented by 0), so you can pass through the cell.
        - A cell that contains the orange trees where you can pick up the oranges and pass through to the next cell. (represented by 1)
        - A cell covered with prickles and thorns that blocks your way to the next cell (represented by -1).
   - As it’s a big field you have to follow certain rules to find the maximum number of oranges you can collect before the storm hits:-
        - You begin at the first cell and you have to reach the last cell by moving right or down through valid cells (cells that do not contain prickles and thorns).
        - After reaching the last cell, you have to return to the first cell by moving left or up through valid cells.
        - When passing through a cell containing oranges, you pick it up, and the cell becomes an empty cell.
        - If there is no valid path between the first and last cell, then no oranges can be collected.
  
   <p align="center"><img src ="/src/assets/orangefield.gif" height = "300"/></p> 
 
   ### Sample Input and output

   ```
   Input: field = [[0,1,-1],[1,0,-1],[1,1,1]]
   Output: 5
   ```
  
  ### Explanation
   ```
   Input: field = [[0,1,-1],[1,0,-1],[1,1,1]]
   Output: 5
   
   You started at (0, 0) and went down, down, right right to reach (2, 2).
   4 oranges were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
   Then, the player went left, up, up, left to return home, picking up one more orange.
   The total number of oranges picked up is 5, and this is the maximum possible.
   ```      
---
### December 11 - Maze Festival

   #### Problem Statement
   - On the occasion of Halloween, a grand corn maze puzzle has been set up in the fields of **Hubb’s farm, New York**. There are several mystery boxes hidden at each magic spot. 
   - Assume that there are `N` magic spots from `1` to `N` in the entire field.
   - Given the points to the spots `P` and `Q` and the distance between them `D` and also a participant who choses the starting spot `A`, the path chosen to reach the final spot `B` and the final magic spot `C`.
   - Identify whether the participant can reach the destination spot or not.   
   - If yes print the minimum distance(shortest path) covered and the path taken by the participant to reach the final magic spot. Else print **"NO PATH FOUND”**.
  
   - Note: If a pathway connects `A` to `B` with distance `D` then it means that it will connect from `B` to `A` with the same distance `D`.
      <p align="center"><img src ="/src/assets/corn-maze.gif" height = "300"/></p> 

   ### Sample Input and output

   ```
    Input:    
    N = 6
    
    P Q D
    1 2 2
    2 5 5
    2 3 4
    1 4 1
    4 3 3
    3 5 1
    
    A = 1, B = 3, C = 6
    
    Output: No path found
   ```
   ```
    N = 10
    
    P Q D
    1 5 78
    1 8 221
    2 7 92
    2 8 159
    3 5 55
    3 6 179
    3 10 237
    4 8 205
    5 6 191
    8 10 157
    
    A = 6, B = 3, C = 2 

    Output: Shortest path = 692
           Path taken = 6 3 5 1 8 2
   ```
  ### Explanation
   ```
    Input:
    N = 10
     
    P Q D
    1 5 78
    1 8 221
    2 7 92
    2 8 159
    3 5 55
    3 6 179
    3 10 237
    4 8 205
    5 6 191
    8 10 157
    
    A = 6, B = 3, C = 2
    Output: Shortest path = 692
            Path taken = 6 3 5 1 8 2
            
  - In the 2nd test case there are 10 magic spots and 10 number of pathways which connects the spots.
    The next 10 lines of input contains 3 numbers representing the names of start spot,
    and destination spot, distance between them 
    for example, for the first magic spot
     - starting spot is 1
     - passing through spot is 5 
     - distance between 1 and 5 is 78
                                        1
                                      /  \    
                                4 - 8     6 - 5   
                                   / \     \ /
                                  2   10  -  3     
                                 /            
                                7
  - For the user's input 6, 3, 2 representing starting, passing through,destination spots respectively there exits a shortest path to reach spot 2 from spot 6 passing through spot 3.
  - The minimum distance travelled is 692
  - Path followed is 6->3->5->1->8->2             
   ```   
   
   #### Resources
  - [Graphs](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)
  - [DFS traversal](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)
  - [BFS traversal](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
---
### December 12 - Ford vs Ferrari

  ### Problem Statement
  - Two friends Carroll Shelby and Ken Miles are playing a game where they arrange all the toy cars in a row and run them in random directions. 
  - Each car has a certain superiority level associated with it and both max and sergio are aware of the superiority levels. They want to know the state of cars once they move       them.
  - We are given an array `cars` of integers representing cars in a row. For each car, the absolute value represents its superiority, and the sign represents its direction (positive meaning right, negative meaning left). 
  - Each car moves at the same speed. Find out the state of the cars after all collisions. 
  - If two cars meet, the less superior one will break. If both are of the same superiority, both will break. Two cars moving in the same direction will never meet.
     <p align="center"><img src ="https://media1.giphy.com/media/mNT2zQTgAEY5q/giphy.gif?cid=ecf05e4743w1a4914iot1yt8hkqfk8cvsosad4uhxe4uzgtz&rid=giphy.gif&ct=g" height =             "300"/></p> 
  
  ### Sample Input and Output
  
   ```
   Input: cars = [4,8,-2]
   Output: [4,8]
   ```
   ```
   Input: cars = [5,-5]
   Output: []    
   ```
   ```
   Input: cars = [10,2,-5]
   Output: [10]    
   ``` 
    
  ### Explanation
   ```
    Input: cars = [4,8,-2]
    Output: [4,8]
    
    - The car with superiority level 8 and -2 collide resulting in car with superiority level 8. 
    - The cars 4 and 8 never collide because they are moving in the same direction.        
    - Therefore, the ouptut is [4,8]    
   ```
   
<details>
    <summary>
        <strong>Resources (Spoiler)</strong>
    </summary>
    <ul>
        <li><a href="https://www.geeksforgeeks.org/stack-data-structure/">Stack</a></li>        
    </ul>
</details>

---    

### December 13 - Desert Shopping 

  #### Problem Statement 
   - You are a diamond merchant in Dubai. You have `x` unsold diamonds, and each diamond `p` has a purity level `mₚ`, and a minimum price `nₚ`.
   - You also have `z` clients, and each client `j` wants a diamond with a purity greater than `kⱼ` and a price **less than or equal to** `rⱼ`.
   - Each client can buy at most one diamond, and each diamond can have at most one buyer. What is the maximum number of diamonds you can sell?
     <p align="center"><img src ="https://media4.giphy.com/media/xT5LMRMGxjCAX5LaGQ/giphy.gif?cid=ecf05e47d5prkcverwbbuqnkq3epxahaah7dwxk7j7y61u4v&rid=giphy.gif&ct=g"                 height ="300"/></p>     
   
   ### Sample Input/Output
   
   ```
     Input:
     z = 3, x = 3
     k₀ = 5, r₀ = 110
     k₁ = 9, r₁ = 500
     k₂ = 20, r₂ = 400
     m₀ = 10, n₀ = 100
     m₁ = 2, n₁ = 200
     m₂ = 30, n₂ = 300
     
     Output: Maximum number of diamonds sold = 2
   ```
   ```
     Input:
     z = 2, x = 2
     k₀ = 3, r₀ = 100
     k₁ = 5, r₁ = 150
     m₀ = 4, n₀ = 145
     m₁ = 2, n₁ = 80
     
     Output: Maximum number of diamonds sold = 2
   ```
  ### Explanation
  ```
   In case 1:
     - Client 0 will be interested in diamond 0 because it has more than k₀ = 5 units of purity and costs less than r₀ = 110 . 
     - Both of the other diamonds are outside of this client's price range.
     - Client 1 will be interested in diamonds 0 and 2 , as both these diamonds have more than k₁ = 9 units of purity and cost less than r₁ = 500 .
     - They will not be interested in the remaining diamonds because it's less pure.
     - Client 2 will be interested in diamond 2 because it has more than k₂ = 20  units of purity and costs less than r₂ = 400 . 
     - They will not be interested in the other two diamonds because they are less pure.
     - All three clients are interested in the same two houses, so you can sell at most two houses in the following scenarios:
     - Client 0 buys diamond 0 and client 1 buys diamond 2.
     - Client 1 buys diamond 0 and client 2 buys diamond 2.
     - Client 0 buys diamond 0 and client 2 buys diamond 2 .
     - Thus, we print the maximum number of diamond you can sell, 2, on a new line.            
   ```
---    

### December 14 - The Math Test
   
   #### Problem Statement
  - Amy has her Math exam tomorrow and she has not prepared for it. 
  - There are `n` chapters in her book and `i`th chapter has chapter `i` concepts. She has `x` hours to prepare for the exam. She decides that she can study `y` number of concepts from the chapters in each hour. 
  - If a chapter has less than `y` concepts, then she will cover all the concepts of that chapter and take a break for the rest of the hour.
  - Return a minimum integer `y` such that she covers all the chapters of her Math book within `x` hours.         
   <p align="center"><img src ="https://media3.giphy.com/media/JRPftUYuIRw3axuh5y/giphy-downsized-large.gif" height ="300"/></p>     
      
   #### Sample Input/Output
   ```
   Input: chapter = [3,6,7,11], x = 8
   Output: 4
   ```
   ```
   Input: chapter = [30,11,23,4,20], x = 5
   Output: 30
   ```
  
   #### Explanation
   ```
   She can study 4 concepts from her chapters per hour such that, she can cover all the concepts from the chapters within 8 hours.
   ```   
---
### December 15 - Twinkling Bracelets
   
   #### Problem Statement
  - Pinky is a college student who works for her mom’s online Bracelet store and sells amazing collections of bracelets on a daily basis.
  - She takes a maximum number of `n` days for the bracelets to be delivered to the customers. 
  - The `i`th customer has ordered `i` number of bracelets.
  - She prepares the bracelets according to the order in which she received the bookings. She schedules a maximum number of bracelets to be made and delivered in a day, such that she has sufficient time to manage her college work. 
  - Return the least number of bracelets that can be made in a day for them to be delivered in n days.      
   <p align="center"><img src ="https://media3.giphy.com/media/3ohhwsUruCzuLhvjuU/giphy.gif" height ="300"/></p>   
     
   #### Sample Input/Output
   ```
   Input: number of bracelets = [3,2,2,4,1,4], n = 3
   Output: 6
   ```
   ```
   Input: number of bracelets = [1,2,3,1,1], n = 4
   Output: 3
   ```  
   #### Explanation
   ```
   Pinky can make 6 bracelets and deliver them in a day such that she delivers all the orders within 3 days.

   Day 1:  3, 2
   Day 2:  2, 4
   Day 3:  1, 4
   ```  
---
### December 16 - Catch Me If You Can 
 
   #### Problem Statement 
   - Leo is a lion that escaped from the zoo, and `X` forest rangers are up for catching him. 
   - The rangers want to catch Leo no matter the cost, and Leo also wants to eliminate as many rangers as possible (preferably everyone) before getting caught (or before running      away after eliminating everyone). Neither the rangers nor Leo will run away before accomplishing their goals.
   - Leo and the officers are on a one-dimensional grid with coordinates ranging from `−10¹º to 10¹º`. Leo is initially standing at coordinate `A`, and the `i`th ranger is initially at coordinate `Ci`. The rangers and Leo then take turns to move, with the ranger team moving first.
   - During their turn, rangers will have to move to an adjacent unoccupied cell one by one, in any order they want. Every ranger will have to move. At every moment of time, no      two rangers can be in the same cell, and also no ranger can be in the same cell as Leo. 
   - If the ranger is unable to move to an adjacent unoccupied cell, he is eliminated (and the cell he was in becomes unoccupied). Note that the ranger team will try to move to      eliminate as few rangers as possible. 
   - After the ranger team's turn, Leo also moves to an adjacent unoccupied cell, or gets caught if he cannot find any adjacent unoccupied cell. 
   - The process then repeats until either Leo is caught, or all rangers are eliminated and Leo runs away.
   - You need to find out the maximum number of rangers that can be eliminated by Leo, and if Leo can run away or not.
  
     <p align="center"><img src ="https://media.giphy.com/media/TSUqYlyxpfgfC/giphy.gif" width="320" height ="300"/></p> 
  #### Sample Input/Output
     
  ```
  Input:
   T = 1, X = 2, A = 2
   (C1 C2) = 1 4
   
  Output:
   1 -1
  ```
  ```
  Input:
   T = 1, X = 1, A=2    
   (C1 C2) = 1 
   
  Ouput:
   1  1    
  ```
     
  #### Explanation
      
   ```
   For test case 1:
      - Leo chooses to always move to the left (i.e. to the smaller coordinate); this forces the ranger at coordinate 1 to always move to the left, and eventually being 
        cornered and eliminated.
      - However, the officer at coordinate 4 cannot be eliminated, and hence Chef will be caught at the end.
        For test case 2:
        Similarly, Leo chooses to always move to the left, and eventually eliminating the only ranger, thus running away at the end.       
   ```
---

   ### December 17 - The Bossy Manager
  
  #### Problem Statement
  - Ram is an assistant manager in the bank. His boss, is very bossy and assigns him to tasks and asks him to complete them as soon as possible. 
  - This manager also has some parameters which are assigned to each and every task which he has to note. They are:
    - The maximum number of tasks he can complete in a single go
    - The time taken to complete the single task for that job
    - The number of tasks each job can process
  - And at last the manager asks Ram to calculate the minimum time needed to process a set of tasks for the given job. Ram did a course on data structures and using his knowledge on this subject he plans to complete this task in less time. Try helping Ram out and see if he can outwit his manager!

   <p align="center"><img src="https://media.giphy.com/media/YwpylUojkfOZa/giphy.gif" /></p>    
    
#### Sample Input/Output:
  ```
  Input:  
  Task size = [3,2,5,7]
  Processing time = [5,4,10,12]  
  Number of tasks = [10,6,10,5]

  Output: The minimum time to process all the tasks is 20.
  ``` 
  ```
  Input: 
  Task size = [4,3]
  Processing time = [6,5]
  Number of tasks = [8,8]
  
  Output: The minimum time to process all the tasks is 15.
  ```
#### Explanation:
  ```
  n=2
  Task size = [4,3]
  Processing time = [6,5]
  Number of tasks = [8,8]

  Queue 0 can process a maximum of 4 tasks in 6 minutes, and queue is 1 can process a maximum of 3 tasks in 5 minutes. Each queue has 8 tasks to process. The time required to perform the assigned tasks in the minimum possible time is calculated as follows:

  For queue 0:
  - At time = 0, a new batch of 4 tasks is initiated 
  - At time= 6, the first batch of tasks is processed and a new batch of 4 tasks is initiated.
  - At time = 12, the second batch of tasks is processed. There are no more tasks left to process in this queue.

  For queue 1:  
  - At time = 0, a new batch of 3 tasks is initiated.
  - At time= 5, the first batch of tasks is processed and a new batch of 3 tasks is initiated.
  - At time = 15, the third batch of tasks is processed. There are no more tasks left to process in this queue.
  The minimum time to process all the tasks is 15.
  ```  
---
### December 18 - Connections
 
   #### Problem Statement 
   - You are given an `n x n` binary matrix grid where `1` represents **house** and `0` represents **wire**.
   - A house is a 4-directionally connected group of `1`'s not connected to any other `1`'s. There are exactly **two** houses in grid. 
   - You may change `0`'s to `1`'s to connect the two houses to form one house.
   - Return the smallest number of `0`'s you must flip to connect the two houses.
   
   <p align="center"><img src ="https://media4.giphy.com/media/xUNd9YJwF6ifDUnqNi/giphy.gif" width="320" height ="300"/></p> 
 
  #### Sample Input/Output
     
  ```
  Input: grid = [[0,1],[1,0]]
  
  Output: 1
  ```
  ```
  Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
  
  Output: 2
  ```       
---
### December 19 - Winter is coming

#### Problem Statement
- Winter semester is about to begin. The previous semester’s professors had already instructed the students that it is mandatory to take up a value added course in order to take up a subject course. There are a total of `num` courses to be taken and they are labelled from `0` to `num-1`. Consider the array `course` where 
`course[i] = [ai, bi]`. 
- It is mandatory for a student to take up the value added course `ai` in order to take up the subject course `bi`.

Eg : the pair `[3,8]` says that one must take up the value added course `3` in order to take up the subject course `8`. 

- These mandatory courses can be indirect as well. Suppose, course `p` is mandatory to take up course `q` and course `q` is mandatory to take up course `r`. Then, course `p`   is mandatory in order to take up course `r`.  
- Consider another array `answer` where `answer[x] = [mx, nx]`. You must answer if course `mx` is mandatory in order to take up course `nx` or not for the `xth` query. 
- Return a boolean array `result`, where `result[x]` is the answer to the `xth` query.

<p align="center"><img src ="https://media.giphy.com/media/oxLsWbH1rvy2A/giphy.gif" width="320" height ="300"/></p> 

#### Sample Input and Output

```
Input: num = 2, course = [[1,0]], answer = [[0,1],[1,0]]
Output: [false,true]
```
```
Input: num = 3, course = [[1,2],[1,0],[2,0]], answer = [[1,0],[1,2]]
Output: [true,true]
```
```
Input: num = 2, course = [], answer = [[1,0],[0,1]]
Output: [false,false]
```
#### Explanation 
```
Input: num = 2, course = [[1,0]], answer = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take the value added course 1 before you can take the subject course 0. 
Course 0 is not mandatory to take up course 1, but the opposite is true.
```  
 ---

### December 20 - High Traffic Server(s)
 
   #### Problem Statement
   In your company there are `n` servers, numbered `0` to `n-1`, that are handling numerous requests at the same time. Each server has limitless processing power, but it can only handle one request at a time. The requests are routed to servers using the following algorithm:
   - The `k`th request arrives. That `k`th request is discarded if all servers are busy (not handled at all).
   - Assign the request to the `(k % n)`th server if it’s available.
   - Otherwise, forward the request to the next server that is accessible. If the kth server is busy, for example, try routing the request to the `(k+1)`th server, then the `(k+2)`th server, and so on.
  
   You are given the arrival time of the requests and the load time(time taken to complete the request by the server). Your objective is to **find the server which handles the most number of requests**.    
   
   <p align="center"><img src ="https://media4.giphy.com/media/XsHkc4MCBXDn0yNybG/giphy.gif" width="320" height ="300"/></p> 
      
  #### Sample Input and output

   ```
   Input: n = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
   Output: [1] 
   ```   
   ```
   Input: n = 3, arrival = [1,2,3,4], load = [1,2,1,2]
   Output: [0]
   ```   
   ```
  Input: n = 3, arrival = [1,2,3], load = [10,12,11]
  Output: [0,1,2]
   ```
  #### Explanation
   ```
   Input: n = 3, arrival = [1,2,3,4], load = [1,2,1,2]
   Output: [0]
   
   The first three requests are processed by the first three servers.
   The third request has arrived. Because the server is accessible, it is handled by server 0.
   Server 0 dealt with two requests, whereas servers 1 and 2 each dealt with one. As a result, server 0 is the busiest.
   ```      
---

### December 21 - Transform to Checkerboard
 
   #### Problem Statement

   - You've been handed a `x*x` binary grid to work with. You can swap any two rows or columns with each other in each move.
   - Return the minimum number of moves to transform the board into a checkerboard. Return `-1` if the task is impossible.
   - This is how a [checkerboard](https://www.nctm.org/uploadedImages/Publications/TCM_Blog/checkerboard.png) is.
   
   <p align="center"><img src ="/src/assets/checkersboard.png" width="780" height ="250"/></p> 
      
  #### Sample Input and output

   ```
   Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
   Output: 2
   ```   
   ```
  Input: board = [[0,1],[1,0]]
  Output: 0
   ```   
   ```
   Input: board = [[1,0],[1,0]]
   Output: -1
   ```
  #### Explanation
   ```
   Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
   Output: 2
   
   One potential sequence of moves is shown.
   The first move swaps the first and second column.
   The second move swaps the second and third row.
   Check the above image for more context.
   ```      
---   
### December 22 - Richie Rich
 
   #### Problem Statement

   - Christian is a world renowned entrepreneur who has a lot of craze for maths. In order to exhibit his love for maths he decided to buy a land and design it in the form of an undirected simple graph with `X` vertices (numbered 1 through `X`) and `Y` edges (numbered 1 through `Y`). 
   - For each valid `p`, the `p`th edge connects vertices `mₚ` and `nₚ`. Christian wants to show off his car and bike collection on the field and therefore wants to place his bikes and cars on the edges so that the graph would be perfectly balanced, which means that for each vertex, the number of bikes edges incident to it must be equal to the number of cars edges incident to it.
   - Obviously, Christian does not want to leave any edges blank, but he immediately realised that in such a case, it generally may be impossible to make the graph perfectly balanced, so instead he decided to display his helicopter collection on some of the edges, so that it is always possible to balance the graph.
   - Since helicopters are the most expensive, Christian’s satisfaction with the graph will be greater when he uses fewer edges to display his helicopter collection.
   - Can you help him choose what he has to display(bike,car or helicopter) on the edges so that he can show off his love for maths and his wealth in a perfectly balanced and satisfactory manner?
   - Return an array, for each valid `p`, the `p`th of these lines should contain the integer `0` if you want the `i`th edge to be a helicopter, `1` if you want it to be a bike or `−1` if you want it to be a car.   
      
  #### Sample Input and output
   
   ```
   Input: X = 5, Y = 6
          [mₚ, nₚ] = [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 3]]
   Output: [-1, 1, 1, -1, 1, -1]
   ```
   ```
   Input: X = 6, Y = 9
          [mₚ, nₚ] = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [3, 6], [4, 5], [5, 6]]  
   Output: [-1, 1, 0, 0, 1, -1, 0, 0, 0]
   ```
  #### Explanation
   <p align="center"><img src ="/src/assets/helicopterGraph.png"/></p> 
   
   ```
   The graph can be perfectly balanced without using any helicopters on the edges.
   Green colour - car on the edges.
   Red colour - bike on the edges.
   Thus, without using any helicopters on the edges the graph is perfectly balanced in this case.
   ```      
 ---
  ### December 23 - Ant Got Track
 
   #### Problem Statement

   - The National Ant Marathon Committee has decided to conduct this year’s marathon. The committee has to decide the route that is cyclic and consists of 4 different roads.
   - Their city has `X` intersections and `Y` bidirectional roads.They want to hold it in all places throughout the city and make sure they cover a new route every day.
   - Two routes are said to be equal if their sets of component roads are equal.
   - You need to determine the maximum number of days the marathon needs to be held such that every route travelled is different.
   - Two arrays `A` and `B` which define a bidirectional road connecting intersections `Ai` and `Bi`. 
      
  <p align="center"><img src="https://c.tenor.com/gkfAjgzEulcAAAAC/ant-ants.gif" /></p>  
   
   #### Sample Input/Output
   ```
   Input: X = 4, Y = 6
             A  B
             1  2
             2  3
             3  4
             4  1
             1  3
             2  4

   Output: 3
   ```
   ```
   Input: X = 3, Y = 4
             A  B
             1  2
             3  2
             1  3
             2  1

   Output: 2
   ```
   #### Explanation
   ```
   In case 1: There are 3 different cyclic routes that can be taken for the marathon.

    1->2->3->4->1
    1->3->2->4->1
    1->2->4->3->1

    Recall that each route is a set of intersections forming a cycle, so each unique route is the same regardless of which city on the route the ants start out at. Thus, we print 3 (the number of routes) as our answer.
   ```         
---
 ### December 24 - Mayday Mayday!!

  #### Problem Statement 
 
  - Lawrence is a delivery partner with grofers and due to the festive season his orders have increased and he is in a very dire situation. Please help Lawrence. 
  - Lawrence gets `X` orders. The orders are numbered from 1 to `X`. He gets order `i` at `Ri` time, and this order contains `Yi` number of groceries. Lawrence needs to deliver each of these `Yi` groceries before `Ti` time and for each unit of groceries he cannot deliver before this deadline he needs to forfeit `Ki` unit of his salary as penalty. 
  - Given all of the orders, help Lawrence to minimize the amount of salary he will have to forfeit .
  - **Important Note:** Lawrence can deliver at most one grocery at a unit time and for each grocery he needs exactly one unit of time to deliver. Also Lawrence can deliver a          grocery instantly, when the grocery is available right next to the delivery address. 
  - If Lawrence wants to deliver a grocery at time `p`, then the latest he can deliver that grocery is at time time `p`. In another words, for order `i` Lawrence can deliver the groceries at time units `Ri, Ri+1, Ri+2, ..., Ti-1`. Please note that Lawrence cannot deliver groceries from order `i` exactly at time unit `Ti`.

<p align="center"><img src="https://media0.giphy.com/media/9VgufqkSI0x9GamjVf/giphy.gif?cid=ecf05e47aapru8nky8rqlvci3muawh0wirfc3gb6g35uwedg&rid=giphy.gif&ct=g" /></p>      
 
 #### Sample Input/Output 
  ```
    Input: X=1
           R₁=1 Y₁=5 T₁=6 K₁=10
        
    Output: 0
  ```
  ```
   Input: X=2
          R₂=1 Y₂=5 T₂=6 K₂=10
          R₂=1 Y₂=5 T₂=6 K₂=10
        
   Output: 50
  ```
   #### Explanation
  ```
   Example 1: There is only 1 order and all of the groceries from this order can be served. So zero salary has to be forfeited.
   Example 2: There are two orders and you cannot serve 5 groceries. You can select these 5 groceries from any order.
  ```
---
 ### Decemebr 25 - Ranthambore Diaries
 
  #### Problem Statement 
  
  - Adhi and his friend Vishal decided to go camping in the forests of Ranthambore 5 years after their previous trip to the forests. However during the nights they can set up       their tents only in the “resting areas” designated by the government. 
  - The forest has `X` resting areas that they can set up their tents in. The resting areas are numbered from 1 to `X` and are connected with `X-1` roads. 
  - Each road has its own length. It is known that between two resting areas there is exactly one path that goes through the roads and resting areas such that no resting area       appears in the path more than once. Roads do not intersect each other and it takes 0 time to pass through a resting area. 
  - During their last visit,Adhi and Vishal previously rested in resting areas `A1, A2, ... AM` so they will rest in one of these areas again. To make the camping trip more         adventurous they do not agree on the resting area beforehand. Rather, Adhi will pick a random resting area `C` from this list of resting areas and Vishal will independently       pick a random resting area `J` from this list of resting areas. Both random choices will be taken uniformly over the list of resting areas. 
  - The day before the camping trip, Vishal was a little scared and he spoke with his brother about their plan and asked him to calculate the expected distance between resting     areas that Adhi and Vishal randomly pick. Please remember that Adhi’s brother knows neither `C` nor `J`. Help him calculate this expected distance.
  - Return two integers numer and denom, which indicates the fraction `numer`/`denom` giving expected distance between the resting areas randomly chosen by Adhi and Vishal. 
  <p align="center"><img src="https://media3.giphy.com/media/LMnpMq01YnUrBjvTLM/giphy.gif?cid=ecf05e4727j6d5fqqok1l8q81h4ndbk6w89q993w8axbng72&rid=giphy.gif&ct=g" /></p>   

#### Sample Input/Output
  ```
   Input: C=6 B=2
          P=1 Q=3 R=1
          P=2 Q=3 R=2
          P=3 Q=4 R=3
          P=4 Q=5 R=4
          P=4 Q=6 R=5
          A1=1 A2=5
    Output: numer=4 denom=1
   ```
   ```
   Input: C=6 B=6
          P=1 Q=3 R=1
          P=2 Q=3 R=2
          P=3 Q=4 R=3
          P=4 Q=5 R=4
          P=4 Q=6 R=5
          A1=1 A2=2 A3=3 A4=4 A5=5 A6=6
   Output: numer=29 denom=6
   ```
---
 ### Bellisima Florencia
  
  #### Problem Statement 
  
  - Florence is a scenic city that has a number of art galleries connected by bidirectional roads, each of which has a travel time associated with it. Each of the art galleries     may have an artist who displays one or more kinds of arts. A couple, Madhav and Akshara, are at art gallery 1 (each of the gallery is numbered consecutively from 1 to `x` ).   
  - They have a list of arts they want to click photos of, and to save time, they will divide the list between them. Determine the total travel time for the couple to click         pictures of all of the types of arts, finally meeting at art gallery `x`. 
  - Their paths may intersect, they may backtrack through art gallery `x`, and one may arrive at a different time than the other. The minimum time to determine is when both have arrived at the destination.
  - For example, there are `x = 5` art galleries displaying `y = 3` types of arts. The following is a graph that shows a possible layout of the art galleries connected by `z = 4` paths. Each of the galleries is labeled gallery number/art types displayed/ who(madhav/akshara) visit(s).
  - Here `B` and `L` represent madhav and akshara, respectively. In this example, both madhav and akshara take the same path, i.e. `1→3→5` and arrive at time `15+5=20` having  clicked pictures of all three types of arts they wanted to. Neither of them visit shopping centers 2 or 4.
  - Complete the art function in the editor. It should return an integer that represents the minimum time required for their photo session .
    art has the following parameters:
      - x: an integer, the number of art galleries
      - y: an integer, the number of types of arts 
      - centers: an array of strings of space-separated integers where the first integer of each element is the number of types of art displayed at a gallery and the                   remainder are the types displayed
      - roads: a 2-dimensional array of integers where the first two values are the art galleries connected by the bi-directional road, and the third is the travel time for             that road.
   <p align="center"><img src="https://s3.amazonaws.com/hr-assets/0/1544041107-a20059b5a2-SynchronousShoppingExample.png" /></p>
   
#### Sample Input/Output
  ```
  Input:  x=5 z=5 y=5
          t₁=1 A₁₁=1
          t₂=1 A₂₂=2
          t₃=1 A₃₃=3
          t₄=1 A₄₄=4
          t₅=1 A₅₅=5
          k₁=1 c₁=2 d₁=10
          k₂=1 c₂=3 d₂=10
          k₃=2 c₃=4 d₃=10
          k₄=3 c₄=5 d₄=10
          k₅=4 c₅=5 d₅=10
        
  Output: 30
  ```
#### Explanation
  <p align="center"><img src ="https://s3.amazonaws.com/hr-assets/0/1544037692-e51dbc72a0-SynchronousShoppingSample0.png" /></p>    
  
   - B represents a location Madhav visits, L represents a location where Akshara visits.
   - Madhav can travel 1→2→4→5  and click pictures of art at all of the art galleries on his way.
   - Akshara can then travel 1→3→5 , and click pictures of art from the artist at the 3rd art gallery only.  
  
---
 
### December 27 - Commnuity Park

  #### Problem Statement 
 
  - For the past 1 month the community park has been facing a lot of electricity issues.This has affected the park lighting very badly. Adults and children face       difficulty in utilizing the park during the nights. The association members have decided to solve this issue after finding a cost efficient lightning option. 
  - Consider each light source can illuminate a circular area with a radius r. Consider there are n major spots in the park , each located at (xi,yi) point.         Since they want to minimize the expenses,they want to buy a minimum number of light sources (k), such that each major spot  is illuminated by at least 1         light source.
  - In other words, your task is to select a minimum number of points in the plane, such that for each given point , there exists a chosen point at a distance of     at most r.
  - Note: More than one light source can be placed at a specific spot
  
  <p align="center"><img src ="/src/assets/park.webp" height = "300"/></p>       
 
 #### Sample Input/Output 
  ```
    Input: 
    n=4 r=2
    x y
    0 2
    0 4
    2 0
    2 4

        
    Output: 
    2
    1 3
    1 1

  ```
  ```
   Input: 
   n=3 r=2
   x y
   1 4
   0 2 
   4 2

   Output: 
   1
   2 2

  ```
   #### Explanation
 
  <p align="center"><img src ="/src/assets/lights.png" height="300" width="300" /></p>
  
  ```
  
In the first test  case  there are 4 major spots located at (0,2) (0,4) (2,0) (2,4) and the radius of illumination 
is given as 2 units.
We can see that if we place 2 light sources at (1,3) and(1,1) , it would cover all the given major areas. 
Though there are other options, we aim at  minimizing the number of lights ,so 2 light sources are enough 
to illuminate the given major spots in the park.
Then number of light sources along with their coordinates are displayed.
  
 ```
 

 
---

## Maintainers

<table>
    <thead>
        <tr>
            <th><a href="https://github.com/NikhileshJr08">Nikhilesh S</a></th>     
            <th><a href="https://github.com/keerthana-5170">Keerthana S</a></th> 
            <th><a href="https://github.com/harshitha060802">Harshitha</a></th>              
            <th><a href="https://github.com/pranav0120">Pranav D</a></th>
            <th><a href="https://github.com/nityasam02">Nitya Samavedam</a></th>
            <th><a href="https://github.com/nithishkb">Nithish Kumar B</a></th>
            <th><a href="https://github.com/Madhumita2002">Madhumita R</a></th>
            <th><a href="https://github.com/Poujhit">Poujhit MU</a></th>
            <th><a href="https://github.com/SahariKrithik">Sahari Krithik</a></th>
            <th><a href="https://github.com/Cipher-unhsiV">Vishnuvasan</a></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center"><a href="https://github.com/NikhileshJr08"><img width="100" src="https://avatars.githubusercontent.com/u/63784914" alt="f"></a></td>  
            <td align="center"><a href="https://github.com/keerthana-5170"><img width="100" src="https://avatars.githubusercontent.com/keerthana-5170" alt="f"></a></td>
            <td align="center"><a href="https://github.com/harshitha060802"><img width="100" src="https://avatars.githubusercontent.com/harshitha060802" alt="f"></a></td>
            <td align="center"><a href="https://github.com/pranav0120"><img width="100" src="https://avatars.githubusercontent.com/u/89603581" alt="f"></a></td>
            <td align="center"><a href="https://github.com/nityasam02"><img width="100" src="https://avatars.githubusercontent.com/u/87812124?s=400&v=4" alt="f"></a></td>
            <td align="center"><a href="https://github.com/nithishkb"><img width="100" src="https://avatars.githubusercontent.com/u/75293567?s=400&v=4" alt="f"></a></td>
            <td align="center"><a href="https://github.com/Madhumita2002"><img width="100" src="https://avatars.githubusercontent.com/Madhumita2002" alt="f"></a></td>
            <td align="center"><a href="https://github.com/Poujhit"><img width="100" src="https://avatars.githubusercontent.com/Poujhit" alt="f"></a></td>
            <td align="center"><a href="https://github.com/SahariKrithik"><img width="100" src="https://avatars.githubusercontent.com/u/54771183" alt="f"></a></td>            
            <td align="center"><a href="https://github.com/Cipher-unhsiV"><img width="100" src="https://avatars.githubusercontent.com/u/64918181?v=4" alt="f"></a></td>
        </tr>
        <tr>
            <td align="center"> :hammer::construction::pencil: </td>
            <td align="center"> :pencil: </td>
            <td align="center"> :pencil: </td>
            <td align="center"> :pencil: </td>
            <td align="center"> :pencil: </td>
            <td align="center"> :pencil: </td>
            <td align="center"> :pencil: </td>
            <td align="center"> :pencil: </td>
            <td align="center"> :pencil: </td>
            <td align="center"> :pencil: </td>
        </tr>
    </tbody>
</table>

----

FAQ
======

#### Who can join the Challenge?
Anyone who is passionate about coding and can dedicate a little time a day for the challenge for the next 31 days.

#### When should I submit the pull request?
You don't need to submit it everyday. Just submit it once you're done with all 31 algorithms.

#### What if I'm not able to code every day?
Not a problem. While coding every day is nice, we understand that other commitments might interfere with it. Plus its holiday season. So you don't have to solve one problem every day. Go at your own pace. One per day or 7 a week or even all 30 in a day.

#### What language should I use to code?
Anything! New to GoLang? Best way to practice it. Wanna find out what all this hype about Python is? Use it! Any and all languages are welcomed. Maybe you could try using a different language for every problem as a mini-challenge?

#### Fork? Pull request? What is all that? I don't know how to use GitHub!
If you are new to Git or GitHub, check out this out [GitHub](https://guides.github.com/activities/hello-world/)

#### Where are the rest of the problems?
Our code ninjas are hard at work preparing the rest of the problems. Don't worry, they'll be up soon.

#### How should I complete these programs?
We have a folder for each day of the month. Simply complete your code and move the file into that folder. Be sure to rename your file to the following format: `language_username` or `language_username_problemname`
Some examples:
`python3_exampleUser.py`
`c_exampleUser.c`
**Please do not modify any existing files in the repository.**

#### I forked the repository but some problems were added only after that. How do I access those problems?
Not to worry! Open your nearest terminal or command prompt and navigate over to your forked repository. Enter these commands:
```bash
git remote add upstream https://github.com/SVCE-ACM/A-December-of-Algorithms-2021.git
git fetch upstream
git merge upstream/main
```
If you're curious, the commands simply add a new remote called upstream that is linked to this repository. Then it 'fetches' or retrieves the contents of the repository and attempts to merge it with your progress.
Note that if you've already added the upstream repository, you don't need to re-add it in the future while fetching the newer questions.

#### I received a merge error. What do I do?
This shouldn't happen unless you modify an existing file in the repository. There's a lot of potential troubleshooting that might be needed, but the simplest thing to do is to make a copy of your code outside the repository and then clone it once again. Now repeat the steps from the answer above. Merge it and then add your code. Now proceed as usual. :)

#### I'm facing difficulties with/need help understanding a particular question.
Open up an [issue](https://github.com/SVCE-ACM/A-December-of-Algorithms-2021/issues) on this repository and we'll do our best to help you out.

###### [[Back to Top]](#----)

![wave](http://cdn.thekrishna.in/img/common/border.png)
