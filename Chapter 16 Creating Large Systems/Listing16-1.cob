IDENTIFICATION DIVISION.
PROGRAM-ID. LISTING16-1.

DATA DIVISION.
WORKING-STORAGE SECTION.
01     INCREMENT               PIC 99 VALUE ZERO.
       88  ENDOFDATA           VALUE ZERO.

PROCEDURE DIVISION.
BEGIN.
       DISPLAY "ENTER AN INCREMENT VALUE (0-99) - " WITH NO ADVANCING
       ACCEPT INCREMENT
       PERFORM UNTIL ENDOFDATA
           CALL "STEADY" USING BY CONTENT INCREMENT
           CALL "DYNAMIC" USING BY CONTENT INCREMENT
           DISPLAY SPACES
           DISPLAY "ENTER AN INCREMENT VALUE (0-99) - " WITH NO ADVANCING
           ACCEPT INCREMENT
       END-PERFORM
       STOP RUN.

IDENTIFICATION DIVISION.
PROGRAM-ID. DYNAMIC.

DATA DIVISION.
WORKING-STORAGE SECTION.
01     RUNNINGTOTAL            PIC 9(5) VALUE ZERO.
01     PRNTOTAL                PIC ZZ,ZZ9.

LINKAGE SECTION.
01     VALUETOADD              PIC 99.

PROCEDURE DIVISION USING VALUETOADD.
BEGIN.
       ADD VALUETOADD TO RUNNINGTOTAL
       MOVE RUNNINGTOTAL TO PRNTOTAL
       DISPLAY "DYNAMIC TOTAL = " PRNTOTAL
       EXIT PROGRAM.
END PROGRAM DYNAMIC.

IDENTIFICATION DIVISION.
PROGRAM-ID. STEADY IS INITIAL.

DATA DIVISION.
WORKING-STORAGE SECTION.
01     RUNNINGTOTAL            PIC 9(5) VALUE ZERO.
01     PRNTOTAL                PIC ZZ,ZZ9.

LINKAGE SECTION.
01     VALUETOADD              PIC 99.

PROCEDURE DIVISION USING VALUETOADD.
BEGIN.
       ADD VALUETOADD TO RUNNINGTOTAL
       MOVE RUNNINGTOTAL TO PRNTOTAL
       DISPLAY "STEADY TOTAL = " PRNTOTAL
       EXIT PROGRAM.
END PROGRAM STEADY.
END PROGRAM LISTING16-1.
       