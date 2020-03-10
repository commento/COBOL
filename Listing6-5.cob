IDENTIFICATION DIVISION.
PROGRAM-ID. LISTING6-5.

DATA DIVISION.
WORKING-STORAGE SECTION.
01     LOOPCOUNT   PIC 9   VALUE 1.
01     LOOPCOUNT2  PIC 9   VALUE 1.

PROCEDURE DIVISION.
P1.
       DISPLAY "S-P1"
       PERFORM P2
       PERFORM P3
       MOVE 7 TO LOOPCOUNT
       PERFORM VARYING LOOPCOUNT FROM 1 BY 1 UNTIL LOOPCOUNT = 2
           DISPLAY "INLINE - " LOOPCOUNT
       END-PERFORM
       DISPLAY "E-P1"
       STOP RUN.

P2.
       DISPLAY "S-P2"
       PERFORM P5 WITH TEST BEFORE VARYING LOOPCOUNT FROM 1 BY 1 UNTIL LOOPCOUNT > 2
       DISPLAY "E-P2".

P3.
       DISPLAY "S-P3"
       PERFORM P5
       PERFORM P6 3 TIMES
       DISPLAY "E-P3".

P4.
       DISPLAY "P4-" LOOPCOUNT2
       ADD 1 TO LOOPCOUNT2.

P5.
       DISPLAY "S-P5"
       DISPLAY LOOPCOUNT "-P5-" LOOPCOUNT2
       PERFORM P4 WITH TEST AFTER UNTIL LOOPCOUNT2 > 2
       DISPLAY "E-P5".

P6.
       DISPLAY "P6".
