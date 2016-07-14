#!/usr/bin/env python3
# Script used to solve the geocaching puzzle ( http://geocaching.parseapp.com/geocache?id=8808y6oeNo )
import hashlib
import decimal
import time

def coord_to_hash(coord):
    m = hashlib.sha512()
    coordb = str.encode(coord)
    m.update(coordb)

    return m.hexdigest()

def createCoord(NCoord, ECoord, NBase='N 43 3', EBase='E 007 0'):
    NStr = str(NCoord)
    EStr = str(ECoord)
    
    Coord = NBase+NStr+" "+EBase+EStr

    return Coord

if __name__ == "__main__":
    # top_right = "N 43 39.999 E 007 09.999"
    # top_left = "N 43 39.999 E 007 00.000"
    # bottom_left = "N 43 30.000 E 007 00.000"
    # bottom_right = "N 43 30.000 E 007 09.999"

    start = time.time()
    
    sha = 'a90c2ef06f807056ca7566ce35e1cc247a16691c926403411fbff7d73d656b60a95dd5b3d0cfeae8ef9339f2cd64bb5e6770f70701d79e5e27655263cb556c0b'
    finalCoord = ''

    decimal.getcontext().prec = 4
    NCoord = decimal.Decimal('0.000')
    ECoord = decimal.Decimal('0.000')
    inc = decimal.Decimal('0.001')
    isFound = False

    for N in range(9999):
        ECoord = decimal.Decimal('1.000')

        for E in range(9999):
            Coord = createCoord(NCoord, ECoord)
            print(Coord)
            hashCoord = coord_to_hash(Coord)

            if hashCoord == sha:
                isFound = True
                finalCoord = Coord
                print("************************")
                break

            ECoord += inc
            
        if finalCoord != '':
            break
        NCoord += inc

    print("les coordonnées de la cache sont :")
    print(finalCoord)

    end = time.time()
    diff = int(end - start)
    print("le décodage a pris "+str(diff)+" secondes.")
