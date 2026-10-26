# Guide — publication Facebook hebdomadaire SANIPURE

Branche `sanipure-facebook` du dépôt FranceDeratisation/Ads-Lyon. Elle sert de stockage public pour les visuels envoyés à Metricool.

## Paramètres fixes
- Metricool : marque « Sanipure », blogId `7676027`, réseaux `facebook` ET `instagram` (compte sanipure.fr) sur chaque post, `facebookData.type = POST`, `instagramData.type = POST`, `autoPublish: true`.
- `instagramData.isAiGenerated` : `true` si le visuel contient une photo de la photothèque (photos générées par IA), `false` pour un visuel 100 % texte (yellow_list, myth).
- Sur Instagram le lien n'est pas cliquable : garder l'URL dans la légende, c'est le même texte pour les deux réseaux.
- Fuseau : Europe/Paris. 6 posts par semaine :
  - Soir (lundi, mercredi, vendredi 18:30) : posts complets (conseils, signes, offre, méthode, FAQ), carrousels possibles.
  - Matin (mardi, jeudi, samedi 08:00) : format court, 1 image. Mardi et jeudi « LE SAVIEZ-VOUS ? » (gabarit `fact`), samedi « ASTUCE DU SAMEDI » (gabarit `fact` ou `yellow_list`). Exemple : `tools/matin_novembre.py`.
  - Faits du matin : uniquement des faits établis et vérifiables, sans chiffre précis non sourcé.
- Lien d'appel à l'action : https://sanipure.fr/contact/
- URL publique d'une image : `https://raw.githubusercontent.com/FranceDeratisation/Ads-Lyon/sanipure-facebook/<chemin>`
  (Metricool copie l'image chez lui à la programmation).
- Rangement des visuels : `AAAA-MM/AAAA-MM-JJ_sujet[_1-couverture|_2-liste].jpg`.

## Style visuel (ne pas changer sans accord de Matthieu)
- Style « worker » : vrai logo SANIPURE, noir #0C0C0C + jaune #FFAE00, titres Montserrat Black en capitales, un mot en jaune, étiquette jaune de thème, bande de chantier en pied.
- Format 1440x1800 (4:5). Générer avec `tools/sanipure_visuels.py` (gabarits `photo`, `yellow_list`, `offer`, `myth`). Exemple complet : `tools/exemple_novembre.py`.
- Photos : uniquement celles de `photos/` (photos siglées SANIPURE). Planche de repérage : `tools/planche-photos.jpg`.
  Jamais de gros plan d'insecte ou de rongeur, jamais de détourage sur fond blanc, jamais de matériel d'une autre marque.
- Toujours regarder le rendu (planche d'aperçu) avant de programmer : pas de texte coupé, pas de chevauchement.

## Règles de contenu
- Ton professionnel, rassurant, pédagogique. On ne culpabilise jamais le client.
- Jamais de promesse d'élimination garantie, jamais de « 100 % », jamais de prix inventé, jamais de faux avis ou faux chiffres.
- Un seul appel à l'action par post, vers https://sanipure.fr/contact/
- Rotation des piliers : conseils pratiques (~35 %), repérer les signes (~20 %), offre/service (~20 %), coulisses/méthode (~15 %), FAQ (~10 %).
- Thèmes : punaises de lit, cafards, rongeurs, guêpes/frelons (printemps-été), fourmis, désinfection ; tenir compte de la saison.
- Ne pas reprendre un sujet publié dans les 8 dernières semaines, ni la même photo dans les 4 dernières semaines (voir `publications.md`).
- Légende : 400 à 900 caractères, liste à puces ou numérotée, lien. SEO local et hashtags : suivre `zones.md` (1re ligne service + ville, phrase de zone, 6 à 8 hashtags, texte alternatif sur chaque image).
- Colonne « Zone » du journal `publications.md` : noter la ville principale ciblée, pour poursuivre la rotation.
