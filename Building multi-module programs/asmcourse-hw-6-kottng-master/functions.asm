section .bss
    arr resq 1
    ar resq 1
    
section .data
    const1 dq 0.35
    const2 dq -0.95
    const3 dq 2.7
    const4 dq 3.0
    const5 dq 2.0
    const6 dq 0.7
    
    const11 dq 0.6
    const12 dq 3.0
    const13 dq -2.0
    const14 dq -1.0
    const15 dq 2.0
    const16 dq 0.7

section .rodata
    out_fat db "%lf", 0

section .text
global f1
global f2
global f3
global diff_f1
global diff_f2
global diff_f3

global test_f1
global test_f2
global test_f3
global test_diff_f1
global test_diff_f2
global test_diff_f3


f1:
    push ebp
    mov ebp, esp
    and esp, -16
    sub esp, 16
    finit 
    fld qword[ebp+8]
    fld qword[ebp+8]
    fmulp
    
    fld qword[const1]
    fmulp
    fld qword[const2]
    fld qword[ebp+8]
    fmulp
    faddp
    fld qword[const3]
    fadd
    
    leave
    ret
f2:
    push ebp
    mov ebp, esp
    and esp, -16
    sub esp, 16
    finit 
    fld qword[ebp+8]
    fld qword[const4]
    fmulp
    fld1
    fadd
    
    leave
    ret

f3:
    push ebp
    mov ebp, esp
    and esp, -16
    sub esp, 16
    finit
    fld1
    fld qword[ebp+8]
    fld qword[const5]
    fadd
    fdiv
    
    leave
    ret
    
diff_f1:
    push ebp
    mov ebp, esp
    and esp, -16
    sub esp, 16
    finit 
    
    fld qword[ebp+8]
    
    fld qword[const6]
    fmulp
    fld qword[const2]
    faddp
    
    leave
    ret
    
diff_f2:
    push ebp
    mov ebp, esp
    and esp, -16
    sub esp, 16
    finit 
    
    fld qword[const4]
    
    leave
    ret
    
diff_f3:
    push ebp
    mov ebp, esp
    and esp, -16
    sub esp, 16
    finit 
    
    
    fld1
    Fchs
    fld qword[ebp+8]
    fld qword[const5]
    fadd
    fdiv
    fld qword[ebp+8]
    fld qword[const5]
    fadd
    fdiv
    
    leave
    ret
    
test_f1:
    push ebp
    mov ebp, esp
    and esp, -16
    sub esp, 16
    finit 
    fld qword[ebp+8]
    fld qword[const11]
    fmulp
    fld qword[const12]
    fadd
    
    leave
    ret
    
test_f2:
    push ebp
    mov ebp, esp
    and esp, -16
    sub esp, 16
    finit 
    fld qword[ebp+8]
    fld qword[const13]
    fadd
    fld st0
    fmulp
    fld qword[ebp+8]
    fld qword[const13]
    faddp
    fmulp
    fld qword[const14]
    fadd
    
    leave
    ret

test_f3:
    push ebp
    mov ebp, esp
    and esp, -16
    sub esp, 16
    finit
    fld1
    fld qword[ebp+8]
    fdiv
    fld qword[const12]
    fmul
    
    leave
    ret

test_diff_f1:
    push ebp
    mov ebp, esp
    and esp, -16
    sub esp, 16
    finit 
    fld qword[const11]
    
    leave
    ret
    
test_diff_f2:
    push ebp
    mov ebp, esp
    and esp, -16
    sub esp, 16
    finit
    
    fld qword[ebp+8]
    fld qword[const13]
    fadd
    fld st0
    fmulp
    fld qword[const12]
    fmul
    
    leave
    ret
    
test_diff_f3:
    push ebp
    mov ebp, esp
    and esp, -16
    sub esp, 16
    finit 
    
    
    fld1
    Fchs
    fld qword[ebp+8]
    
    fdiv
    fld qword[ebp+8]
    
    fdiv
    
    fld qword[const12]
    fmul
    
    leave
    ret
