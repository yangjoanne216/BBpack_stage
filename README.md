# BBpack_stage
Il s'agit d'un logiciel simple de recherche d'informations sur les entreprises. Vous pouvez saisir un code NAF spécifique (obligatoire) et un département (facultatif) pour obtenir des informations sur un certain nombre d'entreprises (par défaut, une seule recherche renvoie jusqu'à 200 entreprises) : numéro SIREN, nom, adresse du siège social, code postal du siège social, code NAF et activité. Les résultats seront générés sous forme de fichier CSV.

## attention
Le code_NAF et le code_département se trouvent dans code_NAF.csv et departement.csv

## Example
Vous trouverez des exemples de fichiers CSV dans les liens suivants :
companies_47.71Z.csv : contient les informations de 200 entreprises avec le code NAF 47.71Z.

companies_11.02B_33.csv : contient les informations de 116 entreprises avec le code NAF 11.02B situées dans le département 33.


## Problèmes actuels
### Le logiciel utilise l'API de pappers(https://www.pappers.fr/api/documentation), mais cette API n'est pas gratuite pour un accès illimité(Il y a 100 jetons API par mois et je l'ai utilisé 70 fois au cours de mes tests du logiciel.).

### L'API ne fournit pas les coordonnées des entreprises.





