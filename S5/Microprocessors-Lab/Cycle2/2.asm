
START:	   LDA 4000
	   LXI D,5001
	   MVI B,00

LOOP:	   STAX D
	   INX D
	   CMP B
	   JZ END
	   DCR A
	   JMP LOOP

END:	   HLT
	   RET
# ORG 4000
# DB B4H
