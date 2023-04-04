# Task:
The Barber Shop Problem. In a quiet town, there is a small barber shop. The salon is small, and only one hairdresser can work in it, serving one visitor. There are several chairs for waiting in the queue. The hairdresser serves visitors all his life. When there is no one in the salon, he sleeps in the chair. When a visitor comes and sees the sleeping hairdresser, he wakes him up, sits in the chair, and "falls asleep" at the moment while the hairdresser serves him. If a visitor comes and the hairdresser is busy, he stands in line and "falls asleep." After cutting the hair, the hairdresser escorts the visitor himself. If there are waiting visitors, the hairdresser wakes one of them up and waits for him to sit in the hairdresser's chair and start cutting his hair. If there is no one, he sits back in his chair and falls asleep until a visitor arrives. Create a multithreaded application that models a day in a barbershop.

# Program algorithm
  The program algorithm is based on the producers and consumers paradigm.
Producers and consumers are interacting processes. They are often organized in a pipeline through which information passes.
Before moving on to the organization of pipelines, let's define that the producer process generates information in a certain buffer that is used by the consumer process.
Here, there are problems of buffer overflow and depletion. Then, when the buffer overflows, the producer will have to wait until at least one element is released in the buffer, and when the buffer is depleted, the consumer will have to wait until at least one new element appears in the buffer [7].
As previously mentioned, producers and consumers are often combined in a pipeline - a sequence of processes in which each consumes the data of its predecessor and supplies data for the subsequent process.
A classic example is Unix pipelines. Consider the interaction of the commands:
$ ps –Af | grep mc.
  The vertical bar "|" between the commands denotes a pipeline, i.e., the output of one command is redirected to the input of another command, thus in the example above, the result of executing ps -Af will be passed to the command grep, which will transform the input stream according to the mask (in this case, the output will be all lines containing the substring "mc") [8, p. 22].
Streams can be associated with files of a special type - channels. A channel is a buffer (a FIFO queue) between the producer process and the consumer process. The producer process writes data to the end of the queue, and the consumer process reads data from its beginning, while the characters are removed. In our case, we have 1 thread responsible for generating new clients, and 2 threads responsible for processing all clients, i.e., producer and consumer, respectively. The program is based on a channel - a queue (in_line). The number of visitors varies from zero and is set using one of the input formats: via console, file, or randomly generated number. The program terminates when there are no more visitors.

# Implemented in C file:
* Input and output in the program is performed using files, command line, or random generation. (all possible input values should be non-negative)
* Several functions are implemented, including the function of creating events "visitor arrived", "barber started cutting visitor", as well as functions for random number generation, and outputting the results of the event creation functions to the screen.
* Two data threads are implemented, which are connected to each other thanks to two mutexes (binary semaphores), and the paradigm of unequal threads is implemented: "Producers and Consumers." One thread produces, the other consumes.
* Parallel computing model: Threads are linked to each other using a FIFO queue (in_line). We create mutexes (binary semaphores), through which we differentiate the program's output so that two threads do not have access to the output at the same time (the result without introducing mutexes is shown in the program testing).

# Program testing:
The program works correctly: all the output of the function is clear and understandable, and no errors occur, here are the results:

![Снимок экрана 2022-12-16 в 20 58 20](https://user-images.githubusercontent.com/75154790/208159902-79f31797-7ae1-481e-a7e9-e120fcf8536c.png)

Let's conduct an experiment to see what will happen if we remove the separation of threads using mutexes in the program, here are the results:

![Снимок экрана 2022-12-16 в 21 43 52](https://user-images.githubusercontent.com/75154790/208167307-a566ddeb-3948-4a9a-8cc8-70da74189178.png) 
  
It is easy to notice that the program starts giving incorrect output on line 22.

Thus, mutexes help to prevent the output of information about the results of both event functions at the same time, i.e., with the help of this technology, the program works correctly: timely output of all correct function results to the screen.

Let's check the correctness of the program's operation using input via a file 

![Снимок экрана 2022-12-16 в 22 45 15](https://user-images.githubusercontent.com/75154790/208177055-df3df3db-5e25-4ead-b075-44ccb9c39741.png)  
  
or a randomly generated number, respectively:
  
![Снимок экрана 2022-12-16 в 22 52 17](https://user-images.githubusercontent.com/75154790/208178229-69484bd3-fd1d-4483-82d6-398e615a7f8a.png)


