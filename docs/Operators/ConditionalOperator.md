## 条件运算符

条件运算符是采用三个值的三元运算符。

如果第一个值不为零，则返回第二个值。 如果第一个值是零，则返回最后一个值。

## 举例  
[在Mathstudio上浏览](http://mathstud.io/?input[0]=YSA%2FIGIgOiBj&input[1]=aWYoYSkgLy8gPw0KIHJldHVybiBiDQplbHNlIC8vIDoNCiByZXR1cm4gYw0KZW5k&input[2]=MSA%2FICJUcnVlIiA6ICJGYWxzZSI%3D&input[3]=MCA%2FICJUcnVlIiA6ICJGYWxzZSI%3D&input[4]=Ly8gcmV0dXJuIHRoZSBsb3dlc3QgdmFsdWUNCmE9MQ0KYj0yDQphIDwgYiA%2FIGEgOiBi&input[5]=Ly8gcmV0dXJuIHRoZSBoaWdoZXN0IHZhbHVlDQphPTENCmI9Mg0KYSA%2BIGIgPyBhIDogYg%3D%3D)


>   ```math
>   a ? b : c
>   ```
>   $a?b:c$


>   ```math
>   if(a) // ?
>       return b
>   else // :
>       return c
>   end
>   ```
>   $b$


>   ```math
>   1 ? "True" : "False"
>   ```
>   $True$


>   ```math
>   0 ? "True" : "False"
>   ```
>   $False$

>   ```math
>    // return the lowest value
>    a=1
>    b=2
>    a < b ? a : b
>   ```
>   $1$

>   ```math
>    // return the highest value
>    a=1
>    b=2
>    a > b ? a : b
>   ```
>   $2$