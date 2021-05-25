
START:	   LXI H,4000
	   MOV A,M
	   RLC
	   RLC
	   RLC
	   RLC
	   ANI 0F
	   MOV B,A
	   MVI C,09

MULTIPLY:	   ADD B
	   DCR C
	   JNZ MULTIPLY
	   MOV B,A
	   MOV A,M
	   ANI 0F
	   ADD B
	   STA 5000
	   HLT
# ORG 4000
# DB 65H
