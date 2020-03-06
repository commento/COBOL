IDENTIFICATION DIVISION.
PROGRAM-ID. Listing4-2.
AUTHOR. Michael Coughlan.
*> Accepts two numbers from the user, multiplies them together
*> and then displays the result.

DATA DIVISION.
WORKING-STORAGE SECTION.
01	Num1	PIC 9  VALUE 5.
01	Num2	PIC 9  VALUE 4.

01  Operator PIC X VALUE SPACE.
       88  MULT        VALUE "*".
       88  DIV         VALUE "/".
       88  SUMM        VALUE "+".
       88  SUB         VALUE "-".

01	Result  PIC 99 VALUE ZEROS.

PROCEDURE DIVISION.
CalculateResult.
       DISPLAY "Enter a single digit number - " WITH NO ADVANCING
       ACCEPT Num1
       DISPLAY "Enter a single digit number - " WITH NO ADVANCING
       ACCEPT Num2
       DISPLAY "Enter an operator (*,/,-,+) - " WITH NO ADVANCING
       ACCEPT Operator
       EVALUATE TRUE
           WHEN MULT  MULTIPLY Num1 BY Num2 GIVING Result
           WHEN DIV   DIVIDE Num1 BY Num2 GIVING Result
           WHEN SUMM  ADD Num1 TO Num2 GIVING Result
           WHEN SUB   SUBTRACT Num2 FROM Num1 GIVING Result
       END-EVALUATE
       DISPLAY "Result is = " Result
       STOP RUN.
