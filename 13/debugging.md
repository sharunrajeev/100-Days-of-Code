# Debugging

Debugging is the process of removing bugs or errors from the code. The first documented bug was found out by *Grace Hopper*. First step to prevent bugs is to have clear understanding of what your are doing and what you need. 

A better way to find a bug is to **describe the problem** by checking the code, this could help us to understand where we could have gone wrong.

The next method is to **reproduce the bug**, this happens when we can't understand what happened. For example, a case where we get an error saying *index out of range* in a list. Now check for the area where the data could go wrong by reproducing each case in which one of the case could be the bug.

Then next step is to **act as a computer**, this would allow us to understand each step and how the computer evaluates and what eventually goes wrong. As humans we may skip steps like a*b might be written as ab which in human mind, we could understand but the computer doesn't.

Most of the IDE and code editors have error detection built in which almost detects most commonly made mistakes like typos or wrong indentation etc. After we **fix the error** they show us, run the code. When we see an unknown error in the screen we could just copy paste it in the google to find the most probable reason that we could have gone wrong. The errors may not be under the same circumstances but *understanding how the user solved* the problem and then implement it in our code would help you to solve it.

Another super easy methods to find bugs which are related to the logic of the code is to write **print statement** where you feel the code could go wrong. For example, you are going into a infinite while loop, try to spot the variable which the while loop depends and check if it increments or decrement or it has a end condition. The print statement can also helps to fix the wrong output by checking for the right answer in the each step.

Next most helpful way to debug is using a **debugger**. Debugger is a special software which helps programmers to find bugs and rectify it. Debuggers allow us to loop through each step the program goes through. Another useful function is that it could *run specific section* of code other than running the whole program. We could create *breakpoints* where the debugger tells us the state of the program at that point. Some of the debuggers for python are :

1. [Thonny, Python IDE for beginners](https://thonny.org/)
2. [Python Tutor - Visualize Python, Java, C, C++, JavaScript, TypeScript, and Ruby code execution](http://pythontutor.com/)
3. [PyCharm: the Python IDE for Professional Developers by JetBrains](https://www.jetbrains.com/pycharm/)

Other ways to debug is to *take a little break* in the middle when you can't solve the bug this would allow us to clear our mind with the assumption we made to look through the code allowing us to find the bug. Next step is to **ask the developer community**, there are so many people like us who are willing to help others so post your queries and others will guide you to solve them. You could use *stack overflow, Quora* and other media platforms to raise queries. *Running code for each time* we build things would allow us to remove small bugs when they are encountered otherwise all the bugs combine to bring up a large number of bugs which could bring down your motivations and confidence to solve the problem.

That's all for today. *Happy debugging!*