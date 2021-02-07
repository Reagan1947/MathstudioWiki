### 创建变量

本节将简单介绍如何在MathStudio脚本语言中创建变量。与其他脚本语言一样，MathStudio也使用变量来存储并引用一些值。不过，MathStudio中的变量不需要赋值就可以使用。 

变量可以用来创建代数表达式，也可以赋予数字之类的值。

变量必须以小写，大写或下划线开头，并且可以包含数字，但不能包含空格。 变量名中的@符号后跟下划线（_）表示下标。 也可以通过@符号将一个长字符串作为变量名。

### 示例

[在MathStudio中浏览](http://mathstud.io/?input[0]=YT04DQphXjI%3D&input[1]=YT0xMjMNCmI9NDU2DQphK2I%3D&input[2]=Zih4KT14XjINCmYoNSk%3D&input[3]=YT14KngNCmI9eSp5DQphK2I%3D&input[4]=eEBfeQ%3D%3D&input[5]=QCJMb25nIFZhcmlhYmxlIE5hbWUiID0gMTI%3D&input[6]=QCJMb25nIFZhcmlhYmxlIE5hbWUiXjI%3D)

> ```math
> a = 8
> a ^ 2
> ```
>
> $64$

> ```math
> a = 123
> b = 456
> a + b
> ```
>
> $579$

> ```math
> f(x) = x^2
> f(5)
> ```
>
> $25$

> ```math
> a = x * x
> b = y * y
> a + b
> ```
>
> $x^2+y^2$

### 下标

> ```math
> x@_y
> ```
>
> $x_y$

### 字符串变量

> ```math
> @"Long Variable Name" = 12
> ```
>
> $12$

> ```math
> @"Long Variable Name" ^ 2
> ```
>
> $144$
