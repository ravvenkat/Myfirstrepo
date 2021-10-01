For little and Big endianess 

https://aticleworld.com/little-and-big-endian-importance/

https://stackoverflow.com/questions/48833976/what-is-uint32-t/48834118
uint32_t is a numeric type that guarantees 32 bits. The value is unsigned, meaning that the range of values goes from 0 to 232 - 1.

This uint32_t* ptr;
declares a pointer of type uint32_t*, but the pointer is uninitialized, that is, the pointer does not point to anywhere in particular. 
Trying to access memory through that pointer will cause undefined behaviour and your program might crash.

This
uint32_t num;
is just a variable of type uint32_t.

This

*(uint32_t*)(ptr + num);
ptr + num returns you a new pointer. It is called pointer arithmetic. It's like regular arithmetic, only that compiler takes the size of types into consideration. Think of ptr + num as the memory address based on the original ptr pointer plus the number of bytes for num uint32_t objects.

The (uint32_t*) x is a cast. This tells the compiler that it should treat the expression x as if it were a uint32_t*. In this case, it's not even needed, because ptr + num is already a uint32_t*.

The * at the beginning is the dereferencing operator which is used to access the memory through a pointer. The whole expression is equivalent to

ptr[num];
Now, because none of these variables is initialized, the result will be garbage.

However, if you initialize them like this:

uint32_t arr[] = { 1, 3, 5, 7, 9 };
uint32_t *ptr = arr;
uint32_t num = 2;

printf("%u\n", *(ptr + num));
this would print 5, because ptr[2] is 5.





**https://electronics.stackexchange.com/questions/145017/for-embedded-code-why-should-i-use-uint-t-types-instead-of-unsigned-int*******************************************************************
1) If you just cast from unsigned to signed integer of the same length back and forth, without any operations in between, 
 you will get the same result every time, so no problem here. But various logical and arithmetical operations are acting differently on signed and unsigned operands.
3) The main reason to use stdint.h types is that the bit size of such a types are defined and equal across all of the platforms, 
  which is not true for int, long e.t.c., as well as char has no standard signess, it can be signed or unsigned by default. 
  It makes easier to manipulate the data knowing the exact size without using extra checking and assumptions.



Type Casting Of Pointers in C":
https://ecomputernotes.com/what-is-c/function-a-pointer/type-casting-of-pointers













