gflib
===
##Description
Python library of finite field calculator
##Usage

This library contains 2 classes 'gf' and 'gfex'.

At first, you need to type as follows.
```
from gflib import gf,gfex
```

###gf class
gf class has one class variable 'gf.space'

You can get the surplus of gf.space if you operate two gf object each other.
```
>>> gf.space=7
>>> gf(3)+gf(5)
1
>>> gf(3)-gf(5)
5
>>> gf(3)*gf(5)
1
>>> gf(3)/gf(5)
2
```

###gfex class
You have to set the constant before using this class by calling 'gfex.set_const(m,p,ply)'.
and you can get the table of the elements by using 'gfex.info()'.
```
>>> gfex.set_const(2,3,[1,1,0])
>>> gfex.info()
[1, 0, 0] 0
[0, 1, 0] 1
[0, 0, 1] 2
[1, 1, 0] 3
[0, 1, 1] 4
[1, 1, 1] 5
[1, 0, 1] 6
[1, 0, 0] 0
```

extension field:![Imgur](https://i.imgur.com/xbdOhzV.png)
p and m value can be set by 1st and 2nd arguments.

3rd argument means the coefficient of primitive polynomial.
(You need to transposition all item except highest degree item)
![Imgur](https://i.imgur.com/lDYVT3V.png)
