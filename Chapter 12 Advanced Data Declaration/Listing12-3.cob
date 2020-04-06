IDENTIFICATION DIVISION.
PROGRAM-ID. LISTING12-3.

DATA DIVISION.
WORKING-STORAGE SECTION.
01     COUNTERS.
       02  COUNTER1    PIC S99.
       02  COUNTER2    PIC S99.
       02  COUNTER3    PIC 9.

PROCEDURE DIVISION.
BEGIN.
       DISPLAY "DEBUG 1. DISCOVER WHY I CANT STOP."
       PERFORM ETERNALLOOPING VARYING COUNTER1
           FROM 13 BY -5 UNTIL COUNTER1 LESS THAN 2
           AFTER COUNTER2 FROM 15 BY -4
               UNTIL COUNTER2 LESS THAN 1
           AFTER COUNTER3 FROM 1 BY 1
               UNTIL COUNTER3 GREATER THAN 5
       STOP RUN.

ETERNALLOOPING.
       DISPLAY "COUNTERS 1, 2, 3 ARE -> " COUNTER1 SPACE COUNTER2 SPACE COUNTER3.
