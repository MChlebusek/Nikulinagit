from dataclasses import dataclass
import dataclasses
from pickle import TRUE
from re import A


def arithmetic(a1:float,sym:str,a2:float):
    """Lihtne kalkulaator
    + liitmine, - lahutamine, *  korrutamine, / jagamine
    :param float a1: Esimene arv
    :param float a2: Teine arv
    :param str sym: Tehe
    :rtype: var Määramata tüüp
    """
    if sym in ["+","-","/","*"]:
        if sym=="/" and a2==0:
            vas="Div/0"
        else:
            vas=eval(str(a1)+sym+str(a2))
    else:
        vas="Tundmatu tehe!"
    return vas

def is_year_leap(aasta: int)->bool:
    """Liigaasta leidmine
    Tagastab True kui aasta on liigaasta ja false kui ei ole 
    :param int aasta: Aasta number
    :rtype: bool funktionid vastus loogilises formaadis
    """
    aasta=int(aasta)
    if aasta%4==0:
        t= True
        p="Liigaaasta"
    else:
        t= False
        p="Tavaline aasta"
    return t,p


def square(a: float):
    """Ruut
    :param float a:ruudu külg
    :rtype: var Määramata tüüp
    """
    try:
        a=float(a)
        if a>0:
            P=4*a
            S=a**2
            d=a*sqrt(2)
            return P,S,d 
        else:
            v="---"
            return v
    except:
        v="---"
        return v
	


def season(num: int):
    """ Aastaajad
    :param int aastaajad
    :rtype: aastaaeg, millesse see kuu kuulub
    """
    num=int(num)
    if num==12 or num==1 or num==2:
        t="talv"
    elif  num==3 or num==4 or num==5:
        t="kevad"
    elif num==6 or num==7 or num==8:
        t="suvel"
    elif num==9 or num==10 or num==11:
        t="sügis"
    else:
        t="viga"
    return t 



