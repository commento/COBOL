IDENTIFICATION DIVISION.
PROGRAM-ID. LISTING15-4_2.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 TextLine.
    02 Letter PIC X OCCURS 80 TIMES. 
      88 Vowel VALUE "A" "E" "I" "O" "U".

01 VowelCount PIC 99 VALUE ZERO.
01 ConsonantCount PIC 99 VALUE ZERO.
01 idx PIC 99.

01     TEXTSIZE PIC 99.
01     TrailingSpaces PIC 99.


PROCEDURE DIVISION.
BEGIN.
       DISPLAY "Enter text : " WITH NO ADVANCING ACCEPT TextLine
       MOVE FUNCTION UPPER-CASE(TextLine) TO TextLine
       INSPECT FUNCTION REVERSE(TextLine) TALLYING TrailingSpaces FOR LEADING SPACES
       COMPUTE TEXTSIZE = FUNCTION LENGTH(TextLine) - TrailingSpaces
       PERFORM VARYING idx FROM 1 BY 1 UNTIL idx > TEXTSIZE
           IF Vowel(idx) ADD 1 TO VowelCount
           ELSE IF Letter(idx) IS ALPHABETIC ADD 1 TO ConsonantCount
           END-IF 
       END-PERFORM
       DISPLAY "The line contains " VowelCount " vowels and " ConsonantCount " consonants." 
       STOP RUN.
