# Exemple réel : les posts de novembre 2026 (sauf semaine 1).
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from sanipure_visuels import *
P=lambda f:U+f
BED=P('a_realistic_high_resolution_indoor_bedroom_scene.jpg')
TAB=P('a_realistic_high_resolution_cinematic_shallow_d.jpg')
FOG=P('a_realistic_cinematic_interior_scene_a_professio.jpg')
KIT=P('a_realistic_cinematic_high_detail_photo_of_a_com.jpg')
OUTD=P('a_crisp_photorealistic_outdoor_scene_of_a_pest_co.jpg')
BACK=P('wide_realistic_high_detail_interior_scene_of_a_m.jpg')
# 9 nov
photo('2026-11-09_voyage_1-couverture.jpg',BED,(0.5,0.4),'PUNAISES DE LIT · VOYAGE',[[('EN VOYAGE,',False)],[('ELLES VOYAGENT',False)],[('AUSSI.',True)]],'Hôtel, location, train de nuit : les bons réflexes avant de défaire vos valises.','N°04','DIAGNOSTIC & DEVIS')
yellow_list('2026-11-09_voyage_2-reflexes.jpg','3 RÉFLEXES',[[('AVANT DE DÉFAIRE',False)],[('VOS VALISES.',True)]],['Inspectez matelas et tête de lit en arrivant','Valise sur le porte-bagages, jamais sur le lit','Au retour : linge lavé à 60 °C ou au sèche-linge'],'Un doute après un séjour ? Contactez-nous.','N°04','DIAGNOSTIC & DEVIS')
# 11 nov
photo('2026-11-11_intervention_1-couverture.jpg',TAB,(0.45,0.4),'NOTRE MÉTHODE',[[('UNE INTERVENTION',False)],[('SANIPURE,',True)],[('ÉTAPE PAR ÉTAPE.',False)]],'Pas de surprise : chaque étape vous est expliquée.','N°05','PARTICULIERS & PROS')
yellow_list('2026-11-11_intervention_2-etapes.jpg','4 ÉTAPES',[[('DU DIAGNOSTIC',False)],[('AU SUIVI.',True)]],['Diagnostic : espèce et étendue identifiées','Préparation : ce qu\'il faut faire avant notre venue','Traitement : protocole adapté à votre logement','Suivi : contrôle et conseils de prévention'],'Un technicien formé, du premier appel au contrôle.','N°05','DIAGNOSTIC & DEVIS')
# 13 nov
photo('2026-11-13_faq-quitter-logement.jpg',FOG,(0.55,0.45),'VOS QUESTIONS',[[('FAUT-IL QUITTER',False)],[('MON LOGEMENT ?',True)]],'Cela dépend du traitement. Votre technicien vous indique avant l\'intervention combien de temps sortir et quand aérer.','N°06','POSEZ VOTRE QUESTION')
# 16 nov
photo('2026-11-16_cafards_1-couverture.jpg',KIT,(0.55,0.5),'CAFARDS',[[('4 SIGNES',True),('QU\'ILS',False)],[('SONT DÉJÀ',False)],[('INSTALLÉS.',False)]],'Ils sortent la nuit. Ce que vous voyez le jour n\'est qu\'une partie du problème.','N°07','PARTICULIERS & PROS')
yellow_list('2026-11-16_cafards_2-signes.jpg','À REPÉRER',[[('CE QUI DOIT',False)],[('VOUS ALERTER.',True)]],['Un insecte qui file quand vous allumez','De petites déjections, comme du poivre moulu','Des capsules brunes derrière les appareils','Une odeur de moisi persistante'],'Intervention et devis : contactez SANIPURE.','N°07','DIAGNOSTIC & DEVIS')
# 18 nov
yellow_list('2026-11-18_gestes-anti-cafards.jpg','PRÉVENTION',[[('5 GESTES',True)],[('ANTI-CAFARDS.',False)]],['Pas de vaisselle sale la nuit','Poubelle fermée et vidée chaque jour','Fuites d\'eau réparées rapidement','Joints refaits autour des éviers et plinthes','Cartons stockés hors de la cuisine'],'Déjà installés ? Ces gestes ne suffiront pas : appelez un pro.','N°08','PARTICULIERS & PROS')
# 20 nov
offer('2026-11-20_deratisation.jpg',OUTD,(0.4,0.45),'DÉRATISATION',[[('SOURIS & RATS.',False)],[('ON S\'EN',False),('OCCUPE.',True)]],['PARTICULIERS','SYNDICS','COMMERCES'],'DEMANDER UN DEVIS','N°09','DEVIS RAPIDE')
# 23 nov
myth('2026-11-23_idee-recue.jpg','IDÉE REÇUE','Les punaises de lit, c\'est un problème d\'hygiène.','FAUX.','Elles se nourrissent de sang, pas de saleté. On les trouve dans des logements impeccables comme dans des hôtels haut de gamme. Le vrai réflexe : agir vite.','N°10','DIAGNOSTIC & DEVIS')
# 25 nov
yellow_list('2026-11-25_preparer-logement.jpg','AVANT LE TRAITEMENT',[[('PRÉPAREZ',False)],[('VOTRE LOGEMENT.',True)]],['Linge et textiles en sacs fermés, lavés à 60 °C','Sol et dessous de lit désencombrés','Meubles laissés dans leur pièce','Fiche de préparation SANIPURE suivie'],'Une bonne préparation, c\'est un traitement plus efficace.','N°11','DIAGNOSTIC & DEVIS')
# 27 nov
photo('2026-11-27_faq-traiter-soi-meme.jpg',BACK,(0.4,0.45),'VOS QUESTIONS',[[('POURQUOI NE PAS',False)],[('TRAITER',False),('SOI-MÊME ?',True)]],'Les sprays du commerce dispersent souvent les insectes dans d\'autres pièces. Un professionnel cible, choisit le bon produit et assure le suivi.','N°12','DIAGNOSTIC & DEVIS')
