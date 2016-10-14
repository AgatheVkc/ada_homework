def getFullUrl(PeriodeAcad, PeriodePedag):
    url = base_url
    url = url.replace('[UNITE_ACADEMIQUE]', str(url_section))
    url = url.replace('[PERIODE_ACADEMIQUE]', str(url_years[PeriodeAcad]))
    url = url.replace('[PERIODE_PEDAGOGIQUE]', str(url_bachelor[PeriodePedag]))
    return url
