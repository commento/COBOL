IDENTIFICATION DIVISION.
PROGRAM-ID. MANDELBROT-SET-PROGRAM.
DATA DIVISION.
WORKING-STORAGE SECTION.
01  COMPLEX-ARITHMETIC.
    05 X               PIC S9V9(9).
    05 Y               PIC S9V9(9).
    05 X-A             PIC S9V9(6).
    05 X-B             PIC S9V9(6).
    05 Y-A             PIC S9V9(6).
    05 X-A-SQUARED     PIC S9V9(6).
    05 Y-A-SQUARED     PIC S9V9(6).
    05 SUM-OF-SQUARES  PIC S9V9(6).
    05 ROOT            PIC S9V9(6).
01  LOOP-COUNTERS.
    05 I               PIC 99.
    05 J               PIC 99.
    05 K               PIC 999.
77  PLOT-CHARACTER     PIC X.
PROCEDURE DIVISION.
CONTROL-PARAGRAPH.
    PERFORM OUTER-LOOP-PARAGRAPH
    VARYING I FROM 1 BY 1 UNTIL I IS GREATER THAN 24.
    STOP RUN.
OUTER-LOOP-PARAGRAPH.
    PERFORM INNER-LOOP-PARAGRAPH
    VARYING J FROM 1 BY 1 UNTIL J IS GREATER THAN 64.
    DISPLAY ''.
INNER-LOOP-PARAGRAPH.
    MOVE SPACE TO PLOT-CHARACTER.
    MOVE ZERO  TO X-A.
    MOVE ZERO  TO Y-A.
    MULTIPLY J   BY   0.0390625   GIVING X.
    SUBTRACT 1.5 FROM X.
    MULTIPLY I   BY   0.083333333 GIVING Y.
    SUBTRACT 1 FROM Y.
    PERFORM ITERATION-PARAGRAPH VARYING K FROM 1 BY 1
    UNTIL K IS GREATER THAN 100 OR PLOT-CHARACTER IS EQUAL TO '#'.
    DISPLAY PLOT-CHARACTER WITH NO ADVANCING.
ITERATION-PARAGRAPH.
    MULTIPLY X-A BY X-A GIVING X-A-SQUARED.
    MULTIPLY Y-A BY Y-A GIVING Y-A-SQUARED.
    SUBTRACT Y-A-SQUARED FROM X-A-SQUARED GIVING X-B.
    ADD      X   TO X-B.
    MULTIPLY X-A BY Y-A GIVING Y-A.
    MULTIPLY Y-A BY 2   GIVING Y-A.
    SUBTRACT Y   FROM Y-A.
    MOVE     X-B TO   X-A.
    ADD X-A-SQUARED TO Y-A-SQUARED GIVING SUM-OF-SQUARES.
    MOVE FUNCTION SQRT (SUM-OF-SQUARES) TO ROOT.
    IF ROOT IS GREATER THAN 2 THEN MOVE '#' TO PLOT-CHARACTER.