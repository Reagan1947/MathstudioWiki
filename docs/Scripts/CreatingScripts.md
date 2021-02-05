### 创建脚本

创建脚本需要使用@符号并提供脚本名称。脚本名称遵循的命名惯例与变量相同。

在脚本中创建的变量只能在该脚本中访问。

### 例子

[在MathStudio中浏览](http://mathstud.io/?input[0]=QGN1YmUoeCkNCngqeCp4&input[1]=Y3ViZSg4KQ%3D%3D&input[2]=QHN1bU9mKG51bWJlcnMpDQpzdW0gPSAwDQpmb3IgbnVtYmVyIGluIG51bWJlcnMNCiBzdW0gKz0gbnVtYmVyDQplbmQNCnN1bQ%3D%3D&input[3]=c3VtT2YoWzEsMiwzLDQsNSw2LDcsOCw5LDEwXSk%3D&input[4]=c3VtT2YoMToyMCk%3D)

> ```math
> @cube(x)
> x*x*x
> ```
>
> **cube** *compiled successfully.*

> ```math
> cube(8)
> ```
>
> $512$

> ```math
> @sumOf(numbers)
> sum = 0
> for number in numbers
>   sum += number
> end
> sum
> ```
>
> **sumOf** *compiled successfully.*

> ```math
> sumOf([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
> ```
>
> $55$

> ```math
> sumOf(1:20)
> ```
>
> $210$
