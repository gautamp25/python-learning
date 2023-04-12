
"""How python works?

Byte code- Byte code represnts the fixed set of instruction.
    size of each byte code is 1 byte or 8 bits
    We can find byte code instruction in the .pyc file

Python compiler- converts program source code into byte code.


Python Compiler - A Python Compiler converts the program source code
code.
Type of Python Compilers :
● CPython
● Jpython/ Jython
● PyPy
RubyPython
IronPython
StacklessPython
● Pythonxy
AnacondaPython

Write Source Code / Program
Compile the Program using Python Compiler
Compiler Converts the Python Program into byte Code
Computer/Machine Can not understand Byte Code so we convert it into Machine Code using
PVM
PVM uses an interpreter which understands the byte code and convert it into machine code
Machine Code instructions are then executed by the processor and results are displayed

_____________       ________________
|            |      |               |
|            |------|               |--------|
|____________|      |_______________|         
[Source code/Program(.py)-->Byte code(.pyc)-->Binary/Machine code-->Computer(Output)]
                        |                   |                    
                        |                   |                    
                        |                   |                              
                        |                   |
                        |                   Run program using PVM
                        Compile using python compiler



-Python Virtual Machine
    -Python Virtual Machine (PVM) is a program which provides programming
        environment. The role of PVM is to convert the byte code instructions into machine
        code so the computer can execute those machine code instructions and display the
        output.
    - Interpreter converts the byte code into machine code and sends that machine code to
        the computer processor for execution.

- Constants
    - A constant is an identifier whose value cannot be changed throughout the execution of
        program whereas the variable value keeps on changing.
    - There are no constants in Python, the way they exist in C and Java.
    - In Python, It is not possible to define constant whose value can not be changed.
    - In Python, Constants are usually defined on a module level and written in all capital
        letters with underscores separating words but remember its value can be changed.
    Ex:
        PI
        TOTAL
        MIN VALUE

Built-in Datatype
    These datatypes are provided by Python Language.
    Following are the built-in data type:
        None Type
        Numeric Types
        Sequences
        Sets
        Mappings

    Numeric Type / Number
        Complex - A complex number is a number that is written in the form of a + bj or a +
        bJ. Where,
        a = Real Part of the number
        b = Imaginary part of the number
        jor J = Square root value of -1
        a and may contain integer or float number.
        Ex:- 5+7j, 0.8+2j
    Bool type
        The bool datatype represents boolean value True or False. Python internally represents
        True as 1 and False as 0.
        Ex: True, False
        True+ True = 2
        True False = 1
    
    Sequence Type
        Following are sequence type:
        String
        List
        Tuple
        Range

        -Sequence Type
            List - A list represents a group of elements. A list can store different types of elements
                which can be modified. Lists are dynamic which means size is not fixed. Lists are
                represented using square bracket [ ].
                Ex: data = [10, 20, -50, 21.3, 'Geekyshows']
                [0] 10
                [1] 20
                [2] -50
                [3] 21.3
                [4] Geekyshows
        -Sequence Type
            Tuple - A tuple contains a group of elements which can be different types. It is similar
                to List but Tuples are read-only which means we can not modify it's element. Tuples
                are represented using parentheses ().
                Ex:- data = (10, 20, -50, 21.3, 'Geekyshows')
                [0] 10 [-5] 10 data[1] = 40
                [1] 20 [-4] 20
                [2] -50 [-3] -50
                [3] 21.3 [-2] 21.3
                [4] Geekyshows [-1] Geekyshows
        -Sequence Type
            Range - Range represents a sequence of numbers. The numbers in the range are not
            modifiable.
            Ex:- rg = range(5) 01234
            rg = range(10, 20, 2) 10 12 14 16 18
            [0] 0 [-5] 0 [0] 10
            [1] 1 [-4] 1 [1] 12
            [2] 2 [-3] 2 [2] 14
            [3] 3 [-2] 3 [3] 16
            [4] 4 [-1] 4 [4] 18
        
        - Set Type
            A set is an unordered collection of elements much like a set in mathematics.
            The order of elements is not maintained in the sets. It means the elements may not
            appear in the same order as they are entered into the set.
            A set does not accept duplicate elements.
            1. Sets are unordered so we can not access its element using index.
            2. Sets are represented using curly brackets {}.
            Ex:
                data = {10, 20, 30, "GeekyShows", "Raj”, 40}
                data - {10, 20, 30, "GeekyShows", "Raj", 40, 10, 20}
        - Mapping Type/dict / Dictionary
            A map represents a group of elements in the form of key value pairs.
            Ex:
                data = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
                data = {'rahul':2000, ‘raj':3000, ‘sonam':8000, }
                [101] Rahul ['rahul'] 2000
                [102] Raj ['raj'] 3000
                [103] Sonam ['sonam'] 8000

Operators
    An operator is a symbol that performs an operation.
        Arithmetic Operators
        Relational Operators / Comparison Operators
        Logical Operators
        Assignment Operators
        Bitwise Operators
        Membership Operators
        Identity Operators

    % Modulus operator to get remainder in integer division 5% 2 1

    ** Exponent  5**2=5² 25

    // Integer Division/ Floor Division 5//2 2

and
    Operand 1 Operand 2 Result
    True True ->True
    True False ->False
    False True ->False
    False False ->False
    True Expression ->Expression
    False Expression ->False

OR
    Operand 1 Operand 2 Result
    True True ->True
    True False ->True
    False True ->True
    False False ->False
    True Expression ->True
    False Expression ->Expression

Bitwise
&= 1 1 ->1 else 0
|= 0 0 ->0 else 1
^= 1 1->0 and 0 0 ->0 else 1

"""