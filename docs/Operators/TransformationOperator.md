## 转换运算符

转换运算符(->)非常强大，有很多用途。 它使用右侧的表达式转换左侧的表达式。

与范围一起使用时，此运算符会创建一个步进值。 1..10的范围从1到10，默认步长为1。1..10-> 2的范围创建相同的步长为2的范围。


## 举例

[在Mathstudio上浏览](http://mathstud.io/?input[0]=eF4yIC0%2BIDQ%3D&input[1]=eF4yK3leMiAtPiBbeD0yLHk9NF0%3D&input[2]=M0BtaWxlcyAtPiBAa2lsb21ldGVycw%3D%3D&input[3]=QGN1cHMgLT4gQHRhYmxlc3Bvb25z&input[4]=NUBob3VycyAtPiBAbWludXRlcw%3D%3D&input[5]=MzBAQyAtPiBARg%3D%3D&input[6]=WzEsMiwzLDQsNV0gLT4gMi4uNA%3D%3D&input[7]=WzEsMiwzLDQsNSw2LDcsOCw5LDEwXSAtPiAoMS4uJCAtPiAyKQ%3D%3D&input[8]=WzEsMiwzLDQsNSw2LDcsOCw5LDEwXSAtPiAoMi4uJCAtPiAyKQ%3D%3D&input[9]=IkhlbGxvIFdvcmxkIiAtPiAxLi41&input[10]=IkhlbGxvIFdvcmxkIiAtPiA2Li4k&input[11]=IkFCQ0RFRkdISUoiIC0%2BICgxLi4kIC0%2BIDIp&input[12]=ImFiY2RlZmciIC0%2BIFtd&input[13]=eCt5K3ogLT4gW10%3D&input[14]=W2EsYixjLGQsZSxmLGddIC0%2BICIi&input[15]=W3gseSx6XSAtPiAr&input[16]=W3gseSx6XSAtPiAq&input[17]=W3gseSx6XSAtPiBe&input[18]=eCt5K3ogLT4gXg%3D%3D&input[19]=YSpiKmMgLT4gKw%3D%3D&input[20]=WzEsMiwzXSAtPiBbNF0%3D&input[21]=WzEsMl0gLT4gWzMsNCw1XQ%3D%3D&input[22]=WzFdIC0%2BIFsyLDMsNF0%3D&input[23]=WzEsMiwzLDQsNSw2LDddIC0%2BICs%3D&input[24]=WzEsMiwzLDQsNSw2LDcsOCw5LDEwXSAtPiAq&input[25]=WzEsMiwzLDQsNV0gLT4gIzI%3D&input[26]=WzEsMiwzLDQsNV0gLT4gIzIuLjQ%3D&input[27]=MSAtPiAjMSAtPiBbMiwzLDQsNV0%3D&input[28]=MyAtPiAjMiAtPiBbMiw1LDcsMTFd&input[29]=QGN1YmUoeCkNCnheMw%3D%3D&input[30]=Y3ViZSAtPiAz&input[31]=QG11bHRpcGx5KGEsYixjKQ0KYSpiKmM%3D&input[32]=bXVsdGlwbHkgLT4gW2EsYixjXQ%3D%3D&input[33]=bXVsdGlwbHkgLT4gWzIsMyw0XQ%3D%3D)


## 代换


> ```math
> x^2 -> 4
> ```
>
> $16$

> ```math
> x^2+y^2 -> [x=2, y=4]
> ```
>
> $20$

## 单位转换

> ```math
> 3@miles -> @kilometers
> ```
>
> $4.83km$

> ```math
> @cups -> @tablespoons
> ```
>
> $16tbsp$

> ```math
> 5@hours -> @minutes
> ```
>
> $300minutes$

> ```math
> 30@C -> @F
> ```
>
> $86℉$

## 范围子列表

> ```math
> [1, 2, 3, 4, 5] -> 2..4
> ```
>
> $[2,3,4]$

> ```math
> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> (1..$ -> 2)
> ```
>
> $[1,3,5,7,9]$

> ```math
> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> (2..$ -> 2)
> ```
>
> $[2,4,6,8,10]$

## 范围的子字符串

> ```math
> "Hello World" -> 1..5
> ```
>
> $Hello$

> ```math
> "Hello World" -> 6..$
> ```
>
> $World$

> ```math
> "ABCDEFGHIJ" -> (1..$ -> 2)
> ```
>
> $ACEGI$

## 划分

> ```math
> "abcdefg" -> []
> ```
>
> $[a,b,c,d,e,f,g]$

> ```math
> x+y+z -> []
> ```
>
> $[x,y,z]$


## 合并

> ```math
> [a, b, c, d, e, f, g] -> ""
> ```
>
> $abcdefg$

> ```math
> [x, y, z] -> +
> ```
>
> $x+y+z$

> ```math
> [x, y, z] -> *
> ```
>
> $xyz$

> ```math
> [x, y, z] -> ^
> ```
>
> ${x^{{y^z}}}$

## 转换
> ```math
> a*b*c -> +
> ```
>
> $a+b+c$

> ```math
> x+y+z -> ^
> ```
>
> ${x^{{y^z}}}$

## 添加列表


> ```math
> [1, 2, 3] -> [4]
> ```
>
> $[1,2,3,4]$

> ```math
> [1, 2] -> [3, 4, 5]
> ```
>
> $[1,2,3,4,5]$

> ```math
> [1] -> [2, 3, 4]
> ```
>
> $[1,2,3,4]$

## 求和


> ```math
> [1, 2, 3, 4, 5, 6, 7] -> +
> ```
>
> $28$

## 乘积

> ```math
> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> *
> ```
>
> $3 628 800$

## 使用索引运算符删除列表中的元素

> ```math
> [1, 2, 3, 4, 5] -> #2
> ```
>
> $[1,3,4,5]$

> ```math
> [1, 2, 3, 4, 5] -> #2..4
> ```
>
> $[1,5]$

## 使用索引运算符（#）将元素插入到列表中


> ```math
> 1 -> #1 -> [2, 3, 4, 5]
> ```
>
> $[1,2,3,4,5]$


> ```math
> 3 -> #2 -> [2, 5, 7, 11]
> ```
>
> $[2,3,5,7,11]$

## 计算表达式

> ```math
> @cube(x)
> x^3
> ```
>
> cube compiled successfully.


> ```math
> cube -> 3
> ```
>
> $27$

> ```math
> @multiply(a, b, c)
> a*b*c
> ```
>
> multiply compiled successfully.


> ```math
> multiply -> [a, b, c]
> ```
>
> $abc$

> ```math
> multiply -> [2, 3, 4]
> ```
>
> $24$