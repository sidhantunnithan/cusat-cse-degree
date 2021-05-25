.model small
.stack 100h
.data
	enter_str1    	db      13,10,'Enter FIRST STRING : ',13,10,'$'
	enter_str2    	db      13,10,'Enter SECOND STRING : ',13,10,'$'
	equal		db	13,10,'THE TWO STRINGS ARE EQUAL.',13,10,'$'
       	not_equal	db	13,10,'THE TWO STRINGS ARE NOT EQUAL',13,10,'$'
       	str1		db	20 dup(?)
       	str2		db	20 dup(?)
       	len1		dw	0
       	len2		dw	0
       	
.code
	mov ax, @data
	mov ds, ax
	
	
	mov ah, 09h
	mov dx, offset enter_str1
	int 21h
	
	lea si, str1

	loop1:
	mov ah, 01h
	int 21h
	mov [si], al
	inc si
	inc len1
	cmp al, 13
	jne loop1
	
	sub len1, 1
;	add len1, 30h
	
	mov ah, 09h
	mov dx, offset enter_str2
	int 21h
	
	lea si, str2
	
	loop2:
	mov ah, 01h
	int 21h
	mov [si], al
	inc si
	inc len2
	cmp al, 13
	jne loop2
	
	sub len2, 1
;	add len2, 30h
	
	mov cx, len1
	lea si, str1
	lea di, str2
	
	mov ax, len1
	mov bx, len2
	cmp ax, bx
	jne noequ
	
	loopcomp:
	mov al, [si]
	mov bl, [di]
	cmp al, bl
	jne noequ
	inc si
	inc di
	dec cx
	jnz loopcomp
	
	mov ah, 09h
	mov dx, offset equal
	int 21h
	jmp endloop
	
	noequ:
	mov ah, 09h
	mov dx, offset not_equal
	int 21h
	
	endloop:
	mov ah, 04ch
	int 21h
end