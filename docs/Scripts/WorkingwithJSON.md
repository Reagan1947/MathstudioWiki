### 使用JSON

MathStudio可以使用JSON函数将JSON数据解析为对象，也可以使用http函数从URL解析JSON数据。

### 示例（译者注：此示例不再可用）

[在MathStudio中浏览](http://mathstud.io/?input[0]=d2VhdGhlciUyMCUzRCUyMGpzb24oJyU3QiUyMmNvb3JkJTIyJTNBJTdCJTIybG9uJTIyJTNBLTAuMTMlMkMlMjJsYXQlMjIlM0E1MS41MSU3RCUyQyUyMnN5cyUyMiUzQSU3QiUyMm1lc3NhZ2UlMjIlM0EwLjA2NiUyQyUyMmNvdW50cnklMjIlM0ElMjJHQiUyMiUyQyUyMnN1bnJpc2UlMjIlM0ExNDAzMTQ5MzYzJTJDJTIyc3Vuc2V0JTIyJTNBMTQwMzIwOTI3MSU3RCUyQyUyMndlYXRoZXIlMjIlM0ElNUIlN0IlMjJpZCUyMiUzQTgwMCUyQyUyMm1haW4lMjIlM0ElMjJDbGVhciUyMiUyQyUyMmRlc2NyaXB0aW9uJTIyJTNBJTIyU2t5JTIwaXMlMjBDbGVhciUyMiUyQyUyMmljb24lMjIlM0ElMjIwMW4lMjIlN0QlNUQlMkMlMjJiYXNlJTIyJTNBJTIyY21jJTIwc3RhdGlvbnMlMjIlMkMlMjJtYWluJTIyJTNBJTdCJTIydGVtcCUyMiUzQTI4OS4xMyUyQyUyMmh1bWlkaXR5JTIyJTNBNjMlMkMlMjJwcmVzc3VyZSUyMiUzQTEwMjYlMkMlMjJ0ZW1wX21pbiUyMiUzQTI4Ny41OSUyQyUyMnRlbXBfbWF4JTIyJTNBMjkwLjM3JTdEJTJDJTIyd2luZCUyMiUzQSU3QiUyMnNwZWVkJTIyJTNBNC4wMyUyQyUyMmRlZyUyMiUzQTQ2LjAwMzclN0QlMkMlMjJjbG91ZHMlMjIlM0ElN0IlMjJhbGwlMjIlM0EwJTdEJTJDJTIyZHQlMjIlM0ExNDAzMjEwMjg0JTJDJTIyaWQlMjIlM0EyNjQzNzQzJTJDJTIybmFtZSUyMiUzQSUyMkxvbmRvbiUyMiUyQyUyMmNvZCUyMiUzQTIwMCU3RCcp&input[1]=d2VhdGhlciUyMCUzRCUyMGpzb24oJyU3QiUyMmNvb3JkJTIyJTNBJTdCJTIybG9uJTIyJTNBLTAuMTMlMkMlMjJsYXQlMjIlM0E1MS41MSU3RCUyQyUyMnN5cyUyMiUzQSU3QiUyMm1lc3NhZ2UlMjIlM0EwLjA2NiUyQyUyMmNvdW50cnklMjIlM0ElMjJHQiUyMiUyQyUyMnN1bnJpc2UlMjIlM0ExNDAzMTQ5MzYzJTJDJTIyc3Vuc2V0JTIyJTNBMTQwMzIwOTI3MSU3RCUyQyUyMndlYXRoZXIlMjIlM0ElNUIlN0IlMjJpZCUyMiUzQTgwMCUyQyUyMm1haW4lMjIlM0ElMjJDbGVhciUyMiUyQyUyMmRlc2NyaXB0aW9uJTIyJTNBJTIyU2t5JTIwaXMlMjBDbGVhciUyMiUyQyUyMmljb24lMjIlM0ElMjIwMW4lMjIlN0QlNUQlMkMlMjJiYXNlJTIyJTNBJTIyY21jJTIwc3RhdGlvbnMlMjIlMkMlMjJtYWluJTIyJTNBJTdCJTIydGVtcCUyMiUzQTI4OS4xMyUyQyUyMmh1bWlkaXR5JTIyJTNBNjMlMkMlMjJwcmVzc3VyZSUyMiUzQTEwMjYlMkMlMjJ0ZW1wX21pbiUyMiUzQTI4Ny41OSUyQyUyMnRlbXBfbWF4JTIyJTNBMjkwLjM3JTdEJTJDJTIyd2luZCUyMiUzQSU3QiUyMnNwZWVkJTIyJTNBNC4wMyUyQyUyMmRlZyUyMiUzQTQ2LjAwMzclN0QlMkMlMjJjbG91ZHMlMjIlM0ElN0IlMjJhbGwlMjIlM0EwJTdEJTJDJTIyZHQlMjIlM0ExNDAzMjEwMjg0JTJDJTIyaWQlMjIlM0EyNjQzNzQzJTJDJTIybmFtZSUyMiUzQSUyMkxvbmRvbiUyMiUyQyUyMmNvZCUyMiUzQTIwMCU3RCclMkMlMjBmaWx0ZXIlM0QlNUJ0ZW1wJTJDJTIwaHVtaWRpdHklNUQp&input[2]=d2VhdGhlcihtYWluJTJDJTIwdGVtcCklNDBLJTIwLSUzRSUyMCU0MEY%3D&input[3]=JTJGJTJGJTIwJUU4JThCJUI5JUU2JTlFJTlDJUU4JTgyJUExJUU3JUE1JUE4JUU0JUJCJUEzJUU3JUEwJTgxJTBBc3ltYm9sJTIwJTNEJTIwJTIyQUFQTCUyMiUwQSUwQSUyRiUyRiUyMCVFNCVCOCU4OSVFNCVCOCVBQSVFNiU5QyU4OCVFNSU4OSU4RCVFNyU5QSU4NCVFNiU5NyVBNSVFNiU5QyU5RiUwQXN0YXJ0RGF0ZSUyMCUzRCUyMGRhdGUoJTIyeS0wbS0wZCUyMiUyQyUyMC0zJTQwbW9udGhzKSUwQSUwQSUyRiUyRiUyMCUyMiUzQyUzQyUyMiVFNiU5MyU4RCVFNCVCRCU5QyVFNyVBQyVBNiVFNyU5NCVBOCVFNCVCQSU4RSVFNSVBRCU5NyVFNyVBQyVBNiVFNCVCOCVCMiVFOCVCRiU5RSVFNiU4RSVBNSUwQXVybCUyMCUzRCUyMCUyMnF1ZXJ5LnlhaG9vYXBpcy5jb20lMkZ2MSUyRnB1YmxpYyUyRnlxbCUzRnElM0RzZWxlY3QlMjAqJTIwZnJvbSUyMHlhaG9vLmZpbmFuY2UuaGlzdG9yaWNhbGRhdGElMjB3aGVyZSUyMHN5bWJvbCUzRCclMjIlMjAlM0MlM0MlMjBzeW1ib2wlMjAlM0MlM0MlMjAlMjInJTIwYW5kJTIwc3RhcnREYXRlJTNEJyUyMiUyMCUzQyUzQyUyMHN0YXJ0RGF0ZSUyMCUzQyUzQyUyMCUyMiclMjBhbmQlMjBlbmREYXRlJTNEJ3RvZGF5JyUyNmZvcm1hdCUzRGpzb24lMjZkaWFnbm9zdGljcyUzRHRydWUlMjZlbnYlM0RodHRwJTNBJTJGJTJGZGF0YXRhYmxlcy5vcmclMkZhbGx0YWJsZXMuZW52JTIyJTBBJTBBc3RvY2tzJTIwJTNEJTIwaHR0cCh1cmwlMkMlMjBmaWx0ZXIlM0QlNUJDbG9zZSUyQ0RhdGUlNUQp&input[4]=cHJpY2VzJTIwJTNEJTIwc3RvY2tzKHF1ZXJ5JTJDJTIwcmVzdWx0cyUyQyUyMHF1b3RlJTJDJTIwKiUyQyUyMENsb3NlKSUwQXJvdW5kKHByaWNlcyk%3D&input[5]=ZGF0ZXMlMjAlM0QlMjBkYXRlKCUyMm0lMkZkJTIyJTJDJTIwc3RvY2tzKHF1ZXJ5JTJDJTIwcmVzdWx0cyUyQyUyMHF1b3RlJTJDJTIwKiUyQyUyMERhdGUpKQ%3D%3D&input[6]=JTJGJTJGJTIwJUU3JUJCJTk4JUU1JTg4JUI2JUU1JTg3JUJBJUU4JThCJUI5JUU2JTlFJTlDJUU3JTlBJTg0JUU4JTgyJUExJUU0JUJCJUI3JTBBTGlzdFBsb3QocHJpY2VzJTJDJTIwbGFiZWxzJTNEZGF0ZXMlMkMlMjB3aWR0aCUzRDcwMCUyQyUyMGhlaWdodCUzRDIyMCUyQyUyMGZsaXBBeGlzJTNEMSk%3D)

### 使用JSON函数解析一个JSON字符串

> ```math
> weather = json('{"coord":{"lon":-0.13,"lat":51.51},"sys":{"message":0.066,"country":"GB","sunrise":1403149363,"sunset":1403209271},"weather":[{"id":800,"main":"Clear","description":"Sky is Clear","icon":"01n"}],"base":"cmc stations","main":{"temp":289.13,"humidity":63,"pressure":1026,"temp_min":287.59,"temp_max":290.37},"wind":{"speed":4.03,"deg":46.0037},"clouds":{"all":0},"dt":1403210284,"id":2643743,"name":"London","cod":200}')
> ```
> 
> <div class="object"><button class="object" onclick="var e=this.children[0];var s=this.parentNode.children[1].style;s.display=='block'?e.innerHTML='▸':e.innerHTML='▾';s.display=='block'?s.display='none':s.display='block';"><span>▾</span> Object<div>29</div></button><ul class="object" style="display: block;"><li class="list">coord<ul><li>lon: <ul><li><div class="MATH04" style="margin-top:0.95em;">-</div><div class="MATH05"><div class="MATH02">13</div><div class="MATH03">100</div></div></li></ul></li><li>lat: 51.51</li></ul></li><li class="list">sys<ul><li>message: <ul><li><div class="MATH05"><div class="MATH02">33</div><div class="MATH03">500</div></div></li></ul></li><li>country: GB</li><li>sunrise: 1&thinsp;403&thinsp;149&thinsp;363</li><li>sunset: 1&thinsp;403&thinsp;209&thinsp;271</li></ul></li><li class="list">weather<ul><li class="list">(1)</li><ul><li>id: 800</li><li>main: Clear</li><li>description: Sky is Clear</li><li>icon: 01n</li></ul></ul></li><li>base: cmc stations</li><li class="list">main<ul><li>temp: 289.13</li><li>humidity: 63</li><li>pressure: 1026</li><li>temp_min: 287.59</li><li>temp_max: 290.37</li></ul></li><li class="list">wind<ul><li>speed: <ul><li><div class="MATH05"><div class="MATH02">403</div><div class="MATH03">100</div></div></li></ul></li><li>deg: 46.0037</li></ul></li><li class="list">clouds<ul><li>all: 0</li></ul></li><li>dt: 1&thinsp;403&thinsp;210&thinsp;284</li><li>id: 2&thinsp;643&thinsp;743</li><li>name: London</li><li>cod: 200</li></ul></div>
> <img src="..\_media\Scripts\WorkingwithJSON\graphing_00.png" alt="graphing_00" style="zoom:50%;" />

### 使用带筛选器的JSON函数解析一个JSON字符串

> ```math
> weather = json('{"coord":{"lon":-0.13,"lat":51.51},"sys":{"message":0.066,"country":"GB","sunrise":1403149363,"sunset":1403209271},"weather":[{"id":800,"main":"Clear","description":"Sky is Clear","icon":"01n"}],"base":"cmc stations","main":{"temp":289.13,"humidity":63,"pressure":1026,"temp_min":287.59,"temp_max":290.37},"wind":{"speed":4.03,"deg":46.0037},"clouds":{"all":0},"dt":1403210284,"id":2643743,"name":"London","cod":200}', filter=[temp, humidity])
> ```
>
> <img src="..\_media\Scripts\WorkingwithJSON\graphing_01.png" alt="graphing_01" style="zoom:50%;" />

### 从JSON数据转换温度

> ```math
> weather(main, temp)@K -> @F
> ```
>
> **61℉**

### 使用HTTP函数绘制苹果的股票价格

> ```math
> // 苹果股票代码
> symbol = "AAPL"
> 
> // 三个月前的日期
> startDate = date("y-0m-0d", -3@months)
> 
> // "<<"操作符用于字符串连接
> url = "query.yahooapis.com/v1/public/yql?q=select * from yahoo.finance.historicaldata where symbol='" << symbol << "' and startDate='" << startDate << "' and endDate='today'&format=json&diagnostics=true&env=http://datatables.org/alltables.env"
> 
> stocks = http(url, filter=[Close,Date])
> ```
>
> ```math
> prices = stocks(query, results, quote, *, Close)
> round(prices)
> ```
>
> ```math
> dates = date("m/d", stocks(query, results, quote, *, Date))
> ```
>
> ```math
> // 绘制出苹果的股价
> ListPlot(prices, labels=dates, width=700, height=220, flipAxis=1)
> ```
