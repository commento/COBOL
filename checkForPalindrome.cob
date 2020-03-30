IDENTIFICATION DIVISION.
PROGRAM-ID. CHECKFORPALINDROME.

DATA DIVISION.
WORKING-STORAGE SECTION.
01     XWORD       PIC X(10).

01     CHARCOUNT   PIC 99.

01     TEXTLENGTH  PIC 99.

PROCEDURE DIVISION.
BEGIN.
       MOVE ZEROS TO CHARCOUNT.
       DISPLAY "ENTER A WORD - " WITH NO ADVANCING
       ACCEPT XWORD
       INSPECT FUNCTION REVERSE(XWORD) TALLYING CHARCOUNT FOR LEADING SPACES
       MOVE FUNCTION UPPER-CASE(XWORD) TO XWORD

       COMPUTE TEXTLENGTH = FUNCTION LENGTH(XWORD) - CHARCOUNT
       IF XWORD(1:TEXTLENGTH) EQUAL TO FUNCTION REVERSE(XWORD(1:TEXTLENGTH))
           DISPLAY XWORD " IS A PALINDROME"
       ELSE
           DISPLAY XWORD " IS NOT A PALINDROME"
       END-IF
       STOP RUN.
