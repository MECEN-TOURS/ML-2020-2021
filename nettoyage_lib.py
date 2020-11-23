"""
Librairie contenant les fonctions permettant de nettoyer les données brutes.

- Comme les dataframe sont relativement compacts on va se permettre de garder les fonctions "pures" en ce sens (restreint) qu'elle ne modifieront pas leurs arguments.
- Les fonctions publiques auront une signature typée.
- Les fonctions seront testées automatiquement pour garantir leur correction.
- Les fonctions seront documentées avec en particulier un exemple d'utilisation.
"""
import pandas as pd
from io import StringIO
import numpy as np

def __produit_df_test():
    CHAINE = """
Id,Genre,Neuf,Surface,Pieces,Quartier,Prix
annonce-138905473-376235, Appartement, 	0, 	90.00, 	3.0, cathédrale, 	374400.0
annonce-140620177-376235, Appartement, 	0, 	146.27, 	5.0, sud, 	499200.0
annonce-140620179-376235, Appartement, 	0, 	110.00, 	5.0, prébendes, 	499200.0
annonce-133494153-376235, Maison, 	0, 	132.00, 	6.0, prébendes, 	508000.0
annonce-137425993-376235, Maison, 	0, 	185.00, 	7.0, strasbourg, 	676000.0
""".strip()
    df = pd.read_csv(StringIO(CHAINE))
    return df
    
    

def conversion_types(df: pd.DataFrame) -> pd.DataFrame:
    """Permet de transformer les types des colonnes naturellement.
    
    Exemple:
>>> df
                         Id         Genre  Neuf  Surface  Pieces     Quartier      Prix
0  annonce-138905473-376235   Appartement     0    90.00     3.0   cathédrale  374400.0
1  annonce-140620177-376235   Appartement     0   146.27     5.0          sud  499200.0
2  annonce-140620179-376235   Appartement     0   110.00     5.0    prébendes  499200.0
3  annonce-133494153-376235        Maison     0   132.00     6.0    prébendes  508000.0
4  annonce-137425993-376235        Maison     0   185.00     7.0   strasbourg  676000.0
>>> df.dtypes
Id           object
Genre        object
Neuf          int64
Surface     float64
Pieces      float64
Quartier     object
Prix        float64
dtype: object
>>> conversion_types(df)
                         Id         Genre  Neuf  Surface  Pieces     Quartier    Prix
0  annonce-138905473-376235   Appartement     0    90.00       3   cathédrale  374400
1  annonce-140620177-376235   Appartement     0   146.27       5          sud  499200
2  annonce-140620179-376235   Appartement     0   110.00       5    prébendes  499200
3  annonce-133494153-376235        Maison     0   132.00       6    prébendes  508000
4  annonce-137425993-376235        Maison     0   185.00       7   strasbourg  676000
>>> conversion_types(df).dtypes
Id           string
Genre        string
Neuf          Int64
Surface     float64
Pieces        Int64
Quartier     string
Prix          Int64
dtype: object    
    """
    return df.convert_dtypes()

def _verifie_conversion_types() -> bool:
    """Vérifie la fonction précédente"""
    entree = __produit_df_test()
    resultat = conversion_types(entree).dtypes.apply(type)
    en_theorie = pd.Series(
        index=["Id", "Genre", "Neuf", "Surface", "Pieces", "Quartier", "Prix"],
        data=[pd.StringDtype, pd.StringDtype, pd.Int64Dtype, np.dtype, pd.Int64Dtype, pd.StringDtype, pd.Int64Dtype]
    )
    return (resultat == en_theorie
    ).all()

def suppression_annonces_redondantes(df: pd.DataFrame) -> pd.DataFrame:
    """Enleve les lignes en doubles."""
    return df.drop_duplicates()

def _verifie_suppression_annonces_redondantes() -> bool:
    """Vérifie la fonction précédente"""
    ...

def suppression_colonne_id(df: pd.DataFrame) -> pd.DataFrame:
    """Enleve la colonnee id, inutile une fois que les
    doublons ont été supprimés.
    """
    return df.drop(axis=1, labels="Id")

def _verifie_suppression_colonne_id() -> bool:
    """Vérifie la fonction précédente"""
    ...

def numerise_les_colonnes(df: pd.DataFrame) -> pd.DataFrame:
    """Convertit les colonnes en numérique (sauf Quartier)"""
    def filtre(genre):
        if genre == "Appartement":
            return 0
        elif genre == "Maison":
            return 1
        
    resultat = df.copy()
    resultat.Genre = resultat.Genre.apply(filtre)
    return resultat

def _verifie_numerise_les_colonnes() -> bool:
    """Vérifie la fonction précédente"""
    ...

def supprime_partiellement_na(df: pd.DataFrame) -> pd.DataFrame:
    """Supprime les lignes ayant des nan dans les colonnes 
    Surface, Pieces ou Prix.
    """
    return df.dropna(axis=0, subset=["Surface", "Pieces", "Prix"])

def _verifie_supprime_partiellement_na() -> bool:
    """Vérifie la fonction précédente"""
    ...

if __name__ == "__main__":
    assert _verifie_conversion_types()
    assert _verifie_suppression_annonces_redondantes()
    assert _verifie_suppression_colonne_id()
    assert _verifie_numerise_les_colonnes()
    assert _verifie_supprime_partiellement_na()