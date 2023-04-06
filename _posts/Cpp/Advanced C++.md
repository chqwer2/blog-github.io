Template Ref to https://ocw.mit.edu/courses/6-096-introduction-to-c-january-iap-2011/13882f48b16656374a40a0d103a3b51c_MIT6_096IAP11_lec09.pdf

http://web.stanford.edu/class/cs106l/full_course_reader.pdf

# Advanced Topics

### Template

Remember functions can take arguments of specific types and have a specific return
type.

```c++
int sum(const int x, const int y) {
    return x + y;
}

double sum (const double x, const double y) {
	return x + y;
}
```

Or you can do this:

```c++
template <typename T>

T sum(const T a, const T b) {
    return a + b;
}
cout << sum<int>(1, 2) << endl;
cout << sum<float>(1.21, 2.43) << endl;

```

```c++
template <typename T, typename U>
U sum(const T a, const U b) {
    return a + b;
}

sum<int, float>(1, 2.5)
```

```c++

```

```c++

```

### Operation Overload

<img src="../../img/Typora/Advanced C++/image-20230128153847993.png" alt="image-20230128153847993" style="zoom:50%;" />

```
1 ostream& operator<<(ostream &output, const USCurrency &o)
2 {
3 output << "$" << o.dollars << "." << o.cents;
4 return output;
```

### enum instead of const int

```
enum suit_t { CLUBS =18 , DIAMONDS =91 , HEARTS =241 , SPADES =13}
```

### Reference

<img src="../../img/Typora/Advanced C++/image-20230128161532167.png" alt="image-20230128161532167" style="zoom:70%;" />

**Converting between const and non-const**

<img src="../../img/Typora/Advanced C++/image-20230128161643421.png" alt="image-20230128161643421" style="zoom:67%;" />.

**Preprocessor Macros**

<img src="../../img/Typora/Advanced C++/image-20230128161803013.png" alt="image-20230128161803013" style="zoom:67%;" />

##### Cast

<img src="../../img/Typora/Advanced C++/image-20230128161922534.png" alt="image-20230128161922534" style="zoom:67%;" />



