## 交集运算符

交集运算符(@&)创建一个新表达式，该表达式仅中的元素为原本两个表达式中相同的元素。


## 举例

[在Mathstudio上浏览](http://mathstud.io/?input[0]=WzEsMiwzXSBAJiBbMiwzLDRd&input[1]=WzEsMl0gQCYgWzIsMyw0XQ%3D%3D&input[2]=WzEsMiw1LDYsNyw4XSBAJiBbNiw3LDEyXQ%3D%3D&input[3]=YStiK2MgQCYgYitjK2Q%3D&input[4]=YStiK2MgQCYgYitjK2QgQCYgYg%3D%3D&input[5]=W1sxLDIsM10sWzQsNSw2XV0gQCYgW1s0LDUsNl0sWzcsOCw5XV0%3D)


> ```math
> [1, 2, 3] @& [2, 3, 4]
> ```
>
> $[2,3]$

> ```math
> [1, 2] @& [2, 3, 4]
> ```
>
> $[2]$

> ```math
> [1, 2, 5, 6, 7, 8] @& [6, 7, 12]
> ```
>
> $[6,7]$

> ```math
> a+b+c @& b+c+d
> ```
>
> $b+c$

> ```math
> a+b+c @& b+c+d @& b
> ```
>
> $b$

> ```math
> [[1, 2, 3], [4, 5, 6]] @& [[4, 5, 6], [7, 8, 9]]
> ```
>
>   <table>
>       <tr>
>           <th>4</th>
>           <th>5</th>
>           <th>6</th>
>       </tr>
>   </table>
