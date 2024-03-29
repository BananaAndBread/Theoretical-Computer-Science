Assignment 1

Description

Implement an FSA validator. Given an FSA description in the fsa.txt (see input file format) your program should output the result.txt containing an error description (see validation result) or a report, indicating if FSA is complete (or incomplete) and warning (see warning messages) if any. Warnings should be sorted according to their code.
Validation result

Errors:

E1: A state s is not in set of states

E2: Some states are disjoint

E3: A transition a is not represented in the alphabet

E4: Initial state is not defined

E5: Input file is malformed

Report:

FSA is complete/incomplete

Warnings:

W1: Accepting state is not defined

W2: Some states are not reachable from initial state

W3: FSA is nondeterministic

Input file format

states={s1,s2,...}	  // s1 , s2, ... ∈ latin letters, words and numbers

alpha={a1,a2, ...}	  // a1 , a2, ... ∈ latin letters, words, numbers and character '_’(underscore)

init.st={s}	  // s ∈ states

fin.st={s1,s2,...}	  // s1, s2 ∈ states

trans={s1>a>s2,... }	  // s1,s2,...∈ states; a ∈ alpha

Example 1

fsa.txt

states={on,off}

alpha={turn_on,turn_off}    

init.st={off}

fin.st={}

trans={off>turn_on>off,on>turn_off>on}

result.txt

Error:

E2: Some states are disjoint

Example 2

fsa.txt

states={on,off}

alpha={turn_on,turn_off}  

init.st={off}

fin.st={}

trans={off>turn_on>on,on>turn_off>off}

result.txt

FSA is incomplete

Warning:

W1: Accepting state is not defined

Submission

You should test your code using codetest service available here and submit archived source files in the moodle. Untested submissions will not be considered.

Supported programming languages:

Java 1.8 (java)

JetBrains Kotlin (kotlin)

Python 2.7.6 (python)

Python 3.4.3 (python3)

c++ (g++ 4.8) (cpp)

c++11 (g++ 4.8) (cpp11)

C# (mono) (cs)
