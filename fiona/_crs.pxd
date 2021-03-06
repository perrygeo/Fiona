cdef extern from "ogr_srs_api.h":
    void    OSRCleanup ()
    void *  OSRClone (void *srs)
    void    OSRDestroySpatialReference (void *srs)
    int     OSRExportToProj4 (void *srs, char **params)
    int     OSRExportToWkt (void *srs, char **params)
    int     OSRImportFromEPSG (void *srs, int code)
    int     OSRImportFromProj4 (void *srs, char *proj)
    int     OSRSetFromUserInput (void *srs, char *input)
    int     OSRAutoIdentifyEPSG (void *srs)
    int     OSRFixup(void *srs)
    const char * OSRGetAuthorityName (void *srs, const char *key)
    const char * OSRGetAuthorityCode (void *srs, const char *key)
    void *  OSRNewSpatialReference (char *wkt)
    void    OSRRelease (void *srs)
    void *  OCTNewCoordinateTransformation (void *source, void *dest)
    void    OCTDestroyCoordinateTransformation (void *source)
    int     OCTTransform (void *ct, int nCount, double *x, double *y, double *z)
