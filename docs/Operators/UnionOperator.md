## 合并运算符

合并运算符(@|)从两个表达式中的不同元素创建一个新表达式。

## 举例

[在Mathstudio上浏览](http://mathstud.io/?input[0]=WzEsMiwzLDRdIEB8IFszLDQsNSw2XQ%3D%3D&input[1]=YStiK2MgQHwgYitjK2Q%3D&input[2]=YStiK2MgQHwgYitjK2QgQHwgYg%3D%3D&input[3]=W1sxLDIsM10sWzQsNSw2XV0gQHwgW1s0LDUsNl0sWzcsOCw5XV0%3D)


> ```math
> [1, 2, 3, 4] @| [3, 4, 5, 6]
> ```
>
> $[1,2,3,4,5,6]$

> ```math
> a+b+c @| b+c+d
> ```
>
> $a+b+c+d$

> ```math
> a+b+c @| b+c+d @| b
> ```
>
> $a+b+c+d$

> ```math
> [[1, 2, 3], [4, 5, 6]] @| [[4, 5, 6], [7, 8, 9]]
> ```
>
>   <table>
>       <tr>
>           <th>1</th>
>           <th>2</th>
>           <th>3</th>
>       </tr>
>       <tr>
>           <th>4</th>
>           <th>5</th>
>           <th>6</th>
>       </tr>
>       <tr>
>           <th>7</th>
>           <th>8</th>
>           <th>9</th>
>       </tr>
>   </table>