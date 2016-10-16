def getFullUrl(PeriodeAcad, PeriodePedag):
    """
    Given an academic period (years) and a pedagogic period (bachelor semester), 
    fills the general URL with the values associated to those parameters.
    
    @param PeriodeAcad :  Academic year string, in the form ('2015-2016')
    @param PeriodePedag : Pedagogic period string, in the form ('Bachelor x')
    @return url :         The complete url associated to those period, from which we can fetch the students.
    
    """
    url = base_url
    url = url.replace('[UNITE_ACADEMIQUE]', str(url_section))
    url = url.replace('[PERIODE_ACADEMIQUE]', str(url_years[PeriodeAcad]))
    url = url.replace('[PERIODE_PEDAGOGIQUE]', str(url_bachelor[PeriodePedag]))
    return url
