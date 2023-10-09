var m01 5
var m02 3
var m03 0
var m04 0

tst m01
jmp 9
hlt
dec m01

# ajouter m02 à m03
tst m02
jmp 15
jmp 20
dec m02
inc m03
inc m04
jmp 12

tst m04
jmp 23
jmp 6
dec m04
inc m02
jmp 20