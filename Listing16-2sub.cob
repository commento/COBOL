IDENTIFICATION DIVISION.
PROGRAM-ID. VALIDATECHECKDIGIT IS INITIAL.
DATA DIVISION.
WORKING-STORAGE SECTION.
01     SUMOFNUMS               PIC 9(5).
01     QUOTIENT                PIC 9(5).
01     CALCRESULT              PIC 99.

LINKAGE SECTION.
01     NUMTOVALIDATE.
       02  D1                  PIC 9.
       02  D2                  PIC 9.
       02  D3                  PIC 9.
       02  D4                  PIC 9.
       02  D5                  PIC 9.
       02  D6                  PIC 9.
       02  D7                  PIC 9.

01     RESULT                  PIC 9.
       88 INVALIDCHECKDIGIT    VALUE 1.
       88 VALIDCHECKDIGIT      VALUE 0.

PROCEDURE DIVISION USING NUMTOVALIDATE, RESULT.
BEGIN.
       COMPUTE SUMOFNUMS = (D1 * 7) + (D2 * 6) + (D3 * 5) + (D4 * 4) +
                           (D5 * 3) + (D6 * 2) + (D7).
       DIVIDE SUMOFNUMS BY 11 GIVING QUOTIENT REMAINDER CALCRESULT
       IF CALCRESULT EQUAL TO ZERO
           SET VALIDCHECKDIGIT TO TRUE
       ELSE
           SET INVALIDCHECKDIGIT TO TRUE
       END-IF
       EXIT PROGRAM.
