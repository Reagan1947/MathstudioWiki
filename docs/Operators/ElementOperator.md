## 元素运算符

元素运算符(@?)检查表达式是否包含元素。

## 举例  
[在Mathstudio上浏览](http://mathstud.io/?input[0]=YT0xOjEw&input[1]=YSBAPyAy&input[2]=YSBAPyAxMg%3D%3D&input[3]=bnVtYmVycz1bb25lPTEsdHdvPTIsdGhyZWU9Myxmb3VyPTRd&input[4]=bnVtYmVycyBAPyB0d28%3D&input[5]=bnVtYmVycyBAPyBmaXZl)


>   ```math
>   a=1:10
>   ```
>   $[1,2,3,4,5,6,7,8,9,10]$

>   ```math
>   a @? 2
>   ```
>   $1$

>   ```math
>   a @? 12
>   ```
>   $0$

>   ```math
>   numbers=[one=1, two=2, three=3, four=4]
>   ```
>   + one:1
>   + two:2
>   + three:3
>   + four:4

>   ```math
>   numbers @? two
>   ```
>   $1$

>   ```math
>   numbers @? five
>   ```
>   $0$
