	   LDA 4000
	   MOV B,A
	   ANI 0F
	   MOV C,A
	   MOV A,B
	   RLC
	   RLC
	   RLC
	   RLC
	   ANI 0F
	   ADD C
	   STA 4001
	   HLT
# ORG 4000
# DB 23H
