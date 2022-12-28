# AdventOfCode22

- Day 1 - I did it in C++ because I ran out of time to set up python. I was generally pretty happy with how I did.
- Day 2 - This was the first time I had tried to write an AoC problem in python. I ended up googling syntax a lot because I didn't know how to declare a function or write an if statement correctly without reverting back to C++ syntax. After the learning hump, I got it! The most annoying thing is trying to read in input. I need to figure this out because I wasted 15 minutes trying to solve a bug that was caused by me keeping the new line when I read in input.
- Day 3 - This was smoother. I was glad I was able to figure out the set implementation after some googling. Python is much much smoother than C++. I again wasted 15 minutes because I forgot that the way I am reading input keeps the /n. I need to figure out how to fix that. Anyway, generally still pleased with how it went. Jeff still beat me. Mayble I'll beat him tomorrow (:
- Day 4 - This took me way longer than it should have. I was getting that 3 > 15 as true. I could not figure out why. I then type casted it to int(3) > int(15) and then it returned what it was supposed to. I still really confused as to why it was evaluating that expression as a string comparison, and how it even ended up with True. I even thought I solved the new line and space problem. But I guess not.
- Day 5 - I liked this one. It's getting easier.
- Day 6 - I did it! I started 5 minutes late. But I was quick! The first part took me roughly 12 min. I read the problem wrong the first time and then had to refactor. The second part only took me 36 seconds! I think I scared my roommates when I shouted when it actually worked the first time (:
- Day 16 - I finally finished part 1! turns out that I got the right answer! (: I was off by one on the example, so I tried adjusting the answer I got for that. But the answer it gave for my input was right! I am very pleased that I was able to finish at least part one for this. I did not copy any one else's code and BFS is starting to make a lot more sense for me. I did read through some of the comments on reddit and copied parts of my code from day 19.

- Day 18 - I struggled with this one some! I finally figured out part 2! I ended up creating a 3d array representing the cubes. I flood filled the array on the outside using a queue. (I tried using recursion first but that doesn't work with bigger input). I then found the inside surface area and subtracted it from the answer from part 1.
- Day 19 - I cheated (kinda of)! For the first part, I figured out a solution that I thought worked correctly. With some trial and error and running others solutions, I figured out that my blueprint 21 was giving 6 instead of 7. Turns out that for this particular blueprint, you can't always assume that you should build a obsidian bot if you can. My solution now will provide the correct answer, but it just takes a very long time. I got part 2 without too much of a problem (:
