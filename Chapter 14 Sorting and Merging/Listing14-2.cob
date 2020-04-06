IDENTIFICATION DIVISION.
PROGRAM-ID. LISTING14-2.

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
       SELECT WORKFILE ASSIGN TO "Work.tmp".

       SELECT BILLABLESERVICEFILE ASSIGN TO "Listing14-1.dat"
           ORGANIZATION IS LINE SEQUENTIAL.

       SELECT SORTEDCALLSFILE ASSIGN TO "Listing14-2.srt"
           ORGANIZATION IS LINE SEQUENTIAL.

DATA DIVISION.
FILE SECTION.

FD     BILLABLESERVICEFILE.
01     SUBSCRIBERREC-BSF.
       88 ENDOFBILLABLESERVICEFILE VALUE HIGH-VALUES.
       02 FILLER                   PIC X(10).
       02 FILLER                   PIC 9.
          88 VOICECALL             VALUE 2.
       02 FILLER                   PIC X(6).

SD     WORKFILE.
01     WORKREC.
       02  SUBSCRIBERID-WF         PIC 9(10).
       02  FILLER                  PIC X(7).

FD     SORTEDCALLSFILE.
01     SUBSCRIBERREC.
       88  ENDOFBILLABLESFILE      VALUE HIGH-VALUES.
       02  SUBSCRIBERID            PIC 9(10).
       02  SERVICETYPE             PIC 9.
       02  SERVICECOST             PIC 9(4)V99.

WORKING-STORAGE SECTION.
01     SUBSCRIBERTOTAL             PIC 9(5)V99.

01     REPORTHEADER                PIC X(33) VALUE "UNIVERSAL TELECOMS MONTHLY REPORT".

01     SUBJECTHEADER               PIC X(31) VALUE "SUBSCRIBERID     BILLABLEVALUE".

01     SUBSCRIBERLINE.
       02  PRNSUBSCRIBERID         PIC 9(10).
       02  FILLER                  PIC X(8) VALUE SPACES.
       02  PRNSUBSCRIBERTOTAL      PIC $$$,$$9.99.

01     PREVSUBSCRIBERID            PIC 9(10).

PROCEDURE DIVISION.
BEGIN.
       SORT WORKFILE ON ASCENDING KEY SUBSCRIBERID-WF
           INPUT PROCEDURE IS SELECTVOICECALLS
           GIVING SORTEDCALLSFILE
       DISPLAY REPORTHEADER
       DISPLAY SUBJECTHEADER
       OPEN INPUT SORTEDCALLSFILE
       READ SORTEDCALLSFILE AT END SET ENDOFBILLABLESFILE TO TRUE
       END-READ
       PERFORM UNTIL ENDOFBILLABLESFILE
           MOVE SUBSCRIBERID TO PREVSUBSCRIBERID, PRNSUBSCRIBERID
           MOVE ZEROS TO SUBSCRIBERTOTAL
           PERFORM UNTIL SUBSCRIBERID NOT EQUAL TO PREVSUBSCRIBERID
               ADD SERVICECOST TO SUBSCRIBERTOTAL
               READ SORTEDCALLSFILE AT END SET ENDOFBILLABLESFILE TO TRUE
               END-READ
           END-PERFORM
           MOVE SUBSCRIBERTOTAL TO PRNSUBSCRIBERTOTAL
           DISPLAY SUBSCRIBERLINE
       END-PERFORM
       CLOSE SORTEDCALLSFILE
       STOP RUN.

SELECTVOICECALLS.
       OPEN INPUT BILLABLESERVICEFILE
       READ BILLABLESERVICEFILE AT END SET ENDOFBILLABLESERVICEFILE TO TRUE
       END-READ
       PERFORM UNTIL ENDOFBILLABLESERVICEFILE
           IF VOICECALL
               RELEASE WORKREC FROM SUBSCRIBERREC-BSF
           END-IF
           READ BILLABLESERVICEFILE AT END SET ENDOFBILLABLESERVICEFILE TO TRUE
           END-READ
       END-PERFORM
       CLOSE BILLABLESERVICEFILE.