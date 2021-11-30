"""
Turn this program from python to java:
var1=78
var2=23
var3="Hello World"
var4=8.9
print(var1+var2)
print(var2*var4)
print(var3)
"""

# below is the solution in a comment because
#  i dont want to make a java file :)


"""
public class Problem15{
    public static void main(String[] args){
        int var1=78;
        int var2=23;
        String var3="Hello World";
        double var4=8.9;
        System.out.println(var1+var2);
        System.out.println(var2*var4);
        System.out.println(var3);

    }
}
"""

# in python

myvar = 23
print("hello" + myvar)

# in java
"""
public class Problem15{
    public static void main(String[] args){
        int myvar=23;
        System.out.println("hello"+myvar);
    }
}
"""


# we will notice that in java you cannot run the program, 
# since there is explicit type declaration, java knows before
# running the program what type of data is in the variable
# and it will throw an error if you try to run it because
# you cannot add a string to an int
# but in python you can run it, but it will throw a runtime error.
# which is different than a compilation error.