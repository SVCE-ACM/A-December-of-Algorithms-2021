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
  Input: n=2
  Output: NO
  ```
  ```
  Input: n=19
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
   
   #### Sample Input/Output
  ```
  Input: [["L","N","A","C"],["W","B","A","D"],["T","Z","F","E"]], name = "DEV"
  Output: false
  ```

  #### Resources
  - [Backtracking](https://www.geeksforgeeks.org/backtracking-algorithms/)

---
### December 4 - SANDHYA AND HER TIC-TAC-TOE LOVE!
  
  #### Problem Statement
  - Sandhya likes to play tic-tac-toe (using 2*2 matrix), and uses the elements 0 and 1. She is wondering how many matrices with X rows and Y columns there are. Everyone obviously knows that - it is just 2X⋅Y. But what no one knows is that, she considers two identical matrices if and only if by permuting the X no.of rows and then permuting the Y no.of columns, and the resulting matrix is transverse of itself. 
  - Help Sandhya by finding the number of X×Y matrices which are distinct according to her definition (even though she doesn't know how to solve them). Since the answer can/may be quite large, compute it modulo 10^9+7.
        
  <p align="center"><img "https://media.giphy.com/media/3oriNKQe0D6uQVjcIM/giphy.gif" /></p>
  
  #### Sample Input/Output
  ```
  Input: 1 5
  Output: 6
  ```
   #### Explaination
    ```
    According to Sandhya's definition, there are 6 different binary matrices. 
    This is because the number of 1-s uniquely identifies a 1×5 matrix and 
    the number of 1-s can take any value between 0 and 5 inclusive.
    ```
   #### Sample Input/Output
  ```
  Input: 10 10
  Output: 508361223
  ```
  
---

### December 5 - Biscuit Bonanza
 
   #### Problem Statement
   - A local biscuit store sells only 2 types of biscuits: circular and rectangular biscuits. They are referred to by the numbers '0' and '1' respectively. The customers stand in a queue and they either purchase circular or rectangular biscuits. 
   - The number of biscuits is equal to the number of customers. They are placed in a stack. 
   - At each step: If the customer at the front of the queue prefers the biscuit on the top of the stack, they will take it and leave the queue.
   - Otherwise, they will directly go to the queue's end.
   <p align="center"><img "https://media.giphy.com/media/nAErqE3k2C3fy/giphy.gif" /></p>
   
   ### NOTE: This continues until none want to take the top biscuit and are thus unable to eat.
   - Consider two integer arrays ‘customers’ and ‘biscuits’ where biscuits[i] is the type of the ith biscuit in the stack (i = 0 is the top of the stack) and customers[j] is the preference of the jth customer in the initial queue (j = 0 is the front of the queue). 
   ### Return 
   The number of customers that are unable to eat.
   ### Input format
   The first line contains the elements of the array customers
   The second line contains the elements of the array biscuits
   ### Constraints   
   1 ≤ customers.length, biscuits.length ≤ 100
   customers.length == biscuits.length
   biscuits[i] is 0 or 1.
   customers[i] is 0 or 1.
   ### Sample Input
   ```
   customers = [1,1,1,0,1] , biscuits = [1,0,0,0,1,1]
   ```
   ### Sample Output
   ```
   3
   ```
   ### Sample Input
   ```
   customers = [1,1,0,0], biscuits = [0,1,0,1]
   ```
   ### Sample Output
   ```
   0 
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
        </tr>
        <tr>
            <td align="center"> :hammer::construction::pencil: </td>
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
