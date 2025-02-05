#------------------------------------------------------------------------------
#         LINAC1 and 2 sections for  T0 Linac1 Diagnost_line  linac2 T1
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
CKXY1I = Hcor( l = 0.1, angle=0.0, eid = 'CKXY.1.I')
CKXY2I = Vcor( l = 0.1, angle=0.0, eid = 'CKXY.2.I')
CKXY3I = Hcor( l = 0.1, angle=0.0, eid = 'CKXY.3.I')


KDC1I = Vcor(l = 0.200, angle=0.0, eid = 'KDC.1.I')

# COLLIMATOR
#DCCOL.1.I =   Ecol() L= 0.00, X_MAX = 0.0200, Y_MAX = 0.0200

Q1I=Quadrupole( l = 0.20, k1 = 0, tilt = 0.00, eid ='Q.1.I')
Q2I=Quadrupole( l = 0.20, k1 = 0, tilt = 0.00, eid='Q.2.I')
Q3I=Quadrupole( l = 0.20, k1 = 0, tilt = 0.00, eid='Q.2.I')


D020 = Drift( l = 0.20)
D010 = Drift( l = 0.10)
#------------------ from gun to Linac ---------------------
T0= ( START1I,  SOLA1I, D020, SOLB1I, D020, CKXY1I, 
    KDC1I, D010, BPM1I, SCRN1I, FCUP1I, D020, Q1I, D020, Q2I, D020, Q3I, D020, 
    D020, CKXY2I, BPM2I, SCRN2I, D010,  D020, DCM1I, 
    D010, TORB1I, D010, CKXY3I, D020 )

#-----------------------------------
# Linac section
#-----------------------------------
enter_Linac1 = Marker(eid='enter_Linac1')
exit_Linac1 = Marker(eid='exit_Linac1')
exit_Linac2 = Marker(eid='exit_Linac2')

D042 = Drift(l=0.42)  # entrance 

LA1RC1 = Cavity(l=1.038, v=0.012, freq=1.3e9, phi=0.0, eid='LA1RC10')
LA1D0346 = Drift(l=0.346)
LA1RC2 = Cavity(l=1.038, v=0.012, freq=1.3e9, phi=0.0, eid='LA1RC20')

LA2RC1 = Cavity(l=1.038, v=0.012, freq=1.3e9, phi=0.0, eid='LA2RC10')
LA2D0346 = Drift(l=0.346)
LA2RC2 = Cavity(l=1.038, v=0.012, freq=1.3e9, phi=0.0, eid='LA2RC20')

### LINAC correctors

CX1Lin=Hcor( l = 0.10, angle=0.0, eid = 'CX.1.Lin')
CY1Lin=Vcor( l = 0.10, angle=0.0, eid = 'CY.1.Lin')
## monitor 
BPM1Lin =  Monitor(eid='BPM.1.Lin')
Diagnost_line=(D020,CX1Lin, D020, CY1Lin, D020, BPM1Lin, D020 )
LINAC=(enter_Linac1, LA1RC1, LA1D0346, LA1RC2, exit_Linac1,D042, Diagnost_line ,D042, LA2RC1, 
	 LA2D0346,LA2RC2 , D042,exit_Linac2)

#---------------------------------------------------

#--------------------------------
# Kicker and Diagnostic section T1 transfer section
#--------------------------------
Q1L=Quadrupole( l = 0.20, k1 = -2.59876543209874, tilt = 0.00, eid ='Q.1.L')
Q2L=Quadrupole( l = 0.20, k1 = 3.094783950617284, tilt = 0.00, eid='Q.2.L')

CX1L=Hcor( l = 0.010, angle=0.0, eid = 'CX.1.L')
CY1L=Vcor( l = 0.010, angle=0.0, eid = 'CY.1.L')


BPM3L=Monitor(eid='BPM.3.L')
BPM4L=Monitor(eid='BPM.4.L')

LN1_FITT1= Marker(eid='LN1_FITT1')
D0080= Drift(l=0.08)
D034=Drift(l=0.34)
D080= Drift(l=0.8)
D050= Drift(l=0.5)

KFBX1T1 =   Hcor(l = 0.20,  angle=0.0, eid = 'KFBX.1.T1')
KFBX2T1 =   Vcor( l= 0.20,  angle=0.0, eid = 'KFBX.2.T1')




D06 = Drift(l=0.600)


D012= Drift( l = 0.12)
D035= Drift( l = 0.35)
ENDLINAC=   Marker()

D150=Drift(l=1.500)


T1=(D020,  Q1L,D034, KFBX1T1, D0080, Q2L,D020, CX1L, 
D010, CY1L, D050,BPM3L, D010,  BPM4L, D010,LN1_FITT1,D150)
        

T02T1=(T0,LINAC, T1)


#########################
########################
# Positron Source 
#######################


D020 = Drift(l=0.02)
D025 = Drift(l=0.25)
#D3 = Drift(l=0.25)
#D4= Drift(l=0.25)

# defining of the quads

Q1TPS= Quadrupole(l=0.2, k1=25)
Q2TPS = Quadrupole(l=0.1, k1=0)
# defining of the bending magnet

BTPS=SBend(l=0.236, angle=0.78539, e1=0.1963495, e2=0.1963495, tilt=0.0, fint=0.0, eid='TPS_bend')

Tranport_to_PS =(BTPS, D025, Q1TPS, D025, BTPS, D025, Q2TPS, D020)
Gun2PS =(T02T1, Tranport_to_PS)
