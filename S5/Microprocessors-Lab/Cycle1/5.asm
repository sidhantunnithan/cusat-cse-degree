
START:	   LXI H,4000
	   MOV B,M
	   MVI C,00
	   INX H
	   MOV A,M

LOOP:	   CMP B
	   JC SKIP
	   SUB B
	   INR C
	   JMP LOOP

SKIP:	   STA 4011
	   MOV A,C
	   STA 4010
	   HLT
# ORG 4000
# DB 05H,09H
