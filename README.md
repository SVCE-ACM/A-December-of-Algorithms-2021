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
   - Front customer leaves the top sandwich and returns to the end of the line making customers = [1,0,0,1].
   - Front customer leaves the top sandwich and returns to the end of the line making customers = [0,0,1,1].
   - Front customer takes the top sandwich and leaves the line making customers = [0,1,1] and biscuits = [1,0,1].
   - Front customer leaves the top sandwich and returns to the end of the line making customers = [1,1,0].
   - Front customer takes the top sandwich and leaves the line making customers = [1,0] and biscuits = [0,1].
   - Front customer leaves the top sandwich and returns to the end of the line making customers = [0,1].
   - Front customer takes the top sandwich and leaves the line making customers = [1] and biscuits = [1].
   - Front customer takes the top sandwich and leaves the line making customers = [] and biscuits = [].
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
### December 9 - Archery with Deepika Kumari


   #### Problem Statement
   - Deepika Kumari is participating in the Commonwealth Games for Archery where there are M participants in total, as per the rules of the game, each pair of participants             compete against each other once. 
   - If the participant wins, he/she is awarded one score point and if a participant loses, he/she is awarded zero score point, likewise the probability of draw in the game is zero.  
   - After all the rounds of games, The Commonwealth Games has decided to distribute the award to all the archers and the award is calculated as the square of his/her score.
   - Calculate the possible budget the Host of the Commonwealth Games will reward for all the archers, given cash value as Z, evaluate if there is at least one case wherein the total cash the Hosts will reward is exactly Z? If any, output one of them.


   <p align="center"><img src ="https://media0.giphy.com/media/QFypAZbq5lz3i/200.gif" /></p> 
  - INPUT : First line contains an integer Q denotes the number of test cases. The Q following lines, each line contains two integers n, k.

-OUTPUT : For each test case, if there isn't a such scenario, output -1.otherwise print n lines, each line contains n characters. j-th character in i-th line is "1" if i-th participant wins j-th participant, otherwise "0". (i-th character in i-th line is always "0")
-Constraints :
1 ≤ T ≤ 100
1 ≤ n ≤ 103
The sum of n over all test cases is at most 104
1 ≤ k ≤ 109
 
-Subtasks:
Subtask #1 (10 points): n ≤ 5
Subtask #2 (30 points): n ≤ 50
Subtask #3 (60 points): original constrains

   
   ### Sample Input and output

   ```
   Input: 3
2 1
3 6
4 10

   Output: counter value = 01
00
-1
0100
0011
1001
1000

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
            <th><a href="https://github.com/Madhumita2002">Madhumita R</a></th>
            <th><a href="https://github.com/Poujhit">Poujhit MU</a></th>
            <th><a href="https://github.com/SahariKrithik">Sahari Krithik</a></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center"><a href="https://github.com/NikhileshJr08"><img width="100" src="https://avatars.githubusercontent.com/u/63784914" alt="f"></a></td>  
            <td align="center"><a href="https://github.com/keerthana-5170"><img width="100" src="https://avatars.githubusercontent.com/keerthana-5170" alt="f"></a></td>
            <td align="center"><a href="https://github.com/harshitha060802"><img width="100" src="https://avatars.githubusercontent.com/harshitha060802" alt="f"></a></td>
            <td align="center"><a href="https://github.com/pranav0120"><img width="100" src="https://avatars.githubusercontent.com/u/89603581" alt="f"></a></td>
            <td align="center"><a href="https://github.com/nityasam02"><img width="100" src="https://avatars.githubusercontent.com/u/87812124?s=400&v=4" alt="f"></a></td>
            <td align="center"><a href="https://github.com/Madhumita2002"><img width="100" src="https://avatars.githubusercontent.com/Madhumita2002" alt="f"></a></td>
            <td align="center"><a href="https://github.com/Poujhit"><img width="100" src="https://avatars.githubusercontent.com/Poujhit" alt="f"></a></td>
            <td align="center"><a href="https://github.com/SahariKrithik"><img width="100" src="https://avatars.githubusercontent.com/u/54771183" alt="f"></a></td>            
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
