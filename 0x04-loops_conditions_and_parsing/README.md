# Loops, conditions and parsing — Alx System Engineering DevOps
0x04. Loops, conditions and parsing

```DevOps```
```Shell```
```Bash```
```Scripting```

## Introduction
```Bash```, short for "Bourne Again Shell," is a popular Unix shell and command language interpreter that is widely used in Linux and Unix-based operating systems. It provides a powerful command-line interface (CLI) for interacting with the system and executing commands, as well as a scripting language for writing shell scripts to automate tasks and perform system administration.

## Advantage of `#!/usr/bin/env bash` over `#!/bin/bash`
Using **#!/usr/bin/env bash** ensures that the correct bash interpreter is used, even if it's located in a different directory. This makes scripts more portable across different systems.

## Loops
### while Loop
```bash
count=0
while [ $count -lt 5 ]; do
    echo $count
    ((count++))
done
```
### until Loop
```bash
count=0
until [ $count -eq 5 ]; do
    echo $count
    ((count++))
done
```
### for Loop
```bash
# Iterate over a sequence of numbers
for ((i = 1; i <= 5; i++)); do
    echo $i
done
# Iterate over items in an array
for i in {1..5}; do
    echo $i
done
```
## Conditional Statements
### **if**, **else**, **elif** Statements
```bash
num=10
if [ $num -eq 10 ]; then
    echo "Number is 10"
elif [ $num -gt 10 ]; then
    echo "Number is greater than 10"
else
    echo "Number is less than 10"
fi
```
### case Statement
```bash
fruit="apple"
case $fruit in
    apple)
        echo "It's an apple";;
    banana)
        echo "It's a banana";;
    *)
        echo "Unknown fruit";;
esac
```
## Using the cut Command
The cut command is used to extract sections from each line of files. Here's an example:

```bash
echo "apple,banana,orange" | cut -d',' -f2
```
This will output banana.

## File and Other Comparison Operators
Comparison operators used in Bash include `-eq` (equal), `-ne` (not equal), `-lt` (less than), `-gt` (greater than), `-le` (less than or equal), and `-ge` (greater than or equal).


## Variable Assignment and Arithmetic
```bash
# Variable Assignment
name="John"
age=30


# Arithmetic
num1=10
num2=5
sum=$((num1 + num2))
echo "Sum: $sum"
```
## Comparison Operators
```bash
num1=10
num2=5
if [ $num1 -gt $num2 ]; then
    echo "$num1 is greater than $num2"
fi
```
## File Test Operators
File test operators in Bash include `-f` (file exists), `-d` (directory exists), `-r` (file readable), `-w` (file writable), and `-x` (file executable).

```bash
# Check if a file exists
if [ -f "/path/to/file" ]; then
    echo "File exists"
else
    echo "File does not exist"
fi

# Check if a directory exists
if [ -d "/path/to/directory" ]; then
    echo "Directory exists"
else
    echo "Directory does not exist"
fi

# Check if a file is readable
if [ -r "/path/to/file" ]; then
    echo "File is readable"
else
    echo "File is not readable"
fi

# Check if a file is writable
if [ -w "/path/to/file" ]; then
    echo "File is writable"
else
    echo "File is not writable"
fi

# Check if a file is executable
if [ -x "/path/to/file" ]; then
    echo "File is executable"
else
    echo "File is not executable"
fi
```

## Making Scripts Portable
To make scripts portable, avoid hardcoding paths and use environment variables where possible. Additionally, use shebang `#!/usr/bin/env bash` for the bash interpreter to ensure compatibility across different systems.

## Contact Me
**Email:** ouadia@elouardy.com \
**Twitter:** https://twitter.com/_ELOUARDY

