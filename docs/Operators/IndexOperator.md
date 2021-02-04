## 索引运算符

索引运算符(#)用于在一定数量或范围内创建索引以插入或删除元素。


## 举例

[在Mathstudio上浏览](http://mathstud.io/?input[0]=WzEsMiwzLDQsNV0gLT4gIzI%3D&input[1]=WzEsMiwzLDQsNV0gLT4gIzIuLjQ%3D&input[2]=WzEsMiwzLDQsNV0gLT4gIyQ%3D&input[3]=MiAtPiAjMSAtPiBbMywgNSwgN10%3D&input[4]=MyAtPiAjMiAtPiBbMiw1LDdd&input[5]=MTEgLT4gIyQgLT4gWzIsMyw1LDdd)

## 删除第二个元素

> ```math
> [1, 2, 3, 4, 5] -> #2
> ```
>
> $[1,3,4,5]$

## 删除一系列元素

> ```math
> [1, 2, 3, 4, 5] -> #2..4
> ```
>
> $[1,5]$

## 使用大小运算符删除最后一个元素

> ```math
> [1, 2, 3, 4, 5] -> #$
> ```
>
> $[1,2,3,4]$

## 在第一个索引处插入

> ```math
> 2 -> #1 -> [3, 5, 7]
> ```
>
> $[2,3,5,7]$

## 在第二个索引处插入

> ```math
> 3 -> #2 -> [2, 5, 7]
> ```
>
> $[2,3,5,7]$

## 在最后插入大小运算符

> ```math
> 11 -> #$ -> [2, 3, 5, 7]
> ```
>
> $[2,3,5,7,11]$