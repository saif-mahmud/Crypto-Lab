.global your_asm_fn
.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp
push	$0xc001f00d
push	%esp	
push	$0xc105ed
push	$0xacce55ed
call	practice
leave
ret


