var m01 37
var m02 2
var m03 0
var m04 0
var m05 0
var m06 0
var m07 0

#copier m01 vers m03
tst m01
jmp 13
jmp 17
dec m01
inc m03
inc m04
jmp 10
tst m04
jmp 20
jmp 25
dec m04
inc m01
jmp 17

#enlver m02 à m03 m06 fois
tst m03
jmp 28
jmp 48
tst m02
jmp 31
jmp 39
tst m03
jmp 34
hlt
dec m02
dec m03
inc m05
jmp 28

#recharger m02
inc m04
tst m05
jmp 44
jmp 25
dec m05
inc m02
jmp 41

# on met le reste à 0 et on rajoute 1 à m04
tst m05
jmp 53
hlt
dec m05
jmp 50