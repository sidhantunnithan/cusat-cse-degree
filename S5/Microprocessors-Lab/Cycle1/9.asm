	   LXI H,4000
	   MOV C,M
	   INX H
	   MOV B,M
	   DCR C

LOO:	   INX H
	   MOV A,M
	   CMP B
	   JC LOP
	   MOV B,A

LOP:	   DCR C
	   JNZ LOO
	   LXI H,4020
	   MOV M,B
	   HLT
# ORG 4000
# DB 05,80,66,34,AB,DF
