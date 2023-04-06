MIT OCW: https://ocw.mit.edu/courses/6-096-introduction-to-c-january-iap-2011/pages/lecture-notes/

Stanford Full Course PDF: http://web.stanford.edu/class/cs106l/full_course_reader.pdf

CPP Reference: https://en.cppreference.com/w/

#### Ref Word List

Literals 文字

### Comment

```
x = 1 + /*sneaky comment here*/ 1;
```

### Header

```c++
# include < iostream >     // Lines beginning with # are preprocessor commands
using namespace std ;

#include <cmath>    

```

### **Data Type**

```c++
INT 4 bytes 
signed: -2147483648 to 2147483647
unsigned: 0 to 4294967295

1 / 4   evaluates to 0
1 / 4.0 evaluates to 2.5

char *x = "Hello";

// User defined, e.g. Vector
vector consists of 2 points: a start and a finish

```

### Class

```c++
class MITStudent {
public:
    char *name;
    int studentID;
};

student1.name
// Pass classes by reference if they need to be modified

// define method implementation outside the class
void Point::offset(double offsetX, double offsetY) {
x += offsetX; y += offsetY;
}
```

**Constructors**

<img src="../../img/Typora/C++ Recap/image-20230128120339994.png" alt="image-20230128120339994" style="zoom:50%;" />

Clone Issue:

```c++
If a constructor with parameters is defined, the default constructor is no longer available

// Copy/Clone the class -- same address (Assigning all fields)
Point r = q;

// You can define your own copy constructor (Can Assign patrial fields)
name = strdup(o.name);  // strdup dis-related two address
```

<img src="../../img/Typora/C++ Recap/image-20230128120458610.png" alt="image-20230128120458610" style="zoom:50%;" />

```c++
// getters to allow read-only access to private fields
private:
	double x, y;
```

**Internal Usage**

```c++
this->val is a shorthand for (*this).val
```

### Array

```c++
type arrayName[dimension];

for(int i = 0; i < 4; i++)
	 cin >> arr[i];

```

### String

```c++
char str1[] = "I'm a s";

strcpy(str3, str1);
strcat(str1, str1);
```

### Pointers

```c++
// When declaring a pointer, * is placed before the variable name to indicate that
int * ptr = & x ;

// Then * is placed before the pointer name to dereference it 
*numPtr = *numPtr * *numPtr ;

const int * ptr ; //  pointer to a constant integer.
int * const ptr ; //  declares a constant pointer to changeable integer data. 

ptr ++ 1;  // point to next value if in array
myArray[3] is *(myArray + 3).

// dangling pointer outside the scope

```

### Memory Management

```c++
// Allocate memory using The new operator
int *x = new int; // The pointer can be return and still exist 

// De-allocates memory using The delete 
delete x;  // ptr to that address
```

<img src="../../img/Typora/C++ Recap/image-20230128143247815.png" alt="image-20230128143247815" style="zoom:53%;" />

Don’t use the memory after deleting it

Only delete if memory was allocated by new

**Allocating Arrays**

```c++
// they can have variable size
    cin >> numItems;
    int *arr = new int[numItems]; 
    delete[] arr;

Allocating Class Instances using new
    Point *p = new Point(2, 4);
    delete p;
    
Destructor is called when de-allocate
    ~Point() {
    cout << "destructor invoked" << endl;
    }
```



### Control

```c++
for(initialization; condition; incrementation)

Pass by value (int a) vs. by reference (int &a)
address in an Interger

Returning multiple values: Passing output variables by reference

```

### Function

```
Argument Type Matters. (Function Overloading)


```



### I/O Stream

```c++
std::cout << i << " Hello , world !\ n " ;   // :: indicates scope resolution operator
cin >> x ;
```

**Escape sequences**





### **Important Functions**

A lot of important functions that you might use in Python aren’t available in C++ by default. Instead, you have to #include the appropriate library at the top of your file. Here are some examples:

- **stringSplit** splits a string by a delimiter (like Python .split())
  \#include “strlib.h” // put this at the top of your file!
  string data = “a,b,c”;
  Vector<string> components = **stringSplit**(data, “,”);
- **toLowerCase** converts a string to its lowercase version (see also toUpperCase) [from “strlib.h”]:
  string data = “ABC”;
  cout << **toLowerCase**(data) << endl; // prints abc
- **getLine** gets a string from the user (see also getInteger) [from “simpio.h”]:
  string data = **getLine**(“Please enter some text: ”);
- **getYesOrNo** gets a boolean from the user [from “simpio.h”]:
  bool yesOrNo = **getYesOrNo**(“Yes or no? ”);
- **startsWith(**str, prefix**)** checks whether a string begins with the prefix (see also endsWith) [from “strlib.h”].
- **stringToInteger(**str**)** and **integerToString(**int**)** do the appropriate conversions, as do **stringToReal(**str**)** and **stringToReal(**d**)** [from “strlib.h”].
- **randomInteger(**low, high**)** returns a random integer between low and high, inclusive [from “random.h”].
- str**.find(**b**)** checks if the character or string b is found in str and returns its index if it’s found, or string::npos otherwise. 

```c++
string a = “pineapple”

cout << a.find(“apple”) << endl; // prints 4
if (a.find(‘p’)!= string::npos) { // equivalent of ‘if ‘p’ in a’
	cout << “p is in string a!” << endl;
}
```



