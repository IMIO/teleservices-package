# teleservices-package changelog

:App involved: iA.Téléservices, Publik
:Info: This is the changelog for the teleservices-package
:Authors: Daniel Muyshond, Nicolas Hislaire, Nicolas Selva
:License: GNU Affero General Public License v3 or later (AGPLv3+)

## [0.3.1] - 28-08-2023

### Fixed

- Some sentances and tips in candidature form; use better formule [dmshd]

### Deleted

- Unused 'Urbanisme' category [dmshd]

## [0.3.0] - 04-05-2023

### Added

- [TELE-1682] Add form wf card and datasource for casier judiciaire BOSA [njphs]

## [0.2.19] -

### Fixed

- [TELE-1547] Fix spelling mistakes [dmshd] [njphs]
- [TELE-1577] Condition acknowl. checkbox for translation document help [dmshd]
- [TELE-1528] Fix spelling mistake [dmshd]
- [TELE-1528] Fix parenthesis instead of curlys [dmshd] [njphs]
- [TELE-1528] Fix None appearing in prod [dmshd] [njphs]
- [SUP-27953] convert ds_personne_concernee to JSON (fix python deprec) [dmshd]
- [SUP-27989] remove form_name, fix spelling and gender use [dmshd]
-             Fix categories mismatch by completing missing categories name in the xml file [dmshd]
- [SUP-27957] Fix python with undefined variables causing bugs, convert depraceted Python to django [dmshd]
- [TELE-1598] fix form-rechercher-un-acte-dans-la-banque-des-actes-d-etat-civil-baec.wcs [njphs]
- [MCITICAPA-3] Permis de conduire : Fix form import in wrong cat, enable form and set "citoyen (test)" as role du demandeur [dmshd]
- [MCITICAPA-3] Euthanasie : Fix form import in wrong cat, enable and set "citoyen (test)" as demandeur
- [MCITICAPA-3] Restore missing category "Modèles" (now labelled "iMio - Modèles") [dmshd]
- [MCITICAPA-3] Coordonnées (modèle) : Fix category, activate + Citoyen(test) as demandeur, update whole xml with recent publik export particularities (types,ect) [dmshd]
- [MCITICAPA-3] Date et heure (modèle) : Fix category, activate + Citoyen(test) as demandeur, update whole xml with recent publik export particularities (types,ect) [dmshd]
- [MCITICAPA-3] Redirection(modèle) : Fix category, activate + Citoyen(test) as demandeur, update whole xml with recent publik export particularities (types,ect) [dmshd]
- [MCITICAPA-3] Redirection Mon Dossier (modèle) : Fix category, activate + Citoyen(test) as demandeur, update whole xml with recent publik export particularities (types,ect)
- [TELE-1614] Tryout to fix AppRegistry error when indus script occurs [dmshd]
- [TELE-1614] Fix unwanted missing demands [dmshd]
- [TELE-1607][SUP-28626] Fix old python condition blocking form completion [dmshd]

### Added

- [TELE-1556] Add form_option for délai migration BAEC [njphs]
- [TELE-1559] Add "pièce justificative" feature option [dmshd]
- [TELE-1516] Add missing hint for 'redirection automatique' form option [dmshd]
- [TELE-1516] Add missing hint for 'reglement communal' form option [dmshd]
- [TELE-1557] Add option allowing additional text for agents [dmshd]
- [TELE-1557] Update descriptions + allow add text field (BAEC/Actes) [dmshd]
- [TELE-1574] Add missing form option in WF for optionnal proof document [dmshd]
- [TELE-1577] Add latest asked changes (Types of docs) [dmshd]
- [TELE-1528] Add defaut value to avoid None if option not set [dmshd] [njphs]
- Add modèle "Tableau de listes" [dmshd]
- Add modele for Carte [njphs][dmshd]
- [TELE-1298] Update default iMio WF : xml, add 'supprimer' global action [dmshd][njphs]

### Updated

- [TELE-1577] Update types of docs descriptions display by directly using the desc in the list item [dmshd]
- [TELE-1578] Update anonymisation in main wf [njphs]
- [TELE-1528] Update Workflow with last changes about migration-request [dmshd] [njphs]
- [TELE-1528] Update Forms with last changes about migration-request [dmshd] [njphs]
- [SUP-27991] Relabel and use capital + add hints in form_options (modele procuratio wf) [dmshd]
- [SUP-27953] Migrate to json value the simplest & easy to do python datasources [dmshd]
- [SUP-27953] migrate page conditions to django (cand.poste à pourvoir) [dmshd]
- [TELE-1601] Uniformize tel hints on some forms [dmshd]
- Update occupation voie publique (xml update+role demandeur+activé) [dmshd]
- Update pret/location materiel form (xml update+role demandeur+activé) [dmshd]
- Update déclaration chien dangereux form (xml update+role demandeur+activé) [dmshd]
- Add missing category slug, activate form, use "Citoyen (test)" (autorisation acquisition animal) [dmshd]
- Déclaration alarme/caméré : Update xml with types, activate, use Citoyen (test) [dmshd]
- Acte de décès : activate, use Citoyen (test) [dmshd]
- [TELE-1612] [TELE-1613] Update python to django for some category [njphs]
- [SUP-28606] Update WF mondossier with donnée de traitement for authentification forte or not [njphs]
- [SUP-28606] Update WF mondossier with donnée de traitement with paiement reference [njphs]
- Fix mail not inclusiv and wrong {{form_name}} usage + uniformize them [dmshd, caro, njphs]
- Remove first names from mail greetings [dmshd, caro, njphs]

### Removed

- [TELE-1557] Delete obsolete comment

## [0.2.18] - 10-11-2022

### Added

- [TELE-1547] Init "Tous les actes" (BAEC) (form + wf) [dmshd] [njphs]

### Removed

- [TELE-1524] Delete merge warning [dmshd] [njphs]

### Updated

- [TELE-1534] Update feedback text following team's reviewing [dmshd]
- [TELE-1534] Use 'title' as id in datasource [dmshd] [njphs]
- [TELE-1534] Update with latest BAEC mods [dmshd] [njphs]

### Fixed

- [TELE-1534] Fix typo in computed var name [dmshd]

## [0.2.17] - 26-10-2022

### Fixed

- [TELE-154] add missing letter in field [dmshd]

### Updated

- [TELE-862] Update datasource 'mode_de_delivrance' (text) [dmshd] [njphs]
- [TELE-1524] Implement new BAEC linking [dmshd] [njphs]

## [0.2.16] - 12-10-2022

### Updated

- [MTELEVIEA-12] Avoid sender / subject redundancy in all mails [dmshd]

## [0.2.15] - 12-10-2022

### Added

- [MTELEVIEA-12] Improve both user/agent UX for bank transfer usecase (see jira for the detail) [dmshd]

### Fixed

- [MTELEVIEA-12] Fix spelling mistake in form option tooltip [dmshd]

## [0.2.13] - 03-10-2022

### Changed

- [TELE-1501] make some fields mandatory in block iMio - Identité Changement Adresse [nhi]

## [0.2.12] - 22-08-2022 -

### Fixed

- [TELE-1434] Remove italic when it is Inadequately used on full sentence [dmshd]

## [0.2.11] - 17-08-2022 -

### Updated

- [TELE-1412] démarche extrait de casier judiciaire add motifs

## [0.2.11] - 08-08-2022 -

### Updated

- [TELE-1412] wf animal supprimer du panier

## [0.2.11] - 28-07-2022 -

### Updated

- [TELE-1389] Form animal add extrain in PJ

## [0.2.11] - 27-07-2022 -

### Updated

- [TELE-1388] Form for many persons

## [0.2.11] - 26-07-2022 -

### Updated

- [TELE-1383] Workflow rendez-vous with possibility of externe agenda

## [0.2.11] - 26-07-2022 -

### Fixed

- [MTELEENGA-11] gratuit but with or whitout extra fees, virement

## [0.1.49] - 26-07-2022 -

### Added

- [MTELEENGA-11] add virement to bien être animal wf

## [0.1.50] - 11-07-2022 -

### Updated

- [TELE-1253] update roles for wf fiche recrutement

## [0.1.49] - 11-07-2022 -

### Added

- [TELE-1371] add form and wf bien être animal

## [0.1.48] - 09-06-2022 -

### Updated

- [TELE-1188] update forms agenda plusieurs personnes

## [0.1.47] - 17-05-2022 -

### Updated

- [TELE-1134] typo in modele coordonnées

## [0.1.47] - 10-05-2022 -

### Updated

- [TELE-1312] add gratuit in changement adresse wf

## [0.1.47] - 03-05-2022 -

### Fixed

- [SUP-23200] fix courriel destinaitaire in candidature spontané wf

## [0.1.47] - 04-04-2022 -

### Updated

- [TELE-1134] fix category of Acte de Reconnaissance pré/post-natale

## [0.1.47] - 04-04-2022 -

### Updated

- [TELE-1288] updated forms Candidature validation nrn

## [0.1.47] - 04-04-2022 -

### Updated

- [TELE-1288] updated forms Population validation nrn

## [0.1.47] - 04-04-2022 -

### Updated

- [TELE-1288] updated forms Actes validation nrn

## [0.1.46] - 30-03-2022 -

### Updated

- [TELE-1282] updated forms Pouplation Description

## [0.1.46] - 30-03-2022 -

### Updated

- [TELE-1282] updated forms Etat-Civil Description

## [0.1.46] - 30-03-2022 -

### Updated

- [TELE-1164] updated form Acte de Reconnaissance pré/post-natale

## [0.1.46] - 30-03-2022 -

### Fixed

- [TELE-1148] updated commentaire in Candidature poste à pourvoir

## [0.1.46] - 30-03-2022 -

### Fixed

- [TELE-1154] fixed commentaire in Certificat de vie

## [0.1.46] - 30-03-2022 -

### Fixed

- [TELE-1283] fixed condition in Occupation de la voie publique

## [0.1.45] - 01-01-2022 -

### update

- [SUP-21926] update webservice réservation agenda for rappel

## [0.1.45] - 01-01-2022 -

### Added

- [TELE-1238] add new wf for pin/puk form and update its form

## [0.1.44] - 24-01-2022 -

### Fixed

- [TELE-1226] fix spelling mistake in status name [dmshd]
- [TELE-1226] fix order of actions making a mail action is not played (mail not sent) [dmshd]

## [0.1.43] - 18-01-2022 -

### Fixed

- [TELE-1207] add datasources and carddefs for new "motifs" and "modes d'envoi" using cards [dmshd]

## [0.1.42] - 13-12-2021 -

### Fixed

- [TELE-1182] add hint in forms and blocs for list item [NSE]

## [0.1.41] - 23-11-2021 -

### Fixed

- [TELE-1163] remove hard burdinne in workflow [nhi]

## [0.1.40] - 22-11-2021 -

### Fixed

- [TELE-1158] fix spelling mistake [dmshd]

## [0.1.39] - 25-10-2021 -

### Fixed

- add pays in data_source

## [0.1.38] - 25-10-2021 -

### Fixed

- add motifs and destinations in data_source

## [0.1.37] - 19-10-2021 -

### Fixed

- [TELE-1144] set install path in jenkinsfile [nhi]

## [0.1.36] - 18-10-2021 -

### Updated

- set version in setup.py
- use iateleservicesCreateDeb pipeline function

## [0.1.35] - 18-10-2021 -

### Updated

- workflow-imio-gestion-des-rendez-vous-et-evenements-package with guichet

## [0.1.34] - 18-10-2021 -

### Removed

- BAEC option in [dmshd]

## [0.1.33] - 14-10-2021 -

### Fixed

- [TELE-1135] Fix spelling mistake in two variables inside two conditions [dmshd]

## [0.1.32] - 14-10-2021 -

### Fixed

- [TELE-1128] Fix links not working because of protocol set to "http" [dmshd]

## [0.1.31] - 14-10-2021 -

### Added

- Install usage in README [dmshd]

## [0.1.30] - 05-10-2021 -

### Fixed

- Fix typo in subject of refus mail in WF dep. citoyen

## [0.1.29] - 05-10-2021 -

### Fixed

- Fix subject of refus mail in WF dep. citoyen

## [0.1.28] - 05-10-2021 -

### Fixed

- Do not verify SSL certificate's validity
- Fix motif refus display in mail in WF dep. citoyen
- Re order auto-jumps for refund in WF dep. citoyen

## [0.1.27] - 28-09-2021 -

### Fixed

- Fix total amount if a coma is used instead of a dot

## [0.1.26] - 24-09-2021 -

### Fixed

- Ghost mail template in wf iMio - Changement d'adresse

## [0.1.25] - 23-09-2021 -

### Fixed

- category of euthanasia's form

## [0.1.24] - 22-09-2021 -

### Updated

- all forms
- all workflows
- all mail-templates
- all blocks

## [0.1.23] - 22-09-2021 -

### Fix

- missing xml tag

### Removed

- one more option in forms

## [0.1.22] - 22-09-2021 -

### Removed

- all roles and most prefill options in forms

## [0.1.21] - 21-09-2021 -

### Updated

- all forms
- all workflows
- all mail-templates
- all blocks

## [0.1.20] - 13-09-2021 -

### Updated

- wf with paiement alert

## [0.1.19] - 13-09-2021 -

### Updated

- wf paiement with pk button basket

## [0.1.18] - 07-09-2021 -

### Updated

- form changement d'adresse with instruction
- category

## [0.1.17] - 07-09-2021 -

### Updated

- wf changement d'adresse

## [0.1.16] - 07-09-2021 -

### Updated

- form radiation pour l'étranger

## [0.1.15] - 30-08-2021 -

### Updated

- pop etat-civil form's with mode d'emploi

## [0.1.14] - 26-08-2021 -

### Updated

- wf iMio - Gestion des rendez-vous et événements - package with documentation
- forms acte with redirection mondossier
- some form's name with Demande
- a mail template in workflow-imio-changement-d-adresse
- url name et internal identifier for all form
- name files of all form
- all form's name

### Merged

- doublon enseignement communal

## [0.1.12] - 11-08-2021 -

### Updated

- wf Chien dangereux
- wf document pdf

### Added

- mode d'emploi on Finance and Logement forms
- mode d'emploi chien dangereux
- mode d'emploi on Environement forms
- Mode d'emploi on euthanasie form

### Patched

- card candidature poste à pourvoir slug's
- candidature cards slug's
- form imio compteur d'eau champ société

## [0.1.11] - 09-08-2021 -

### Disabled

- all forms

### Updated

- form and wf chien dangereux
- form and wf demande d'occuptation de la voie publique
- form Déclaration de résidence secondaire
- lien mondossier in form Acte
- form changement d'adresse
- block-identite_changement_adresse.wcs
- form acte de nationalité
- workflow for radiation pour l'étranger
- form certificat de radiation
- wf departement citoyen
- form candidature spontanée

### Patched

- remove data source motif and destination
- form_option_cp in cohabitation legale and radiation pour l'étranger

### Added

- Cards lien vers formulaire

## [0.1.9] - 05-08-2021 -

### Updated

- forms iMio from category emplois

### Patched

- forms redirection with correct wf

## [0.1.8] - 29-07-2021 -

### Patched

- forms iMio - Redirection Modele link to workflow

## [0.1.7] - 29-07-2021 -

### Patched

- cards

## [0.1.6] - 28-07-2021 -

### Updated

- form iMio - Candidature spontanée

## [0.1.5] - 27-07-2021 -

### Updated

- localite in iMio - Demande d'occupation de la voie publique

## [0.1.4] - 27-07-2021 -

### Patched

- error message rn
- regex rn

## [0.1.3] - 27-07-2021 -

### Patched

- condition rn

## [0.1.2] - 27-07-2021 -

### Patched

- View of card card-imio-candidature-pour-l-enseignement-communal-fonctions-disponibles

## [0.1.1] - 26-07-2021 -

### Patched

- View of card card-imio-candidature-pour-l-enseignement-communal-fonctions-disponibles

## [0.1.0] - 26-07-2021 -

### Updated

- form form-imio-candidature-enseignement-communal

### Added

- carddefs for fonction in this form
  [nse]

## [0.0.55] - 12-07-2021 -

### Updated

- forms internal identifier
  [nse]

## [0.0.54] - 12-07-2021 -

### Updated

- form iMio - Déclaration de chien dangereux
  [nse]

## [0.0.53] - 12-07-2021 -

### Added

- description to forms

### Updated

- change blocs de champs name
  [nse]

## [0.0.52] - 06-07-2021 -

### deleted

- url name from all forms
  [nse]

## [0.0.50] - 06-07-2021 -

### updated

- agenda forms name
  [nse]

## [0.0.49] - 06-07-2021 -

### Added

- Modele coordonées
  [nse]

## [0.0.48] - 06-07-2021 -

### Patched

- category of redirection forms
  [nse]

## [0.0.47] - 05-07-2021 -

### Patched

- category of some forms
- name of some forms
  [nse]

## [0.0.46] - 05-07-2021 -

### Patched

- category of some forms
  [nse]

## [0.0.45] - 05-07-2021 -

### Updated

- category url_name
  [nse]

## [0.0.44] - 05-07-2021 -

### Updated

- category id
  [nse]

## [0.0.43] - 05-07-2021 -

### Updated

- change file name forms
  [nse]

## [0.0.42] - 05-07-2021 -

### Updated

- open and close hour in agenda forms
  [nse]

## [0.0.41] - 02-07-2021 -

### Added

- category iMio - ... and move forms into
  [nse]

## [0.0.40] - 01-07-2021 -

### Patched

- 2 forms agenda
  [nse]

## [0.0.39] - 01-07-2021 -

### Patched

- Changelog
  [nse]

## [0.0.38] - 01-07-2021 -

### Patched

- bloc de champs personne for forms agenda
  [nse]

## [0.0.37] - 01-07-2021 -

### Added

- workflow for forms agenda
- froms agenda
- category iMio - agenda
- bloc de champs personne for forms agenda
  [nse]

## [0.0.36] - 01-07-2021 -

### Updated

- workflow par défaut and herit
  [nse]

## [0.0.35] - 01-07-2021 -

### Added

- modele date et heure
- datasourec heure et minute
  [nse]

## [0.0.21] - 30-06-2021 -

### Delete

- many forms for test
  [nse]

## [0.0.20] - 28-06-2021 -

### Update

- blocs de champs
  [nse]

## [0.0.19] - 25-06-2021 -

### Added

- mails template for wf par defaut

### Update

- wf par defaut comment alert
- blocs de champs
  [nse]

## [0.0.18] - 24-06-2021 -

### Added

- Many blocs de champs
- Many forms
  [nse]

## [0.0.17] - 23-06-2021 -

### Update

- rename repo of blocs de champs V2
  [nse]

## [0.0.16] - 23-06-2021 -

### Update

- rename repo of blocs de champs
  [nse]

## [0.0.15] - 23-06-2021 -

### Update

- workflow bea chien dangereux
  [nse]

## [0.0.14] - 23-06-2021 -

### Update

- workflow changement d'adresse V2
  [nse]

## [0.0.13] - 23-06-2021 -

### Update

- workflow changement d'adresse
  [nse]

## [0.0.12] - 23-06-2021 -

### Update

- all workflows v2
  [nse]

## [0.0.11] - 23-06-2021 -

### Update

- all workflows

### Delete

- all forms
  [nse]

## [0.0.10] - 22-06-2021 -

### Added

- add many workflows V2
  [nse]

## [0.0.9] - 22-06-2021 -

### Added

- add many workflows
- add directory blockdef
  [nse]

## [0.0.8] - 21-06-2021 -

### Added

- remove theaters mail-templates
- rename categories as category
  [nhi]

## [0.0.7] - 21-06-2021 -

### Added

- add pays datasource
  [nhi]

## [0.0.6] - 21-06-2021 -

### Added

- add mail-templates
- fix deployment path
  [nhi]

## [0.0.5] - 21-06-2021 -

### Added

- add some files to test indus
  [nhi]

## [0.0.4] - 17-06-2021 -

### Added

- add init.py
- add random form to test
  [nhi]

## [0.0.3] - 17-06-2021 -

### Added

- update version
- clarify authors
- add debian folder
  [nhi]

## [0.0.2] - 15-06-2021 -

### Added

- adapt Jenkinsfile
  [nhi]

### Removed

- old files
  [nhi]

## [0.0.1] - 15-04-2021 -

### Added

- all files that where in the 'script-teleservices'
  and that will potentially be useful in this one.
  [dmu]
