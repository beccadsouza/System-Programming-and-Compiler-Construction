COPY    START     0
RDBUFF  MACRO     &INDEV,&BUFADR,&RECLTH
        CLEAR     X
        CLEAR     A
        CLEAR     S
        +LDT      #4096
        TD        =X'&INDEV'
        JEQ       *-3
        RD        =X'&INDEV'
        COMPR     A,S
        JEQ       *+11
        STCH      &BUFADR,X
        TIXR      T
        JLT       *-19
        STX       &RECLTH
        MEND
WRBUFF  MACRO     &OUTDEV,&BUFADR,&RECLTH
        CLEAR     X
        LDT       &RECLTH
        LDCH      &BUFADR,X
        TD        =X'&OUTDEV'
        JEQ       *-3
        WD        =X'&OUTDEV'
        TIXR      T
        JLT       *-14
        MEND
