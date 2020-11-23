"""
Librairie contenant les fonctions permettant de nettoyer les données brutes.
"""

def conversion_types(df):
    """Permet de transformer les types des colonnes naturellement."""
    return df.convert_dtypes()

def suppression_annonces_redondantes(df):
    """Enleve les lignes en doubles."""
    return df.drop_duplicates()

def suppression_colonne_id(df):
    """Enleve la colonnee id, inutile une fois que les
    doublons ont été supprimés.
    """
    return df.drop(axis=1, labels="Id")