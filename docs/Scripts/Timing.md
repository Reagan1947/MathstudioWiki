### 计时

reset和time命令可以计算运行代码所需的时间。

reset命令重置定时器，time命令返回以毫秒为单位的时间。

### 示例

[在MathStudio中浏览](http://mathstud.io/?input[0]=cmVzZXQNCg0KbnVtYmVycyA9IDE6MTAwMA0Kc3VtID0gMA0KZm9yIG51bWJlciBpbiBudW1iZXJzDQogc3VtICs9IG51bWJlcg0KZW5kDQpzdW0NCg0KdGltZQ%3D%3D)

> ```math
> reset
> 
> numbers = 1:1000
> sum = 0
> for number in numbers
>  sum += number
> end
> sum
> 
> time
> ```
>
> $530$
