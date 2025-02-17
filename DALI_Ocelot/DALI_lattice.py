#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#' DAIL lattice  '
# Najmeh Mirian , HZDR, 28- 01- 2025
#
#------------------------------------------------------------------------------
#         LINAC1 and 2 sections for  T0 Linac1 Diagnost_line  linac2 T1
#			Positron  transmission line
# 			MIR FEL  transmission line
#			FIR FEL transmission line
#------------------------------------------------------------------------------

# Gun to Acc

from ocelot.cpbd.elements import *
START1I = Marker(eid='START.1.I')

# INSTR &
# MONITOR
BPM1I =  Monitor(eid='BPM.1.I')
BPM2I =  Monitor(eid='BPM.2.I')
SCRN1I = Monitor(eid='SCRN.1.I')
SCRN2I = Monitor(eid='SCRN.2.I')
FCUP1I = Monitor(eid='FCUP.1.I')
DCM1I =  Monitor(eid='DCM.1.I')
TORB1I = Monitor(eid='TORB.1.I')

# SOLENOID
SOLA1I = Solenoid(l = 0.1, k = 0.0, eid = 'SOLA.1.I')  
SOLB1I = Solenoid(l = 0.1, k = 0.0, eid = 'SOLB.1.I')  


# soft Kicker
CKXY1I = Hcor( l = 0.05, angle=0.0, eid = 'CKXY.1.I')
CKXY2I = Vcor( l = 0.05, angle=0.0, eid = 'CKXY.2.I')
CKXY3I = Hcor( l = 0.05, angle=0.0, eid = 'CKXY.3.I')


KDC1I = Vcor(l = 0.100, angle=0.0, eid = 'KDC.1.I')

# COLLIMATOR
#DCCOL.1.I =   Ecol() L= 0.00, X_MAX = 0.0200, Y_MAX = 0.0200

Q1I=Quadrupole( l = 0.10, k1 = 0, tilt = 0.00, eid ='Q.1.I')
Q2I=Quadrupole( l = 0.10, k1 = 0, tilt = 0.00, eid='Q.2.I')
Q3I=Quadrupole( l = 0.10, k1 = 0, tilt = 0.00, eid='Q.2.I')


D020 = Drift( l = 0.20)
D025 = Drift( l = 0.25)
D010 = Drift( l = 0.10)
D015 = Drift( l = 0.15)
#------------------ from gun to Linac ---------------------
T0= ( START1I,  SOLA1I, D020, SOLB1I, D025, CKXY1I, 
    KDC1I, D020, BPM1I, SCRN1I, FCUP1I, D025, Q1I, D025, Q2I, D025, Q3I, D025, 
    D025, CKXY2I, BPM2I, SCRN2I, D015,  D020, DCM1I, 
    D015, TORB1I, D015, CKXY3I, D020 )

#-----------------------------------
# Linac section
#-----------------------------------
enter_Linac1 = Marker(eid='enter_Linac1')
exit_Linac1 = Marker(eid='exit_Linac1')
exit_Linac2 = Marker(eid='exit_Linac2')

D042 = Drift(l=0.42)  # entrance 
D025= Drift( l = 0.25)
LA1RC1 = Cavity(l=1.038, v=0.012, freq=1.3e9, phi=0, eid='LA1RC10')
LA1D0346 = Drift(l=0.346)
LA1RC2 = Cavity(l=1.038, v=0.012, freq=1.3e9, phi=-0, eid='LA1RC20')

LA2RC1 = Cavity(l=1.038, v=0.012, freq=1.3e9, phi=-0, eid='LA2RC10')
LA2D0346 = Drift(l=0.346)
LA2RC2 = Cavity(l=1.038, v=0.012, freq=1.3e9, phi=-0, eid='LA2RC20')

### LINAC correctors

CX1Lin=Hcor( l = 0.050, angle=0.0, eid = 'CX.1.Lin')
CY1Lin=Vcor( l = 0.050, angle=0.0, eid = 'CY.1.Lin')
## monitor 
BPM1Lin =  Monitor(eid='BPM.1.Lin')
Diagnost_line=(D025,CX1Lin, D025, CY1Lin, D025, BPM1Lin, D020 )
LINAC=(enter_Linac1, LA1RC1, LA1D0346, LA1RC2, exit_Linac1,D042, Diagnost_line ,D042, LA2RC1, 
	 LA2D0346,LA2RC2 , D042,exit_Linac2)

#---------------------------------------------------

#--------------------------------
# Kicker and Diagnostic section T1 transfer section
#--------------------------------
Q1L=Quadrupole( l = 0.20, k1 = -2.59876543209874, tilt = 0.00, eid ='Q.1.L')
Q2L=Quadrupole( l = 0.20, k1 = 2.4783950617284, tilt = 0.00, eid='Q.2.L')

CX1L=Hcor( l = 0.050, angle=0.0, eid = 'CX.1.L')
CY1L=Vcor( l = 0.050, angle=0.0, eid = 'CY.1.L')


BPM3L=Monitor(eid='BPM.3.L')
BPM4L=Monitor(eid='BPM.4.L')


D0080= Drift(l=0.08)
D034=Drift(l=0.34)
D080= Drift(l=0.8)
D050= Drift(l=0.5)

KFBX1T1 =   Hcor(l = 0.90,  angle=0.0, eid = 'KFBX.1.T1')
KFBX2T1 =   Vcor( l= 0.20,  angle=0.0, eid = 'KFBX.2.T1')




D06 = Drift(l=0.600)



D035= Drift( l = 0.35)
ENDLINAC=   Marker()

D100=Drift(l=1.000)
LN1_FITT1= Marker()

T1=(D020,  Q1L,D034,  Q2L, D025,KFBX1T1,D020, CX1L, 
D015, CY1L, D050,BPM3L, D015,  BPM4L, D015,LN1_FITT1,D010)
        

T02T1=(T0,LINAC, T1)


#########################
########################
# Positron Source 
#######################
import math
# deflection angle of dipoles
fl1b_a = 45.0 * math.pi / 180.0
# reference trajectory length through dipoles
fl1b_l = 0.300 * fl1b_a
# edge angles of dipoles
fl1b_e = 11.25 * math.pi / 180.0
print(fl1b_a, fl1b_l,fl1b_e)
septum_angle=15*math.pi/180
print(septum_angle)
#Dipol_length(0.05,fl1b_a, 0.5)

#################

# Design of Transfer to Position Source  TPS

D010 = Drift(l=0.1)
D025 = Drift(l=0.25)
D010 = Drift(l=0.10)
D045 = Drift(l=0.45)
D200 = Drift(l=2)
M1= Marker(eid='M1')
# defining of the quads
Q1TPS = Quadrupole(l=0.15, k1=5.977873987227499)
Q2TPS = Quadrupole(l=0.15, k1=6.0263520817110265)
Q3TPS= Quadrupole(l=0.1, k1=0)
# defining of the bending magnet
#Septom magnet 
BsTPS=SBend(l=0.1, angle=-septum_angle, e1=-septum_angle/2, e2=-septum_angle/2, tilt=0.0, fint=0.0, eid='PS_bend')
BTPS=SBend(l=fl1b_l, angle=-fl1b_a, e1=-fl1b_e, e2=-fl1b_e, tilt=0.0, fint=0.0, eid='PS_bend')

Tranport_to_PS=(D020,BsTPS, D200, BTPS,D025, Q1TPS, D045,Q2TPS, D045, BTPS,M1, D025, Q3TPS, D200 ,M1)
Gun2PS =(T02T1, Tranport_to_PS)


#########################
########################
# MIR FEL Source 
#######################

# Design of Transfer to MIR source 

# Design of Transfer to MIR  TMIR

D010 = Drift(l=0.1)
D025 = Drift(l=0.25)
D020 = Drift(l=0.20)
D055 = Drift(l=0.55)
D0325 = Drift(l=0.325)
D100 = Drift(l=1.)
D250 = Drift(l=2.5)
M1 = Marker()
# defining of the quads
Q0TMIR= Quadrupole(l=0.15, k1=5)
Q1TMIR= Quadrupole(l=0.18, k1=7.591419818385525)
Q2TMIR = Quadrupole(l=0.15, k1=0.6492804179761399)
Q3TMIR= Quadrupole(l=0.15, k1=5)
Q4TMIR= Quadrupole(l=0.15, k1=0)
# defining of the bending magnet
#Septom magnet 
BsTMIR=SBend(l=0.1, angle=septum_angle, e1=septum_angle/2, e2=septum_angle/2, tilt=0.0, fint=0.0, eid='MIR_bend')
BTMIR=SBend(l=0.22, angle=0.6, e1=0.3, e2=0.3, tilt=0.0, fint=0.0, eid='MIR_bend')

Tranport_to_MIR=(D020,BsTMIR, D250, Q0TMIR,D025, BTMIR, D020, Q1TMIR, D055,Q2TMIR, 
	D0325, BTMIR,M1, D015, Q3TMIR, D025, Q4TMIR, D025, M1)

Q5TMIR= Quadrupole(l=0.2, k1=8)
Q6TMIR= Quadrupole(l=0.2, k1=8.791237417530642)
Q7TMIR = Quadrupole(l=0.2, k1=8.791237417530642)
Q8TMIR= Quadrupole(l=0.1, k1=2)
Q9TMIR= Quadrupole(l=0.1, k1=0)
angle=0.6+0.2617993877991494/2
D040=Drift(l=0.40)
D030=Drift(l=0.30)
BTMIR2=SBend(l=0.22, angle=-angle, e1=-angle/2, e2=-angle/2, tilt=0.0, fint=0.0, eid='MIR_bend')
#BTMIR3=SBend(l=0.1, angle=-septum_angle, e1=-septum_angle/2, e2=-septum_angle/2, tilt=0.0, fint=0.0, eid='MIR_bend')
Tranport_to_MIR2=(Q5TMIR,D030, BTMIR2, D040, Q6TMIR, D020,Q7TMIR, D040,BTMIR2, M1, D030,Q8TMIR ,D015,M1)

latcell_to_MIR=(T02T1,Tranport_to_MIR,Tranport_to_MIR2)





#####################################
# FIR FEL Source 
#####################################


QD250 = Drift(l=2.5)
D020 = Drift(l=0.2)
D020 = Drift(l=0.2)
D035=Drift(l=0.35)

QTIR1 = Quadrupole(l=0.2, k1=-0.75)
QTIR2 = Quadrupole(l=0.20, k1=3)
QTIR3 = Quadrupole(l=0.2, k1=-1.5)

CLARCH1 = Cavity(l=1.038, v=0.0, freq=1.3e9, phi=0.0, eid='Dchirper')
DCLAD0346 = Drift(l=0.346)
CLARCH2 = Cavity(l=1.038, v=0.0, freq=1.3e9, phi=0.0, eid='Dchirper')
DCLAD0 = Drift(l=0.346/2)

ChirRC1=(DCLAD0, CLARCH1,DCLAD0346,CLARCH2,DCLAD0 )
D015=Drift(l=0.15)
###
cellTIR = (D250, QTIR1, D020, ChirRC1, D020)

#
BTIR=SBend(l=0.2, angle=0.5, e1=0.25, e2=0.25, tilt=0.0, fint=0.0, eid='IR_bend')  # angle= 
QTIR4 = Quadrupole(l=0.2, k1=9.71)
QTIR5 = Quadrupole(l=0.2, k1=6)
QTIR6 = Quadrupole(l=0.2, k1=-5)


CELLTSIR=(  D010,QTIR2, D020, QTIR3, D020,D020, BTIR, D035, QTIR4,D015, QTIR4, D035,BTIR, D035,QTIR5, D035)#,QTIR6,D035)



TIR_cell=(T02T1,cellTIR, CELLTSIR )

##########################
### second line 




BTIR2=SBend(l=0.2, angle=-0.5, e1=-0.25, e2=-0.25, tilt=0.0, fint=0.0, eid='IR_bend')
QTIR2_1 = Quadrupole(l=0.2, k1=9.69)
QTIR2_2 = Quadrupole(l=0.2, k1=5)
QTIR2_3 = Quadrupole(l=0.2, k1=-1)
#QTIR8 = Quadrupole(l=0.2, k1=-8.5)
D035=Drift(l=0.35)
D015=Drift(l=0.15)
CELLTSIR2=(D010,QTIR2, D020, QTIR3, D020, BTIR2, D035, QTIR2_1,D020, QTIR2_1, D035,BTIR2, D015,QTIR2_2, D020, QTIR2_3, D010)


TIR_cell2=(T02T1,cellTIR, CELLTSIR2 )