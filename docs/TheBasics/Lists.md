### 列表
**列表**是一个方括号包围的有序集合，由逗号分隔。

把**列表**赋值给`变量`后，就可以访问列表中的元素。

MathStudio中的**列表**是从`1`开始索引的，这意味着列表中首个元素的**下标**为`1`。

一个**列表**`变量`中的元素可以通过**整数**、**范围**或**整数列表**进行读取。

### 例子
[在MathStudio中浏览](http://mathstud.io/?input[0]=WzEsMiwzLDQsNV0%3D&input[1]=MToxMA%3D%3D&input[2]=QFsxMF0%3D&input[3]=YT1bMTAsMjAsMzBdDQphKDEp&input[4]=YT1bMTAsIDIwLCAzMF0NCmEoMSkrYSgyKSthKDMp&input[5]=YT1bMSwyLDMsNCw1LDYsNyw4LDldDQphKDIuLjUp&input[6]=YT1bMSwyLDMsNCw1LDYsNyw4LDldDQphKDEuLiQgLT4gMik%3D&input[7]=cHJpbWVzPVsyLDMsNSw3LDExLDEzLDE3LDE5LDIzXQ0KcHJpbWVzKFsyLDVdKQ%3D%3D&input[8]=YT1bMSwyLDMsNCw1LDYsNyw4LDldDQphKCMkKQ%3D%3D&input[9]=YT1bMSwyLDMsNCw1LDYsNyw4LDldDQphKCMkIC0gMSk%3D&input[10]=WzEsMiwzLDRdIC0%2BIFs1LDZd&input[11]=WzEsMiwzLDQsNSw2LDcsOCw5XSAtPiAyLi41&input[12]=WzEsMiwzLDQsNSw2LDcsOCw5XSAtPiA2Li4k&input[13]=WzEsIDIsIDMsIDQsIDUsIDYsIDcsIDgsIDldIC0%2BICgxLi4kIC0%2BIDIp&input[14]=WzEsMiwzLDQsNSw2LDcsOCw5XSAtPiAjMi4uNQ%3D%3D&input[15]=WzEsMiwzLDQsNSw2LDcsOCw5XSAtPiAjNi4uJA%3D%3D)

### 创建列表
> ```math
> [1, 2, 3, 4, 5]
> ```
>
> **[1, 2, 3, 4, 5]​**

> ```math
> 1:10
> ```
>
> **[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]**

> ```math
> @[10]
> ```
>
> **[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]**

### 用索引读取列表中的元素
> ```math
> a = [10, 20, 30]
> a(1)
> ```
>
> **10**

> ```math
> a = [10, 20, 30]
> a(1) + a(2) + a(3)
> ```
>
> **60**

### 用范围读取列表中的元素
> ```math
> a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
> a(2..5)
> ```
>
> **[2, 3, 4, 5]**

> ```math
> a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
> a(1..$ -> 2)
> ```
>
> **[1, 3, 5, 7, 9]**

### 用另一个列表读取列表中的元素
> ```math
> primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
> primes([2, 5])
> ```
>
> **[3, 11]**

### 用末端索引访问元素
> ```math
> a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
> a(#$)
> ```
>
> **9**

> ```math
> a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
> a(#$ - 1)
> ```
>
> **8**

### 用箭头符号合并列表
> ```math
> [1, 2, 3, 4] -> [5, 6]
> ```
>
> **[1, 2, 3, 4, 5, 6]**

### 用箭头符号截取列表
> ```math
> [1, 2, 3, 4, 5, 6, 7, 8, 9] -> 2..5
> ```
>
> **[2, 3, 4, 5]**

> ```math
> [1, 2, 3, 4, 5, 6, 7, 8, 9] -> 6..$
> ```
>
> **[6, 7, 8, 9]**

>  ```math
> [1, 2, 3, 4, 5, 6, 7, 8, 9] -> (1..$ -> 2)
>  ```
>
> **[1, 3, 5, 7, 9]**

### 用箭头符号去除列表中的元素
> ```math
> [1, 2, 3, 4, 5, 6, 7, 8, 9] -> #2..5
> ```
>
> **[1, 6, 7, 8, 9]**

> ```math
> [1, 2, 3, 4, 5, 6, 7, 8, 9] -> #6..$
> ```
>
> **[1, 2, 3, 4, 5]**

