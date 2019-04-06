.global get_num
.section .text

get_num:

push	%ebp
mov	%esp,%ebp
xor	%edx,%edx
mov	8(%ebp),%eax
mov	$5,%ebx
idiv	%ebx
jmp	*table(,%edx,4)

one:
movl	$0xba5eba11,%eax
jmp	complete

two:
mov	$0xbadcab1e,%eax
jmp	complete

three:
mov	$0xc5c0ffee,%eax
jmp	complete

four:
mov	$0x07ece422,%eax
jmp	complete

five:
mov	$0xc5461fab,%eax
jmp	complete

complete:
leave
ret

table:
	.long	one
	.long	two
	.long	three
	.long	four
	.long	five


