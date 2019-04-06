.global _main
.section .data
	file_to_run: .asciz "/bin/sh"
.section .text

_main:
    pushl %ebp
    movl %esp, %ebp
    subl $0x8, %esp         # array of two pointers. array[0] = file_to_run  array[1] = 0

    movl $file_to_run, %edi
    movl %edi, -0x8(%ebp)   
    movl $0, -0x4(%ebp)

    movl $11, %eax                      # sys_execve
    movl $file_to_run, %ebx              # file to execute       
    leal -8(%ebp), %ecx                 # command line parameters
    movl $0, %edx                       # environment block
    int  $0x80              

    leave
    ret


