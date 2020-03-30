IDENTIFICATION DIVISION.
PROGRAM-ID. LISTING15-5.

DATA DIVISION.
WORKING-STORAGE SECTION.
01     XSTRING         PIC X(45) VALUE "WHEN,TO THE,SESSIONS,OF SWEET SILENT".
01     DESTINATIONSTRINGS.
       02  DESTSTR1    PIC X(4).
       02  DESTSTR2    PIC X(10).
       02  DESTSTR3    PIC X(3).
       02  DESTSTR4    PIC X(18).

01     CHARCOUNTS.
       02  CCOUNT      PIC 99 OCCURS 4 TIMES.

PROCEDURE DIVISION.
BEGIN.
       UNSTRING XSTRING DELIMITED BY ","
           INTO DESTSTR1 COUNT IN CCOUNT(1)
                DESTSTR2 COUNT IN CCOUNT(2)
                DESTSTR3 COUNT IN CCOUNT(3)
                DESTSTR4 COUNT IN CCOUNT(4)
       END-UNSTRING

       DISPLAY DESTSTR1 " = " CCOUNT(1)
       DISPLAY DESTSTR2 " = " CCOUNT(2)
       DISPLAY DESTSTR3 " = " CCOUNT(3)
       DISPLAY DESTSTR4 " = " CCOUNT(4)
       STOP RUN.
