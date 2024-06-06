# Web stack debugging #3 — Alx System Engineering DevOps
0x17. Web stack debugging #3


``DevOps``
``SysAdmin``
``Scripting``
``Debugging``


## strace tool
`strace` is a powerful diagnostic, debugging, and instructional tool for Linux and other Unix-like operating systems. It's used to trace system calls and signals. Essentially, it shows you what's happening under the hood when a program runs—what system calls it makes, what errors occur, etc.

Here's a quick rundown of how to use it:

1- **Basic Usage**: To trace the system calls made by a program, you can run:
```bash
strace <program>
```
2- **Trace a Running Process**: If you have a process already running and want to trace it, you can attach strace to it using its PID (Process ID):
```bash
strace -p <PID>
```
3- **Output to File**: You can redirect the output of strace to a file for easier analysis:
```bash
strace -o output.txt <program>
```
4- **Filter by System Call Type**: If you're only interested in specific types of calls, like file or network operations, you can use the -e option:

```bash
strace -e trace=open,close,read,write <program>
```
5- Verbose Output: For more detailed information, you can increase verbosity:

```bash
strace -v <program>
```
It's a super useful tool for debugging and seeing what a program is really doing with system resources.

## Contact Me
**Email:** ouadia@elouardy.com \
**Twitter:** https://twitter.com/_ELOUARDY
