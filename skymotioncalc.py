import numpy as np
import astropy.constants as const
import astropy.units as u

def calc_2Dskymotion_gen_rad(starmass_Msun, a_AU, e, f, f_earth): 
    M_sun_kg = 1.98840987e+30 #kg
    G = 6.6743e-11 #m^3/kgs^2
    a = a_AU * 1.49597871e+11 #m 
    
    gamma = (a)*(1-(e**2)) / (1+(e*np.cos(f)))  #units of meters
    
    factor1 = (gamma**2) - (2*gamma*np.cos(f-f_earth)) + (1)       #units of meters^2
    factor2 = gamma * ( (2*np.cos(f))+e)*np.sin(f) - np.sin(f+f_earth) - (e*np.sin(f_earth) )  
    
    Lambda = ( (G*starmass_Msun*M_sun_kg) / (a*(1-(e**2))) )**0.5
    
    coeff2 = ( (1) / ((gamma**2) - (2*gamma*np.cos(f-f_earth)) + (1)) )**1.5
    
    xterm = ( -factor1*np.sin(f) ) + ( factor2*(gamma*np.cos(f) - np.cos(f_earth)) )
    yterm = ( -factor1*(e + np.cos(f)) ) + ( factor2*(gamma*np.sin(f) - np.sin(f_earth)) )
  
    mag_skymotion = Lambda*coeff2*([(xterm**2)+(yterm**2)]**0.5)
    return mag_skymotion

def calc_2Dskymotion_solar_arcsec(a_AU, e, f, f_earth): 
    M_sun = 1.98840987e+30 #kg
    G = 6.6743e-11 #m^3/kgs^2
    a = a_AU * 1.49597871e+11 #m
    
    gamma = a*(1-(e**2)) / (1+(e*np.cos(f)))
    
    factor1 = (gamma**2) - (2*gamma*np.cos(f-f_earth)) + 1
    factor2 = gamma*((2*np.cos(f))+e)*np.sin(f) - np.sin(f+f_earth) - (e*np.sin(f_earth))
    
    coeff1 = ((G * M_sun) / (a*(1 - (e**2))))**0.5
    coeff2 = (1 / ((gamma**2) - (2*gamma*np.cos(f-f_earth)) + 1))**1.5
    
    xterm = ( -factor1*np.sin(f) ) + ( factor2*(gamma*np.cos(f) - np.cos(f_earth)) )
    yterm = ( -factor1*(e + np.cos(f)) ) + ( factor2*(gamma*np.sin(f) - np.sin(f_earth)) )
  
    mag_skymotion_rad = coeff1*coeff2*(((xterm**2)+(yterm**2))**0.5)
    mag_skymotion_arcsec = mag_skymotion_rad*206265
    return mag_skymotion_arcsec

