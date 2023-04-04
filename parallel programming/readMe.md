#ABC 4.0
#Task:
The Barber Shop Problem. In a quiet town, there is a small barber shop. The salon is small, and only one hairdresser can work in it, serving one visitor. There are several chairs for waiting in the queue. The hairdresser serves visitors all his life. When there is no one in the salon, he sleeps in the chair. When a visitor comes and sees the sleeping hairdresser, he wakes him up, sits in the chair, and "falls asleep" at the moment while the hairdresser serves him. If a visitor comes and the hairdresser is busy, he stands in line and "falls asleep." After cutting the hair, the hairdresser escorts the visitor himself. If there are waiting visitors, the hairdresser wakes one of them up and waits for him to sit in the hairdresser's chair and start cutting his hair. If there is no one, he sits back in his chair and falls asleep until a visitor arrives. Create a multithreaded application that models a day in a barbershop.

#Program algorithm
  The program algorithm is based on the producers and consumers paradigm.
Producers and consumers are interacting processes. They are often organized in a pipeline through which information passes.
Before moving on to the organization of pipelines, let's define that the producer process generates information in a certain buffer that is used by the consumer process.
Here, there are problems of buffer overflow and depletion. Then, when the buffer overflows, the producer will have to wait until at least one element is released in the buffer, and when the buffer is depleted, the consumer will have to wait until at least one new element appears in the buffer [7].
As previously mentioned, producers and consumers are often combined in a pipeline - a sequence of processes in which each consumes the data of its predecessor and supplies data for the subsequent process.
A classic example is Unix pipelines. Consider the interaction of the commands:
$ ps –Af | grep mc.
  The vertical bar "|" between the commands denotes a pipeline, i.e., the output of one command is redirected to the input of another command, thus in the example above, the result of executing ps -Af will be passed to the command grep, which will transform the input stream according to the mask (in this case, the output will be all lines containing the substring "mc") [8, p. 22].
Streams can be associated with files of a special type - channels. A channel is a buffer (a FIFO queue) between the producer process and the consumer process. The producer process writes data to the end of the queue, and the consumer process reads data from its beginning, while the characters are removed...
