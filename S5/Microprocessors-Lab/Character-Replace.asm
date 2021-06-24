.model small
.stack 100h
.data
    msg1 db "ENTER STRING: $"
    msg2 db "ENTER THE CHARACTER TO BE REPLACED: $"
    msg3 db "ENTER THE CHARACTER TO BE REPLACED WITH: $"
    msg4 db "CHARACTER NOT FOUND. $"
    input db 20 dup('$')
    char1 db 1 dup('$')
    char2 db 1 dup('$')
    ifcharfound db 1 dup('$')

.code
start:              
    mov ax,@data        ; init data segment
    mov ds,ax

    lea dx,msg1         ; print prompt to enter string
    mov ah,09h
    int 21h

   	mov si,00h          ; increment counter 

l1:                     ; loop to read input string
	mov ah,01h
	int 21h
	mov input[si], al
	inc si
	cmp al,0dh
	jne l1

    lea dx,msg2         ; print prompt to enter character to be replaced
    mov ah,09h
    int 21h

    mov ah,01h          ; read one character from stdin
	int 21h
	mov char1, al

    mov dl, 0ah         ; print newline
    mov ah,02h      
	int 21h
    
    lea dx,msg3         ; print prompt to enter character to be replaced with
    mov ah,09h
    int 21h

    mov ah,01h          ; read one character from stdin
	int 21h
	mov char2, al

    mov dl, 0ah         ; print newline
    mov ah,02h      
	int 21h

    mov si,00h
l2:                     ; read character from input string
	mov dl,input[si]    
    cmp dl, char1       ; if character not to be replaced skip replacement
    jne l3
    mov ifcharfound, 01 ; check to see if character found
    mov dl, char2       ; replace character
l3:                     ; print character to stdout
	mov ah,02h      
	int 21h
	inc si
	cmp al,0dh          ; if 0x0D end loop
	je l4
	jmp l2

l4:                     ; check if any replacements were done
    mov dl, ifcharfound
    cmp dl, 01
    je l6
    lea dx,msg4         ; print message that no replacements were done
    mov ah,09h
    int 21h

l6:
	mov ah,4ch
	int 21h
end start

end
