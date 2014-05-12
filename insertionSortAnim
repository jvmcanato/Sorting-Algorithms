import pylab
import random

def insertionSort_anim(a):
    x = range(len(a))
    for i in range(1, len(a)):
        val = a[i]
        j = i-1
        while j >= 0 and a[j] > val:
            a[j+1] = a[j] # creating the space for the insertion
            j = j-1
        a[j+1] = val # insertion
        pylab.plot(x, a, 'k.', markersize=6)
        pylab.savefig("InsertionAnim/" + '%04d' % i + ".png")
        pylab.clf()

# running the algorithm
a = range(300)
random.shuffle(a)
insertionSort_anim(a)
