from pychemia import Structure


def Al2O3():
    return Structure(symbols=['Al', 'Al', 'Al', 'Al', 'Al', 'Al', 'Al', 'Al', 'Al', 'Al', 'Al', 'Al', 'O', 'O', 'O',
                              'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                     cell=[[4.807634, 0.0, 0.0], [-2.403817, 4.163534, 0.0], [0.0, 0.0, 13.11727]],
                     reduced=[[0.0, 0.0, 0.352185], [0.666667, 0.333333, 0.685518], [0.333333, 0.666667, 0.018852],
                              [0.0, 0.0, 0.647815], [0.666667, 0.333333, 0.981148], [0.333333, 0.666667, 0.314482],
                              [0.0, 0.0, 0.147815], [0.666667, 0.333333, 0.481148], [0.333333, 0.666667, 0.814482],
                              [0.0, 0.0, 0.852185], [0.666667, 0.333333, 0.185518], [0.333333, 0.666667, 0.518852],
                              [0.306167, 0.0, 0.25], [0.972834, 0.333333, 0.583333], [0.639501, 0.666667, 0.916667],
                              [0.693833, 0.0, 0.75], [0.360499, 0.333333, 0.083333], [0.027166, 0.666667, 0.416667],
                              [0.0, 0.306167, 0.25], [0.666667, 0.639501, 0.583333], [0.333333, 0.972834, 0.916667],
                              [0.0, 0.693833, 0.75], [0.666667, 0.027166, 0.083333], [0.333333, 0.360499, 0.416667],
                              [0.693833, 0.693833, 0.25], [0.360499, 0.027166, 0.583333],
                              [0.027166, 0.360499, 0.916667], [0.306167, 0.306167, 0.75],
                              [0.972834, 0.639501, 0.083333], [0.639501, 0.972834, 0.416667]],
                     periodicity=True)


def CaTiO3():
    return Structure(symbols=['Ca', 'Ti', 'O', 'O', 'O'],
                     cell=3.885326,
                     reduced=[[0.0, 0.0, 0.0], [0.5, 0.5, 0.5], [0.0, 0.5, 0.5], [0.5, 0.0, 0.5], [0.5, 0.5, 0.0]],
                     periodicity=True)


def Cr():
    return Structure(symbols=['Cr', 'Cr'],
                     cell=2.812697,
                     reduced=[[0.0, 0.0, 0.0], [0.5, 0.5, 0.5]],
                     periodicity=True)


def LiF():
    return Structure(symbols=['Li', 'Li', 'Li', 'Li', 'F', 'F', 'F', 'F'],
                     cell=4.061103,
                     reduced=[[0.0, 0.0, 0.0], [0.0, 0.5, 0.5], [0.5, 0.0, 0.5], [0.5, 0.5, 0.0],
                              [0.5, 0.5, 0.5], [0.5, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]],
                     periodicity=True)


def MgB2():
    return Structure(symbols=['Mg', 'B', 'B'],
                     cell=[[3.075169, 0.0, 0.0], [-1.537585, 2.663175, 0.0], [0.0, 0.0, 3.527008]],
                     reduced=[[0.0, 0.0, 0.0], [0.333333, 0.666667, 0.5], [0.666667, 0.333333, 0.5]],
                     periodicity=True)


def MgO():
    return Structure(symbols=['Mg', 'Mg', 'Mg', 'Mg', 'O', 'O', 'O', 'O'],
                     cell=4.255556,
                     reduced=[[0.0, 0.0, 0.0], [0.0, 0.5, 0.5], [0.5, 0.0, 0.5], [0.5, 0.5, 0.0],
                              [0.5, 0.5, 0.5], [0.5, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]],
                     periodicity=True)


def NaCl():
    return Structure(symbols=['Na', 'Na', 'Na', 'Na', 'Cl', 'Cl', 'Cl', 'Cl'],
                     cell=5.690301,
                     reduced=[[0.0, 0.0, 0.0], [0.0, 0.5, 0.5], [0.5, 0.0, 0.5], [0.5, 0.5, 0.0],
                              [0.5, 0.5, 0.5], [0.5, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]],
                     periodicity=True)


def Si():
    return Structure(symbols=['Si', 'Si'],
                     cell=[[0.0, 2.733099, 2.733099], [2.733099, 0.0, 2.733099], [2.733099, 2.733099, 0.0]],
                     reduced=[[0.875, 0.875, 0.875], [0.125, 0.125, 0.125]],
                     periodicity=True)


def SiO2():
    return Structure(symbols=['Si', 'Si', 'O', 'O', 'O', 'O'],
                     cell=[4.044448, 4.044448, 2.621168],
                     reduced=[[0.0, 0.0, 0.0], [0.5, 0.5, 0.5], [0.303008, 0.303008, 0.0], [0.696992, 0.696992, 0.0],
                              [0.196992, 0.803008, 0.5], [0.803008, 0.196992, 0.5]],
                     periodicity=True)


def SnO2():
    return Structure(symbols=['Sn', 'Sn', 'O', 'O', 'O', 'O'],
                     cell=[4.830595, 4.830595, 3.243083],
                     reduced=[[0.0, 0.0, 0.0], [0.5, 0.5, 0.5], [0.306537, 0.306537, 0.0], [0.693463, 0.693463, 0.0],
                              [0.193463, 0.806537, 0.5], [0.806537, 0.193463, 0.5]],
                     periodicity=True)


def TiO2_anatase():
    return Structure(symbols=['Ti', 'Ti', 'Ti', 'Ti', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                     cell=[3.826325, 3.826325, 9.657949],
                     reduced=[[0.5, 0.75, 0.875], [0.5, 0.25, 0.125], [0.0, 0.25, 0.375], [0.0, 0.75, 0.625],
                              [0.0, 0.25, 0.167606], [0.0, 0.75, 0.832394], [0.5, 0.25, 0.917606],
                              [0.5, 0.75, 0.082394], [0.5, 0.75, 0.667606], [0.5, 0.25, 0.332394],
                              [0.0, 0.75, 0.417606], [0.0, 0.25, 0.582394]],
                     periodicity=True)


def ZnO():
    return Structure(symbols=['Zn', 'Zn', 'O', 'O'],
                     cell=[[3.287169, 0.0, 0.0], [-1.643584, 2.846772, 0.0], [0.0, 0.0, 5.304577]],
                     reduced=[[0.333333, 0.666667, 0.999681], [0.666667, 0.333333, 0.499681],
                              [0.333333, 0.666667, 0.378762], [0.666667, 0.333333, 0.878762]],
                     periodicity=True)
