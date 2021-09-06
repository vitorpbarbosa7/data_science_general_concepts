; hello_world.asm
;
; Author: Vitor Barbosa
; Date: 03-09-2021

; Define first section

global _start

section .text:

_start: ; equivalent of main in c and __main__ in python
; Here we write we want to display
; We use syscalls, a way to communicate with the kernel at low level
; the syscall which allow us to write a message is as follows:
; #define __NR_write 64
; __SYSCALL(__NR_write, sys_write)
; What matters here is the number 
	mov eax, 0x4		; use the write syscall
	mov ebx, 1		; use standard output stdout
	mov ecx, message	; use the message as the buffer (data in memory to process later)
	mov edx, message_length ; supply the length
	int 0x80		; invoke the system to request for a process

	mov eax, 0x1 
	mov ebx, 0 		; Message which means the sys_call was executed with success
	int 0x80

; Section .data to define variables to the program
section .data:
; First variable .message
; 0xA is the representation for new line, the famous \n
	message: db "Hello World!", 0xA
; Keep track of the message length
	message_length equ $-message
