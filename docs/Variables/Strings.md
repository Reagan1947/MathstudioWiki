### 字符串

字符串是一个有序的字符集合，比如“Hello World”或“MathStudio”。创建字符串可以使用双引号也可以使用单引号。

字符串可以使用字符串连接符(<<)进行连接，该操作符将所有值转换为字符串。

### 例子

[在MathStudio中浏览](http://mathstud.io/?input[0]=IkhlbGxvIFdvcmxkIg%3D%3D&input[1]=J0hlbGxvIFdvcmxkJw%3D%3D&input[2]=IkhlbGxvIiA8PCAiICIgPDwgIldvcmxkIg%3D%3D&input[3]=IkhlbGxvIFdvcmxkIiAtPiAxLi41&input[4]=IkhlbGxvIFdvcmxkIiAtPiA3Li4k&input[5]=IkFCQ0RFRkdISUpLIiAtPiAoMS4uJCAtPiAyKQ%3D%3D)

> ```math
> "Hello World"
> ```
>
> ***Hello World***

> ```math
> 'Hello World'
> ```
>
> ***Hello World***

### 字符串连接符

> ```math
> "Hello" << " " << "World"
> ```
>
> ***Hello World***

### 使用区间(range)截取字符串

> ```math
> "Hello World" -> 1..5
> ```
>
> ***Hello***

> ```math
> "Hello World" -> 7..$
> ```
>
> ***World***

> ```math
> "ABCDEFGHIJK" -> (1..$ -> 2)
> ```
>
> ***ACEGIK***
